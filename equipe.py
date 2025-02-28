from crewai import Crew
from uteis.groq_api import groqllm

#Chamando os agentes
from agentes.agenteCoordEquipe import chamaCoordenadorEquipe
from agentes.agenteCoordGuiaEstudos import chamaCoordGuiaEstudos
from agentes.agenteCoordPlanoEstudos import chamaCoordPlanoEstudos
from agentes.agenteCoordMaterialEstudos import chamaCoordMaterialEstudos
from agentes.agenteCoachMotivacional import chamaCoachMotivacional

#Chamando as tarefas dos agentes
from tarefas.tarefaCoordGuiaEstudos import tarefaCoordGuiaEstudos
from tarefas.tarefaCoordPlanoEstudos import tarefaCoordPlanoEstudos
from tarefas.tarefaCoordMaterialEstudos import tarefaCoordMaterialEstudos
from tarefas.tarefaCoachMotivacional import tarefaCoachMotivacional

def formarEquipe(solicitacao):
    # Criando agentes
    coordCentral = chamaCoordenadorEquipe()
    guiaEstudos = chamaCoordGuiaEstudos(solicitacao)
    planoEstudos = chamaCoordPlanoEstudos(solicitacao)
    materialEstudos = chamaCoordMaterialEstudos(solicitacao)
    coachMotivador = chamaCoachMotivacional()
        
    # Criando tarefas
    trf_GuiaEstudos = tarefaCoordGuiaEstudos(solicitacao, guiaEstudos)
    trf_PlanoEstudos = tarefaCoordPlanoEstudos(solicitacao, planoEstudos)
    trf_MaterialEstudos = tarefaCoordMaterialEstudos(solicitacao, materialEstudos)
    tarefa_motivador = tarefaCoachMotivacional(coachMotivador)

    # Criando a equipe
    equipe = Crew(
        name='Coordenação de Estudos Especializado',
        description='Uma equipe de especialistas em educação para ajudar estudantes a manterem o foco nos estudos.',
        members=[coordCentral, guiaEstudos, planoEstudos,materialEstudos,coachMotivador],
        tasks=[trf_GuiaEstudos, trf_PlanoEstudos,trf_MaterialEstudos,tarefa_motivador]
  
    )

    return equipe

