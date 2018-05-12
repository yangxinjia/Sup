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
    logger.info('<<=============== new_project request')
    request_body = request.json
    try:
	logger.info('get id and name')
        id = request_body["id"]
	logger.info('get id ok')
        project = request_body["project"]
	logger.info('get name ok')
    except:
	logger.warn('failed')
        resp_dict = {'status': '400', 'message': 'I think you should tell me your project\'s id and name,shouldn\'t you? '}
        logger.warn('return fail info')
	return jsonify(resp_dict)
    logger.info('check id')
    (c_status, c_result) = commands.getstatusoutput('./shell/check_id.sh %s'%id)    
    logger.info('check_id.sh done')
    if c_result != "1": ## if id  exist
	logger.warn('id already exsit')
	logger.warn('new_project failed')
        status = "400"
        message = "id(%s) alreay exist"%id
    else: ##
	logger.info('id not exsit')
    	logger.info('new_project ok')
	(c_status, c_result) = commands.getstatusoutput('./shell/new_project.sh %s %s'%(id,project))
	if c_result == "ok":
	    status = "200"
	    message = "ok"
	else :
	    status = "400"
	    message = c_result
    resp_dict = {'status': status,'id': id, 'message': message, 'project': project}
    logger.info('=================>> return ok')
    return jsonify(resp_dict)
@app.route('/function/view_project', methods = ['POST','GET'])
def view_project():
    try:
	if request.method == "GET": 
	    logger.info('<<=============== view_project request')
	    logger.info('get projects status from server')
	    (r_status, r_pr) = commands.getstatusoutput('./shell/r_pr.sh')
	    (s_status, s_pr) = commands.getstatusoutput('./shell/s_pr.sh')
	    logger.info('get projects status ok')
	    run_projects = r_pr.split()
	    stop_projects = s_pr.split()
	    logger.info('parse running projects info')
	    run_project_id = ""
	    run_return_arr = []
	    for i in range(0,len(run_projects)):
	        project_name = ""
	        project = run_projects[i]
		project_info = project.split('-')
		for j in range(0,len(project_info)):
		    if project_info[j] == "Sup":
			for m in range(0,j):
			    if project_name == "":
				project_name = project_info[m]
			    else:  
				project_name = str(project_name)+"-"+str(project_info[m])
		        project_id = project_info[j+1]
			run_return_project = {"id":project_id, "name":project_name}
			run_return_arr.append(run_return_project)
	    logger.info('parse run_projects ok')
	    stop_project_id = ""
            stop_return_arr = []
	    logger.info('parse stopped projects info')
            for i in range(0,len(stop_projects)):
                project_name = ""
                stop_project = stop_projects[i]
                project_info = stop_project.split('-')
                for j in range(0,len(project_info)):
                    if project_info[j] == "Sup":
                        for m in range(0,j):
                            if project_name == "":
                                project_name = project_info[m]
                            else:  
                                project_name = str(project_name)+"-"+str(project_info[m])
                        project_id = project_info[j+1]
                        stop_return_project = {"id":project_id, "name":project_name}
                        stop_return_arr.append(stop_return_project)
	    logger.info('parse stopped projects ok')
	    logger.info('write resp_dict')
	    resp_dict = {
                "status": "200",
                "message": "ok",
                "running": run_return_arr,
                "stopped": stop_return_arr
            }
	    logger.info('=================>> return ok')
        return jsonify(resp_dict)
    except :
	logger.error('what f*ck an internal err!')
	resp_dict = {
	    "status": "400",
	    "message": "internal err"
	}
	logger.error('=================>> return err')
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
