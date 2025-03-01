from crewai import Agent
from uteis.groq_api import groqllm


def chamaCoordenador(solicitacao):
    
    disciplina = solicitacao['disciplina']
    assunto = solicitacao['assunto']
    topicos = ', '.join(solicitacao['topicos'])

    return Agent(
        role='Coordenador de Estudos',
        goal=f'Sua tarefa é criar um plano de estudo estruturado com base nas seguintes informações: Disciplina: {disciplina}, Assunto: {assunto}, Tópicos: {topicos}',
        backstory='Você é um especialista em educação com experiência em criar planos de estudos eficientes.',
        llm=groqllm,
        verbose=True
    )
