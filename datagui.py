# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 22:39:37 2021

@author: byzjz
"""


"""
button
b1=button(windows,text,command)
command绑定事件

创建一个新窗口
win=tkinter.Tk() 创建窗口
win.geometry("600x400"+300+200) 设置窗口的位置及大小
win.mainloop() 进入消息循环

布局
pack(pack先依照side命令进行排布，再按照anchor进行对齐)
相关参数
side:组件的排布方式
left,right,top,buttom

anchor 组件的对齐方式
n(上边),s(下边)，w(左边)，e(右边),nw(左上角),ne(右上角),sw(左下角),se(右下角),center(中心)
ipadx x方向的内边距  ipady y方向的外边距
padx x方向的外边距  pady y方向的外边距

label参数
label(master,option...)

master：框架的父容器
bg:标签背景色
cursor，鼠标移动到标签时，光标的形状(可设置为arrow,circle,cross,plus)
front 设置字体
text 设置文本
width 设置标签的宽度
height 标签的高度
padx x轴间距
pady y轴间距
fill x 横向填充 y 纵向填充  both 横向和纵向都填充

place()布局
anchor定义控件在窗体内的方位
in 此选项定义控件相对于参考控件的位置
x 定义控件的绝对水平位置
y 定义控件的绝对垂直位置
(x,y)即为距离窗体左上角的坐标

grid()布局

输入框
Entry

如果设置菜单选项的大小?

add_command
add_commnd添加菜单项
如果该菜单是顶层菜单，则添加的菜单以此向右添加
如果该菜单是顶层菜单的一个菜单项，则添加的是下拉菜单

add_command参数
label 指定菜单项的名称
command  指定被点击时调用的方法
acceletor 指定快捷键
underline  指定是否有下划线

add_cascade 添加子菜单
add_cascade的作用是为了引出后面的菜单

add_cascade参数
menu  指定把某个菜单级联到该菜单项上
label  指定该菜单项的名称

控件的command参数要通过 command=lambda:的形式传参数
调用window.quit退出窗口

弹出菜单 Menu中的post方法，接受两个参数，即x和y坐标，会在相应的位置弹出菜单

canvas create_arc绘制扇形
create_arc参数
canvas.create_arc(coord,start,extent,fill)

coord元组设置矩形所形成的椭圆的左上角坐标及右下角坐标:
coord=x1,y1,x2,y2

start 从x轴正方向(起始方向)开始，单位未度进行绘制，start为起始绘制角度的设置
extent：以start参数作为参考，以start参数给定的角度开始，逆时针延伸角度，这个角度为extent设置的值
fill：设施绘制区域的填充颜色 fill="red"

create_text  画布上添加文字信息
create_text(x,y,text) x,y为文字信息的坐标

定义了画布后，图形的起始和结束坐标是相对与画布的，而不是相对于窗体

scrollbar滚动条
scrollbar(master,option)

orient 指定绘制"horizontal"(垂直滚动条) "vertical"(水平滚动条)


下拉框 combobox
current()获取当前所选元素的索引，get()方法获取元素本身
current(index)可以设置下拉框的默认值



radiobutton 单选按钮
单选按钮组件用于实现多选一的问题，每一个单选按钮都可以与以一个python的函数或方法与之相关联
当按钮按下的时，对应的函数或方法将被自动执行
每一组单选按钮组件应该只与一个变量相关联，然后每一个按钮表示该变量的单一值

参数
radiobutton(master,options)

组件选项：
command 指定该按钮相关联的函数或方法
value 1 标志该单选按钮的值 2 在同一组中的所有按钮应该拥有各不相同的值  
      3 通过将该值与variable选项的值对比，即可判断用户选中了哪个按钮

variable 1 同一组件中的所有按钮的variable选项应该都指向同一个变量
         2 通过该变量与value选项的值对比，即可判断用户选中了哪个按钮
         用于跟踪用户的选择，在所有radiobutton之间共享

单选按钮方法
deselect() 取消该按钮的选中状态
select() 将按钮设置为选中状态

message box
确认/取消对话框 askokcancel 
askokcancel(title,message,**options)
askokcancel返回布尔类型，点击确认返回true,点击取消返回false

鼠标事件
<Button-1> 鼠标左键
<Double-Button-1> 双击鼠标左键

listbox相关方法
curselection()
返回一个元组，包含被选中的选项的序号(从0开始)

delete(first,last=None)
删除参数first到last范围内(包含first和last)的所有选项
如果忽略last参数，表示删除first参数指定的选项

get(first,last=None)
返回一个元组，包含参数first到last范围内的所有选项的文本

python对可变对象(list,dict,set)采用引用传递的方式，对不可变对象(number,string,tuple)等，采用值传递
要在函数内修改外部的不可变对象，可以将其定义为全局对象(global)

批量删除
curselection()在多选模式下，返回一个元组，元组中是选定元素的下标，用户先进行选择，选择完后点击删除
获取curselection()返回的元组，逐个读出元组中的元素delete


正则表达式
.可以匹配除换行符之外的任何字符
*匹配前面的字符0次或多次

特殊字符: \.^$?+*{}[]()|
使用以上特殊字符的字面值，必须使用\进行转义

re.sub(x,s,m)
返回一个字符串，每个匹配的地方用x进行替换，返回替换后的字符串最多替换m次

