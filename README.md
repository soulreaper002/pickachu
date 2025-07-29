# pickachu
# Basic Rag: Begining 

                 ┌──────────────────────┐
                 │   Data Sources       │
                 │ (PDF, CSV, API etc.) │
                 └─────────┬────────────┘
                           │
                    Data Ingestion
                           │
                 ┌─────────▼────────────┐
                 │  Text Chunking       │
                 │  & Preprocessing     │
                 └─────────┬────────────┘
                           │
                    Embedding Generation
                           │
                 ┌─────────▼────────────┐
                 │  Vector Store        │
                 │ (FAISS / Pinecone)   │
                 └─────────┬────────────┘
                           │
                   ┌───────▼────────┐
                   │   Retriever    │
                   └───────┬────────┘
                           │
                 Retrieved Relevant Context
                           │
                 ┌─────────▼────────────┐
                 │   Prompt Builder     │
                 └─────────┬────────────┘
                           │
                    LLM Response Generation
                           │
                 ┌─────────▼────────────┐
                 │ Final Answer to User │
                 └──────────────────────┘
