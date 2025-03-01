from crewai import Agent
from uteis.groq_api import groqllm


def chamaCoach():

    return Agent(
        role='Motivador',
        goal='Escrever uma mensagem motivacional para o estudante.',
        backstory='Você é um coach motivacional com experiência em ajudar estudantes a manterem o foco.',
        llm=groqllm,
        verbose=True
    )
