#!/usr/bin/python3

from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
import os

application = Flask(__name__)

application.config['MYSQL_DATABASE_USER'] = os.environ['MYSQL_DATABASE_USER']
application.config['MYSQL_DATABASE_PASSWORD'] = os.environ['MYSQL_DATABASE_PASSWORD']
application.config['MYSQL_DATABASE_DB'] = os.environ['MYSQL_DATABASE_DB']
application.config['MYSQL_DATABASE_HOST'] = os.environ['MYSQL_DATABASE_HOST']
application.config['MYSQL_DATABASE_PORT'] = int(os.environ['MYSQL_DATABASE_PORT'])

mysql = MySQL()
mysql.init_app(application)

@application.route('/persons/', methods=['GET'])
def getPersons():
  try:
    conn = mysql.connect()
    cur = mysql.get_db().cursor()
    cur.execute('SELECT * FROM persons')
    rows = cur.fetchall()
    response = jsonify(rows)
    response.status_code = 200
    return response
  except Exception as e:
    print(e)
    return str(e), 500

@application.route('/person/', methods=['POST'])
def createPerson():
  try:
    conn = mysql.connect()
    cur = mysql.get_db().cursor()
    data = request.get_json(force=True)

    cur.execute('INSERT INTO persons (Firstname, Lastname) VALUES (%(firstname)s, %(lastname)s)', { 'firstname': data['Firstname'], 'lastname': data['Lastname']})
    conn.commit()
    response = ''
    response.status_code = 201
    return response
  except Exception as e:
    print(e)
    return str(e), 500

if __name__ == '__main__':
  ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
  ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
  application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)