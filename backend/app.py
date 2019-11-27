#!/usr/bin/python3

from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)
CORS(app)

def getMysqlConnection():
  return mysql.connector.connect(host='database', database=os.environ.get('MYSQL_DATABASE_DB', 'persons'), user=os.environ.get('MYSQL_DATABASE_USER', 'root'), password=os.environ.get('MYSQL_DATABASE_PASSWORD', ''))

@app.route('/persons/', methods=['GET'])
def getPersons():
  try:
    conn = getMysqlConnection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM person')
    row_headers=[x[0] for x in cur.description]
    rows = cur.fetchall()
    json_data=[]
    for result in rows:
      json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)
    cur.close()
    conn.close()
  except Exception as e:
    print(e)
    return str(e), 500

@app.route('/person', methods=['POST'])
def createPerson():
  try:
    conn = getMysqlConnection()
    cur = conn.cursor()
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')

    cur.execute('INSERT INTO person (Firstname, Lastname) VALUES (%(firstname)s, %(lastname)s)', { 'firstname': firstname, 'lastname': lastname})
    conn.commit()
    return Response('', 200)
    cur.close()
    conn.close()
  except Exception as e:
    print(e)
    return str(e), 500

if __name__ == '__main__':
  ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
  ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
  app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)