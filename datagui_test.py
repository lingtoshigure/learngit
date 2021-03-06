# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 22:39:37 2021

@author: byzjz
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
import time
import threading
from get_xueqiu import Xueqiuspider


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

#判断是否导入了文件
global is_import_file
is_import_file=False
        
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

#开始下载/停止下载标志位
download_flag=[]
download_flag.append(1)

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
    global is_import_file
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
        is_import_file=True
        
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
  

    
    
    
#下载管理
def download_start(stock_num,dwin,download_progress,flag):
     xueqiu = Xueqiuspider()
     t=threading.Thread(target=xueqiu.run(stock_num,dwin,download_progress,flag),name='t')
     t.start()

def download_stop(flag):
    t=threading.Thread(target=is_download_stop(flag),name='t2')
    t.start()

def is_download_stop(flag):
    flag[0]=0
    print('停止下载')

#判断用户输入是否正确
def is_stock_correct(stock_num):
    if (len(stock_num)==8 and (re.match('SH600*', stock_num).span()!=None or re.match('SH601*', stock_num).span()!=None or re.match('SH603*', stock_num).span()!=None or re.match('SH605*', stock_num).span()!=None or re.match('SH688*', stock_num).span()!=None or re.match('SZ000*', stock_num).span()!=None or re.match('SZ001*', stock_num).span()!=None or re.match('SZ002*', stock_num).span()!=None or re.match('SZ300*', stock_num).span()!=None)):
        download_start()
    else:
        messagebox
        
    
def download(flag):
    strV='SH601318'
    dwin=Tk()
    dwin.title("下载管理")
    dwin.geometry("400x250")
    label_download=Label(dwin,text="股票代码")
    stock_num=Entry(dwin,font=('Arial',14))
    
    label_download.place(x=40,y=10)
    stock_num.place(x=100,y=10)
    start_download=Button(dwin,text="开始下载",command=lambda:download_start(stock_num.get(),dwin,download_progress,flag))
    start_download.place(x=50,y=100)
    stop_download=Button(dwin,text="停止下载",command=lambda:download_stop(download_flag))
    stop_download.place(x=300,y=100)
    
    download_progress=ttk.Progressbar(dwin,length=200,mode="determinate",orient=HORIZONTAL)
    download_progress.place(x=100,y=150)
    
    
    
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
                if int(data_list[index][key])==count_sum:
                    break
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
def tag_delete(tag_listbox,tag_all):
    tmp_tag=tag_listbox.curselection()
    tag_index=list(tmp_tag)
    tag_index.sort(reverse=True)
    print(tag_index)
    
    value=askokcancel('提示','确认删除?')
    delete_tmp=[]
    if value==True:
        for item in tag_index:
            delete_tmp.append(tag_listbox.get(item))
            tag_listbox.delete(item)
            del tag_all[item]
        #将更新后的标签信息覆写回文件中    
        f=open('tag.json','w+')
        for item in tag_all:
            tag_new=json.dumps(item,ensure_ascii=False)
            f.write(tag_new)
            f.write('\n')
        f.close()
    
    return delete_tmp
        
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
    
    return tag_tmp['tag'],data_label['tag']
    

#确认选项名
def tag_choice_confirm(enchoice,choicelist,tag_tmp,data_label,choice_index):
    choicelist.insert("end",enchoice.get())
    #将添加的选项添加到tag_tmp字典中
    tag_tmp[enchoice.get()]=choice_index[0]
    data_label[enchoice.get()]=0
    
    choice_index[0]=choice_index[0]+1
    enchoice.delete(0,END)
    
    return tag_tmp,data_label,choice_index[0]

