//myrun
import DolphinDB as ddb
import getData as gt
import numpy as np
import time
import datetime
s=ddb.DBConnection()
s.initialize()
s.connect("192.168.1.107", 8848,"","")
ss="1..10000000"

x=np.zeros((10000000,),dtype=np.int32)
s_tt=time.time()
s_tc=time.clock()
s_dd= datetime.datetime.now()
p=s.run(ss)
ddb.np_int(x,p)
e_dd=datetime.datetime.now()
e_tc=time.clock()
e_tt=time.time()
dur=e_dd-s_dd
print('time.time() Running time:'+str(e_tt-s_tt)+'sec\n')
print('time.clock() Running time:'+str(e_tc-s_tc)+'sec\n')
print('datetime.datetime.now() Running time:'+str(dur)+'\n')
