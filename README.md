# Geo Model Chat: A Knowledge-based Q&A System for Reservoir Geological Modeling

**Authors:**  
Nie Zijun, Li Jieyu  
School of Geosciences, Yangtze University, Wuhan, China  
Contact: 1368915107@qq.com

---

## 🎯 Project Overview

Geo Model Chat is an **intelligent knowledge-based question answering (QA) system** dedicated to petroleum reservoir geological modeling. Built upon **Large Language Models (LLMs)**, **Retrieval-Augmented Generation (RAG)**, and a domain-specific **Knowledge Graph (KG)**, the system delivers high-precision semantic retrieval, advanced reasoning, and explainable answers for scientific and engineering applications in oil & gas domains.

> **Supported by the paper:**  
> **Geo Model Chat: A Knowledge-based Q&A System for Petroleum Reservoir Geological Modeling Based on Large Language Models**  
> _Nie Zijun, Li Jieyu, School of Geosciences, Yangtze University, Wuhan, China_

---

## 🏗️ Project Structure

```text
GeoModel-Chat/
├── geofront/       # Frontend: Interactive user interface (Vue.js)
├── geobackend/     # Backend: APIs, LLM orchestration, agents, knowledge retrieval, KG integration
├── README.md
├── ...

```
---
## 🚀 Quick Start
## Frontend (geofront)
```text
cd geofront
# Install dependencies
npm install

# Compiles and hot-reloads for development
npm run serve

# Compiles and minifies for production
npm run build

# Lints and fixes files
npm run lint
```

## Backend (geobackend)
Python 3.11+ required
Contains FastAPI backend, agent orchestration, RAG pipelines, KG interfaces, etc.
See /geobackend/README.md for detailed setup instructions.

---

## 🧩 System Architecture

- **RAG Module**: Conducts semantic search across expert-curated domain literature.
- **Knowledge Graph (KG)**: Captures structured entities/relationships in reservoir geology for multi-hop reasoning.
- **Multi-Agent Framework**: Key agents (`kg_Agent`, `search_Agent`) synergize RAG & KG, support open-domain and customized Q&A.
- **Visualization**: Real-time knowledge graph visualization and explainable answer tracing.

<details>
<summary><strong>System Workflow (Click to expand)</strong></summary>

1. **User query input**  
2. **Search via**:  
   - Document RAG retrieval  
   - KG reasoning (Cypher/NER/LLM prompt-based)  
3. **Integrated context understanding** → Answer generation  
4. **Interactive visualization** of knowledge/answers  
</details>

---

## 🗂️ Dataset & Knowledge Graph

- **Expert-grade Dataset**:  
  4300+ curated papers (CNKI) on reservoir geological modeling.

- **Automated KG Extraction**:
  - **Entities**: Geological terms (e.g., facies, porosity), regions (e.g., Ordos Basin), technical methods (e.g., sedimentation modeling)
  - **Relation extraction**: Via LLM prompt engineering
  - **Organization**: Hierarchical structure with semantic tags for deep reasoning

- **Storage & Querying**:  
  Neo4j graph database supporting complex semantic and spatiotemporal queries
  
---

## 🧪 Performance & Research Contributions
- **Accuracy**:  Up to +20.4% over baseline LLMs and RAG chatbots
- **Metrics**:Precision@5, expert-rated relevancy, answer length, system explainability
- **Ablation Studies**:Prove the critical value of KG-enhanced reasoning versus standard RAG
- **Expert Validation**:Averaged user satisfaction >4.2/5 (12 PhD/Master evaluators, domain+NLP backgrounds)
  
  ---
  
## 💡 Key Technologies & Requirements

### 🖥️ Development Stack
- **Languages**:
  - Python 3.11 (Backend/ML)
  - JavaScript + Vue.js (Frontend/Visualization)

### 📚 Core Libraries
| Category          | Key Libraries                                                                 |
|-------------------|-------------------------------------------------------------------------------|
| LLM Orchestration | `langchain`, `openai`, `tiktoken`                                             |
| Vector DB         | `chromadb`, `faiss-cpu`                                                       |
| Knowledge Graph   | `neo4j` (with Cypher query support)                                           |
| API & Web         | `fastapi`, `uvicorn`, `gradio`                                                |
| Data Processing   | `numpy`, `pandas`                                                             |

  ---
  
## 👨‍💻 Applications
- **Scientific research and education in petroleum geology**
- **Digital oilfield, reservoir modeling, specialized Q&A services**





  
