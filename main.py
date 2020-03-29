#!/usr/bin/env python  
#coding=utf-8
#author: zepinglai

import os
from flask import Flask,jsonify,request
from config import configs
import time, json

app = Flask(__name__)

def GetHostName():
        sys = os.name
        if sys == 'nt':
                hostname = os.getenv('computername')
                return hostname
        elif sys == 'posix':
                host = os.popen('echo $HOSTNAME')
                try:
                        hostname = host.read()
                        return hostname
                finally:
                        host.close()
        else:
                return 'Unkwon hostname'

@app.route('/')
def HelloWorld():
    return str(configs.HOME_CONTENT)

@app.route('/stat')
def stat():
    return 'ok'

@app.route('/conf')
def conf():
    DEBUG = configs.DEBUG
    DB_NAME = configs.DB_NAME
    DB_HOST = configs.DB_HOST

    res = {"DEBUG": DEBUG,
           "DB_NAME": DB_NAME,
           "DB_HOST": DB_HOST	
	  }
 
    return jsonify(res)	

@app.route('/hi')
def HostName():
	return GetHostName()


@app.route('/head')
def head():
    print(request.headers)
    return json.loads(json.dumps(dict(request.headers)))



@app.route('/test')
def test():

    NowTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    ReqUrl = request.url
    UrlRoot = request.url_root
    RemoteIp = request.remote_addr
    #ReqIP2 = request.headers['X-Real-Ip']
    #ReqIP3= request.headers["X-Forwarded-For"] 
    
    print(request.headers)   

    ReqHederHost = request.headers['Host']
    if request.headers.has_key('X-Forwarded-For') == True :
        ForwardIp = request.headers['X-Forwarded-For']
    else : 
        ForwardIp = ""
	
    #print ForwardIp
    #print ReqIP2
    #print ReqIP3

    res = {"AppName": "Python Web Demo",
           "HostName": GetHostName(),
           "NowTime": str(NowTime),
           "Author": "zeze",
           "ReqUrl": str(RemoteIp),
           "ReqHederHost": ReqHederHost
          }

    return jsonify(res)

if __name__ == '__main__':
    app.debug = configs.DEBUG
    app.run(host='0.0.0.0',port=5000)
