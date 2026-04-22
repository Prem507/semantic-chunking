import PyPDF2
import nltk
import numpy as np
import pandas as pd

from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import  cosine_similarity

from aiasync import preprocess, stop_words

nltk.download('punkt')
nltk.download('stopwords')


files = [
    r"D:\Desktop\CSV\AnnualHealthCheck.pdf",
    r"D:\Desktop\CSV\LeavePolicy.pdf",
    r"D:\Desktop\CSV\NoticePeriod.pdf",
    r"D:\Desktop\CSV\OfficeTime.pdf",
    r"D:\Desktop\CSV\Separation.pdf",
    r"D:\Desktop\CSV\Travel.pdf",
    r"D:\Desktop\CSV\USA_Employee_Handbook-Freely_Available.pdf"
]

documents = []

for file in files:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        text += page_text
    documents.append(text)

print(f"no of documents loaded: {len(documents)}")

sentences = []
for doc in documents:
    sentences.extend(sent_tokenize(doc))
print(f"total senetences loaded{len(sentences)}")

print("Loading Transformer Model....")
model = SentenceTransformer('all-MiniLM-L6-v2')
sentence_embeddings = model.encode(sentences)

chunks = []
current_chunk = [sentences[0]]
similarity_threshold = 0.7

for i in range(1, len(sentences)):
    sim = cosine_similarity(
        [sentence_embeddings[i-1]],
        [sentence_embeddings[i]]
    )[0][0]

    if sim > similarity_threshold:
        current_chunk.append(sentences[i])

    else:
        chunks.append(" ".join(current_chunk))
        current_chunk = [sentences[i]]

if current_chunk:
    chunks.append(" ".join(current_chunk))
print(f"semantic chunks loaded{len(chunks)}")

stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()
def preprocess(text):
    tokens = word_tokenize(text)
    clean_tokens = []
    for word in tokens:
        if word.isalpha() and word not in stop_words:
            clean_tokens.append(stemmer.stem(word))

    return " ".join(clean_tokens)
processed_chunks = [preprocess(c)for c in chunks]
# CHUNK EMBEDDINGS
chunk_embeddings = model.encode(processed_chunks)

# QUERY
query = input("Ask Question: ")
processed_query = preprocess(query)
query_embedding = model.encode([processed_query])

# SIMILARITY
similarities = cosine_similarity(query_embedding, chunk_embeddings)[0]

threshold = 0.20
top_k = 3

top_indices = pd.Series(similarities).nlargest(top_k).index.tolist()

# OUTPUT
if similarities[top_indices[0]] < threshold:
    print("\nSorry, no answer found.")
else:
    print("\nBest Context Answers:\n")

    for idx in top_indices:
        if similarities[idx] >= threshold:
            print("Context Answer:\n", chunks[idx])
            print("Score:", similarities[idx])
            print("----------------------------------")