文件读写
a :打开一个文件用于追加，如果该文件已存在，文件指针将会放在文件的结尾，即新的内容将会被写入到已有内容之后
如果该文件不存在，创建新文件进行写入

类：
class A:
    def __init__(self)

_init_()方法为类的构造函数方法，创建这个类的实例时就会调用该方法

self代表类的实例，self在定义类的方法时是必须有的，在调用时，不需要传入相应的参数
类的方法与普通函数只有一个特别的区别，它们必须有一个额外的第一个参数名称，按照惯例名是self

if __name__=='__main__'(双下划线):的作用
一个python文件通常有两种使用方法,第一是作为脚本直接执行，第二是import到其他的python脚本中被调用
if _name_=='main'下的代码只有在第一种情况下(即文件作为脚本直接执行)才会被执行，而import到其他脚本中是不会被执行的

写测试的时候，要将主界面放在__name__=='__main__'下，这样不会弹出主界面

如果要使用函数修改不变量，可以将要修改的值用列表存储，然后向函数传递列表
"""
from tkinter import*
from tkinter import ttk
from tkinter.filedialog import*
import tkinter
from tkinter.messagebox import askokcancel,showinfo,WARNING
import ast
import logging
import json
import os
import copy

#设置日志格式
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

#logging.basicConfig(filename='info.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
logging.basicConfig( level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

#存放评论信息的结构体
#分开两个结构体:socket_all中包含comment和tag和label,socket只包含comment和tag

class stock:
    def __init__(self):
        self.comment_text=''
        self.label_list=[]
        self.tag=0


        
#tag_all存放所有的标签信息
tag_all=[]
if os.path.exists("tag.json")==False:
    f=open('tag.json','w')
    f.close()
else:
    f=open('tag.json','r')
    for line in f.readlines():
        dic=json.loads(line)
        tag_all.append(dic)
    f.close()



#comment_all从xueqiu_comment文件中读取数据，存放所有的评论信息(评论,标签，标志位)
#comment_all存放stock结构体
comment_all=[]

f=open('xueqiu_comment.json','r')
for line in f.readlines():
    comment_dict=ast.literal_eval(line)
    
    tmp=stock()
    tmp.comment_text=comment_dict['comment_text']
    for item in tag_all:
        tmp.label_list.append(item)
    tmp.tag=comment_dict['tag']
    comment_all.append(tmp)
f.close()

#comment_all正常读取
print('comment_all长度',len(comment_all))
    


#comment用于主界面listbox存放评论
comment=[]

 #评论下标,双击主界面某一评论时，更新该值
global comment_detail_index


data_label=[]

#存放统计数据的选项统计信息
data_list=[]


if os.path.exists("statistics.json")==False:
    f=open('statistics.json','w')
    f.close()
else:
    f=open('statistics.json','r')
    for line in f.readlines():
        dic=json.loads(line)
    
      
        data_list.append(dic)
    f.close()

for item in data_list:
    print(item)

#存放已经标记的评论
labeled_comment=[]

if os.path.exists("labeled_comment.json")==False:
    f=open('labeled_comment.json','w')
    f.close()
else:
    f=open('labeled_comment.json','r')
    for line in f.readlines():
        comment_dict=ast.literal_eval(line)
        #print(comment_dict)
        tmp=stock()
        tmp.comment_text=comment_dict['comment_text']
        tmp.label_list=comment_dict['label_list']
        tmp.tag=comment_dict['tag']
        labeled_comment.append(tmp)
    f.close()
    


#目录查询
def selectPath(new_path):
    
    _path=askdirectory()
    new_path.set(_path)
    #正确获取文件路径
    print(new_path.get())

#文件目录添加和文件添加
def create_file(new_path,new_folder):
    #接收用户输入数据打印
    #folder没有读取到数据?
    
    print(new_folder.get()) 
    print(new_folder)
    #print(new_path.get())
    
    #dirs = path.get()
    #file = open(dirs+'/'+folder.get(),"w")
    messagebox.showinfo("提示","文件创建成功")
        
#新建文件
def new_file():
    new_file_win=Tk()
    new_file_win.title("新建文件")
    new_file_win.geometry("300x150")
    
    #存储用户输入信息
    new_path=StringVar()
    new_folder=StringVar() 
    
    Label(new_file_win,text="目标路径").place(x=10,y=10)
    Entry(new_file_win,textvariable=new_path).place(x=70,y=10)
    Button(new_file_win,text="路径选择",command=lambda:selectPath(new_path)).place(x=220,y=10)
    
    
    Label(new_file_win,text="文件名").place(x=10,y=60)
    Entry(new_file_win,textvariable=new_folder).place(x=70,y=60)
    Button(new_file_win,text="确定",command=lambda:create_file(new_path,new_folder)).place(x=220,y=60)
    
    new_file_win.mainloop()
    


    
#文件导入
def importfile(lb):
    
    global filename
    filename=askopenfilename(defaultextension=".txt")
    logging.info("导入文件",filename)
    if(filename==""):
        filename=None
    else:
        #root.title("导入"+os.path.basename(filename))
        #导入新的文件，先清空listbox和comment中的内容
        lb.delete(0,len(comment)-1)
        comment.clear()
        
        f=open(filename,"r")
        for line in f.readlines():
            #先将读出的字符串转成字典，再按照字段读出数据
            comment_dict=ast.literal_eval(line)
            
            comment.append(comment_dict['comment_text'])
            lb.insert("end",comment_dict['comment_text'])
        
        f.close()
        
    return filename
        
#文件保存      
def filesave():
    global filename
    try:
        f=open(filename,'w')
        #写入保存内容
        #f.write(msg)
        f.closed()
    except:
        filesaveas()
#文件另存为
def filesaveas():
    f=asksaveasfilename(initialfile="未命名.txt",defaultextension=".txt")
    global filename
    filename=f
    #存文件
  
            
#3个提示信息
def downloadMessage1(nwin):
    msg=Label(nwin,text="下载中...")#padx设置x方向内边距, pady设置y方向内边距
    msg.grid(row=2)
    
def downloadMessage2(nwin):
    msg=Label(nwin,text="下载停止")#padx设置x方向内边距, pady设置y方向内边距
    msg.grid(row=2)

def downloadMessage3(nwin):
    msg=Label(nwin,text="下载完毕")#padx设置x方向内边距, pady设置y方向内边距
    msg.grid(row=2)
    
#下载管理
def download():
    dwin=Tk()
    dwin.title("下载管理")
    dwin.geometry("400x200")
    label1=Label(dwin,text="股票代码")
    info1=Entry(dwin,font=('Arial',14))
    label1.grid(row=0,column=0)
    info1.grid(row=0,column=1)
    begin=Button(dwin,text="开始下载",command=lambda:downloadMessage1(dwin))
    begin.grid(row=1,column=0,padx=50,pady=50)
    end=Button(dwin,text="停止下载",command=lambda:downloadMessage2(dwin))
    end.grid(row=1,column=1,pady=50)
    
    dwin.mainloop()
    
#统计图
#用listbox存选项
#用循环画多个扇形
#统计图中读出的数据格式
#data_list=[{'tag':'是否为推广贴','是':'50','否':'60'},{'tag':'评论情感色彩','积极':'70','消极':'100','中立':'20'},{'tag':'是否与股票相关','是':'50','否':'44'}]

#扇形填充颜色
data_color=['red','blue','yellow','green','purple','orange','white','black']
#存放下拉框显示的标签名
data_label_name=[]
for item in data_list:
    data_label_name.append(item['tag'])

def show_chart(event,canvas_chart,data_label,data_listbox):
    index=data_label.current()
    
    #清空画布重新绘图
    
    #统计标签选项总数
    count_sum=0
    for item in data_list:
        print(item)
        
    for key in data_list[index]:
        if key!='tag':
            print('key:',key)
            
            count_sum=count_sum+int(data_list[index][key])
    print('sum:',count_sum)       
    #绘制扇形
    init_arc=0
    i=0
    #清空之前的选项
    data_listbox.delete(0,END)
    
    for key in data_list[index]:
        if key!='tag':
            if count_sum!=0:
                canvas_chart.create_arc(250,250,50,50,start=init_arc,extent=int(data_list[index][key])/count_sum*360,fill=data_color[i])
                init_arc=init_arc+int(data_list[index][key])/count_sum*360
                data_tmp=key+'  '+data_color[i]+'  '+str(int(int(data_list[index][key])/count_sum*100))+'%'
                data_listbox.insert(END,data_tmp)
                i=i+1
    
    
    
#data_label是下拉框，在下拉框中选择标签后生成统计图和相关信息  
def datachart():
    cwin=Tk()
    cwin.title("统计图")
    cwin.geometry("500x500")
    
    data_label=ttk.Combobox(cwin,values=data_label_name,state='readonly')
    
    #下拉框事件绑定
    data_label.bind("<<ComboboxSelected>>",lambda event:show_chart(event,canvas_chart,data_label,data_listbox))
    data_label.current(0)
    data_label.place(x=20,y=20,anchor='w')
    
    canvas_chart=Canvas(cwin,height=300,width=300) #设置画布样式
    canvas_chart.place(x=100,y=40)
    
    #循环画出每个标签中的多个扇形
    
    #canvas_chart.create_arc(250,250,50,50,start=0,extent=240,fill="red")
    #canvas_chart.create_arc(250,250,50,50,start=240,extent=120,fill="blue")
    
    data_listbox=Listbox(cwin)
    data_listbox.place(x=180,y=310)
    
    cwin.mainloop()
    
#在标签管理界面中删除标签
#同时也要删除统计数据中的对应标签
def tag_delete(tag_listbox):
    tmp_tag=tag_listbox.curselection()
    tag_index=list(tmp_tag)
    tag_index.sort(reverse=True)
    print(tag_index)
    
    value=askokcancel('提示','确认删除?')
    if value==True:
        for item in tag_index:
            tag_listbox.delete(item)
            del tag_all[item]
        #将更新后的标签信息覆写回文件中    
        f=open('tag.json','w+')
        for item in tag_all:
            tag_new=json.dumps(item,ensure_ascii=False)
            f.write(tag_new)
            f.write('\n')
        f.close()
        
        #在标签管理类中删除标签后也要在统计图文件中删除对应的标签
        #统计图中是否需要删除标签?
    
   

#新建标签
#第一个输入框输入标签
#第二个输入框输入标签的选项，后面有一个确认按钮，点击确认后添加到下方的listbox
#listbox展示全部的标签选项，点击鼠标右键可以删除选中的选项
#点击最下方的确认按钮后，创建成功，写入到保存标签的文件中，同时也加入到commet类中的label中


#添加标签名
def tag_name_confirm(entag,tag_tmp,data_label):
    
    tag_tmp['tag']=entag.get()
    data_label['tag']=entag.get()
    print(tag_tmp['tag'])
    

#确认选项名
def tag_choice_confirm(enchoice,choicelist,tag_tmp,data_label,choice_index):
    choicelist.insert("end",enchoice.get())
    #将添加的选项添加到tag_tmp字典中
    tag_tmp[enchoice.get()]=choice_index[0]
    data_label[enchoice.get()]=0
    
    choice_index[0]=choice_index[0]+1
    enchoice.delete(0,END)

#新建标签时，删除标签选项信息   
def choice_delete(even,choice):
    tmp=choice.curselection()
    print(tmp)
    index=tmp[0]
    choice.delete(index)
    
   
    
#将新建的标签信息，写入到文件中
#添加选项的默认选择值choice=0
#新建标签信息添加到统计图文件中
def create_confirm(event,tag_tmp,new_label,data_label,tag_all,tag_listbox):
    tag_tmp['choice']=0
    tag_all.append(tag_tmp)
    tag_listbox.insert('end',tag_tmp['tag'])
    #choice_list.insert('end', tag_tmp['tag'])
    f=open("tag.json","a")
    #确认后将新的标签信息写回到listbox中
    
    tag_tmp=json.dumps(tag_tmp,ensure_ascii=False)
    f.writelines(tag_tmp)
    f.write('\n')
    f.close()
    
    #将标签写入到统计数据中
    #要先将统计数据中是选项计数清零，加入新的标签后再写回文件中
   
    data_list.append(new_label)
    
    
    f=open('statistics.json','w')
    for item in data_list:
        print(item)
        item=json.dumps(item,ensure_ascii=False)
        f.writelines(item)
        f.write('\n')
    f.close()
   
    
    messagebox.showinfo('提示','创建成功')
    
    #增加标签后，xueqiu_comment中的标志位要重新置为0，已标注评论文件中的数据清空,统计数据中的选项计数要清零
    
    
def tag_add(tag_listbox):
    #创建一个字典保存当前创建的标签内容
    tag_tmp={}
    new_label={}
    
    tag_add_win=Tk()
    tag_add_win.geometry("350x400")
    tag_add_win.title("新建标签")
    fm_tag_add=Frame(tag_add_win,width=350,height=85)
    fm_tag_choice=Frame(tag_add_win,width=350,height=85)
    fm_choice_list=Frame(tag_add_win,width=350,height=180)
    fm_add_confirm=Frame(tag_add_win,width=350,height=50)
    fm_tag_add.grid(row=0)
    fm_tag_choice.grid(row=1)
    fm_choice_list.grid(row=2)
    fm_add_confirm.grid(row=3)
    
    #标签选项对应的值
    choice_index=[]
    choice_index.append(1)
    
    input_label=Label(fm_tag_add,text="标签")
    input_label.place(x=60,y=30)
    
    #输入标签
    input_tag=Entry(fm_tag_add)
    input_tag.place(x=95,y=30)
    #标签确认
    input_tag_button=Button(tag_add_win,text="确认",command=lambda:tag_name_confirm(input_tag,tag_tmp,new_label))
    input_tag_button.place(x=250,y=25)
   
    
    input_choice=Label(fm_tag_choice,text="选项")
    input_choice.place(x=60,y=20)
    
    #输入选项
    input_choice=Entry(fm_tag_choice)
    input_choice.place(x=95,y=20)
    #选项确认
    #确认选项后添加到字典中
    choice_button=Button(fm_tag_choice,text="确认",command=lambda:tag_choice_confirm(input_choice,choice_list,tag_tmp,new_label,choice_index))
    choice_button.place(x=250,y=15)
    
   
    #滚动条
    choice_sc=Scrollbar(fm_choice_list)
    choice_sc.pack(side=RIGHT,fill=Y)

    #列表滚动，滚动条跟着滚动
    #choice_list显示标签选项
    choice_list=Listbox(fm_choice_list,yscrollcommand=choice_sc.set)
    choice_list.pack(side=LEFT,fill=BOTH,expand=True)
    #右键删除选项
    #删除listbox对应项后，也要删除tag_tmp字典中的对应项
    choice_list.bind('<Button-3>',lambda event:choice_delete(event,choice_list))

    #滚动条动，列表跟着滚动
    choice_sc.config(command=comment_list.yview)
    
    #创建确认按钮
    #确认创建后，添加到文件中
    #tag_confirm_button=Button(fm_add_confirm,text="确认",command=lambda event:create_confirm(event,tag_tmp,new_label,data_label,tag_all,choice_list,tag_listbox))
    tag_confirm_button=Button(fm_add_confirm,text="确认")
    tag_confirm_button.bind('<Button-1>',lambda event:create_confirm(event,tag_tmp,new_label,data_label,tag_all,tag_listbox))
    tag_confirm_button.place(x=160,y=10)
    

    
    tag_add_win.mainloop()
    
    
#标签管理
def tag():
    tag_win=Tk()
    tag_win.geometry("400x400")
    tag_win.title("标签管理")
   
    
    #使用listbox展示所有标签,listbox为多选模式
    #设置滚动条
    main_tag_sc=Scrollbar(tag_win)
    main_tag_sc.pack(side=RIGHT,fill=Y)

    #列表滚动，滚动条跟着滚动
    tag_listbox=Listbox(tag_win,width=100,height=15,selectmode=MULTIPLE,yscrollcommand=main_tag_sc.set)
    tag_listbox.pack(side=LEFT,fill=BOTH,expand=True)

    #滚动条动，列表跟着滚动
    main_tag_sc.config(command=tag_listbox.yview)
    
    for item in tag_all:
        tag_listbox.insert("end",item['tag'])
        
    menubar=Menu(tag_win)
    
    menubar.add_command(label='新建',command=lambda:tag_add(tag_listbox))
    menubar.add_command(label='删除',command=lambda:tag_delete(tag_listbox))
    tag_win['menu']=menubar
    
    tag_win.mainloop()



    

def confirm():
    answer=askokcancel(title="删除标签",message="确认删除标签?",icon=WARNING)
    



#查看上一条评论
def pre_comment(even,text):
    global comment_detail_index
    comment_detail_index-=1
    #print(comment_detail_index)
    logging.info("当前查看下标:",comment_detail_index)
    if comment_detail_index<0:
        comment_detail_index=0
        messagebox.showinfo('提示','已经是第一条评论了')
    #清空text原有内容
    text.delete('1.0','end')
    #读入新的内容
    text.insert('end',comment[comment_detail_index])

#查看下一条评论
def nex_comment(even,text):
    global comment_detail_index
    comment_detail_index+=1
    print(comment_detail_index)
    
    
    if comment_detail_index>len(comment):
       comment_detail_index=len(comment)-1;
       messagebox.showinfo('提示','已经是最后一条评论了')
    text.delete('1.0','end')
    text.insert('end',comment[comment_detail_index])


    

#批量删除
#不能分开下标使用delete，每次delete后，listbox元素下标会发生变化，不能继续用原来的下标
#可以将要删除的索引从大的开始删除，这样删除后不会影响到较小的索引
def main_delete_multiple():
    tmp=comment_list.curselection()
    index=list(tmp)
    
    index.sort(reverse=True)
    #print(index)
    
    #删除提示
    value=askokcancel('提示','确认删除?')
    if value==True:
          for item in index:
              logging.info("删除评论索引")
              comment_list.delete(item)
          #根据tag删除评论
          #xueqiu_comment能正常删除，但是labeled_comment不能正常删除
          for item in index:
              logging.info("删除评论")
              print("删除评论comment:",comment[item])
              print("删除评论comment_all:",comment_all[item].comment_text)
              del comment[item]
              if comment_all[item].tag==1:
                 for comment_tmp in labeled_comment:
                     if comment_tmp.comment_text==comment_all[item].comment_text:
                         print(comment_tmp.comment_text)
                         del comment_tmp
                         print("删除",comment_tmp)
                         del comment_all[item]
                         print("删除",comment_all[item])
              else:
                  del comment_all[item]
                  print("删除",comment_all[item])
          
          f=open('xueqiu_comment.json','w')
          
          for item in comment_all:
              tmp={}
              item=item.__dict__
              tmp['comment_text']=item['comment_text']
              tmp['tag']=item['tag']
              f.write(str(tmp))
              f.write('\n')
          f.close()
          
          f=open('labeled_comment.json','w')
          for item in labeled_comment:
              tmp=item.__dict__
              comment_tmp=json.dumps(tmp,ensure_ascii=False)
              f.write(comment_tmp)
              f.write('\n')
          f.close()
    

    
#使用3个frame划分布局
#上半部分放text显示评论，下半部分放评论标签,最底放两个按钮
#将text_detail作为参数传入
#问题：只能移动一次，只能看到下一条评论(值传递，无法修改到外部变量)
def comment_detail(even):
    
   
    global comment_detail_index
    #评论内容
    str=comment_list.get(comment_list.curselection())
    tmp=comment_list.curselection()
    print(tmp)
    comment_detail_index=tmp[0]
    print(comment_detail_index)
  
    detail_win=Tk()
    detail_win.geometry("400x400")
    detail_win.title('评论详情')
    '''
    detail_menu=Menu(detail_win)
    detail_menu.add_command(label='添加标签')
    detail_menu.add_command(label='删除标签')
    detail_menu.add_command(label='删除评论')
    detail_win['menu']=detail_menu
    '''
    
    fm_text=Frame(detail_win,width=400,height=200,bg='blue')
    fm_tag=Frame(detail_win,width=400,height=150,bg='red')
    fm_button=Frame(detail_win,width=400,height=50,)
    fm_text.grid(row=0)
    fm_tag.grid(row=1)
    fm_button.grid(row=2)
    #显示详细评论
    text_detail=Text(fm_text,width=55,height=14)
    text_detail.pack(side='left')
    #显示标签信息
    
    text_detail.insert("end", str)
    
    tag_sc=Scrollbar(fm_tag)
    tag_sc.pack(side=RIGHT,fill=Y)

    #列表滚动，滚动条跟着滚动
    tag_list=Listbox(fm_tag,width=55,height=10,selectmode=MULTIPLE,yscrollcommand=tag_sc.set)
    tag_list.pack(side=LEFT,fill=BOTH,expand=True)
    #滚动条动，列表跟着滚动
    tag_sc.config(command=tag_list.yview)
    
    tag_name=[]
    for item in tag_all:
        tag_name.append(item['tag'])
        
    for item in tag_name:
        tag_list.insert("end",item)
    
   
    
    
    #放置选择上一条和下一条按钮
    #点击按钮后更新评论下标索引，和文本中评论内容
    pre_button=Button(fm_button,text="上一条")
    pre_button.bind("<Button-1>",lambda event:pre_comment(event,text_detail))
    
    nex_button=Button(fm_button,text="下一条")
    nex_button.bind("<Button-1>",lambda event:nex_comment(event,text_detail))
    
    
    pre_button.place(x=0,y=0)
    nex_button.place(x=350,y=0)
    
    detail_win.mainloop()

        
def finished_comment():
    global comment_detail_index
    #评论内容
    
  
    finished_win=Tk()
    finished_win.geometry("400x400")
    finished_menu=Menu(finished_win)
    finished_menu.add_command(label='添加标签')
    finished_menu.add_command(label='删除标签')
    finished_menu.add_command(label='删除评论')
    finished_win['menu']=finished_menu
    
    fm_text=Frame(finished_win,width=400,height=200)
    fm_tag=Frame(finished_win,width=400,height=150)
    fm_button=Frame(finished_win,width=400,height=50,)
    fm_text.grid(row=0)
    fm_tag.grid(row=1)
    fm_button.grid(row=2)
    #显示详细评论
    text_detail=Text(fm_text,width=55,height=14)
    text_detail.pack(side='left')
    #显示标签信息
    
    text_detail.insert("end", str)
    
    label1=Label(fm_tag,text="是否推广贴")
    label1.grid(row=0,column=0)
    v1=IntVar()
    v2=IntVar()
    v1.set(0)
    v2.set(0)
    b1=Radiobutton(fm_tag,text="是",variable=v1,value=1)
    b1.grid(row=0,column=1)
    b2=Radiobutton(fm_tag,text='否',variable=v1,value=2)
    b2.grid(row=0,column=2)
    
    label2=Label(fm_tag,text="评论情感色彩")
    label2.grid(row=1,column=0)
    b3=Radiobutton(fm_tag,text="积极",variable=v2,value=1)
    b3.grid(row=1,column=1)
    b4=Radiobutton(fm_tag,text="中性",variable=v2,value=2)
    b4.grid(row=1,column=2)
    b5=Radiobutton(fm_tag,text="消极",variable=v2,value=3)
    b5.grid(row=1,column=3)
    
    
   
    
    
    #放置选择上一条和下一条按钮
    #点击按钮后更新评论下标索引，和文本中评论内容
    pre_button=Button(fm_button,text="上一条")
    pre_button.bind("<Button-1>",lambda event:pre_comment(event,text_detail))
    
    nex_button=Button(fm_button,text="下一条")
    nex_button.bind("<Button-1>",lambda event:nex_comment(event,text_detail))
    
    
    pre_button.place(x=0,y=0)
    nex_button.place(x=350,y=0)
    
    finished_win.mainloop()
   
#未标注评论



#查看上一条未来标注评论
#标签和按钮重新布局
def pre_unlabeled_comment(fm_choice,unlabeled_index,unlabeled_comment_list,text):
    for widget in fm_choice.winfo_children():
        widget.grid_forget()
    
     
    unlabeled_index[0]=unlabeled_index[0]-1
    print("评论下标",unlabeled_index[0])
    if unlabeled_index[0]<0:
        unlabeled_index[0]=0
        messagebox.showinfo('提示','已经是第一条评论了')
    text.delete('1.0','end')
    text.insert('end',unlabeled_comment_list[unlabeled_index[0]].comment_text)
        
#查看下一条未标注评论
#标签和按钮重新布局
#选项的选择信息没有用的是上一条

def nxt_unlabeled_comment(fm_choice,unlabeled_index,unlabeled_comment_list,text):
    for widget in fm_choice.winfo_children():
        widget.grid_forget()
    
   
    unlabeled_index[0]=unlabeled_index[0]+1
    print("评论下标:",unlabeled_index[0])
    if unlabeled_index[0]>=len(unlabeled_comment_list):
        unlabeled_index[0]=len(unlabeled_comment_list)-1
        messagebox.showinfo('提示','已经是最后一条评论了')
    
    text.delete('1.0','end')
    text.insert('end',unlabeled_comment_list[unlabeled_index[0]].comment_text)

#记录对选项的选择
#传入一个stock结构体，记录当前的选择
def select(v,index,unlabeled_index,unlabeled_comment_list):
    print('select:',v.get())
    print(len(unlabeled_comment_list))
    unlabeled_comment_list[unlabeled_index[0]].label_list[index]['choice']=v.get()
    
    print('tag:',unlabeled_comment_list[unlabeled_index[0]].label_list[index])
    
#确认对评论的标注,将已经标注的文件写入到labeled_comment.json中
#要将xueqiu_comment中对应评论的tag改为1,写回到xueqiu_comment中
#统计图数据中对应标签的选项计数递增,点击确认后写回到统计图数据文件中
def b_confirm(event,unlabeled_index,unlabeled_comment_list,data_list,tag_all):
    f=open('labeled_comment.json','a')
    
    tmp=unlabeled_comment_list[unlabeled_index[0]].__dict__
    comment_tmp=json.dumps(tmp,ensure_ascii=False)
    f.write(comment_tmp)
    f.write('\n')
    
    f.close()
    #更新xueqiu_comment中tag的值
    #找到对应的评论
    
    #stock object is not iterable
    print(unlabeled_comment_list[unlabeled_index[0]].comment_text)
    print(unlabeled_comment_list[unlabeled_index[0]].tag)
        
    for item in comment_all:
        if item.comment_text==unlabeled_comment_list[unlabeled_index[0]].comment_text:
            item.tag=1
    
    
    #更新xueqiu_comment
    
    f=open('xueqiu_comment.json','w')
    for item in comment_all:
        tmp={}
        item=item.__dict__
        tmp['comment_text']=item['comment_text']
        tmp['tag']=item['tag']
        f.write(str(tmp))
        f.write('\n')
    f.close()
    
        
        
    
    #遍历所有标签，得到被选中的选项
    #这里还是有问题，只是识别了相同的选项，但是不同的标签可能拥有相同的选项
    #应该判断是相同的label后再识别选项
    for item in unlabeled_comment_list[unlabeled_index[0]].label_list:
        for key in item:
            if key!='tag'and key!='choice':
                if item[key]==item['choice']:
                    for tmp in data_list:
                        if tmp['tag']==item['tag']:
                            for tmp_key in tmp:
                                if tmp_key==key:
                                    tmp[tmp_key]=str(int(tmp[tmp_key])+1)
                       
    
    for item in data_list:
        print(item)
        
    #将更新后的data_list写回statistics.json中
    f=open('statistics.json','w')
    for item in data_list:
         item=json.dumps(item,ensure_ascii=False)
         f.writelines(item)
         f.write('\n')
    f.close()
        
#对标签的选项进行选择
def label_choice(even,fm_choice,label_list,tag_all,unlabeled_index,unlabeled_comment_list):
    #隐藏没有选定的标签的选项
    for widget in fm_choice.winfo_children():
        widget.grid_forget()
        
    index=label_list.current()
    i=1
    global v
    v=IntVar()
    #设置选项的默认值
    
    #v.set(tag_all[index]['choice'])
    #为什么v的值没有更新？
    
    v.set(unlabeled_comment_list[unlabeled_index[0]].label_list[index]['choice'])
    print("v:",v.get())
    print("当前评论默认选项:",unlabeled_comment_list[unlabeled_index[0]].label_list[index]['choice'])
    
    #根据标签选项生成按钮
   
    for key in unlabeled_comment_list[unlabeled_index[0]].label_list[index]:
        if key!='tag'and key!='choice':
           
            b=Radiobutton(fm_choice,text=key,variable=v,value=unlabeled_comment_list[unlabeled_index[0]].label_list[index][key],command=lambda:select(v,index,unlabeled_index,unlabeled_comment_list))
           
            b.grid(row=0,column=i)
            i=i+1

#提示是否确认删除
#先调用nxt_unlabeled_comment转到下一条评论再删除评论           

def unlabeled_comment_delete(fm_choice,comment_list,unlabeled_index,unlabeled_comment_list,unlabeled_comment_text):
     value=askokcancel('提示','确认删除?')
     if value==True:
         nxt_unlabeled_comment(fm_choice,unlabeled_index,unlabeled_comment_list,unlabeled_comment_text)
         print("unlabeled_index:",unlabeled_index[0])
         print("当前评论:",unlabeled_comment_list[unlabeled_index[0]].comment_text)
         print("删除评论:",unlabeled_comment_list[unlabeled_index[0]-1].comment_text)
        
         #删除评论comment和comment_all
        
         
         for index in range(0,len(comment_all)-1):
             if comment_all[index].comment_text==unlabeled_comment_list[unlabeled_index[0]-1].comment_text:
                 break;
         #主界面评论没有被删除
         print("index:",index)
         print("comment删除:",comment[index])
         print("comment_all删除:",comment_all[index].comment_text)
         print("listbox删除:",comment_list.get(index))
         #判断listbox不为空
         comment_list.delete(index)
         del unlabeled_comment_list[unlabeled_index[0]-1]
         del comment[index]
         del comment_all[index]
         
         #更新xueqiu_comment
         f=open('xueqiu_comment.json','w')
         for item in comment_all:
             tmp={}
             item=item.__dict__
             tmp['comment_text']=item['comment_text']
             tmp['tag']=item['tag']
             f.write(str(tmp))
             f.write('\n')
         f.close()
         
         
         
    
         
    
def unlabeled_comment(comment_list):
    unlabeled_comment_win=Toplevel()
    unlabeled_comment_win.geometry("500x470")
    unlabeled_comment_win.title('未标注评论')
    
    unlabeled_menu=Menu(unlabeled_comment_win)
  
    unlabeled_menu.add_command(label='删除评论',command=lambda :unlabeled_comment_delete(fm_choice,comment_list,unlabeled_index,unlabeled_comment_list,unlabeled_comment_text))
    unlabeled_comment_win['menu']=unlabeled_menu
    
    #评论下标
    
    unlabeled_index=[]
    unlabeled_index.append(0)
    #数据不会在这里更新
    print(unlabeled_index[0])
    
    #从comment_all中选出tag=0的评论
    #问题读入的长度为空
    #这个可以放到外面，程序运行时就读取
    unlabeled_comment_list=[]
    for item in comment_all:
        if item.tag=='0':
            #这里用了浅拷贝，应该使用深拷贝
            #item.label_list=tag_all;
            item.label_list=copy.deepcopy(tag_all)
            #标签正常导入
            unlabeled_comment_list.append(item)
    
    print("评论长度:",len(unlabeled_comment_list))
    
    tag_name=[]
    #tag_name存放标签名，在下拉框中显示
    for item in tag_all:
        tag_name.append(item['tag'])
    
    
    fm_text=Frame(unlabeled_comment_win,width=500,height=200)
    #fm_choice_view=Frame(unlabeled_comment_win,width=500,height=230,bg='blue')
    fm_confirm=Frame(unlabeled_comment_win,width=500,height=35)
    fm_page=Frame(unlabeled_comment_win,width=500,height=35)
    fm_tag=Frame(unlabeled_comment_win,width=200,height=200)
    fm_choice=Frame(unlabeled_comment_win,width=300,height=200)
    
    fm_text.place(x=0,y=0)
   
    fm_tag.place(x=0,y=200)
    fm_choice.place(x=200,y=200)
    fm_confirm.place(x=0,y=400)
    fm_page.place(x=0,y=435)
    
    unlabeled_comment_text=Text(fm_text,width=70,height=15)
    unlabeled_comment_text.grid(row=0,column=0)
    print(unlabeled_comment_list[0].comment_text)
    unlabeled_comment_text.insert('end',str(unlabeled_comment_list[0].comment_text))
    
    #显示标签和评论信息
    #在左侧的下拉框选择标签后，在右侧显示选项
    label_list=ttk.Combobox(fm_tag,values=tag_name,state='readonly')
    label_list.grid(row=0,column=0)
    
    #下拉框事件绑定
    label_list.bind("<<ComboboxSelected>>",lambda even:label_choice(even,fm_choice,label_list,tag_all,unlabeled_index,unlabeled_comment_list))
    
    #点击确认后将评论信息写入到已标注文件中，同时需要更新统计图中的选项对应的计数
    tag_confirm_button=Button(fm_confirm,text='确认')
    tag_confirm_button.place(x=230,y=0)
    tag_confirm_button.bind('<Button-1>',lambda event:b_confirm(event,unlabeled_index,unlabeled_comment_list,data_list,tag_all))
    
    pre=Button(fm_page,text='上一条',command=lambda:pre_unlabeled_comment(fm_choice,unlabeled_index,unlabeled_comment_list,unlabeled_comment_text))
    pre.place(x=5,y=0)
    
    nxt=Button(fm_page,text='下一条',command=lambda :nxt_unlabeled_comment(fm_choice,unlabeled_index,unlabeled_comment_list,unlabeled_comment_text))
    nxt.place(x=450,y=0)
    
    
    unlabeled_comment_win.mainloop()

def labeled_comment(comment_list):
    




       
root=Tk()
root.title("数据标注软件")
root.geometry("800x450")
menubar=Menu(root)

fmenu=Menu(menubar)
fmenu.add_command(label="新建",command=new_file)
fmenu.add_command(label='导入',command=lambda:importfile(comment_list))
fmenu.add_command(label='导出',command=filesaveas)
fmenu.add_command(label='保存',command=filesave)
fmenu.add_command(label='另存为',command=filesaveas)

dmenu=Menu(menubar)
dmenu.add_command(label='下载',command=download)
dmenu.add_command(label='生成统计图',command=datachart)

dmenu.add_command(label='添加标注')
dmenu.add_command(label='删除评论',command=main_delete_multiple)
dmenu.add_command(label='已标注评论',command=finished_comment)
dmenu.add_command(label='未标注评论',command=lambda:unlabeled_comment(comment_list))


menubar.add_cascade(label='文件',menu=fmenu)
menubar.add_cascade(label='数据',menu=dmenu)
menubar.add_command(label='标签',command=tag)

root['menu']=menubar

#主界面 listbox+滚动条，显示股票评论，listbox设置为多选
#双击一条评论，弹出新的窗口comment_detail查看评论的详细信息

#设置滚动条
sc=Scrollbar(root)
sc.pack(side=RIGHT,fill=Y)

#列表滚动，滚动条跟着滚动
comment_list=Listbox(root,width=100,height=15,selectmode=MULTIPLE,yscrollcommand=sc.set)
comment_list.pack(side=LEFT,fill=BOTH,expand=True)

#滚动条动，列表跟着滚动
sc.config(command=comment_list.yview)

#双击显示评论
comment_list.bind("<Double-Button-1>",comment_detail)


#添加评论到listbox中
for item in comment:
    comment_list.insert("end",item)


root.mainloop()