
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
from processing import getDV

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
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
                    <body>
                        <p>O NUP com DV é {uni:05d}.{seq:06d}/{ano:04d}-{dv:02d}</p>
                        <p><a href="/">Clique aqui para calcular DV novamente.</a>
                    </body>
                </html>
            '''.format(uni=uni, seq=seq, ano=ano, dv=dv)

    return '''
        <html>
            <body>
                {erros}
                <p>Complete o NUP que deseja saber o DV:</p>
                <form method="post" action=".">
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

@app.route('/teste', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("main_page.html", errors=errors, NUP=NUP)
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
