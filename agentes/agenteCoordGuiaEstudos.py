from crewai import Agent
from uteis.api_key import groqllm


def chamaCoordGuiaEstudos(solicitacao):
    
    disciplina = solicitacao['disciplina']
    assunto = solicitacao['assunto']
    topicos = ', '.join(solicitacao['topicos'])

    return Agent(
        role='Coordenador de Guia de Estudos',
        goal=f'Sua tarefa é criar um Guia de estudo estruturado com base nas seguintes informações: Disciplina: {disciplina}, Assunto: {assunto}, Tópicos: {topicos}',
        backstory='Você é um especialista em educação com experiência em criar planos de estudos eficientes.',
        llm=groqllm
    )
