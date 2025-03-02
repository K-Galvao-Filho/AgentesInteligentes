from crewai import Agent
from uteis.groq_api import groqllm

def chamaEspecialista(solicitacao):
    
    disciplina = solicitacao['disciplina']
    assunto = solicitacao['assunto']
    topicos = ', '.join(solicitacao['topicos'])

    return Agent(
        role='Coordenador de Estudos',
        goal=f'Sua tarefa é pesquisar no Youtube por vídeos que explique as Disciplina: {disciplina} sobre o Assunto: {assunto} e seus Tópicos: {topicos}',
        backstory='Você é um especialista em educação com experiência em criar planos de estudos eficientes.',
        llm=groqllm,
        verbose=True
    )
