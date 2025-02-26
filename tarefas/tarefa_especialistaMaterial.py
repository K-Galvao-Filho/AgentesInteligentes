from crewai import Task

def tarefaEspecialista(solicitacao, agente):
    disciplina = solicitacao['disciplina']
    assunto = solicitacao['assunto']
    topicos = ', '.join(solicitacao['topicos'])

    return Task(
        description=f'Pesquisar no Youtube por vídeos que explique as Disciplina: {disciplina} sobre o Assunto: {assunto} e seus Tópicos: {topicos}',
        agent=agente,
        expected_output='Lista de vídeos relacionados ao assunto.',
        output_file="saida\VideosYoutube.txt"
    )
