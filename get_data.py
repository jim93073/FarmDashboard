import inspect
import json
import os
from datetime import datetime
from dateutil import parser
from functools import wraps

from flask import (Flask, abort, jsonify, redirect, g,
                   render_template as flast_render_template,
                   request, send_from_directory, session)
from sqlalchemy import text
from werkzeug.security import check_password_hash, generate_password_hash
import datetime, calendar
import config
import db
import utils

app = Flask(__name__)
app.secret_key = config.FLASK_SECRET_KEY
db.connect()

def get_temp(start='2021-05-10',end='2021-05-18'):
    labels_temp = []
    data_temp = []
    data = db.get_datas('Mushroom','temperature1',start,end)
    for d in data:
        labels_temp.append(str(d[1]))
        data_temp.append(str(d[2]))
    return labels_temp, data_temp

def get_hum(start='2021-05-10',end='2021-05-18'):
    labels_hum = []
    data_hum = []
    data = db.get_datas('Mushroom','humidity',start,end)
    for d in data:      
        labels_hum.append(str(d[1]))
        data_hum.append(str(d[2]))
    print(labels_hum)
    print(data_hum)
    return labels_hum, data_hum

def get_CO2(start='2021-05-10',end='2021-05-18'):
    labels_CO2 = []
    data_CO2 = []
    data = db.get_datas('Mushroom','co2',start,end)
    for d in data:
        labels_CO2.append(str(d[1]))
        data_CO2.append(str(d[2]))
    return labels_CO2, data_CO2

@app.route('/mushroom_chart', methods=['GET'])
def index():
      
    labels_temp, data_temp = get_temp()
    labels_hum, data_hum = get_hum()
    labels_CO2, data_CO2 = get_CO2()
    

    return flast_render_template('mushroom.html',
    mushroom_img_name=json.dumps(mushroom_img_name),
    labels_temp = json.dumps(labels_temp),
    labels_hum = json.dumps(labels_hum),
    labels_CO2 = json.dumps(labels_CO2),
    data_temp = json.dumps(data_temp),
    data_hum = json.dumps(data_hum),
    data_CO2 = json.dumps(data_CO2)
    )

@app.route('/post_date', methods=['GET'])
def set_date():
    start_time = request.args.get('start-time')
    end_time = request.args.get('end-time')
  
    start_time_formate = datetime.datetime.strptime(start_time, '%Y-%m-%d' )
    end_time_formate = datetime.datetime.strptime(end_time, '%Y-%m-%d' )
    delta_day = end_time_formate - start_time_formate
    
    mushroom_img_name = [(end_time_formate - datetime.timedelta(days=x)).strftime("%Y-%m-%d") for x in range(delta_day.days)]
    mushroom_img_name.reverse()
   
    labels_temp, data_temp = get_temp(start_time,end_time)
    labels_hum, data_hum = get_hum(start_time,end_time)
    labels_CO2, data_CO2 = get_CO2(start_time,end_time)
    
    
    return flast_render_template('mushroom.html',
    mushroom_img_name=json.dumps(mushroom_img_name),
    labels_temp = json.dumps(labels_temp),
    labels_hum = json.dumps(labels_hum),
    labels_CO2 = json.dumps(labels_CO2),
    data_temp = json.dumps(data_temp),
    data_hum = json.dumps(data_hum),
    data_CO2 = json.dumps(data_CO2))


def main():
    app.run('0.0.0.0', port=6688,debug=config.DEBUG, threaded=True)


if __name__ == '__main__':
    main()
    # print(db.get_datas('Mushroom','Temperature1','2021-05-17','2021-05-18')[0][1])
    # curl_server = engine.execute('select * from Mushroom')

