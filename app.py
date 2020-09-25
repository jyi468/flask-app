from flask import Flask, jsonify, request

app = Flask(__name__)

# export FLASK_APP=app.py
# export FLASK_ENV=development
# export FLASK_RUN_PORT=5000
# 200 - Success
# 404 - Not found
# 405 - Not allowed
@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/hithere')  # Return resource at route hithere
def hi_there_everyone():
    return 'I just hit /hithere'


"""
All communications between server/server, server/browser, browser/browser can only be done via TEXT 
Can send representations of image, videos via text but can't actually send that image
This is because of TCP
Therefore, an image/video of a page could be :
- 2d array text of RGB values

This is why we use JSON to communicate
"""


@app.route('/add_two_nums', methods=["POST"])  # Could add "GET" to methods if we wanted to allow
def add_two_nums():
    # Get x, y from post data
    dataDict = request.get_json()
    if 'y' not in dataDict:
        return 'ERROR', 305
    x = dataDict['x']
    y = dataDict['y']

    # add z = x + y
    z = x + y

    # Prepare a JSON
    retJSON = {
        'z': z
    }
    # return jsonifyied json
    return jsonify(retJSON), 200


@app.route('/bye')
def bye():
    # Prepare response for request that came to /bye
    # Return usually string, JSON, page
    c = 2*123
    s = str(c)
    # c = 1/0
    retJson = {
        'field1': 'abc',
        'field2': 'def'
    }
    return jsonify(retJson)


if __name__ == "__main__":
    app.run(debug=True, port=6000)  # important to set this to true to debug any errors
