import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from langchain.chains import ConversationalRetrievalChain
from pydantic import BaseModel
from collections import defaultdict
from langchain import HuggingFaceHub
from fastapi.responses import HTMLResponse


load_dotenv()

app = FastAPI(title="ConversationalRetrievalChainDemo")

# Configure templates and static files directories
templates = Jinja2Templates(directory="static")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load the HuggingFace Hub model
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm = HuggingFaceHub(repo_id="google/flan-t5-small", model_kwargs={"temperature": 0, "max_length": 512})

# Create the ConversationalRetrievalChain
def create_chain():
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.vectorstores import Chroma
    embeddings = HuggingFaceEmbeddings()
    docsearch = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        return_source_documents=True
    )

chain = create_chain()
chat_history = defaultdict(list)

# Define the Pydantic model for chat requests
class ChatRequest(BaseModel):
    Userid: str
    query: str

# Handle the chat POST request
@app.post("/Chat_me")
def chat_me(request: ChatRequest):
    Userid = request.Userid
    query = request.query
    result = chain({'question': query, 'chat_history': chat_history[Userid]})
    chat_history[Userid].append((query, result['answer']))
    with open(f"{Userid}.txt", "a") as file:
        file.write(f"{query} {result['answer']}\n")
    return {"response": 'Answer: ' + result['answer']}

# Render the HTML template
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
