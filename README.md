
# AI Research Assistant using LangChain and Groq

## 📌 Overview
This project is an AI-powered research assistant built with **LangChain** and **Groq LLMs**.  
It generates **structured, academic-style research outputs** based on user queries, including a topic, concise bullet-point summaries, sources, and tools used.

The system intelligently decides when to rely on **general knowledge** and when to invoke **external tools** such as web search and Wikipedia for up-to-date or factual background information.

---

## 🚀 Key Features
- Structured research output validated using **Pydantic**
- Academic-style bullet summaries (5–8 points)
- Intelligent decision-making for tool usage
- DuckDuckGo search integration for current information
- Wikipedia integration for background context
- Automatic source and tool attribution
- Persistent storage of results with timestamps
- Simple, professional, and non-hallucinatory responses

---

## 🧠 Technologies Used
- Python  
- LangChain  
- Groq (LLaMA 3.1)  
- Pydantic  
- DuckDuckGo Search (ddgs)  
- Wikipedia API  
- python-dotenv  

---

## 📂 Project Structure
```text
ai-research-agent/
│
├── main.py                 # Main execution script
├── tools.py                # Search, Wikipedia, and Save tools
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore
└── research_output.txt     # Generated output file (gitignored)
````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Kpellehboy/AI-Research-Agent.git
```

### 2️⃣ (Recommended) Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS / Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> ⚠️ Never commit your `.env` file to GitHub.

---

## ▶️ How to Run

```bash
python main.py
```

You will be prompted:

```text
What can I help you research?
```

---

## 📝 Sample Output

```text
Topic: Careers after MSc in Computer Science – AI Applications in Europe

Summary:
- Graduates can pursue roles such as AI Researcher, Data Scientist, and Machine Learning Engineer.
- AI professionals are in high demand across technology, finance, healthcare, and automotive sectors.
- Many European countries offer strong employment opportunities due to mature tech ecosystems.
- Advanced skills in Python and AI frameworks improve employability.
- Doctoral studies remain an option for research-focused graduates.
- Continuous learning is essential due to rapid AI advancements.

Sources:
- General knowledge

Tools Used:
- llm only
```

All outputs are automatically saved to **`research_output.txt`** with timestamps.

---

## 🧩 How the System Works

1. User submits a research query
2. The system checks whether current information is required
3. If needed, web search and Wikipedia tools are invoked
4. The LLM generates a response following strict formatting rules
5. Output is validated using a Pydantic schema
6. Results are saved and displayed

---

## 🔮 Future Enhancements

* APA / IEEE citation formatting
* PDF and Markdown export
* Web API using FastAPI
* Cloud deployment (AWS / GCP)
* Multi-topic batch research
* Frontend interface

---

## 👤 Author

**Elijah M. Flomo,**
Computer Science Student 
---

## 📄 License

This project is open-source and intended for educational, academic, and portfolio use.

