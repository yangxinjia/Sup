# -*- coding: utf8 -*-

import requests
import json
import os
import time
import sys
from sys import argv

def check():
	try:## 待优化
		url = 'http://39.104.109.10:8501'
		url = url + '/rec/image'
		e_face_num = 9
		e_img_cutboard = []
		e_face_cutboard = [[604, 542, 158, 137], [1007, 335, 116, 107], [1176, 366, 103, 97], [670, 363, 99, 94], [1054, 203, 93, 87], [695, 180, 83, 79], [538, 292, 84, 78], [280, 214, 57, 60], [2, 271, 52, 59]]
		e_age = [26, 26, 29, 41, 36, 41, 58, 30, 39, 0, 0, 0]
		e_sex = [2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1]
		age_diff = 0
		cutboard_diff = 2
		age = []
		sex = []
		data = {
        	"Context": {
  	    	"SessionId":"checkout-test",
	    	"Type": 2,
        	"Functions": [200, 201, 202, 203, 204, 205]
        	},
        	"Image":
        	  {
    		      "Data": {
        		      "URI":"http://file.dg-atlas.com:3003/images/face/b_1.jpg"
    		      }
        	  }
    		}
		res = requests.post(url=url,data=json.dumps(data))

		r_dict = json.loads(res.content)
		message = r_dict['Context']['Message']
		face_num = len(r_dict['Result']['Faces'])
		faces = r_dict['Result']['Faces']
		i = 0
		while i < face_num :
			if faces[i]['Attributes'][0]['AttributeId'] == 1 :## 待优化
				age.append(faces[i]['Attributes'][0]['ValueInt'])
			else :
				age.append(0)
				return "read face%d age failed(maybe age is not the first attribute)"%i
			if faces[i]['Attributes'][1]['AttributeId'] == 16 :## 待优化
				sex.append(faces[i]['Attributes'][1]['ValueId'])
			else :
				sex.append(0)
				return "read face%d sex failed(maybe sex is not the second attribute)"%i
			i += 1
		if face_num == e_face_num :
			face_num_result_status = "1"
			face_num_result_context = 'num pass \nThere are %d face(s) in image as expect!\n'%(face_num)
		else :
			face_num_result_status = "0"
			face_num_result_context = 'num fail \nThere are %d face(s) in image not as expect %d face(s)\n'%(face_num,e_face_num)
		i = 0
		## time.sleep(1)
		age_fail = 0
		while i < face_num :
			if abs(age[i] - e_age[i]) <= age_diff :
				#print "face_%d age checkout OK,age=%d"%(i,age[i])
				pass
			else :
				age_fail += 1
				#print "face_%d age checkout ERR,rec_age=%d,expect_age=%d"%(i,age[i],e_age[i])
			i += 1
		if age_fail == 0 :
			face_age_result_status = "1"
			face_age_result_context = "age pass\n"
		else:
			face_age_result_status = "0"
			face_age_result_context = "age fail\n"
		##	time.sleep(1)

		##print '\ncheck sex ========'
		i = 0
		while i < face_num :
			if sex[i] == 1:
				sex_str = "man"
			else :
				sex_str = "women"
			if e_sex[i] == 1:
				e_sex_str = "man"
			else :
				e_sex_str = "women"
			sex_fail = 0
			if sex[i] == e_sex[i] :
				#print "face_%d sex checkout OK,sex=%s"%(i,sex_str)
				pass
			else :
				sex_fail += 1
				#print "face_%d sex checkout ERR,rec_sex=%s,expect_sex=%s"%(i,sex_str,e_sex_str)
			i += 1
			#time.sleep(1)
		if sex_fail == 0 :
			face_sex_result_status = "1"
			face_sex_result_context = "sex pass\n"
		else :
			face_sex_result_status = "0"
			face_sex_result_context = "sex fail\n"

#e_face_cutboard = [[604, 542, 158, 137], [1007, 335, 116, 107], [1176, 366, 103, 97], [670, 363, 99, 94], [1054, 203, 93, 87], [695, 180, 83, 79], [538, 292, 84, 78], [280, 214, 57, 60], [2, 271, 52, 59]]
		## print '\ncheck cutboard ========='
		i = 0
		cutboard_fail = 0
		while i < face_num:
			diff_x = abs(faces[i]['Img']['Cutboard']['X'] - e_face_cutboard[i][0])
			diff_y = abs(faces[i]['Img']['Cutboard']['Y'] - e_face_cutboard[i][1])
			diff_w = abs(faces[i]['Img']['Cutboard']['Width'] - e_face_cutboard[i][2])
			diff_h = abs(faces[i]['Img']['Cutboard']['Height'] - e_face_cutboard[i][3])
			if diff_x <= cutboard_diff and diff_y <= cutboard_diff and diff_h <= cutboard_diff and diff_w <= cutboard_diff :
				pass
				#print "face_%d cutboard checkout OK"%i
			else :
				cutboard_fail += 1
				#print "face_%d cutboard checkout ERR!,"%i
			i += 1
		if cutboard_fail == 0 :
			face_cutboard_result_status = "1"
			face_cutboard_result_context = "cutboard pass\n"
		else :
			face_sex_result_status = "0"
			face_sex_result_context = "cutboard fail\n"
		#if face_num_result_status == 1 and face_sex_result_status == 1 and face_age_result_status == 1 and face_cutboard_result_status == 1 :
		#	return "PASS"
		#else :
		#	return "%s\n%s\n%s\n%s"%(face_num_result_context,face_age_result_context,face_sex_result_context,face_cutboard_result_context) 
		return "%s%s%s%s"%(face_num_result_status,face_age_result_status,face_sex_result_status,face_cutboard_result_status)
	except :
		return 'http err / read image failed'
if __name__ == "__main__":
	test=check()
	print test


