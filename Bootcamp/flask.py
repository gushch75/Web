from flask import Flask
app = Flask(__name__)
@app.route('/')
def main():
    return'Hello world'

    if _name_=='_main_':
        app.run