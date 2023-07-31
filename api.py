from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from langchain.chains import ConversationalRetrievalChain
from pydantic import BaseModel
from collections import defaultdict


load_dotenv()

app = FastAPI(title="ConversationalRetrievalChainDemo")


templates = Jinja2Templates(directory="templates")

load_dotenv()

from langchain import HuggingFaceHub
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

llm=HuggingFaceHub(repo_id="google/flan-t5-small", model_kwargs={"temperature":0, "max_length":512})


def create_chain():

    from langchain.embeddings import HuggingFaceEmbeddings
    embeddings = HuggingFaceEmbeddings()

    from langchain.vectorstores import Chroma
    docsearch = Chroma(persist_directory="chroma_db", embedding_function=embeddings)


    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        return_source_documents=True
    )



chain = create_chain()
chat_history = defaultdict(list)


class ChatRequest(BaseModel):
    Userid: str
    query: str

@app.post("/Chat_me")
def chat_me(request: ChatRequest):
    # Extract the Userid and question from the request body
    Userid = request.Userid
    query = request.query
    result = chain({'question': query, 'chat_history': chat_history[Userid]})
    chat_history[Userid].append((query, result['answer']))
    file1 = open("{0}.txt".format(Userid), "a")  # append mode
    file1.write(query + " " + result['answer']+"\n")
    file1.close()
    return {"response": 'Answer: ' + result['answer']}


# langchain_router = LangchainRouter(
#     langchain_url="/chat", langchain_object=chain, streaming_mode=1
# )
# langchain_router.add_langchain_api_route(
#     "/chat_json", langchain_object=chain, streaming_mode=2
# )

# app.include_router(langchain_router)

