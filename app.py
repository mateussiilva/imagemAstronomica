from flask import Flask,render_template
from backend.main import InformacoesPostagem


app = Flask(__name__)

conteudo = """
Why would the sky look like a giant target? Airglow. Following a giant thunderstorm over Bangladesh in late April, giant circular ripples of glowing air appeared over Tibet, China, as pictured here. The unusual pattern is created by atmospheric gravity waves, waves of alternating air pressure that can grow with height as the air thins, in this case about 90-kilometers up.  Unlike auroras powered by collisions with energetic charged particles and seen at high latitudes, airglow is due to chemiluminescence, the production of light in a chemical reaction.  More typically seen near the horizon, airglow keeps the night sky from ever being completely dark.



"""


dados_post = InformacoesPostagem(title_post='Airglow Ripples over Tibet', url_image='https://apod.nasa.gov/apod/image/2211/rippledsky_dai_960.jpg', content=conteudo)



@app.route("/")
def home(nome="Pagina Inicial", title="", image=''):
    return render_template("index.html", name_page=nome, titulo_pagina=dados_post.title_post, image=dados_post.url_image, conteudo_site=dados_post.content)