#新建标签时，删除标签选项信息   
def choice_delete(event,choice,tag_tmp):
    tmp=choice.curselection()
    
    index=tmp[0]
   
    check_tmp1=tag_tmp[choice.get(index)]
    check_tmp2=choice.get(index)
    del tag_tmp[choice.get(index)]
    for item in tag_tmp:
        print(item)
    choice.delete(index)
    return check_tmp1,check_tmp2
    
   
    
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
    test_tag=tag_tmp
    
    tag_tmp=json.dumps(tag_tmp,ensure_ascii=False)
    f.writelines(tag_tmp)
    f.write('\n')
    f.close()
    
    #将标签写入到统计数据中
    #要先将统计数据中是选项计数清零，加入新的标签后再写回文件中
   
    data_list.append(new_label)
    test_data=data_list
    
    
    f=open('statistics.json','w')
    for item in data_list:
        print(item)
        item=json.dumps(item,ensure_ascii=False)
        f.writelines(item)
        f.write('\n')
    f.close()
   
    
    messagebox.showinfo('提示','创建成功')
    
    return test_tag,test_data
    
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
    
    choice_list.bind('<Button-3>',lambda event:choice_delete(event,choice_list,tag_tmp))
   

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
    menubar.add_command(label='删除',command=lambda:tag_delete(tag_listbox,tag_all))
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
    
    return unlabeled_comment_list[unlabeled_index[0]].comment_text
        
#查看下一条未标注评论
#标签和按钮重新布局
#选项的选择信息没有用的是上一条

def nxt_unlabeled_comment(fm_choice,unlabeled_index,unlabeled_comment_list,text):
    for widget in fm_choice.winfo_children():
        widget.grid_forget()
    
   
    unlabeled_index[0]=unlabeled_index[0]+1
    print("评论下标:",unlabeled_index[0])
    if unlabeled_index[0]>=len(unlabeled_comment_list):
        unlabeled_index[0]=len(unlabeled_comment_list)
        messagebox.showinfo('提示','已经是最后一条评论了')
    
    text.delete('1.0','end')
    text.insert('end',unlabeled_comment_list[unlabeled_index[0]].comment_text)
    
    return unlabeled_comment_list[unlabeled_index[0]].comment_text

#记录对选项的选择
#传入一个stock结构体，记录当前的选择
def select(v,index,unlabeled_index,unlabeled_comment_list):
    print('select:',v.get())
    print(len(unlabeled_comment_list))
    unlabeled_comment_list[unlabeled_index[0]].label_list[index]['choice']=v.get()
    
    print('tag:',unlabeled_comment_list[unlabeled_index[0]].label_list[index])
    
    return unlabeled_comment_list[unlabeled_index[0]].label_list[index]['choice']
    
#确认对评论的标注,将已经标注的文件写入到labeled_comment.json中
#要将xueqiu_comment中对应评论的tag改为1,写回到xueqiu_comment中
#统计图数据中对应标签的选项计数递增,点击确认后写回到统计图数据文件中
#将新的评论加入到labeled_commen中
def b_confirm(event,unlabeled_index,unlabeled_comment_list,data_list,labeled_comment):
    labeled_comment.append(unlabeled_comment_list[unlabeled_index[0]].__dict__)
    print('新增已标注评论:',unlabeled_comment_list[unlabeled_index[0]])
    
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

#提示是否删除
#转跳到下一条评论再删除

