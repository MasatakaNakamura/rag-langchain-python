from langchain_community.document_loaders import UnstructuredHTMLLoader

file_path = "./datas/html/銀河_ソフトウェア_社内ページ.html"

loader = UnstructuredHTMLLoader(file_path)
data = loader.load()

print(data)