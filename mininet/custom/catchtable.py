import httplib
import json
  
class StaticFlowPusher(object):
  
    def __init__(self, server):
        self.server = server
  
    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])
  
    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200
  
    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200
  
    def rest_call(self, data, action):
        path = '/wm/core/switch/all/table/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        #print ret
        conn.close()
        return ret
  
pusher = StaticFlowPusher('127.0.0.1')
  
flow1 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_1",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "actions":"output=flood"
    }
  
flow2 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_2",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "actions":"output=flood"
    }
  
#pusher.set(flow1)
#pusher.set(flow2)
#pusher.get(flow1)
#print"switch01 has ",len(pusher.get(flow1)['00:00:00:00:00:00:00:02']['table'])

tmp_list=pusher.get(flow1).keys()
n=len(pusher.get(flow1))
i=0
while ( i<n ):
    a=tmp_list[i]
    print a, " has ",len(pusher.get(flow1)[a]['table'])," tables\n"
    i+=1
else:
    pass