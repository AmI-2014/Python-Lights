'''
Created on Apr 4, 2014

@author: bonino

Copyright (c) 2014 Dario Bonino
 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
'''
import rest,time
        

if __name__ == '__main__':
    
    # the base url
    base_url = 'http://192.168.0.101'
    
    # the username
    username = 'dog-gateway'
    
    #get the hue lights
    response1 =  rest.send(url = base_url+'/api/'+username+'/lights')
    
    # iterate over the hue lights
    for light in response1:
        url_to_call = base_url+"/api/dog-gateway/lights/"+light+"/state"
        body = '{"on":true, "effect":"colorloop"}'
        rest.send('PUT', url_to_call, body, {'Content-Type':'application/json'})
    
    for i in range(0,10):    
        time.sleep(1)
        print 10-i
    
    
    # iterate over the hue lights
    for light in response1:
        url_to_call = base_url+"/api/dog-gateway/lights/"+light+"/state"
        body = '{"on":false}'
        rest.send('PUT', url_to_call, body, {'Content-Type':'application/json'})