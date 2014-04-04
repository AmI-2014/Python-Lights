'''
Created on Apr 4, 2014

@author: bonino
'''
import urllib2, json

def send(method = 'GET', url=None, data = None, headers = {}):
    #the response dictionary, initially empty
    response_dict = dict()
    
    #check that the url is not empty
    if(url!=None):
        #build the request
        req = urllib2.Request(url, data, headers)
        req.get_method = lambda: method
        
        #try to call the url
        result = None
        try:
            #get the result
            result = urllib2.urlopen(req)
        except urllib2.URLError, e:
            #print the error
            print e.reason
        
        #check result
        if(result != None):
            #decode the result
            result_as_string = result.read().decode('utf8')
            #convert into a dict
            response_dict = json.loads(result_as_string)
            
    
    return response_dict