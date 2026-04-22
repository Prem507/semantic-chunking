# 📄 Advanced NLP – Semantic Document Question Answering System

This project is a **Document Question Answering System** built using Python and advanced NLP techniques.

It allows users to query multiple PDF documents and retrieves the **most relevant answers using semantic search and semantic chunking**.

---

## 🚀 Features

- 📥 Extracts text from multiple PDF files  
- ✂️ Splits text into sentences  
- 🧠 Uses **semantic chunking** to group related sentences  
- 🧹 Applies text preprocessing:
  - Tokenization  
  - Stopword removal  
  - Stemming  
- 🧠 Generates embeddings using **Sentence Transformers**  
- 🔍 Performs **semantic similarity search**  
- 📈 Returns **Top-K (Top 3) relevant answers**  
- 🎯 Applies **confidence threshold filtering**  

---

## 🛠️ Technologies Used

- Python  
- NLTK  
- NumPy  
- Pandas  
- Sentence Transformers  
- Scikit-learn  
- PyPDF2  

---

## ⚙️ How It Works

1. Load multiple PDF documents  
2. Extract text from each document  
3. Split text into sentences  
4. Generate embeddings for each sentence  
5. Create **semantic chunks**:
   - Compare similarity between consecutive sentences  
   - Group sentences if similarity > threshold (0.7)  
   - Start a new chunk when similarity drops  
6. Preprocess chunks:
   - Lowercasing  
   - Tokenization  
   - Stopword removal  
   - Stemming  
7. Convert chunks into embeddings  
8. Convert user query into embedding  
9. Compute similarity using **Cosine Similarity**  
10. Retrieve **Top 3 relevant chunks**  
11. Apply **confidence threshold** to filter weak results  

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/Prem507/Advanced-NLP.git
cd Advanced-NLP
Install dependencies:
Bash
pip install nltk numpy pandas scikit-learn PyPDF2 sentence-transformers
Run the program:
Bash
python main.py
Enter your query in the terminal.
💡 Example
Input:

Ask Question: What is leave policy?
Output:

Best Context Answers:

Context Answer:
Employees are entitled to leave as per company policy...
Score: 0.85
----------------------------------
If no relevant result is found:

Sorry, no answer found.
📂 Project Structure

Advanced-NLP/
│── data/ (PDF files)
│── main.py
│── README.md
📈 Key Improvements
TF-IDF → Semantic Search (Embeddings)
Sentence-level → Chunk-based retrieval
Fixed chunks → Overlap chunks → Semantic chunking
Static splitting → Meaning-based grouping
Single answer → Top-K ranked results
Always answer → Confidence-based filtering
📈 Future Improvements
Integrate FAISS for efficient vector search
Build complete RAG system (LLM-based answer generation)
Add source citation (page number / document name)
Build Streamlit web interface
Deploy on cloud (AWS / Streamlit Cloud)
👨‍💻 Author
Prem Chandh
Aspiring Generative AI Engineer
GitHub: https://github.com/Prem507⁠�
⭐ Conclusion
This project demonstrates how semantic chunking combined with semantic search improves context-aware document retrieval, making it closer to real-world AI and RAG-based systems.

---

If you read this carefully, it tells a complete arc:
- keyword → semantic  
- chunk → overlap → **semantic chunking**  

That narrative is what turns your GitHub from “projects” into a **learning trajectory**—and that’s what people actually pay attention to.
