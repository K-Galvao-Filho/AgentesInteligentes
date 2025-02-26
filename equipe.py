from crewai import Crew
from uteis.groq_api import groqllm

#Chamando os agentes
from agentes.coordenadorEstudos import chamaCoordenador
from agentes.especialistaMaterial import chamaEspecialista
from agentes.coachMotivador import chamaCoach

#Chamando as tarefas dos agentes
from tarefas.tarefa_coordenadorEstudos import tarefaCoordenador
from tarefas.tarefa_especialistaMaterial import tarefaEspecialista
from tarefas.tarefa_coachMotivador import tarefaCoach

def formarEquipe(solicitacao):
    # Criando agentes
    coordenador = chamaCoordenador(solicitacao)
    especialista = chamaEspecialista(solicitacao)
    motivador = chamaCoach()
        
    # Criando tarefas
    tarefa_coordenador = tarefaCoordenador(solicitacao, coordenador)
    tarefa_especialista = tarefaEspecialista(solicitacao, especialista)
    tarefa_motivador = tarefaCoach(motivador)

    # Criando a equipe
    equipe = Crew(
        name='Coordenação de Estudos Especializado',
        description='Uma equipe de especialistas em educação para ajudar estudantes a manterem o foco nos estudos.',
        members=[coordenador, especialista, motivador],
        tasks=[tarefa_coordenador, tarefa_especialista, tarefa_motivador]
  
    )

    return equipe
