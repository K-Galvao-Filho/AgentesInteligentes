import os
from crewai import LLM

GROQ_API_01 = os.environ.get("GROQ_API_KEY_01")
GROQ_API_02 = os.environ.get("GROQ_API_KEY_02")
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

groqllm = LLM(
    model="groq/llama3-70b-8192",
    #model="groq/deepseek-r1-distill-llama-70b",
    api_key=GROQ_API_01
)
groqllm2 = LLM(
    model="groq/llama3-70b-8192",
    #model="groq/deepseek-r1-distill-llama-70b",
    api_key=GROQ_API_02
)

