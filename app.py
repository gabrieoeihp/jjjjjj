from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ligar')
def ligar():
    return render_template('clicar.html')

if __name__ == '__main__':
    app.run()
