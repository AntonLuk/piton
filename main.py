from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    a = 4
    b = 10 - a
    return 'Hello, %s!' % 'Vasya'

if __name__ == '__main__':
    app.run()