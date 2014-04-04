'''
Created on Apr 4, 2014

@author: bonino
'''
import rest,time
        

if __name__ == '__main__':
            
    # the base url
    base_url = 'http://192.168.0.102:8083'

    
    #get the zwave devices
    response =  rest.send(url = base_url+'/ZWaveAPI/Data/0')

    #search switches
    for device_key in response['devices']:
        #iterate over device instances
        for instance in response['devices'][device_key]['instances']:
            #search for the 37 (SwitchBinary) command class
            if ('37' in response['devices'][device_key]['instances'][instance]['commandClasses'].keys()):
                #debug
                print "device %s is a switch"%device_key
                #turn it on
                url_to_call = base_url+"/ZWaveAPI/run/devices["+device_key+"].instances["+instance+"].commandClasses[37].Set(255)"
                rest.send(url = url_to_call)
    
    #reverse count to off           
    for i in range(0,10):    
        time.sleep(1)
        print 10-i

    #search switches
    for device_key in response['devices'].keys():
        #iterate over device instances
        for instance in response['devices'][device_key]['instances']:
            #search for the 37 (SwitchBinary) command class
            if ('37' in response['devices'][device_key]['instances'][instance]['commandClasses'].keys()):
                #debug
                print "device %s is a switch"%device_key   
                #turn it off
                url_to_call = base_url+"/ZWaveAPI/run/devices["+device_key+"].instances["+instance+"].commandClasses[37].Set(0)"
                rest.send(url = url_to_call)
    