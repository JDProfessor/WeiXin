此程序实现的功能是向关注微信开发者账号的用户发送信息.

config	    	模块 :设置基本的开发者信息.
			    	1.appID
			    	2.appsecret

getUserMsg  	模块 :获取关注微信公共号的列表.

tokenGenerator  模块:获取access_token,有效期7200S(将程序后台运行,可自动更新token)

sendMsg     	模块 :发送信息类.
					1.SendText  :发送文字信息
					2.SendImage :发送图片信息
					
upload			模块 :上传图片(大于1M将其压缩),获取media_id.

token.txt		 : 记录获取的token

