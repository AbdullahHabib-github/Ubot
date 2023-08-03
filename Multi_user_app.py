
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from dotenv import load_dotenv
from  langchain.schema import Document
from langchain.chains import RetrievalQA
from langchain import HuggingFaceHub
from Model import MODEL_ID
from langchain import PromptTemplate
import os
from langchain.vectorstores import Chroma
import json
from typing import Iterable

def load_docs_from_jsonl(file_path)->Iterable[Document]:
    array = []
    with open(file_path, 'r') as jsonl_file:
        for line in jsonl_file:
            data = json.loads(line)
            obj = Document(**data)
            array.append(obj)
    return array


def list_folders(directory):
    folders = []
    for root, _, dirnames in os.walk(directory):
        for folder in dirnames:
            folders.append(folder)
    return folders


load_dotenv()

app = FastAPI(title="GIKI chatbot")
templates = Jinja2Templates(directory="templates")



with open("hugging_face_token.txt", 'r') as file:
    for line in file:
        TOKEN= (line)
os.environ["HUGGINGFACEHUB_API_TOKEN"] = TOKEN


llm = HuggingFaceHub(repo_id=MODEL_ID, model_kwargs={"temperature": 0, "max_length": 512})
from langchain.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings()

template = """As a GIKI website chat bot, your goal is to provide accurate and helpful information about GIKI,
an educational insitute located in Pakistan. You should answer user inquiries based on the context provided. If he greets, then greet him. Don't include prefix 'Answer'.
avoid making up answers.If you don't know the answer, tell the user that you dont know the answer.
If the user tells you his name, you should ask them their phone number.
if the user tells you his phone number, you ask them if they have any questions
To answer a question go through the your training data and use the following context (delimited by <ctx></ctx>):
<ctx>
{context} 
</ctx>

Question: {question}"""


class ChatRequest(BaseModel):
    Userid: str
    query: str



docsearch = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

@app.post("/Chat_me")
def chat_me(request: ChatRequest):
    Userid = request.Userid
    query = request.query
    all_folders = list_folders("Chat_histories")


    if "{0}.jsonl".format(Userid) in all_folders:    #####if the user already exists

        docs=load_docs_from_jsonl("Chat_histories/{0}.jsonl".format(Userid))

        db2 = Chroma.from_documents(docs, embeddings)

        db2_data=docsearch._collection.get(include=['documents','metadatas','embeddings'])
        db2._collection.add(
            embeddings=db2_data['embeddings'],
            metadatas=db2_data['metadatas'],
            documents=db2_data['documents'],
            ids=db2_data['ids']
        )

    
        chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=db2.as_retriever(),
                chain_type_kwargs={
                "prompt": PromptTemplate(
                template=template,
                input_variables=["context","question"],
            ),
        },)

    else:    ### if the user is logging in for the first time    

        chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=docsearch.as_retriever(),
                chain_type_kwargs={
                "prompt": PromptTemplate(
                template=template,
                input_variables=["context","question"],
            ),
        },
        )
    
    result = chain.run(query)


    import datetime
    import json

    # Print the current date and time
    dic={"page_content": query + " " + result, "metadata": {"source": "chathistory", "loc": Userid, "lastmod": str(datetime.datetime.now())}}
    jsonl_file_path = "Chat_histories/{0}.jsonl".format(Userid)

    # Open the JSONL file in append mode and write the dictionary
    with open(jsonl_file_path, "a") as jsonl_file:
        jsonl_file.write(json.dumps(dic) + "\n")

    return {"response": 'Answer: ' + result}


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



