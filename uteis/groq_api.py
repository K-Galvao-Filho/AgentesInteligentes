#import os
from crewai import LLM

#ROQ_API = os.environ.get("GROQ_API_KEY")
groqllm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=4000,
    top_p=0.9
)
