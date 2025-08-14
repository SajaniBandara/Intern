from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/station2')
def station2():
    return render_template('station2.html')

@app.route('/station3')
def station3():
    return render_template('station3.html')

if __name__ == '__main__':
    app.run(debug=True)
