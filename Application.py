from flask import Flask
#from views import view 


application = Flask(__name__)

@application.route('/')

def hello():
    return 'high'

#application.register_blueprint(view, url_prefix="/")

#if __name__ == '__main__':
 #   application.run(debug=True)
