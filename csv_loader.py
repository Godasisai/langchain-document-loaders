import os
from langchain_community.document_loaders import CSVLoader

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "Social_Network_Ads.csv")

print(csv_path)
print(os.path.exists(csv_path))

loader = CSVLoader(file_path=csv_path)

docs = loader.load()

print(len(docs))
print(docs[1])