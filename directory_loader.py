from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

loader = DirectoryLoader(
    path="8.langchain-document-loaders/books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt = PromptTemplate(
    template="Summarize the following text:\n\n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt | model | parser

for i, doc in enumerate(docs, start=1):
    print(f"\nPage {i}")
    print(doc.metadata)

    result = chain.invoke({
        "text": doc.page_content
    })

    print(result)
    print("-" * 50)