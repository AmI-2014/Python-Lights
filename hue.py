'''
Created on Apr 4, 2014

@author: bonino
'''
'''
Created on Apr 4, 2014

@author: bonino
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
        rest.send('PUT', url_to_call, body, {'Content-type':'application/json'})
    
    for i in range(0,10):    
        time.sleep(1)
        print 10-i
    
    
    # iterate over the hue lights
    for light in response1:
        url_to_call = base_url+"/api/dog-gateway/lights/"+light+"/state"
        body = '{"on":false}'
        rest.send('PUT', url_to_call, body, {'Content-type':'application/json'})