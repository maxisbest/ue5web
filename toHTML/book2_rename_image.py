# -*- coding:utf-8 -*-

import docx2txt
import os
import shutil
from utils.mytools import yfillvars
from utils.mytools import yfillzero

#get book settings and assgin variables
prog_name,p_name,ch_name,chapter_total,media_sub_name,\
    src_file_doc,books_path,books_media_name=yfillvars()
cwd = os.path.dirname(os.path.abspath(__file__))

'''
yes=input('continue?')
if yes!='yy':
    exit()
'''

p_path=os.path.join(cwd,p_name)
ch_path=os.path.join(p_path,ch_name)
prj_media_path = os.path.join(ch_path,media_sub_name)

if not os.path.exists(prj_media_path):
    os.makedirs(prj_media_path)
    print('Dir have been made: %s' % prj_media_path)
books_media_path = os.path.join(books_path, books_media_name)
if not os.path.exists(books_media_path):
    os.makedirs(books_media_path)
    print('books_media_path have been made: %s' % books_media_path)

doc_name=ch_name+'.docx'
doc_abs_path=os.path.join(ch_path,doc_name)
if not os.path.exists(doc_abs_path):
    print('%s not exists. exit.' % doc_name)
    exit()

#调用了一个外部模块, 把图片文件解压到media_path中
docx2txt.process(doc_abs_path, prj_media_path)

filelist = os.listdir(prj_media_path)
filelist_sorted=sorted(filelist)
print(filelist_sorted)

for eachname in filelist_sorted:
    if '.png' in eachname:
        src_file_abs_path = os.path.join(prj_media_path,eachname)

        std_name=p_name+ch_name+yfillzero(eachname)
        dst_file_abs_path = os.path.join(books_media_path,std_name)

        shutil.copyfile(src_file_abs_path, dst_file_abs_path)
        print('%s copied to %s.'% (eachname,std_name))