
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from processing import getDV

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def adder_page():
    errors = ""
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

        if seq is not None and ano is not None and seq >=0 and ano > 0:
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
                    <p>23422. <input name="seq" /> / <input name="ano" /> -??</p>
                    <p><input type="submit" value="Calcular DV" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

