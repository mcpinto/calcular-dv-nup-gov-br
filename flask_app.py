# Duas versões: uma simples e outra mais explicativa para calcular DV de NUP
from flask import Flask, redirect, render_template, request, url_for
from processing import getDV

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home_page():
    return '''
        <!doctype html>
        <html>
            <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">
                <link rel="shortcut icon" type="image/x-icon" href="https://python.org/static/favicon.ico">
                <title>Página Inicial</title>
            </head>
            <body>
            <nav class="navbar navbar-inverse">
                <div class="container">
                    <div class="navbar-header">
                        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                            <span class="sr-only">Toggle navigation</span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </button>
                        <a class="navbar-brand" href=".">Página Inicial</a>
                    </div>
                </div>
            </nav>
            <div class="container">
                <div class="row">
                    <p>&nbsp;</p>
                    <p>Calcular DV de NUP da Administração Pública federal - formato <a href="./simples">simples</a></p>
                    <p>Calcular DV de NUP da Administração Pública federal - formato <a href="./calcula-dv-nup">explicativo</a></p>
                    <p>&nbsp;</p>
                    <p>&nbsp;</p>
                </div>
                <footer class="text-center text-lg-start">
                    <a href="https://unlicense.org/"><img src="./static/images/no-copyright-196p.png" alt="Say No to Copyright" title="Say No to Copyright" width="50p" height="50p" /></a>
                    <a href="https://creativecommons.org/publicdomain/zero/1.0/deed.pt_BR">Nenhum direito reservado</a>.
                </footer>
            </div><!-- /.container -->
            </body>
        </html>
        '''

@app.route('/simples', methods=['GET', 'POST'])
def adder_page():
    erros = ''
    if request.method == "POST":
        uni = None
        seq = None
        ano = None
        try:
            uni = int(request.form["uni"])
        except:
            erros += "<p>{!r} não é um código de unidade válido.</p>\n".format(request.form["uni"])
        try:
            seq = int(request.form["seq"])
        except:
            erros += "<p>{!r} não é um código sequencial válido.</p>\n".format(request.form["seq"])
        try:
            ano = int(request.form["ano"])
        except:
            erros += "<p>{!r} não é um ano válido.</p>\n".format(request.form["ano"])

        if uni is not None and seq is not None and ano is not None and uni >= 0 and seq >= 0 and ano >= 0:
            dv = getDV(uni, seq, ano)
            return '''
                <html>
                    <head>
                        <meta charset="utf-8">
                        <title>Calcular DV de NUP da Administração Pública federal</title>
                    </head>
                    <body>
                        <p>O NUP com DV é {uni:05d}.{seq:06d}/{ano:04d}-{dv:02d}</p>
                        <p>&nbsp;</p>
                        <p><a href="./simples">Clique aqui para calcular DV novamente.</a></p>
                    </body>
                </html>
            '''.format(uni=uni, seq=seq, ano=ano, dv=dv)

    return '''
        <html>
            <head>
                <meta charset="utf-8">
                <title>Calcular DV de NUP da Administração Pública federal</title>
            </head>
            <body>
                {erros}
                <p>&nbsp;</p>
                <p>Complete o NUP que deseja saber o DV:</p>
                <form method="post" action="./simples">
                    <p><input name="uni" type="number" min="0" max="99999" size="5" value="23422" /> .
                    <input name="seq" type="number" min="0" max="999999" size="6" autofocus /> /
                    <input name="ano" type="number" min="0" max="9999" size="4" value="2023" /> -??</p>
                    <p><input type="submit" value="Calcular DV" /></p>
                </form>
            </body>
        </html>
    '''.format(erros=erros)

errors = []
NUP = ['00000', '000000', '0000', '00']

@app.route('/calcula-dv-nup', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        tmp1 = errors.copy()
        tmp2 = NUP.copy()
        errors.clear()
        NUP[3] = '00'
        return render_template("main_page.html", errors=tmp1, NUP=tmp2)
    errors.clear()
    NUP[3] = '00'
    uni = None
    seq = None
    ano = None
    try:
        uni = int(request.form["uni"])
    except:
        errors.append("{!r} não é um código de unidade válido.".format(request.form["uni"]))
    try:
        seq = int(request.form["seq"])
    except:
        errors.append("{!r} não é um código sequencial válido.".format(request.form["seq"]))
    try:
        ano = int(request.form["ano"])
    except:
        errors.append("{!r} não é um ano válido.".format(request.form["ano"]))

    if uni is not None and seq is not None and ano is not None:
        if 0 <= uni <= 99999 and 0 <= seq <= 999999 and 0 <= ano <= 9999:
            NUP[0] = '{:05d}'.format(uni)
            NUP[1] = '{:06d}'.format(seq)
            NUP[2] = '{:04d}'.format(ano)
            NUP[3] = '{:02d}'.format(getDV(uni, seq, ano))
        else:
            if uni < 0 or uni > 99999:
                errors.append("{} não é código de unidade válido.".format(uni))
            if seq < 0 or seq > 999999:
                errors.append("{} não é código sequencial válido.".format(seq))
            if ano < 0 or ano > 9999:
                errors.append("{} não é ano válido.".format(ano))

    return redirect(url_for('index'))
