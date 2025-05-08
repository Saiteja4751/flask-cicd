from flask import *

app = Flask(__name__)

@app.route('/first')
def template():
    return render_template('index.html')
@app.route('/')
def hello_world():
    return 'added sucessfully with sowmya'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
