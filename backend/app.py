#!/usr/bin/python3

from flask import Flask, request, jsonify
import os

application = Flask(__name__)

#app.config["MYSQL_URI"] = 'mongodb://' + os.environ.get('MONGODB_USERNAME') + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

@application.route('/persons/', methods=['GET'])
def getPersons():
  return jsonify(
    Firstname= 'Hello',
    Lastname= 'World!'
  )

@application.route('/person/', methods=['POST'])
def createPerson():
  data = request.get_json(force=True)
  person = {
    'PersonID': 0,
    'Firstname': data['Firstname'],
    'Lastname': data['Lastname']
  }

  return jsonify(person), 201

if __name__ == '__main__':
  ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
  ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
  application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)