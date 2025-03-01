import os
from crewai import LLM

GROQ_API_KEY = os.environ.get("GROQ_API_KEY_01")
groqllm = LLM(
    model="groq/llama-3.3-70b-versatile",
    #model="groq/deepseek-r1-distill-llama-70b",
    api_key=GROQ_API_KEY,
    temperature=0.7,
    max_tokens=4000,
    top_p=0.9
)
