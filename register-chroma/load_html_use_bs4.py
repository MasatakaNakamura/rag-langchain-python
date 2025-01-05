from langchain_community.document_loaders import BSHTMLLoader

def load_html_to_text():
    file_path = "./datas/html/銀河_ソフトウェア_社内ページ.html"

    encoding = "euc-jp"

    loader = BSHTMLLoader(
        file_path=file_path, 
        open_encoding=encoding
    )

    return loader.load()
        
    # print(data)