#!/usr/bin/python
#
import requests,tokenGenerator

def upload_file(filename):
	files = {}
	access_token = tokenGenerator.getToken()
	url = 'http://file.api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=image'%access_token
	files["media"] = open(filename,'rb')
	req = requests.post(url,files=files)
	content = eval(req.content)
	return content["media_id"]

if __name__ == '__main__':
	media_id = upload_file('panda.jpg')
	print media_id