def unlabeled_comment_delete(fm_choice,comment_list,unlabeled_index,unlabeled_comment_list,labeled_comment_text):
     value=askokcancel('提示','确认删除?')
     if value==True:
         nxt_unlabeled_comment(fm_choice,unlabeled_index,unlabeled_comment_list,labeled_comment_text)
         print("unlabeled_index:",unlabeled_index[0])
         print("当前评论:",unlabeled_comment_list[unlabeled_index[0]].comment_text)
         print("删除评论:",unlabeled_comment_list[unlabeled_index[0]-1].comment_text)
        
         #删除评论comment和comment_all
        
         
         for index in range(0,len(comment_all)):
             if comment_all[index].comment_text==unlabeled_comment_list[unlabeled_index[0]-1].comment_text:
                 break;
         #主界面评论没有被删除
         print("index:",index)
         
         print("comment_all删除:",comment_all[index].comment_text)
         print("listbox删除:",comment_list.get(index))
         #判断listbox不为空
         print("is_import_file:",is_import_file)
         if is_import_file==True:
             comment_list.delete(index)
             del comment[index]
        
         del unlabeled_comment_list[unlabeled_index[0]-1]
        
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
    tag_confirm_button.bind('<Button-1>',lambda event:b_confirm(event,unlabeled_index,unlabeled_comment_list,data_list,labeled_comment))
    
    pre=Button(fm_page,text='上一条',command=lambda:pre_unlabeled_comment(fm_choice,unlabeled_index,unlabeled_comment_list,unlabeled_comment_text))
    pre.place(x=5,y=0)
    
    nxt=Button(fm_page,text='下一条',command=lambda :nxt_unlabeled_comment(fm_choice,unlabeled_index,unlabeled_comment_list,unlabeled_comment_text))
    nxt.place(x=450,y=0)
    
    
    unlabeled_comment_win.mainloop()

#更新评论同时更新old_labeled_choice
#Text控件中的评论内容和label对应的选项内容是分别更新的，old_labeled_choice保存上一条/下一条评论的选项的选择信息
#点击上一条和下一条按钮后old_labeled_choice用来更新选项信息
def labeled_nxt_comment(fm_choice,labeled_index,labeled_comment,labeled_comment_text,old_labeled_choice):
    for widget in fm_choice.winfo_children():
        widget.grid_forget()
    
    labeled_index[0]=labeled_index[0]+1
    if labeled_index[0]>len(labeled_comment):
        labeled_index[0]=len(labeled_comment)
        messagebox.showinfo('提示','已经是最后一条评论了')
    
    labeled_comment_text.delete('1.0','end')
    labeled_comment_text.insert('end',labeled_comment[labeled_index[0]].comment_text)
    
    #更新选项记录
    old_labeled_choice=[]
   
   
    for i in range(0,len(labeled_comment[labeled_index[0]].label_list)):
        tmp={}
        for key in labeled_comment[labeled_index[0]].label_list[i]:
            if key=='tag':
                tmp['tag']=labeled_comment[labeled_index[0]].label_list[i]['tag']
                
            if key=='choice':
                tmp['old_choice']=labeled_comment[labeled_index[0]].label_list[i]['choice']
        old_labeled_choice.append(tmp)
    
    for item in old_labeled_choice:
        print("old_labeled_choice",item)
    
    return labeled_comment[labeled_index[0]].comment_text,old_labeled_choice
            

def labeled_pre_comment(fm_choice,labeled_index,labeled_comment,labeled_comment_text,old_labeled_choice):
    for widget in fm_choice.winfo_children():
        widget.grid_forget()
    
    labeled_index[0]=labeled_index[0]-1
    if labeled_index[0]<0:
        labeled_index[0]=0
        messagebox.showinfo('提示','已经是第一条评论了')
    
    labeled_comment_text.delete('1.0','end')
    labeled_comment_text.insert('end',labeled_comment[labeled_index[0]].comment_text)
    
    #更新选项记录
    old_labeled_choice=[]
   
   
    for i in range(0,len(labeled_comment[labeled_index[0]].label_list)):
        tmp={}
        for key in labeled_comment[labeled_index[0]].label_list[i]:
            if key=='tag':
                tmp['tag']=labeled_comment[labeled_index[0]].label_list[i]['tag']
                
            if key=='choice':
                tmp['old_choice']=labeled_comment[labeled_index[0]].label_list[i]['choice']
        old_labeled_choice.append(tmp)
    
    return  labeled_comment[labeled_index[0]].comment_text,old_labeled_choice
            
    
    
#单独保存原来的选择
#用list保存原来的标签和选择

#修改已经标注评论的选项
#更新已评论数据中的数据
#修改选项后要更新统计图中的数据
#点击确认后要清空old_labeled_choice


