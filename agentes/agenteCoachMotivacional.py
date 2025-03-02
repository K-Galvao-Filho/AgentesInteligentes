from crewai import Agent
from uteis.api_key import groqllm


def chamaCoachMotivacional():

    return Agent(
        role='Coach Motivacional',
        goal='Escrever uma mensagem motivacional para o estudante.',
        backstory='Você é um coach motivacional com experiência em ajudar estudantes a manterem o foco.',
        llm=groqllm
    )
