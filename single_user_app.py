
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from collections import defaultdict
from dotenv import load_dotenv
from langchain.chains import  RetrievalQA
from langchain import HuggingFaceHub
from Model import MODEL_ID
import os
from langchain import PromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Chroma

load_dotenv()

app = FastAPI(title="RetrievalChainDemo")
templates = Jinja2Templates(directory="templates")


with open("hugging_face_token.txt", 'r') as file:
    for line in file:
        TOKEN= (line)
os.environ["HUGGINGFACEHUB_API_TOKEN"] = TOKEN





llm = HuggingFaceHub(repo_id=MODEL_ID, 
model_kwargs={"temperature": 0, "max_length": 512},
verbose=False,
)


# support_template = """As a GIKI website chat bot, your goal is to provide accurate and helpful information about TechROVA products,
# an educational insitute located in Pakistan.
# You should answer user inquiries based on the context provided and avoid making up answers.
# If you don't know the answer, go through the previous chats first and if not, then use your own training data.

# {context}
# Question: {question}"""



sales_template = """As a GIKI website chat bot, your goal is to provide accurate and helpful information about TechROVA products,
an educational insitute located in Pakistan. You should answer user inquiries based on the context provided. If he greets, then greet him. Don't include prefix 'Answer'.
avoid making up answers.
If you don't know the answer, go through the previous chat history first and if not, then use your own training data.
Use the following context (delimited by <ctx></ctx>) and the chat history (delimited by <hs></hs>) to answer the question:
<ctx>
{context} 
</ctx>
<hs> {history} </hs>
Question: {question}"""

SALES_PROMPT = PromptTemplate(
template=sales_template, input_variables=["history", "context", "question"]
)


from langchain.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings()

from langchain.vectorstores import Chroma
docsearch = Chroma(persist_directory="chroma_db", embedding_function=embeddings)


chain = RetrievalQA.from_chain_type(
llm=llm,
chain_type="stuff",
retriever=docsearch.as_retriever(),
chain_type_kwargs={
    "verbose": False,
    "prompt": SALES_PROMPT,
    "memory": ConversationBufferMemory(
        memory_key="history",
        input_key="question"),
},
verbose = False)



chat_history = defaultdict(list)


class ChatRequest(BaseModel):
    Userid: str
    query: str


@app.post("/Chat_me")
def chat_me(request: ChatRequest):
    Userid = request.Userid
    query = request.query
    result = chain({'query': query, 'chat_history': chat_history[Userid]})
    chat_history[Userid].append((query, result['result']))
    file1 = open("{0}.txt".format(Userid), "a")  # append mode
    file1.write(query + " " + result['result'] + "\n")
    file1.close()
    return {"response": result['result']}


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# chat_history = defaultdict(list)

# while True:

#     query = input(" > ")
#     ui=input("ui")
#     result = chain({'query': query, 'history': chat_history[ui]})
#     chat_history[ui].append((query, result['result']))
#     print(result["result"],"\n")