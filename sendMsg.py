#!/usr/bin/python
#coding:utf-8

import httplib,urllib,tokenGenerator,getUserMsg

httpClient = None

class SendText:
	def __init__(self,OPENID,contex):
		self.params = '{"touser":"%s","msgtype":"text","text":{"content":"%s"}}'%(OPENID,contex)

		self.headers ={"Content-type":"application/x-www-form-urlencoded", "Accept": "text/plain"} 

	def send_method(self):
		access_token = tokenGenerator.getToken()
		self.httpClient = httplib.HTTPConnection("api.weixin.qq.com")
#		self.httpClient = httplib.HTTPConnection("localhost",9000)
		self.httpClient.request("POST", "/cgi-bin/message/custom/send?access_token=%s"%access_token, self.params, self.headers)

	def response_method(self):
		self.response = self.httpClient.getresponse()
		print self.response.status
		print self.response.reason
		print self.response.read()

if __name__ == '__main__':
	openidlist = getUserMsg.get_user_id()
	for OPENID in openidlist:
		contex = raw_input('Input message ')
		sendtext = SendText(OPENID,contex)
		sendtext.send_method()
		sendtext.response_method()

