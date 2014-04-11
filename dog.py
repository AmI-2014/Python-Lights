'''
Created on Apr 10, 2014

@author: bonino
'''
import rest,time

if __name__ == '__main__':
    
    # the base url of the Dog gateway
    base_url = 'http://192.168.0.102:8080/api/v1/'
    
    #the url of all devices
    all_devices_url = base_url+'devices'
    
    #get the list of available devices in JSON format
    all_devices = rest.send(url = all_devices_url, headers = {'Accept':'application/json'})
    
    # iterate over all devices
    for device in all_devices:
        #debug
        #print device
        
        # iterate over all devices
        for i in range(0, len(all_devices[device])):
            #get the device class
            device_class =  all_devices[device][i]['class']
            #print the device class
            print device_class
            #get the device id
            device_id = all_devices[device][i]['id']
            #print the device id
            print device_id
            
            #if the device class is 'MeteringPowerOutlet', turn it on
            if(device_class == 'MeteringPowerOutlet'):
                #compose the url to turn on the device
                on_url = base_url+'devices/'+device_id+'/commands/on'
                #send the request
                rest.send('PUT',on_url,'{}',{'Content-Type':'application/json'})
                
    time.sleep(10)
    
    # iterate over all devices
    for device in all_devices:
        #debug
        #print device
           
        # iterate over all devices
        for i in range(0, len(all_devices[device])):
            #get the device class
            device_class =  all_devices[device][i]['class']
            #print the device class
            print device_class
            #get the device id
            device_id = all_devices[device][i]['id']
            #print the device id
            print device_id
             
            #if the device class is 'MeteringPowerOutlet', turn it off
            if(device_class == 'MeteringPowerOutlet'):
                #compose the url to turn off the device
                on_url = base_url+'devices/'+device_id+'/commands/off'
                #send the request
                rest.send('PUT',on_url,'{}',{'Content-Type':'application/json'})
    
        
