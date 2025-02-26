from equipe import formarEquipe

solicitacao = {
    "disciplina": "Matemática",
    "assunto": "Funções",
    "topicos": ["Função quadrática", "Função exponencial", "Função logarítmica"]
}

def executar_equipe(solicitacao):
    equipe = formarEquipe(solicitacao)  # Aqui, solicitacao precisa ser um dicionário válido
    resultado = equipe.kickoff()
    return resultado

if __name__ == "__main__":
    executar_equipe(solicitacao)  # Passando o dicionário completo, e não apenas a string "Funções"

# Consolidando os resultados
with open("material_completo.txt", "w", encoding="utf-8") as arquivo_final:
    arquivo_final.write("\n\n=== Plano de Estudos ===\n")
    with open("PlanoDeEstudo.txt", "r", encoding="utf-8") as plano:
        arquivo_final.write(plano.read())
    
    arquivo_final.write("\n\n=== Material de Estudos ===\n")
    with open("VideosYoutube.txt", "r", encoding="utf-8") as material:
        arquivo_final.write(material.read())
    
    arquivo_final.write("\n\n=== Dicas Motivacionais ===\n")
    with open("Motivacao.txt", "r", encoding="utf-8") as dicas:
        arquivo_final.write(dicas.read())

print("Material completo gerado com sucesso! Verifique o arquivo 'material_completo.txt'.")