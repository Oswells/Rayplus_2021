from flask import Flask, url_for, request, render_template, redirect, session, make_response

import time

app = Flask(__name__)
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=400):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code


@app.errorhandler(InvalidUsage)
def invalid_usage(error):
    response = make_response(error.message)
    response.status_code = error.status_code
    return response
@app.route('/exception')
def exception():
    raise InvalidUsage('No privilege to access the resource', status_code=403)
if __name__ == "__main__":
    app.run(debug=True)