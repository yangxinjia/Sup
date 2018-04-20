# -*- coding: utf8 -*-

import requests
import json
import os
import time
import sys
from sys import argv


##################################

url = 'http://39.104.109.10:8501'
inte_ping = url + '/ping'
inte_single = url + '/rec/image'
inte_batch = url + '/rec/image/batch'

###################################

def get(name,url):
    try:
		begin = time.time()*1000
		res = requests.get(url)
		end = time.time()*1000
		cost = end - begin
		code = 200
		message = '%s test complete, cost %.2fms'%(name,cost)
		return code, message, res.text
    except:
		code = 404
		message = '%s test failed'%name
		return code, message, None
def post(name,url,data):
	try:
		print 'doing %s test'%name
		begin = time.time()*1000
		res = requests.post(url=url,data=json.dumps(data))
		end = time.time()*1000
		cost = end - begin
		r_dict = json.loads(res.content)
		code = r_dict['Context']['Status']
		message = '%s test complete, cost %.2fms '%(name, cost) + r_dict['Context']['Message']
		return code, message, res.text
	except :
		code = 404
		message = "%s test failed, server connect failed"%name
		return code, message, None
def objNumber(name,url,data,expect):
	try :
		begin = time.time()*1000
		res = requests.post(url=url,data=json.dumps(data))
		end = time.time()*1000
		cost = end - begin
		r_dict = json.loads(res.content)
		message = r_dict['Context']['Message']
		face_num = len(r_dict['Result']['Faces'])
		if face_num == expect :
			code = 200 
			message = '%s test complete , cost %.2fms, SUCCESS,There are %d face(s) in image as expect!'%(name, cost, face_num)
		else :
			code = 400
			message = 'Failed, cost %.2fms, There are %d face(s) in image not as expect %d face(s)'%(cost, face_num, expect)
		return code, message, res.text
	except :
		code = 404
		message = "%s test failed, server connect failed / read image failed"%name
		return code, message, None
	
######################################
img_url = "http://file.dg-atlas.com:3003/images/face/b_1.jpg"
img_local = "file:///images/1.jpg"
img_base64 = '"BinData":"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"'
single_data = {
        "Context": {
  	    "SessionId":"all-single",
	    "Type": 2,
        "Functions": [200, 201, 202, 203, 204, 205]
        },
        "Image":
          {
    	      "Data": {
        	      "URI":"%s"%img_url
    	      }
          }
    	}
batch_data = {
  		"Context": {
  			"SessionId":"all-batch",
			"Type": 2,
    		"Functions": [200, 201, 202, 203, 204, 205]
  		},
  		"Images": [
   			{
    		"Data": {
        	"URI": "http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
        		}
    			},
    		{
		"Data": {
        	"URI": "http://file.dg-atlas.com:3003/images/face/yangmi2.jpg"
    				}
    	},
			{
    		"Data": {
        	"URI": "http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
        		}
    			},
    		{
		"Data": {
        	"URI": "http://file.dg-atlas.com:3003/images/face/yangmi2.jpg"
    				}
    	},
    		{
    		"Data": {
        	"URI": "http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
        		}
    			},
    		{
		"Data": {
        	"URI": "http://file.dg-atlas.com:3003/images/face/yangmi2.jpg"
    				}
    	}    	
    	]
    	}
det_res_data = {
  		"Context": {
  			"SessionId":"test face with detect result",
			"Type": 2,
    		"Functions": [201,202,203,204,205]
  			},
  		"Image": {
			"Data": {
        	"URI": "http://file.dg-atlas.com:3003/images/face/2.jpg"
    		},
    	"UserObject":
    	[
    		{
    			"Type":1,
    			"RotatedRect": {
						"CenterX": 104.01509094238281,
                        "CenterY": 163.18853759765626,
                        "Width": 129.2895050048828,
                        "Height": 125.56614685058594,
                        "Angle": 0
    			}
    		}
    	]
    	}
    	}
