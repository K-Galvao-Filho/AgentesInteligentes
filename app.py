import os
import markdown
import gradio as gr
from xhtml2pdf import pisa
from equipe import formarEquipe

def converter_html_para_pdf(source_html, output_filename):
    """
    Converte uma string de HTML para PDF e salva no arquivo output_filename.
    Retorna 0 em caso de sucesso ou um valor diferente de 0 em caso de erro.
    """
    with open(output_filename, "wb") as output_file:
        pisa_status = pisa.CreatePDF(source_html, dest=output_file)
    return pisa_status.err

def executar_equipe_interface(disciplina, assunto, topicos_str):
    # Converter a string de tópicos para uma lista
    topicos = [t.strip() for t in topicos_str.split(',') if t.strip()]
    
    # Construir o dicionário de solicitação conforme esperado
    solicitacao = {
        "disciplina": disciplina,
        "assunto": assunto,
        "topicos": topicos
    }
    
    # Executar a rotina da equipe
    equipe = formarEquipe(solicitacao)
    equipe.kickoff()
    
    # Garantir que o diretório de saída exista
    output_folder = "saida"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Consolidar os materiais em um arquivo Markdown
    markdown_path = os.path.join(output_folder, "material_completo.txt")
    with open(markdown_path, "w", encoding="utf-8") as arquivo_final:
        arquivo_final.write("\n\n=== Dicas Motivacionais ===\n\n")
        with open(os.path.join(output_folder, "Motivacao.txt"), "r", encoding="utf-8") as dicas:
            arquivo_final.write(dicas.read())        
        
        arquivo_final.write("\n\n=== Plano de Estudos ===\n\n")
        with open(os.path.join(output_folder, "PlanoDeEstudo.txt"), "r", encoding="utf-8") as plano:
            arquivo_final.write(plano.read())
        
        arquivo_final.write("\n\n=== Material de Estudos ===\n\n")
        with open(os.path.join(output_folder, "VideosYoutube.txt"), "r", encoding="utf-8") as material:
            arquivo_final.write(material.read())
        
    # Ler o conteúdo Markdown para exibição
    with open(markdown_path, "r", encoding="utf-8") as f:
        markdown_text = f.read()
    
    # Converter Markdown para HTML
    html_content = markdown.markdown(markdown_text)
    html_with_style = f"""  <!DOCTYPE html>
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
                            </html>"""
    
    # Salvar o HTML gerado
    html_path = os.path.join(output_folder, "material_completo.html")
    with open(html_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_with_style)
    
    # Converter o HTML para PDF usando xhtml2pdf
    pdf_path = os.path.join(output_folder, "material_completo.pdf")
    erro = converter_html_para_pdf(html_with_style, pdf_path)
    if erro:
        pdf_path = None  # Em caso de erro, retorna None para o PDF
    
    # Retornar o conteúdo Markdown para visualização e o caminho do PDF para download
    return markdown_text, pdf_path

iface = gr.Interface(
    fn=executar_equipe_interface,
    inputs=[
        gr.Textbox(label="Disciplina", value="Matemática"),
        gr.Textbox(label="Assunto", value="Funções"),
        gr.Textbox(label="Tópicos (separados por vírgula)", value="Função quadrática, Função exponencial, Função logarítmica")
    ],
    outputs=[
        gr.Markdown(label="Material Completo (Markdown)"),
        gr.File(label="Download do PDF")
    ],
    title="Interface - Material de Estudos",
    #description="Interface para gerar material de estudo em Markdown e converter para PDF, utilizando xhtml2pdf (sem necessidade de instalações externas)."
)

iface.launch()
