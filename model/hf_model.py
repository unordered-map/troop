# Hugging Face local model integration
from huggingface_hub import snapshot_download

def hugging_face():
    print("Hugging face model loaded successfully!")
    

    model_path = snapshot_download(repo_id="gpt2")
    print(model_path)

