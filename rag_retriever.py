from sentence_transformers import SentenceTransformer
import faiss
import os

class RAGRetriever:
    def __init__(self, file_path='knowledge_base.txt'):
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.texts = []

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()

        # Split by paragraphs
        self.texts = [para.strip() for para in content.split('\n') if para.strip()]
        self.embeddings = self.embedder.encode(self.texts, convert_to_numpy=True)

        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(self.embeddings)

    def retrieve(self, query, top_k=3):
        q_emb = self.embedder.encode([query], convert_to_numpy=True)
        dists, ids = self.index.search(q_emb, top_k)
        return [self.texts[i] for i in ids[0]]
