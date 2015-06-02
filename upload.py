#!/usr/bin/python
#
import requests,tokenGenerator,os
from PIL import Image

def compress_image(filename):
	size = os.stat(filename).st_size
	if size > 1048576:
		im1 = Image.open(filename)
		im2 = im1.resize((1024,768))
		im2.save('compressed_'+filename)
		filename = 'compressed_'+filename
	return filename

def upload_file(filename):
	files = {}
	access_token = tokenGenerator.getToken()
	filename = compress_image(filename)
	url = 'http://file.api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=image'%access_token
	files["media"] = open(filename,'rb')
	req = requests.post(url,files=files)
	content = eval(req.content)
	return content["media_id"]

if __name__ == '__main__':
	media_id = upload_file('panda.jpg')
	print media_id
#	filename = compress_image('shu.jpg')
#	print filename
