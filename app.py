#there are two ways of creating REST apis in flask
#1. using flask without any external library
#2. using flask_restful 

#we will use the #2


#flask_restful can be installed via the pip command:
#pip3 install flask-restful

from flask import *
#import pymysql for database connect
import pymysql
from flask_restful import Resource, Api


# create a flask app
app = Flask(__name__)

# create an api object 
api = Api(app)

#we need to make a class for a particular resource
# the class will inherit from the Resource thus implementing post, get, delete, put request methods

class Employees(Resource):
    def get(self):
        return jsonify({"message" : "GET REQUEST"})
    
    def post(self):
        return jsonify({"message" : "POST REQUEST"})
    
    def put(self):
        return jsonify({"message" : "PUT REQUEST"})
    
    def delete(self):
        return jsonify({"message" : "DELETE REQUEST"})
    
    # we need to add our resource/class that we defined along with its corresponding url

    api.add_resource(Employees, '/employees')

    if __name__ == '__main__':
        app.run(debug=True)
