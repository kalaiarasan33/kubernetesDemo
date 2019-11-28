import sys
import logging
import rds_config
import pymysql
#rds settings


rds_host  = "mysql"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    print("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

"""
def lambda_handler(event, context):
    user=event['user']
    email=event['email']
    feedback=event['feedback']
    phone=event['phone']  
    s="Insert into `AuroraDemoDB`  values ('{}','{}','{}','{}')".format(user,email,feedback,phone)

    with conn.cursor() as cur:
      cur.execute(s)
      conn.commit()
        
    conn.commit()

    return "your feedback has been updated"

"""

from flask import Flask, render_template, redirect, url_for, session, flash,request
import requests
import json



app = Flask(__name__)


@app.route('/test', methods=['POST'])
def api():
    user=request.form['user']  
    email=request.form['email']
    feedback=request.form['feedback']
    phone=request.form['phone']
    s="Insert into `AuroraDemoDB`  values ('{}','{}','{}','{}')".format(user,email,feedback,phone)
    with conn.cursor() as cur:
      cur.execute(s)
      conn.commit()
        
    conn.commit()

    return "your feedback has been updated"
    


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

    
