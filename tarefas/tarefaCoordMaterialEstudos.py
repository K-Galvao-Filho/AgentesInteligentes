from crewai import Task

def tarefaCoordMaterialEstudos(solicitacao, agente):

    return Task(
        description=f'formate os dados vindo de {solicitacao} para que todos eles posam ser visto separadamente.',
        agent=agente,
        expected_output='Lista de vídeos relacionados ao assunto.',
        output_file="saida\VideosYoutube.txt"
    )
