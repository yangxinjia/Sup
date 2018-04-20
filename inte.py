GET /status
RESPONSE:
{
	"status": "200"
	"project": [
		{
			"id": "1",
			"project": "ise-face",
			"status": "running"
			"function": [1, 2, 3, 4, 5, 6, 7, 8]
			},
		{
			"id": "2",
			"project": "ise-vehicle",
			"status": "stopping",
			"function": [1, 2, 3, 4, 5]
			}
	]
}
POST /new_project
REQUEST:
{
	"id": "1"
	"project": "ise-face"
}
RESPONSE:
{
	"status": "200"
	"message": "run ok"
	"id": "1"
	"project": "ise-face"
}
GET /function/view_project
POST /function/view_case
REQUEST:
{
	"id": "1"
	// 或者
	"project": "ise-face"
}
RESPONSE:
{
	"status": "200"
	"id": "1"
	"project": "ise-face"
	"functions": {
		"1": "all-single",
		"2": "all-batch",
		"3": "det-single", 
		"4": "det-align-single",
		"5": "det-align-quality-single",
		"6": "test-with-det-result",
		"7": "test-with-det-and-align-result",
		"8": "check-result"
	}
}
//id 、 name不存在
{
	"status": "400"
	"message": "id/name not exsit"
}

POST /function/test
REQUEST:
{
	"id": "1"
	"project": "ise-face"
	"functions": [1, 2, 3, 4, 5, 6, 7, 8]
}
RESPONSE:
{
	"status": "200"
	"id": "1"
	"project": "ise-face"
	"result": {
		"1": {
			"test_result": "PASS"
			"test_message": "single image all functions test ok!"
		} 
		## *************
		"8": {
			"test_result": "ERR"
			"rest_message": "there are 8 faces not as expect 9 faces!"
		}
	}
}
## id 、 name不存在
{
	"status": "400"
	"message": "id/name not exsit"
}