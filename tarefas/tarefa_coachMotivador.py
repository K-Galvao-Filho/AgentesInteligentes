from crewai import Task

def tarefaCoach(agente):

    return Task(
        description='Escrever uma mensagem motivacional para o estudante.',
        agent=agente,
        expected_output='Mensagem motivacional.',
        output_file="saida\Motivacao.txt"
    )
