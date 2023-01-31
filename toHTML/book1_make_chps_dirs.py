# -*- coding:utf-8 -*-
'''
本程序运行在工作目录projects/下.项目命名规则为project001, project002...
要指明书本的word文档文件名, 并放在projectxxx下
每本书几个章节也要指明
程序运行后将:
1)创建项目的名称, 例如project001; 2)在project001目录下建立章节文件夹,
例如project/ch01; 3)把总的word文档分别拷贝到章节文件夹中; 4)...
'''

import os
import shutil
import re
from utils.mytools import yfillvars

'''yfillvars会返回一个列表变量，注意顺序不要搞错了。
vars = [prog_name, p_name, ch_name, chapter_total, media_sub_name, \
        src_file_doc, books_path]'''
prog_name,p_name,ch_name,chapter_total,media_sub_name,\
    src_file_doc,books_path,books_media_name=yfillvars()
cwd = os.path.dirname(os.path.abspath(__file__))

#print(cwd)

yes=input('continue?')
if yes!='yy':
    exit()

p_path=os.path.join(cwd,p_name)
if not os.path.exists(p_path):
    os.makedirs(p_path)

ch_path=os.path.join(p_path,ch_name)
if not os.path.exists(ch_path):
    os.makedirs(ch_path)
    print('章节子目录%s成功创建.' % ch_path)
else:
    print('章节子目录%s已存在,不用创建.' % ch_path)

