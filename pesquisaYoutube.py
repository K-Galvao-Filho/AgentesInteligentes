from googleapiclient.discovery import build
from uteis.api_key import YOUTUBE_API_KEY

def pesquisarYoutube(consulta, num_resultados=10):
    """
    Pesquisa vídeos no YouTube com base na consulta fornecida e retorna os resultados.

    Args:
        consulta (str): A consulta de pesquisa.
        chave_api (str): Sua chave de API do YouTube Data.
        num_resultados (int, opcional): Número máximo de resultados a serem retornados. Padrão é 5.

    Returns:
        list: Uma lista de dicionários contendo informações sobre os vídeos.
    """
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    requisicao = youtube.search().list(
        part="snippet",
        maxResults=num_resultados,
        q=consulta
    )

    resposta = requisicao.execute()

    videos = []
    for item in resposta.get("items", []):
        if item["id"]["kind"] == "youtube#video":
            video_info = {
                "Título": item["snippet"]["title"],
                "Descrição": item["snippet"]["description"],
                "URL": f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                "Canal": item["snippet"]["channelTitle"],
                "Publicado em": item["snippet"]["publishTime"]
            }
            videos.append(video_info)

    return videos
