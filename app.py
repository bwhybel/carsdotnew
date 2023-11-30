from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        color = request.form['color']
        return redirect(url_for('built', make=make, model=model, year=year, color=color))

@app.route('/built')
def built():
    make = request.args.get('make', default='mazda', type=str)
    model = request.args.get('model', default='miata', type=str)
    year = request.args.get('year', default=2007, type=int)
    color = request.args.get('color', default='blue', type=str)
    return "New Car!! A {color} {year} {make} {model}!".format(make=make, model=model, year=year, color=color)