def labeled_select(v_choice,index,labeled_index,labeled_comment,old_labeled_choice):
    print(labeled_comment[labeled_index[0]].comment_text)
    labeled_comment[labeled_index[0]].label_list[index]['choice']=v_choice.get()
    print(labeled_comment[labeled_index[0]].label_list)
    
   
    for item in old_labeled_choice:
        if item['tag']==labeled_comment[labeled_index[0]].label_list[index]['tag']:
            item['new_choice']=v_choice.get()
            
    return labeled_comment[labeled_index[0]].label_list[index]['choice'],old_labeled_choice
      
    
    


def labeled_label_choice(even,fm_choice,label_list,tag_all,labeled_index,labeled_comment,old_labeled_choice):
    for widget in fm_choice.winfo_children():
        widget.grid_forget()
        
    index=label_list.current()
    i=1
   
    v_choice=IntVar()
    v_choice.set(labeled_comment[labeled_index[0]].label_list[index]['choice'])
    print("v:",v_choice.get())
    print("当前评论默认选项:",labeled_comment[labeled_index[0]].label_list[index]['choice'])
    
    #根据标签选项生成按钮
    for key in labeled_comment[labeled_index[0]].label_list[index]:
        
        if key!='tag'and key!='choice':
           
            b=Radiobutton(fm_choice,text=key,variable=v_choice,value=labeled_comment[labeled_index[0]].label_list[index][key],command=lambda:labeled_select(v_choice,index,labeled_index,labeled_comment,old_labeled_choice))
           
            b.grid(row=0,column=i)
            i=i+1
            
def labeled_change_confirm(event,labeled_index,labeled_comment,data_list,old_labeled_choice):
    
    #更新统计图数据
    for item in data_list:
        for tmp in old_labeled_choice:
            if item['tag']==tmp['tag']:
                i=0
                for key in item:
                    if i==tmp['old_choice']:
                        item[key]=str(int(item[key])-1)
                    if i==tmp['new_choice']:
                        item[key]=str(int(item[key])+1)
                    i=i+1
    
    print('统计图数据')
    for item in data_list:
        print(item)
    
    #更新文件数据
    f=open('statistics.json','w')
    for item in data_list:
         item=json.dumps(item,ensure_ascii=False)
         f.writelines(item)
         f.write('\n')
    f.close()
    
    f=open('labeled_comment.json','w')
    for item in labeled_comment:
        tmp=labeled_comment[labeled_index[0]].__dict__
        comment_tmp=json.dumps(tmp,ensure_ascii=False)
        f.write(comment_tmp)
        f.write('\n')
    f.close()
    
    return data_list
    
#删除已标注评论(在xueqiu_comment和labeled_comment中删除)
def labeled_comment_delete(fm_choice,comment_list,labeled_index,labeled_comment,labeled_comment_text,old_labeled_choice):
    value=askokcancel('提示','确认删除?')
    if value==True:
         nxt_unlabeled_comment(fm_choice,labeled_index,labeled_comment,labeled_comment_text)
         print("labeled_index:",labeled_index[0])
         print("当前评论:",labeled_comment[labeled_index[0]].comment_text)
         print("删除评论:",labeled_comment[labeled_index[0]-1].comment_text)
        
         #删除评论comment和comment_all
        
         
         for index in range(0,len(comment_all)):
             if comment_all[index].comment_text==labeled_comment[labeled_index[0]-1].comment_text:
                 break;
         #主界面评论没有被删除
         print("index:",index)
         
         print("comment_all删除:",comment_all[index].comment_text)
         print("listbox删除:",comment_list.get(index))
         #判断listbox不为空
         print("is_import_file:",is_import_file)
         if is_import_file==True:
             comment_list.delete(index)
             del comment[index]
        
         del labeled_comment[labeled_index[0]-1]
        
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
         
         #更新labeled_comment
         f=open('labeled_comment.json','w')
         for item in labeled_comment:
             tmp={}
             item=item.__dict__
             comment_tmp=json.dumps(item,ensure_ascii=False)
             f.write(comment_tmp)
             f.write('\n')
         f.close()
         
    

