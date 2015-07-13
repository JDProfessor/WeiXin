#!/usr/bin/python
#coding:utf-8

import requests,json,tokenGenerator

access_token = tokenGenerator.getToken()
url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s'%access_token
data = {
     "button":[
     {	
          "type":"click",
          "name":"功能一",
          "key":"V1001_TODAY_MUSIC"
      },
      {
           "name":"功能二",
           "sub_button":[
           {	
               "type":"view",
               "name":"搜索",
               "url":"http://www.soso.com/"
            },
            {
               "type":"view",
               "name":"腾讯视频",
               "url":"http://v.qq.com/"
            },
            {
               "type":"click",
               "name":"赞一下我们",
               "key":"V1001_GOOD"
            }]
       }]
 }

data = json.dumps(data,ensure_ascii=False)
print data
r = requests.post(url,data)
print r.text
