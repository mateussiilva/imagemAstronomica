from flask import Flask,render_template
from backend.main import InformacoesPostagem


app = Flask(__name__)
dados_post = InformacoesPostagem(title_post='Airglow Ripples over Tibet', url_image='https://apod.nasa.gov/apod/image/2211/rippledsky_dai_960.jpg')



@app.route("/")
def home(nome="Pagina Inicial", title="", image=''):
    return render_template("index.html", name_page=nome, titulo_pagina=dados_post.title_post, image=dados_post.url_image)

