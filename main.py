import nest_asyncio
nest_asyncio.apply()


from  langchain.schema import Document

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

docs=load_docs_from_jsonl('data.jsonl')

# Text Splitter
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs= text_splitter.split_documents(docs)


import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

print("starting to download embedding")
# Embeddings
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings()

print("embedding downloaded")

from langchain import HuggingFaceHub

llm=HuggingFaceHub(repo_id="google/flan-t5-small", model_kwargs={"temperature":0, "max_length":512})

# print(docs[0])
from langchain.vectorstores import Chroma
docsearch = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

from langchain.chains import ConversationalRetrievalChain
# from langchain.chat_models import ChatOpenAI

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=docsearch.as_retriever(),
    return_source_documents=True
)


import sys

chat_history = []
while True:
    # this prints to the terminal, and waits to accept an input from the user
    query = input('Prompt: ')
    # give us a way to exit the script
    if query == "exit" or query == "quit" or query == "q":
        print('Exiting')
        sys.exit()
    # we pass in the query to the LLM, and print out the response. As well as
    # our query, the context of semantically relevant information from our
    # vector store will be passed in, as well as list of our chat history
    result = qa_chain({'question': query, 'chat_history': chat_history})
    print('Answer: ' + result['answer'])
    # we build up the chat_history list, based on our question and response
    # from the LLM, and the script then returns to the start of the loop
    # and is again ready to accept user input.
    chat_history.append((query, result['answer']))
    file1 = open("myfile.txt", "a")  # append mode
    file1.write(query + " " + result['answer']+"\n")
    file1.close()

