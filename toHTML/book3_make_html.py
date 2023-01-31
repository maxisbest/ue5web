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

txt_file_name=ch_name+'.txt'
txt_file_path = os.path.join(ch_path,txt_file_name)
if not os.path.exists(txt_file_path):
    print("%s not ready. exits now." %txt_file_name)
    exit()

#f_txt_file=codecs.open(txt_file_path, 'r', encoding='utf-8')

html_file = ch_name+'.html'
html_file= os.path.join(ch_path,html_file)
if not os.path.exists(html_file):
    f_dst = codecs.open(html_file, 'w', encoding='utf-8')
else:
    print('%s存在, 其内容将被擦除.'% html_file)
    f_dst = codecs.open(html_file, 'w', encoding='utf-8')
    f_dst.truncate()

f_src=codecs.open(txt_file_path,'r',encoding='utf-8')

# 🌿枝叶 🍀四叶草 🍁枫叶 🍂落叶 🍃叶子在风中飘落
# 💄 🐾 👙💦 🍺 🍒 🍓 💡🍴⇗
# ○ • ● ○ ◦
# 🐶 😾

yiji_dot='>'
erji_dot='>>'
sanji_dot='>>>'
tu_lead='↗'

mylines = f_src.readlines() #分开每行, 创建一个list变量
tu_seq=1
for line in mylines:
    line=line.strip()
    line=re.sub('：', ':', line) #英文冒号':'--替换中文冒号'：'
    #三级标题的情况
    if line and re.search(r'^###\d*.', line):  # 如果不是空行,并且match
        cd_line=re.sub(r'###\d*.', '', line,count=1)  # 移除类似'###12.'这样的字符串. count=1 means only do once.
        #print(cd_line)

        pic_pos=re.search(r'图\d*:', cd_line) # 看line中是否有'图10:'这样的patt
        if pic_pos:
            # print(pic_pos,pic_pos[0],len(pic_pos))
            #ynum=re.sub(r'[图:]','', pic_pos[0]) #清除掉"图"和":", 只保留数字
            ynum='{0:03d}'.format(tu_seq)  # 将剩下的数字变成001这样的式样
            tu_seq=tu_seq+1
            line = p_name+ch_name+'image'+ynum+'.png'
            # line=project002ch01image001.png
            dst_line= "图"+ynum+tu_lead+'<img  src ="/media/%s">'%(line)
            # the above line will match u3d_nginx.conf settings.
            dst_line= '<div class="yimg">'+dst_line+'</div>'
        else:
            dst_line='<p class="sanji">'+sanji_dot+cd_line+ '</p>'

    #二级标题的情况
    elif re.search(r'^##\d*.', line):
        dst_line = re.sub(r'##\d*.', '', line)  # 清除掉'##12.'
        dst_line = '<p class="erji">' +erji_dot + dst_line + '</p>'
    #一级标题的情况
    elif re.search(r'^#\d+.', line):
        dst_line = re.sub(r'#\d+.', '', line)  # 清除掉'#12.' # re.sub(r'\d+.png', new_text, text_for_post)
        dst_line =  '<p class="yiji">' +yiji_dot + dst_line + '</p>'
    else:
        dst_line=line

    f_dst.write(dst_line+'\n')

f_src.close()
f_dst.close()