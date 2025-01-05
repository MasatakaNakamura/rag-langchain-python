from huggingface_hub import snapshot_download

model_name = "intfloat/multilingual-e5-base"
download_path = snapshot_download(
    repo_id=model_name,
    local_dir = f"path_to_model/{model_name}",
    local_dir_use_symlinks=False
    )
