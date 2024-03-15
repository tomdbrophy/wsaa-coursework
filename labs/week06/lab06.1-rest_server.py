from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/books', methods=['GET'])
def getall():
    return 'get all'

@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
    return 'find by id'

@app.route('/books', methods=['POST'])
def create():
    # read in json from the body
    jsonstring = request.json
    return f'create {jsonstring}'

@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json
    return f'update {id} {jsonstring}'

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return f'delete {id}'

if __name__ == '__main__':
    app.run(debug = True)