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
        description = request.form['description']
        # Here you can handle the data. For example, store it in a database.
        print(f'{make} {model} {year} {description}')
        return 'Created a new car listing!'
