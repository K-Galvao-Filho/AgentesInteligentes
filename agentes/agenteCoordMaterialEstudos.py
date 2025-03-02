from crewai import Agent
from uteis.api_key import groqllm2


def chamaCoordMaterialEstudos(solicitacao):
    
    disciplina = solicitacao['disciplina']
    assunto = solicitacao['assunto']
    topicos = ', '.join(solicitacao['topicos'])

    return Agent(
        role='Coordenador de Material de Estudos',
        goal=f'Sua tarefa é pesquisar no Youtube por vídeos que explique as Disciplina: {disciplina} sobre o Assunto: {assunto} e seus Tópicos: {topicos}',
        backstory='Você é um especialista em educação com experiência em criar planos de estudos eficientes.',
        llm=groqllm2
    )
