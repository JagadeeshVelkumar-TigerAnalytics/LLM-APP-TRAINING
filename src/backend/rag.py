from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def get_relevant_document_using_rag_in_langchain(question,open_ai_key,base_url):
    loader = PyPDFLoader(r"C:\Users\jagadeesh.velku\OneDrive - TIGER ANALYTICS INDIA CONSULTING PRIVATE LIMITED\Desktop\LLM APP Training\books\Evolution of Computer.pdf")

    file = loader.load()

    # print(file[0].page_content)
    docs = "\n--------\n".join([doc.page_content for doc in file])
    print(docs)

    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=10)
    # docs = text_splitter.split_documents(file)

    # for doc in docs:
    #     print(doc.page_content)
    
    embedding = OpenAIEmbeddings(model="text-embedding-3-small",base_url=base_url, api_key=open_ai_key)
    vector_embeds = embedding.embed_documents(docs)
    print(vector_embeds)
    vector_db = FAISS.from_documents(documents=file ,embedding=embedding)

    relevant_docs = vector_db.similarity_search(query=question, k=3)
    print("relevant_docs are -> ", relevant_docs[0].page_content)
    return relevant_docs[0].page_content