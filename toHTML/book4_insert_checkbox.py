# -*- coding:utf-8 -*-
# 本程序运行在工作目录projects/下

import os
import codecs
import re
from utils.mytools import yfillvars

prog_name,p_name,ch_name,chapter_total,media_sub_name,\
    src_file_doc,books_path,books_media_name=yfillvars()
cwd = os.path.dirname(os.path.abspath(__file__))

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
#--------------------------

src_file_name = ch_name + '.html'
src_file_abs_path= os.path.join(ch_path, src_file_name)
if not os.path.exists(src_file_abs_path):
    print('%s not ready.' % src_file_name)
    exit()
else:
    f_src=codecs.open(src_file_abs_path,'r',encoding='utf-8')

dst_file_name = ch_name + '_for_post' + '.html'
dst_file_abs_path = os.path.join(ch_path, dst_file_name)
f_dst=codecs.open(dst_file_abs_path,'w',encoding='utf-8')

# cb--checkbox
cb_starts='''<label class="cb_container"><span class="ysuper">'''
cb_ends = '''</span>
  <input type="checkbox">
  <span class="checkmark"></span>
</label>'''

i=1
mylines = f_src.readlines() #分开每行, 创建一个list变量
for line in mylines:
    line=line.strip()
    if line and re.search('~~~', line):  # 如果不是空行,并且 match ~~~
        y_i = '{0:03d}'.format(i) #把format中的位置0变量，用0填充到3位数
        ysub= cb_starts + y_i + cb_ends #生成 checkbox
        line_inserted=re.sub('~~~', ysub, line)#构造要写到dst中的行
        f_dst.write(line_inserted+'\n')
        i=i+1
    else:
        f_dst.write(line+'\n')

f_dst.close()
f_src.close()
