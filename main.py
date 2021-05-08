#coding=utf-8
#!/usr/bin/env python
# authoe: zeping lai

from flask import Flask,jsonify,request
import os
import sys
import time
import logging



appName = "" if (os.environ.get("APP_NAME") is None) else os.environ.get("APP_NAME")
appVersion = "" if (os.environ.get("APP_VERSION") is None) else os.environ.get("APP_VERSION")


def appHostname():
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

app = Flask(__name__)

@app.route('/')
def HelloWorld():
    return "Hello, %s !" % appName 

@app.route('/health')
def health():
    return appName + ' is healthy'

@app.route('/hostname')
def HostName():
    return appHostname()

@app.route('/version')
def version():
    return appVersion


@app.route('/env')
def env():
    res={}
    envKeys = os.environ.keys()
    for envKey in envKeys:
        envVal=os.environ.get(envKey)
        res[envKey]=envVal
    return jsonify(res)


@app.route('/info')
def info():
    dateTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    requestUrl = request.url
    requestRemoteAddr = request.remote_addr
    requestHeadersHost = request.headers['Host']

    if request.headers.has_key('X-Forwarded-For') == True :
        requestHeadersForward = request.headers['X-Forwarded-For']
    else:
        requestHeadersForward = ""
    res = {"appName": appName,
           "hostname": appHostname(),
           "dateTime": str(dateTime),
           "requestUrl": str(requestUrl),
           "requestRemoteAddr": str(requestRemoteAddr),
           "requestHeadersForward": str(requestHeadersForward),
           "requestHeadersHost": str(requestHeadersHost)
    }
    return jsonify(res)


@app.route('/ip')
def ip():
    dateTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    requestUrl = request.url
    requestRemoteAddr = request.remote_addr
    requestHeadersHost = request.headers['Host']

    if request.headers.has_key('X-Forwarded-For') == True :
        requestHeadersForward = request.headers['X-Forwarded-For']
    else:
        requestHeadersForward = "No X-Forwarded-For"
    return requestHeadersForward


if __name__ == '__main__':
    if len(sys.argv) < 2:
        logging.error("usage: %s port" % (sys.argv[0]))
        sys.exit(-1)

    p = int(sys.argv[1])
    logging.info("start at port %s" % (p))
    app.run(host='0.0.0.0', port=p, debug=True, threaded=True)