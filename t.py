import os
import json
import commands
(status, output) = commands.getstatusoutput('./hello.sh')
status = str(status)
resp_dict = {
    "status": "200",
    "message": "ok",
    "running": status,
    "stopped": output
    }
print resp_dict
j = json.dumps(resp_dict,sort_keys=True,indent=4)
print resp_dict
print j
