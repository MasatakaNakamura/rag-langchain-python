from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from create_uuid import get_uuid
from load_html_use_bs4 import load_html_to_text
from chunk_documents import chunk_documents

# HuggingFaceモデルの初期化
embeddings = HuggingFaceEmbeddings(model_name="./path_to_model/intfloat/multilingual-e5-base")

# ベクトルDBの初期化
vector_store = Chroma(    
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)

html_doc = load_html_to_text()
documents = chunk_documents(html_doc)

# ドキュメントのIDを生成
uuids = get_uuid(documents)

# ベクトルDBにドキュメントを追加
vector_store.add_documents(documents=documents, ids=uuids)

# 類似度検索
results = vector_store.similarity_search(
    "銀河グループの年間予定",
    k=2,
)

# 類似度検索結果表示
for res in results:
    print(f"* {res.page_content} [{res.metadata}]")