<div align="center">

<!-- Animated Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00c6ff,100:0072ff&height=200&section=header&text=Medical%20Chatbot%20AI&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Your%20Intelligent%20Healthcare%20Companion&descAlignY=60&descSize=18" width="100%"/>

<!-- Typing Animation -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=00C6FF&center=true&vCenter=true&width=600&lines=RAG-Powered+Medical+Assistant+%F0%9F%A9%BA;Built+with+LangChain+%2B+GPT+%2B+Pinecone;Ask+Anything+About+Your+Health+%F0%9F%94%AC;Deployed+Live+on+Render+%F0%9F%9A%80" alt="Typing SVG" />
</a>

<br/>

<!-- Badges -->
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.2-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=for-the-badge&logo=openai&logoColor=white)
![Pinecone](https://img.shields.io/badge/Pinecone-Vector%20DB-00BF7D?style=for-the-badge&logo=pinecone&logoColor=white)

<br/>

[![Live Demo](https://img.shields.io/badge/🌐%20Live%20Demo-medical--chatbotai.onrender.com-00c6ff?style=for-the-badge)](https://medical-chatbotai.onrender.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 🧠 What is Medical Chatbot AI?

> An intelligent, RAG-powered medical assistant that answers healthcare questions using a curated medical knowledge base — powered by **GPT-4o-mini**, **LangChain**, and **Pinecone vector search**.

Unlike generic AI chatbots, this system retrieves answers **grounded in real medical literature**, reducing hallucinations and delivering contextually accurate responses.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔍 **RAG Architecture** | Retrieval-Augmented Generation for accurate, grounded answers |
| 🧬 **Medical Knowledge Base** | Indexed from curated medical PDFs |
| ⚡ **Fast Vector Search** | Pinecone-powered semantic similarity search |
| 🤖 **GPT-4o-mini** | Cost-efficient, fast OpenAI language model |
| 🌐 **Live Web UI** | Clean Flask-based chat interface |
| ☁️ **Cloud Deployed** | Hosted on Render — accessible anywhere |

---

## 🏗️ Architecture

<div align="center">
  <img src="https://drive.google.com/uc?export=view&id=1lPEYrveF9GlqoQX877dDgLgDAIYuKmbg" alt="Medical Chatbot Demo" width="1500"/>
</div>

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| **Backend** | Python 3.11, Flask |
| **LLM** | OpenAI GPT-4o-mini |
| **Embeddings** | OpenAI text-embedding-ada-002 |
| **Vector Store** | Pinecone (Serverless) |
| **RAG Framework** | LangChain |
| **Deployment** | Render |

</div>

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- OpenAI API Key
- Pinecone API Key

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/medical-chatbot.git
cd medical-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

### 4. Build the Pinecone index

```bash
python store_index.py
```

### 5. Run the app

```bash
python app.py
```

Visit `http://localhost:8080` in your browser.

---

## 📁 Project Structure

```
medical-chatbot/
├── 📂 src/
│   ├── helper.py          # PDF loading, chunking, embeddings
│   └── prompt.py          # System prompt for the LLM
├── 📂 templates/
│   └── chat.html          # Chat UI
├── 📂 static/             # CSS, JS assets
├── 📂 data/               # Medical PDF knowledge base
├── app.py                 # Flask application
├── store_index.py         # Pinecone index builder
├── requirements.txt
└── .env
```

---

## 🔄 RAG Pipeline

```
1. 📄 PDF Ingestion       → Load medical PDFs from /data
2. ✂️  Text Chunking      → Split into 500-token chunks
3. 🔢 Embedding           → OpenAI text-embedding-ada-002
4. 📌 Vector Storage      → Upsert to Pinecone index
5. 🔍 Semantic Retrieval  → Top-k similarity search
6. 🤖 LLM Generation      → GPT-4o-mini synthesizes answer
7. 💬 Response Delivery   → Streamed back to Flask UI
```

---

## 🌐 Live Demo

> 🔗 **[https://medical-chatbotai.onrender.com/](https://medical-chatbotai.onrender.com/)**

> ⚠️ **Note:** Hosted on Render's free tier — the first request may take 30–60 seconds to wake up from idle.

---

## ⚙️ Environment Variables

| Variable | Description |
|---|---|
| `OPENAI_API_KEY` | Your OpenAI API key |
| `PINECONE_API_KEY` | Your Pinecone API key |
| `PORT` | Server port (default: `8080`) |

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👨‍💻 Author

**Rishikesh Kshirsagar**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/YOUR_LINKEDIN)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/YOUR_GITHUB)

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0072ff,100:00c6ff&height=120&section=footer" width="100%"/>

*Built with ❤️ for better healthcare accessibility*

</div>
