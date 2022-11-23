from flask import Flask,render_template
from flask_bootstrap import Bootstrap
# from backend.main import InformacoesPostagem


app = Flask(__name__)
Bootstrap(app)


# dados_post = InformacoesPostagem(title_post='Airglow Ripples over Tibet', url_image='https://apod.nasa.gov/apod/image/2211/rippledsky_dai_960.jpg', content=conteudo)



title_post = 'A Double Star Cluster in Perseus'
url_image = "https://apod.nasa.gov/apod/image/2211/DoubleCluster_Lease_3756.jpg"

@app.route("/")
def home(title_post=title_post, url_image=url_image):
    return render_template("index.html", titulo_pagina=title_post, image=url_image)

