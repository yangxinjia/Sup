# coding:utf-8
#!/usr/sbin/env python
import json
import os
import commands
import logging
import sys
from collections import OrderedDict
from flask import Flask, jsonify, request
from check import check
from function_test import *

logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
file_handler = logging.FileHandler("test.log")
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)

app = Flask(__name__)
@app.route('/ctl/new_project', methods = ['POST'])
def new_project():
    logger.info('new_project request')
    request_body = request.json
    try:
	logger.info('get id and name')
        id = request_body["id"]
        project = request_body["project"]
	logger.info('success')
    except:
	logger.warn('failed')
        resp_dict = {'status': '400', 'message': 'I think you should tell me your project\'s id and name,shouldn\'t you? '}
        return jsonify(resp_dict)
	logger.warn('return fail info')
    logger.info('check id')
    (c_status, c_result) = commands.getstatusoutput('./shell/check_id.sh %s'%id)    
    logger.info('check_id.sh done')
    if c_result != "": ## if id  exist
	logger.warn('id already exsit')
	logger.error('new_project failed')
        status = "400"
        message = "id(%s) alreay exist"%id
    else: ##
	logger.info('id not exsit')
        status = "200"
        message ="ok"
    	logger.warn('new_project ok')
    resp_dict = {'status': status,'id': id, 'message': message, 'project': project}
    return jsonify(resp_dict)
    logger.info('return ok')
@app.route('/function/view_project', methods = ['POST','GET'])
def view_project():
    try:
	if request.method == "GET": 
	    (r_status, r_pr) = commands.getstatusoutput('./shell/r_pr.sh')
	    (s_status, s_pr) = commands.getstatusoutput('./shell/s_pr.sh')
	    resp_dict = {
                "status": "200",
                "message": "ok",
                "running": {
		    "id": "123",
		    "project": ""
	            },
                "stopped": s_pr
            }
        return jsonify(resp_dict)
    except :
	resp_dict = {
	    "status": "400",
	    "message": "internal err"
	}
	return jsonify(resp_dict)
    #return json.dumps(resp_dict,sort_keys=True,indent=4)
@app.route('/function/view_case', methods = ['POST','GET'])
def view_case():
    if request.method == "GET": 
        return "Oh my friend ! Why do you GET a POST interface"
    if request.method == "POST":
        request_body = request.json
        try:
            id = request_body["id"]
        except:
            id = None
        try:
            project = request_body["project"]
        except:
            project = None
        if id == None and project == None :
            code = 400
            message = "Please tell me your project's id/name"
        else :
            a=1

@app.route('/function/test', methods = ['POST','GET'])
def test():
    if request.method == "GET": 
        return "Oh my friend ! Why do you GET a POST interface"
    if request.method == "POST":
        request_body = request.json
        id = request_body["id"]
        project = request_body["project"]
        func = []
        func = request_body["function"]

        test = check()
    resp_dict = {
            "status": "12345",
            "id": id,
            "project": "ise",
            "result": url
    }
    return json.dumps(resp_dict,sort_keys=True,indent=4,mimetype='application/json')
app.Debug = True
app.run(host = '0.0.0.0', port = 6000)
logger.removeHandler(file_handler)
#if __name__ == "__main__":
#    port = 5013
#    httpd = make_server("0.0.0.0", port, application)
#    print "serving http on port {0}...".format(str(port))
#    httpd.serve_forever()
