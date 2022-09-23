from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def paginaum():
    return render_template('paginaum.html')



@app.route('/feminina', methods=['GET', 'POST'])
def feminina():
    return render_template('feminina.html')


@app.route('/juvenil', methods=['GET', 'POST'])
def juvenil():
    return render_template('juvenil.html')




if __name__ == '__main__':
    app.run(debug=True)