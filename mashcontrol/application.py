from flask import Flask, url_for, redirect
import settings

application = Flask(__name__)


@application.route('/')
def index():
    return redirect(url_for('static',filename='index.html'))

if __name__ == '__main__':
    
    application.debug = settings.DEBUG
    application.run("0.0.0.0")