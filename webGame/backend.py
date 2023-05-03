from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/open_tkinter_file/<filename>')
def open_tkinter_file(filename):
    os.system('python ' + filename)

if __name__ == '__main__':
	app.run(host='127.0.0.1',port=5500)