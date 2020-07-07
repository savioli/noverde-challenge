import os
import json

from flask import Flask
from controllers import LoanRequestController

# application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

server = Flask(__name__)

# Gets the environment variables and passes to the configuration

# App configuration
server.config['MODE'] = os.environ['MODE']
server.config['STORAGE'] = os.environ['STORAGE']
server.config['DEBUG'] = os.environ['DEBUG']

if os.environ['X_API_KEY'] == '' :

    server.config['X_API_KEY'] = None

else:

    server.config['X_API_KEY'] = os.environ['X_API_KEY']

# MongoDB Configuration
server.config['MONGODB_HOSTNAME'] = os.environ['MONGODB_HOSTNAME']
# server.config['MONGO_INITDB_ROOT_USERNAME'] = os.environ['MONGO_INITDB_ROOT_USERNAME']
# server.config['MONGO_INITDB_ROOT_PASSWORD'] = os.environ['MONGO_INITDB_ROOT_USERNAME']
# server.config['MONGODB_DATABASE'] = os.environ['MONGODB_DATABASE']
# server.config['MONGO_INITDB_DATABASE'] = os.environ['MONGO_INITDB_DATABASE']

# Redis Configuration
server.config['REDIS_HOSTNAME'] = os.environ['REDIS_HOSTNAME']
# server.config['MONGO_INITDB_ROOT_USERNAME'] = os.environ['MONGO_INITDB_ROOT_USERNAME']
# server.config['MONGO_INITDB_ROOT_PASSWORD'] = os.environ['MONGO_INITDB_ROOT_USERNAME']
# server.config['MONGODB_DATABASE'] = os.environ['MONGODB_DATABASE']
# server.config['MONGO_INITDB_DATABASE'] = os.environ['MONGO_INITDB_DATABASE']

# RabbitMQ
server.config['RABBITMQ_DEFAULT_USER'] = os.environ['RABBITMQ_DEFAULT_USER']
server.config['RABBITMQ_DEFAULT_PASS'] = os.environ['RABBITMQ_DEFAULT_PASS']
server.config['RABBITMQ_HOSTNAME'] = os.environ['RABBITMQ_HOSTNAME']

# Celery Flower
# server.config['CELERY_BROKER'] = os.environ['CELERY_BROKER']
# server.config['FLOWER_BROKER'] = os.environ['FLOWER_BROKER']

server.secret_key = os.environ['SECRET_KEY']

API_VERSION = '1'

# POST
app_apply_for_loan_route = '/v' + '{}' + '/loan'
route = app_apply_for_loan_route.format(API_VERSION)

try:
    
    view_func = LoanRequestController.as_view('app_apply_for_loan_route')
    
    server.add_url_rule(rule=route, view_func=view_func)

except Exception as e:
    pass

# GET
app_consult_loan_route = '/v' + '{}' + '/loan/<string:uuid>'
route = app_consult_loan_route.format(API_VERSION)

try:
    
    view_func = LoanRequestController.as_view('app_consult_loan_route')
    
    server.add_url_rule(rule=route, view_func=view_func)

except Exception as e:
    pass


