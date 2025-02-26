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
with open("saida\material_completo.txt", "w", encoding="utf-8") as arquivo_final:
    arquivo_final.write("\git n\n=== Plano de Estudos ===\n\n")
    with open("saida\PlanoDeEstudo.txt", "r", encoding="utf-8") as plano:
        arquivo_final.write(plano.read())
    
    arquivo_final.write("\n\n=== Material de Estudos ===\n\n")
    with open("saida\VideosYoutube.txt", "r", encoding="utf-8") as material:
        arquivo_final.write(material.read())
    
    arquivo_final.write("\n\n=== Dicas Motivacionais ===\n\n")
    with open("saida\Motivacao.txt", "r", encoding="utf-8") as dicas:
        arquivo_final.write(dicas.read())

import markdown

# 1. Ler o arquivo material_completo.txt
with open("saida\material_completo.txt", "r", encoding="utf-8") as file:
    markdown_text = file.read()

# 2. Converter Markdown para HTML
html_content = markdown.markdown(markdown_text)

# 3. Adicionar estilos básicos ao HTML (opcional)
html_with_style = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Material Completo</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }}
        h1, h2, h3 {{ color: #2c3e50; }}
        code {{ background: #f4f4f4; padding: 2px 5px; border-radius: 3px; }}
        pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }}
        blockquote {{ border-left: 4px solid #ccc; margin: 0; padding-left: 10px; color: #555; }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""

# 4. Salvar o HTML em um arquivo
with open("saida\material_completo.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_with_style)

print("HTML gerado com sucesso! Verifique o arquivo 'material_completo.html'.")
print("Material completo gerado com sucesso! Verifique o arquivo 'material_completo.txt'.")
