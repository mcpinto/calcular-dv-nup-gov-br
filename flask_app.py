
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
from processing import getDV

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def adder_page():
    errors = ''
    if request.method == "POST":
        seq = None
        ano = None
        try:
            seq = int(request.form["seq"])
        except:
            errors += "<p>{!r} não é um código sequencial válido.</p>\n".format(request.form["seq"])
        try:
            ano = int(request.form["ano"])
        except:
            errors += "<p>{!r} não é um ano válido.</p>\n".format(request.form["ano"])

        if seq is not None and ano is not None and seq >=0 and ano >= 0:
            dv = getDV(seq, ano)
            return '''
                <html>
                    <body>
                        <p>O NUP com DV é 23422.{seq:06d}/{ano:04d}-{dv:02d}</p>
                        <p><a href="/">Clique aqui para calcular DV novamente.</a>
                    </body>
                </html>
            '''.format(seq=seq, ano=ano, dv=dv)

    return '''
        <html>
            <body>
                {errors}
                <p>Complete o NUP que deseja saber o DV:</p>
                <form method="post" action=".">
                    <p>23422. <input name="seq" type="number" min="0" max="999999" size="6" autofocus /> / <input name="ano" type="number" min="0" max="9999" size="4" value="2023" /> -??</p>
                    <p><input type="submit" value="Calcular DV" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

errors = []
NUP = ['23422', '000000', '0000', '00']


@app.route('/teste', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("main_page.html", errors=errors, NUP=NUP)
    seq = None
    ano = None
    try:
        seq = int(request.form["seq"])
    except:
        errors.append("<p>{!r} não é um código sequencial válido.</p>\n".format(request.form["seq"]))
    try:
        ano = int(request.form["ano"])
    except:
        errors.append("<p>{!r} não é um ano válido.</p>\n".format(request.form["ano"]))

    if seq is not None and ano is not None:
        if 0 <= seq <= 999999 and 0 <= ano <= 9999:
            NUP[1] = '{:06d}'.format(seq)
            NUP[2] = '{:04d}'.format(ano)
            NUP[3] = '{:02d}'.format(getDV(seq, ano))
        else:
            if seq < 0 or seq > 999999:
                errors.append("<p>{} não é um ano válido.</p>\n".format(seq))
            if ano < 0 or ano > 9999:
                errors.append("<p>{} não é um ano válido.</p>\n".format(ano))

    return redirect(url_for('index'))
