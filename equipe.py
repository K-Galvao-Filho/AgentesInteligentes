from crewai import Crew

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

from pesquisaYoutube import pesquisarYoutube

def formarEquipe(solicitacao):

    disciplina = solicitacao['disciplina']
    assunto = solicitacao['assunto']
    topicos = ', '.join(solicitacao['topicos'])
    entradaYoutube = f"{disciplina}, {assunto}, {topicos}"
    
    saidaYoutube = pesquisarYoutube(entradaYoutube)

    # Criando agentes
    coordCentral = chamaCoordenadorEquipe()
    coachMotivador = chamaCoachMotivacional()
    guiaEstudos = chamaCoordGuiaEstudos(solicitacao)
    planoEstudos = chamaCoordPlanoEstudos(solicitacao)
    materialEstudos = chamaCoordMaterialEstudos(solicitacao)
        
    # Criando tarefas
    tarefa_motivador = tarefaCoachMotivacional(coachMotivador)
    trf_GuiaEstudos = tarefaCoordGuiaEstudos(solicitacao, guiaEstudos)
    trf_PlanoEstudos = tarefaCoordPlanoEstudos(solicitacao, planoEstudos)
    trf_MaterialEstudos = tarefaCoordMaterialEstudos(saidaYoutube, materialEstudos)
    

    # Criando a equipe
    equipe = Crew(
        name='Coordenação de Estudos Especializado',
        description='Uma equipe de especialistas em educação para ajudar estudantes a manterem o foco nos estudos.',
        members=[coordCentral, coachMotivador, guiaEstudos, planoEstudos,materialEstudos],
        tasks=[tarefa_motivador, trf_GuiaEstudos, trf_PlanoEstudos,trf_MaterialEstudos]
  
    )

    return equipe

