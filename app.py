from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        description = request.form['description']
        return redirect(url_for('submit', make=make, model=model, year=year, description=description))

@app.route('/built')
def submit():
    make = request.args.get('make')
    model = request.args.get('model')
    year = request.args.get('year')
    description = request.args.get('description')
    return render_template('built.html', make=make, model=model, year=year, description=description)
