import logging
from typing import List
from llama_index.llms.gemini import Gemini
from llama_index.core import Settings, VectorStoreIndex
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_parse import LlamaParse
import google.generativeai as genai

class DocumentProcessor:
    def __init__(self, gemini_api_key: str, llama_cloud_api_key: str):
        """Initialize document processor with API keys"""
        self.gemini_api_key = gemini_api_key
        self.llama_cloud_api_key = llama_cloud_api_key
        
        # Configure Gemini
        genai.configure(api_key=self.gemini_api_key)
        
        # Initialize Gemini LLM
        self.llm = Gemini(
            model="models/gemini-1.5-flash",
            api_key=self.gemini_api_key,
            temperature=0.3,
            top_p=0.85,
            max_tokens=4096
        )
        
        # Initialize embeddings
        self.embed_model = GeminiEmbedding(
            model="models/embedding-001",
            api_key=self.gemini_api_key,
            dimension=768
        )
        
        # Set global configurations
        Settings.llm = self.llm
        Settings.embed_model = self.embed_model
    
    def process_document(self, file_path: str):
        """Process document and create query engine"""
        # Parse document
        documents = self.parse_document(file_path)
        
        # Process nodes
        nodes = self.process_nodes(documents)
        
        # Create index and query engine
        return self.create_rag_pipeline(nodes)
    
    def parse_document(self, file_path: str) -> List:
        """Parse document using LlamaParse"""
        parser = LlamaParse(
            api_key=self.llama_cloud_api_key,
            result_type="markdown"
        )
        return parser.load_data(file_path)
    
    def process_nodes(self, documents: List) -> List:
        """Process documents into nodes"""
        node_parser = SimpleNodeParser.from_defaults(
            chunk_size=1024,
            chunk_overlap=200
        )
        return node_parser.get_nodes_from_documents(documents)
    
    def create_rag_pipeline(self, nodes: List):
        """Create RAG pipeline with FAISS vector store"""
        index = VectorStoreIndex(
            nodes=nodes,
            show_progress=True
        )
        
        return index.as_query_engine(
            similarity_top_k=3,
            response_mode="compact"
        )
