import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader

from langchain.document_loaders import TextLoader
loader = TextLoader('../../../state_of_the_union.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

import pinecone 

# initialize pinecone
pinecone.init(
    api_key="YOUR_API_KEY",  # find at app.pinecone.io
    environment="YOUR_ENV"  # next to api key in console
)

index_name = "langchain-demo"

docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)

# if you already have an index, you can load it like this
# docsearch = Pinecone.from_existing_index(index_name, embeddings)

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query)


print(docs[0].page_content)
