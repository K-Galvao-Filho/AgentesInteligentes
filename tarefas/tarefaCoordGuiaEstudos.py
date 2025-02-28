from crewai import Task

def tarefaCoordGuiaEstudos(solicitacao, agente):
    disciplina = solicitacao['disciplina']
    assunto = solicitacao['assunto']
    topicos = ', '.join(solicitacao['topicos'])

    return Task(
        description=f'Criar um Guia de estudo estruturado com base nas seguintes informações: Disciplina: {disciplina}, Assunto: {assunto}, Tópicos: {topicos}.',
        agent=agente,
        expected_output='Plano de estudos personalizado.',
        output_file="saida\GuiaDeEstudos.txt"
    )
