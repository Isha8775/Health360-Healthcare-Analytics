from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clinical')
def clinical():
    return render_template('clinical.html')

@app.route('/lifestyle')
def lifestyle():
    return render_template('lifestyle.html')

@app.route('/population')
def population():
    return render_template('population.html')

@app.route('/story')
def story():
    return render_template('story.html')

if __name__ == '__main__':
    app.run(debug=True)