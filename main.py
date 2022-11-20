import requests as re
import json as js 
from os import system, rename, path

def baixarImagem(url):
    image = system(f"wget --no-verbose {url}")
    return image
def renomearImage(old_name, new_name):
    rename(src=old_name,dst=new_name )

key = "KrL7X150niTvBvtXjOM1GyGfzocWyOTZPrsC4Ki4"
url_base = f"https://api.nasa.gov/planetary/apod?api_key={key}"

content = re.get(url_base)
informacao_postagem = {}


if content.status_code == 200:
    json_file = content.json()
    for k,v in json_file.items():
        if k == 'copyright':
            informacao_postagem["copyright"] = v
        elif k == 'date':
            informacao_postagem["data"] = v
        elif k == 'explanation':
            informacao_postagem["conteudo"] = v
        elif k == 'hdurl':
            informacao_postagem["url_image"] = v
        elif k == 'title':
            informacao_postagem["titulo"] = v



nome_imagem = f"{informacao_postagem['data']}+imagem.jpg"
image_padrao = baixarImagem(informacao_postagem["url_image"])
# renomearImage(image_padrao, nome_imagem)
print(image_padrao)