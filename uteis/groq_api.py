#import os
from crewai import LLM

#GROQ_API = s.environ.get("GROQ_API_KEY")
groqllm = LLM(
    model="groq/llama3-70b-8192",
    api_key="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",
    temperature=0.7,
    max_tokens=4000,
    top_p=0.9
)
groqllm2 = LLM(
    model="groq/deepseek-r1-distill-llama-70b",
    temperature=0.7,
    max_tokens=4000,
    top_p=0.9
)
