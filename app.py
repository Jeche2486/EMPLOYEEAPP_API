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