det_align_res_data = {
  		"Context": {
  			"SessionId":"test with det and align result",
			"Type": 2,
    		"Functions": [202, 203, 204, 205]
  			},
  		"Image": {
		"Data":
		{
        	"URI": "http://file.dg-atlas.com:3003/images/face/2.jpg"
    	},
    	"UserObject":
    	[
    		{
    			"Type":1, 
    			"RotatedRect": {
                        "CenterX": 104.01507568359375,
                        "CenterY": 163.18853759765626,
                        "Width": 129.2895050048828,
                        "Height": 125.56617736816406,
                        "Angle": 0
                    },
    			"AlignResult": {
                    "LandMarks": [
                        {
                            "X": 42.151084899902347,
                            "Y": 128.3915252685547
                        },
                        {
                            "X": 44.36152648925781,
                            "Y": 148.8240509033203
                        },
                        {
                            "X": 46.78252410888672,
                            "Y": 169.04331970214845
                        },
                        {
                            "X": 50.88808059692383,
                            "Y": 189.27719116210938
                        },
                        {
                            "X": 64.83514404296875,
                            "Y": 209.61688232421876
                        },
                        {
                            "X": 85.46305847167969,
                            "Y": 220.99864196777345
                        },
                        {
                            "X": 105.74412536621094,
                            "Y": 224.39483642578126
                        },
                        {
                            "X": 126.5783462524414,
                            "Y": 221.39808654785157
                        },
                        {
                            "X": 148.02944946289063,
                            "Y": 210.5086669921875
                        },
                        {
                            "X": 163.28236389160157,
                            "Y": 190.03530883789063
                        },
                        {
                            "X": 167.6958770751953,
                            "Y": 169.00326538085938
                        },
                        {
                            "X": 170.1040802001953,
                            "Y": 148.36505126953126
                        },
                        {
                            "X": 171.7147674560547,
                            "Y": 127.74252319335938
                        },
                        {
                            "X": 67.53559875488281,
                            "Y": 123.70899963378906
                        },
                        {
                            "X": 72.72139739990235,
                            "Y": 119.0531005859375
                        },
                        {
                            "X": 78.8800048828125,
                            "Y": 117.83152770996094
                        },
                        {
                            "X": 84.75827026367188,
                            "Y": 119.46309661865235
                        },
                        {
                            "X": 89.5882568359375,
                            "Y": 125.08256530761719
                        },
                        {
                            "X": 84.22439575195313,
                            "Y": 126.5879898071289
                        },
                        {
                            "X": 78.60393524169922,
                            "Y": 127.051513671875
                        },
                        {
                            "X": 72.50447845458985,
                            "Y": 126.13532257080078
                        },
                        {
                            "X": 79.11409759521485,
                            "Y": 122.00415802001953
                        },
                        {
                            "X": 58.008644104003909,
                            "Y": 113.61238098144531
                        },
                        {
                            "X": 65.00761413574219,
                            "Y": 105.35356140136719
                        },
                        {
                            "X": 73.92240142822266,
                            "Y": 102.90748596191406
                        },
                        {
                            "X": 82.78498077392578,
                            "Y": 103.34152221679688
                        },
                        {
                            "X": 91.59754943847656,
                            "Y": 108.67638397216797
                        },
                        {
                            "X": 83.17317199707031,
                            "Y": 109.59127807617188
                        },
                        {
                            "X": 74.6130142211914,
                            "Y": 110.47110748291016
                        },
                        {
                            "X": 66.18251037597656,
                            "Y": 112.14903259277344
                        },
                        {
                            "X": 122.61847686767578,
                            "Y": 125.067138671875
                        },
                        {
                            "X": 127.44728088378906,
                            "Y": 119.68953704833985
                        },
                        {
                            "X": 133.4035186767578,
                            "Y": 117.83233642578125
                        },
                        {
                            "X": 139.72933959960938,
                            "Y": 118.90980529785156
                        },
                        {
                            "X": 145.2809600830078,
                            "Y": 123.32405090332031
                        },
                        {
                            "X": 140.14830017089845,
                            "Y": 125.79804992675781
                        },
                        {
                            "X": 134.06942749023438,
                            "Y": 126.90226745605469
                        },
                        {
                            "X": 128.26846313476563,
                            "Y": 126.54802703857422
                        },
                        {
                            "X": 134.39541625976563,
                            "Y": 121.85868835449219
                        },
                        {
                            "X": 119.36629486083985,
                            "Y": 108.48489379882813
                        },
                        {
                            "X": 128.49342346191407,
                            "Y": 103.31526184082031
                        },
                        {
                            "X": 137.63113403320313,
                            "Y": 102.762451171875
                        },
                        {
                            "X": 146.8190155029297,
                            "Y": 104.79586791992188
                        },
                        {
                            "X": 154.3605194091797,
                            "Y": 112.68818664550781
                        },
                        {
                            "X": 146.00924682617188,
                            "Y": 111.98152160644531
                        },
                        {
                            "X": 137.07786560058595,
                            "Y": 110.54641723632813
                        },
                        {
                            "X": 128.2144012451172,
                            "Y": 109.70960998535156
                        },
                        {
                            "X": 97.42212677001953,
                            "Y": 125.23490905761719
                        },
                        {
                            "X": 95.1898193359375,
                            "Y": 136.624267578125
                        },
                        {
                            "X": 92.60646057128906,
                            "Y": 147.89474487304688
                        },
                        {
                            "X": 88.43441009521485,
                            "Y": 160.37547302246095
                        },
                        {
                            "X": 98.02206420898438,
                            "Y": 160.29830932617188
                        },
                        {
                            "X": 113.42533111572266,
                            "Y": 160.28860473632813
                        },
                        {
                            "X": 123.3865966796875,
                            "Y": 160.4420166015625
                        },
                        {
                            "X": 119.0652084350586,
                            "Y": 147.84658813476563
                        },
                        {
                            "X": 116.38886260986328,
                            "Y": 136.5155029296875
                        },
                        {
                            "X": 114.12789916992188,
                            "Y": 125.15399169921875
                        },
                        {
                            "X": 105.08479309082031,
                            "Y": 151.54248046875
                        },
                        {
                            "X": 83.57109832763672,
                            "Y": 184.79962158203126
                        },
                        {
                            "X": 94.38666534423828,
                            "Y": 179.00555419921876
                        },
                        {
                            "X": 106.27517700195313,
                            "Y": 178.4947509765625
                        },
                        {
                            "X": 118.13911437988281,
                            "Y": 179.28680419921876
                        },
                        {
                            "X": 128.42779541015626,
                            "Y": 185.3101806640625
                        },
                        {
                            "X": 117.5818099975586,
                            "Y": 188.96029663085938
                        },
                        {
                            "X": 106.1819076538086,
                            "Y": 189.99081420898438
                        },
                        {
                            "X": 94.68253326416016,
                            "Y": 188.90118408203126
                        },
                        {
                            "X": 94.65536499023438,
                            "Y": 183.37954711914063
                        },
                        {
                            "X": 106.2350845336914,
                            "Y": 183.4700927734375
                        },
                        {
                            "X": 117.81787109375,
                            "Y": 183.5926513671875
                        },
                        {
                            "X": 117.56680297851563,
                            "Y": 184.58990478515626
                        },
                        {
                            "X": 106.35211181640625,
                            "Y": 184.64044189453126
                        },
                        {
                            "X": 94.87628173828125,
                            "Y": 184.4532470703125
                        }
                    ],
                    "LandMarkScores": [
                        0.9949007034301758,
                        0.9967343807220459,
                        0.9957691431045532,
                        0.9961163401603699,
                        0.9954380989074707,
                        0.9955792427062988,
                        0.9966347813606262,
                        0.9971779584884644,
                        0.996334433555603,
                        0.9965066909790039,
                        0.9967049360275269,
                        0.9964585304260254,
                        0.9952529072761536,
                        0.9960481524467468,
                        0.9958694577217102,
                        0.9955973625183106,
                        0.9959121346473694,
                        0.9972424507141113,
                        0.99528568983078,
                        0.996115505695343,
                        0.9945670366287231,
                        0.9947199821472168,
                        0.9932114481925964,
                        0.9969191551208496,
                        0.9969614148139954,
                        0.9953176975250244,
                        0.9940799474716187,
                        0.9960289597511292,
                        0.9956164360046387,
                        0.9953164458274841,
                        0.9957338571548462,
                        0.9965873956680298,
                        0.9971585869789124,
                        0.9968327879905701,
                        0.9962722063064575,
                        0.9948995113372803,
                        0.9960882067680359,
                        0.9958994388580322,
                        0.9971781969070435,
                        0.9962587952613831,
                        0.9966213703155518,
                        0.9966254830360413,
                        0.9957631826400757,
                        0.9966607689857483,
                        0.996656060218811,
                        0.9973025918006897,
                        0.9967730045318604,
                        0.9974938631057739,
                        0.9975224137306213,
                        0.9982364177703857,
                        0.9972507953643799,
                        0.9962124824523926,
                        0.9962975978851318,
                        0.997671365737915,
                        0.997482419013977,
                        0.9978366494178772,
                        0.9977959394454956,
                        0.9968498349189758,
                        0.9962090253829956,
                        0.9942681789398193,
                        0.9976301193237305,
                        0.9965794682502747,
                        0.9965383410453796,
                        0.9945312142372131,
                        0.9976165890693665,
                        0.9959769248962402,
                        0.9954864978790283,
                        0.99801105260849,
                        0.9966152906417847,
                        0.9967199563980103,
                        0.9972236752510071,
                        0.9949285984039307
                    ],
                    "Box": {
                        "X": 0,
                        "Y": 0,
                        "Width": 0,
                        "Height": 0
                    },
                    "Scores": [
                        {
                            "key": "local_is_face",
                            "value": 0.9982861876487732
                        },
                        {
                            "key": "global_is_face",
                            "value": 0.9989998936653137
                        },
                        {
                            "key": "global_front_face",
                            "value": 0.9991173148155212
                        }
                    ]
                }
            }
         ]
    	}
    	}
######################################
def case1():
	ping = get('ping',inte_ping)
def case2():
	single = post('single',inte_single,single_data)
def case3():
	batch = post('batch',inte_batch,batch_data)
def case4():
	rec_with_det = post('rec1',inte_single,det_res_data)
def case5():
	rec_with_det_align = post('rec2',inte_single,det_align_res_data)
def case6():
	face_num_test = objNumber('objNum',inte_single,single_data,9)
######################################
if __name__ == "__main__":
## 执行用例
	code1, message1, context1= get('ping',inte_ping)
	print "code1: %s"%code1
	print "message1: %s"%message1
	#print "context1: %s\n\n"%context1
	code2, message2, context2= post('single',inte_single,single_data)
	print "code2: %s"%code2
	print "message2: %s"%message2
	#print "context2: %s\n\n"%context2
	code3, message3, context3= post('batch',inte_batch,batch_data)
	print "code3: %s"%code3
	print "message3: %s"%message3
	#print "context3: %s\n\n"%context3
	code4, message4, context4= objNumber('objNum',inte_single,single_data,9)
	print "code4: %s"%code4
	print "message4: %s"%message4
