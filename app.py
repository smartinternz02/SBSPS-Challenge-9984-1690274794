from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/dashboards')
def dashboards():
    return render_template('dashboards.html')

@app.route('/stories')
def stories():
    return render_template('stories.html')

if __name__ == '__main__':
    app.run(debug=True)