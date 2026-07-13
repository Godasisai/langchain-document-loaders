from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

print("Current Folder:", os.getcwd())

pdf_path = r"C:\Users\hp\OneDrive\Documents\Desktop\Langchain_models\8.langchain-document-loaders\hh.pdf"

print("File Exists:", os.path.exists(pdf_path))

loader = PyPDFLoader(pdf_path)

docs = loader.load()

print("Pages:", len(docs))
print(docs[0].metadata)

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt = PromptTemplate(
    template="Write a summary of the following PDF page:\n\n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({
    "text": docs[0].page_content
})

print(result)