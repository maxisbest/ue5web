# -*- coding:utf:8 -*-

import pysftp
import os
import codecs
import re
from utils.mytools import yfillvars

yfilename=r'C:\Users\maxyi\Desktop\ubshare\projects\zz\ypas.html'

prog_name,p_name,ch_name,chapter_total,media_sub_name,\
    src_file_doc,books_path,books_media_name=yfillvars()

cnopts = pysftp.CnOpts()
# cnopts.hostkeys = None

with codecs.open(yfilename,'r',encoding='utf-8') as fypas:
    lines=fypas.readlines()
if lines:
    line=lines[99].strip()
    line_frags=line.split()
    #print(line_frags)
    ypss1=str(int(line_frags[1])-int(line_frags[0]))
    cloud_pss=line_frags[2]+ypss1+line_frags[-1]
    #print(ypss2)

cloud='111.231.57.45'

yremote=cloud
yusername='ubuntu'
ypass = cloud_pss

with pysftp.Connection(yremote, username=yusername, password=cloud_pss) as yftp:

    local_file_names = os.listdir(
        r'C:\Users\maxyi\Desktop\ubshare\projects\media')
    #以上，获得本地media文件夹下所有文件的文件名
    local_file_paths = [] #要拷贝到服务器的文件清单将放在这个变量中
    for eachname in local_file_names:
        if p_name in eachname: #例如, 如果usaco在文件名中，则将其放入local_file_paths
            local_file_path = os.path.join(
                r'C:\Users\maxyi\Desktop\ubshare\projects\media', eachname)
            local_file_paths.append(local_file_path)
    print('local_file_paths: %s' % local_file_paths)
    print(len(local_file_paths))

    ydir='u3d/media'
    #yover_write=True
    with yftp.cd(ydir):
        for eachfile in local_file_paths:
            yftp.put(eachfile)
        print('Done!')
