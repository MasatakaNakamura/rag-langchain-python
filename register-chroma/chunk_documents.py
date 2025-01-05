from langchain.text_splitter import RecursiveCharacterTextSplitter
from bs4 import BeautifulSoup
from langchain.schema import Document

def chunk_documents(documents):
    # ドキュメントを分割するためのTextSplitterを作成
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,  # 各チャンクの最大文字数
        chunk_overlap=100  # チャンク間の重複文字数
    )

    # ドキュメントをチャンクに分割
    chunks = text_splitter.split_documents(documents)

    # 各チャンクを表示
    # for i, chunk in enumerate(chunks):
    #     print(f"Chunk {i + 1}:")
    #     print(chunk.page_content)
    #     print(chunk.metadata)
    #     print("-" * 40)
        
    return chunks