def labeled_comment_f(comment_list,tag_all,labeled_comment):
    labeled_comment_win=Tk()
    
    labeled_comment_win.geometry("500x470")
    labeled_comment_win.title('已标注评论')
    
    labeled_menu=Menu(labeled_comment_win)
  
    labeled_menu.add_command(label='删除评论',command=lambda :labeled_comment_delete(fm_choice,comment_list,labeled_index,labeled_comment,labeled_comment_text,old_labeled_choice))
    labeled_comment_win['menu']=labeled_menu
    
    #已标注评论下标,为什么类型是dict?
    labeled_index=[]
    labeled_index.append(0)
   
    
    #初始化
    old_labeled_choice=[]
    
    #判断labeled_comment是否为空
    if len(labeled_comment)>0:
        for i in range(0,len(labeled_comment[labeled_index[0]].label_list)):
            tmp={}
            for key in labeled_comment[labeled_index[0]].label_list[i]:
                if key=='tag':
                    tmp['tag']=labeled_comment[labeled_index[0]].label_list[i]['tag']
                
                if key=='choice':
                    tmp['old_choice']=labeled_comment[labeled_index[0]].label_list[i]['choice']
            old_labeled_choice.append(tmp)
        
  
    
    for item in old_labeled_choice:
        print(item)
    
    tag_name=[]
    for item in tag_all:
        tag_name.append(item['tag'])
    
    fm_text=Frame(labeled_comment_win,width=500,height=200)
   
    fm_confirm=Frame(labeled_comment_win,width=500,height=35)
    fm_page=Frame(labeled_comment_win,width=500,height=35)
    fm_tag=Frame(labeled_comment_win,width=200,height=200)
    fm_choice=Frame(labeled_comment_win,width=300,height=200)
    
    fm_text.place(x=0,y=0)
    fm_tag.place(x=0,y=200)
    fm_choice.place(x=200,y=200)
    fm_confirm.place(x=0,y=400)
    fm_page.place(x=0,y=435)
    
    labeled_comment_text=Text(fm_text,width=70,height=15)
    labeled_comment_text.grid(row=0,column=0)
    
    labeled_comment_text.insert('end',str(labeled_comment[0].comment_text))
    
    #显示标签和评论信息
    #在左侧的下拉框选择标签后，在右侧显示选项
    label_list=ttk.Combobox(fm_tag,values=tag_name,state='readonly')
    label_list.grid(row=0,column=0)
    
    #下拉框事件绑定
    label_list.bind("<<ComboboxSelected>>",lambda even:labeled_label_choice(even,fm_choice,label_list,tag_all,labeled_index,labeled_comment,old_labeled_choice))
    
    #点击确认后将评论信息写入到已标注文件中，同时需要更新统计图中的选项对应的计数
    tag_confirm_button=Button(fm_confirm,text='确认')
    tag_confirm_button.place(x=230,y=0)
    tag_confirm_button.bind('<Button-1>',lambda event:labeled_change_confirm(event,labeled_index,labeled_comment,data_list,old_labeled_choice))
    
    pre=Button(fm_page,text='上一条',command=lambda:labeled_pre_comment(fm_choice,labeled_index,labeled_comment,labeled_comment_text,old_labeled_choice))
    pre.place(x=5,y=0)
    
    nxt=Button(fm_page,text='下一条',command=lambda :labeled_nxt_comment(fm_choice,labeled_index,labeled_comment,labeled_comment_text,old_labeled_choice))
    nxt.place(x=450,y=0)
    
    
    labeled_comment_win.mainloop()
        
if __name__=='__main__':           
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
    dmenu.add_command(label='下载',command=lambda:download(download_flag))
    dmenu.add_command(label='生成统计图',command=datachart)

    dmenu.add_command(label='添加标注')
    dmenu.add_command(label='删除评论',command=main_delete_multiple)
    dmenu.add_command(label='已标注评论',command=lambda:labeled_comment_f(comment_list,tag_all,labeled_comment))
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