from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text):
    print("Đang xử lý text-embedding...")
    vector = model.encode(text)
    print("Xong task embedding!")
    return np.array(vector).astype("float32")