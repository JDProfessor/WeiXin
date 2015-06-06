#!/usr/bin/python
#
import tokenGenerator,sys

def get_user_id():
	access_token = tokenGenerator.getToken()
	url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s'%access_token
	response_msg = eval(tokenGenerator.request_get(url))
	try:
		return response_msg["data"]["openid"] 
	except KeyError:
		print response_msg
		sys.exit(1)

if __name__ == '__main__':
	print get_user_id()	
