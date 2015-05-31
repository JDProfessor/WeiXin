#!/usr/bin/python
#
import urllib2,config,time

APPID = config.appID
APPSECRET = config.appsecret

def request_get(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	response_msg = response.read()
	return response_msg

def request_token(APPID,APPSECRET):
	url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' %(APPID,APPSECRET)
	response_msg = request_get(url)
	return response_msg

def reserve_token(response_msg):
	with open('token.txt','w') as f:
		f.write(response_msg)
		f.flush

def getToken():
    with open('token.txt','r') as f:
        response_msg = eval(f.read())
        access_token = response_msg['access_token']
    return access_token

def countdown():
	expires_in = 0	
	while 1 :
		if expires_in < 300:
			response_msg = request_token(APPID,APPSECRET)
			reserve_token(response_msg)
			response_msg = eval(response_msg)
			expires_in = response_msg['expires_in']
		else :
			time.sleep(1)
			expires_in -= 1
		#	print expires_in

if __name__ == '__main__':
	countdown()
