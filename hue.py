'''
Created on Apr 4, 2014

@author: bonino
@author: de russis

Copyright (c) 2014 Dario Bonino and Luigi De Russis
 
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
    
    # lights URL
    lights_url = base_url+'/api/'+username+'/lights/'
    
    #get the hue lights
    all_the_lights =  rest.send(url = lights_url)
    
    # iterate over the hue lights, turn them on with the color loop effect
    for light in all_the_lights:
        url_to_call = lights_url+light+"/state"
        body = '{ "on" : true, "effect" : "colorloop" }'
        rest.send('PUT', url_to_call, body, { 'Content-Type':'application/json' })
    
    # wait 10 seconds...
    for i in range(0,10):    
        time.sleep(1)
        print 10-i
    
    # iterate over the hue lights and turn them off
    for light in all_the_lights:
        url_to_call = lights_url+light+"/state"
        body = '{ "on" : false }'
        rest.send('PUT', url_to_call, body, { 'Content-Type':'application/json' })