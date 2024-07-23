'''
工作室名字：CC妙妙屋
根据地用户：只有几个人知道的秘密基地
最喜欢的现有模块：兴趣推荐，留言区
现有模块改进灵感：自定义页面（介绍莲花楼）
原创模块：
原创模块一句话功能介绍：作者小学六年回忆
'''
import streamlit as st
from PIL import Image,ImageOps,ImageEnhance
import  pandas as pd
import time
page = st.sidebar.radio('CC妙妙屋', ['六年兴趣', '我的图片处理工具', '我的智慧词典', '我的留言区','《莲花楼》'])

def page_1():
    with open('记念.mp4','rb') as f:
        mymp4 = f.read()
    st.audio(mymp4,format='audio/mp4',start_time=0)
    st.write('我们即将踏入中学，中学的大门也在向我们敞开，从此，作者回忆六年的青春时光,let us go!!!')
    st.write('小学时光不止于学校，还有居家，那是我的六年青葱')
    msg2 = ':blue[CC的回忆从此拉开序幕......(作为一个小学毕业生，我的兴趣爱好也是我的回忆六年小学时光)]'
    st.write(msg2)
    st.image('图片一.jpg')
    #第一个序幕（视频并列）
    st.write('CC兴趣爱好一：看规则怪谈~')
    st.write('我相信你们或多或少都能了解规则怪谈，那你们爱看什么类的呢，让我们来看一看吧')
    st.write('其实作者上课无聊时，会回忆着规则怪谈，这也是我六年的回忆吧')
    st.image('规则怪谈.jpg')
    st.write('哪一个小说类型都是丰富且精彩的，那么哪一个是你心中的NO 1 呢？')
    st.write('下面是作者推荐的')
    go = st.selectbox('这些都是规则怪谈请选择会跳转到相应页面', ['宿舍怪谈', '诡楼怪谈','社区怪谈'])
    if go == '宿舍怪谈':
        st.link_button('点击观看', 'https://b23.tv/WZTd2mQ')
    elif go == '诡楼怪谈':
        st.link_button('点击观看', 'https://b23.tv/J8Q3FIy')
    elif go =='社区怪谈':
        st.link_button('点击观看', 'https://www.bilibili.com/video/BV1ft421H7dj')
    #第二个序幕
    st.write('-----------------------------------------------------------')
    st.write('CC兴趣爱好二：看动画片《菲梦少女》，小时候的自己一放学就等待着那份童真去看')
    st.write('这些哪一个是你的NO 1呢？')
    b,b1,b2,b3,b4 = st.columns([8, 6, 9, 8, 9])
    with b:
        st.image('启明星.jpg')
        st.write('记得那个美乐蒂吗，那是我的童真')
    with b1:
        st.image('将军.jpg')
        st.write('那个宁雪艳，那一朵孤高傲视的花，展开了他的希望，带着将军而来')
    with b2:
        st.image('银河系.jpg')
        st.write('星辰组合重回的时候，震撼不止，二人在一次的同台，又给了我多少的震撼呢')
    with b3:
        st.image('闪烁.jpg')
        st.write('四季组合一舞给了我太多的闪亮')
    with b4:
        st.image('爱已启动.jpg')
    st.write('---------------------------------------------------------------------')
    go = st.selectbox('请选择会跳转到相应页面', ['爱已启动', '银河系'])
    if go == '爱已启动':
        st.link_button('点击观看', 'https://www.bilibili.com/video/BV1ok4y1N7SS')
    elif go == '银河系':
        st.link_button('点击观看', 'https://www.bilibili.com/video/BV1jJ411P7SV')
    #第三个序幕
    st.write('-------------------------------------------------------------------')
    st.write('CC兴趣爱好三：撸狗')
    st.write('这是我老家的修勾，很可爱的')
    s,s1,s2,s3 = st.columns([7, 6, 7, 8])
    with  s:
        st.image('小丑照片.jpg')
    with s1:
        st.image('小丑照片1.jpg')
    with s2:
        st.image('小丑照片2.jpg')
    with s3:
        st.image('小丑照片3.jpg')
def page_2():
    st.write(':sunglasses:图片处理小程序:sunglasses:')
    msg2 = ':blue[:sun_with_face:上传图片，会处理返回输出:sun_with_face:]'
    st.write(msg2)
    uploaded_file = st.file_uploader('上传图片',type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        # st.write(file_name,file_type,file_size)
        img = Image.open(uploaded_file)
        gt = st.toggle('改色')
        ch = st.toggle('亮度滤镜')
        co = st.toggle('增强对比度')
        message = ''
        if ch:
            message += '增加亮度'+ ','
            e = ImageEnhance.Brightness(img)
            img = e.enhance(1.2)
        if gt:
            message += '改色'+','
            img = img_change(img,0,2,1)
        if co:
            message += '增强对比度'
            image_contrast = ImageEnhance.Contrast(img)
            img = image_contrast.enhance(2.0)
        st.write('你将会得到一张', message, '的图片')
        st.write('程序可能会有点慢，请耐心等待')
        st.image(img)
def page_3():
    st.write(':blue[:sun_with_face:智慧词典]:sun_with_face:')
    st.write('有隐藏彩蛋，康康你会不会触发呢？')
    st.write('提示：哪一天有蛋糕可以吃；冬天会下什么；这个是由于什么做的')
    with open('words_space.txt','r',encoding = 'utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]

    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i  in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for  i  in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入你要查询的单词：')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if  n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message = ''
            for  k,v in times_dict.items():
                message +=str(k)+'#'+str(v)+'\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：',times_dict[n])
        if word == 'birthday':
            st.balloons()
        if word =='snow':
            st.snow()
        if word =='python':
            st.code('''
                    #恭喜你出发彩蛋，这是一行python代码
                    print('hello world')''')
        if word == 'friend':
            st.write('恭喜触发彩蛋，有一句话送给你：朋友是一杯清茶，很淡；朋友是一屡清风，很柔；朋友是一丝丝的小雨，很甜。')
def page_4():
    st.write('我的留言区')
    with open('leave_messages.txt','r',encoding = 'utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i]  = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌛'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🌈'):
                st.write(i[1],':',i[2])
        elif i[1] =='小笛':
            with st.chat_message('🌕'):
                st.write(i[1],':',i[2])
        elif i[1] =='库莎':
            with st.chat_message('🌟'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是...',['阿短','编程猫','小笛','库莎'])
    new_message = st.text_input('想要说的话...')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message +=i[0]+'#'+i[1]+'#'+i[2]+'\n'
            message = message[:-1]
            f.write(message)
def page_5():
    #选择题在后面（没做）
    with open('就在江湖之上.mp4','rb') as f:
        mymp4 = f.read()
    st.audio(mymp4,format='audio/mp4',start_time=0)
    st.write(':blue[你好，《莲花楼》你是否看过，你有是否是莲络人，接下来带你走进《莲花楼》]')
    st.write('-----------------------------------------------------------------------')
    st.write('这是莲花楼探案三人组')
    st.image('莲花楼5.jpg')
    st.write('让我们来看看莲花楼三小只吧(加一个狐狸精哦~)')
    tab1,tab2,tab3,tab4,tab5= st.columns([8, 6.5, 8, 6.5,7.2])
    with tab1:
        st.image('莲花楼1（1).jpg')
        st.write('他身中碧茶之毒，只保留了一成功力，作为李莲花结识方小宝与笛飞声探案，他的身上再也没有李相夷的潇洒，多了份从容，可是，李莲花本就命不久矣')
    with tab2:
        st.image('莲花楼1.jpg')
        st.write('这是李相夷，四顾门门主李相夷，江湖第一李相夷！')
        st.write('意气风发的他创造了多少的神话，记忆犹新的是：红绸剑舞，为博美人一笑；可是，他却遭师兄暗算，从东海大战后，隐姓埋名作为李神医')
    with  tab3:
        st.image('莲花楼4.jpg')
        st.write('这位是方小宝，李相夷师兄之子，李相夷的徒弟，他的天真')
    with tab4:
        st.image('莲花楼3.jpg')
        st.write('这是笛飞声，他与李相夷东海大战，后又找到李莲花知道真相，执意要再打一场，可却失忆后与李莲花探案')
        st.write('金鸳盟盟主')
    with tab5:
        st.image('狐狸精.jpg')
        st.write('李莲花养的狐狸精，很可爱的')
    st.write('----------------------------------------------------------------')
    st.write('接下来让我们看看反派：角丽谯')
    st.image('莲花楼2.jpg')
    st.write('反派就数咱谯姐，一起红衣征服我的心，虽然是反派，但是也收获一大批粉丝')
    st.write('-------------------------------------------------------------------')
    go = st.selectbox('请选择会跳转到相应页面', ['红绸剑舞', '高然打戏混剪'])
    if go == '红绸剑舞':
        st.link_button('点击观看', 'https://www.bilibili.com/video/BV1Qm411y7XT')
    elif go == '高然打戏混剪':
        st.link_button('点击观看', 'https://www.bilibili.com/video/BV19u411n7Ca')
    st.write('-------------------------------------------------------------------')
    st.write('探案三人组都是谁')
    col1, col2 = st.columns([1, 1])
    with col1:
        cb1 = st.checkbox('A.李莲花')
    with col2:
        cb2 = st.checkbox('B.方小宝')
    col3, col4 = st.columns([1, 1])
    with col3:
        cb3 = st.checkbox('C.乔婉娩')
    with col4:
        cb4 = st.checkbox('D.笛飞声（阿飞）')
    b1 = st.button('第1题答案')
    if b1:
        if cb1 == True and cb2 == True and cb3 == False and cb4 ==True :
            st.write('回答正确！')
        else:
            st.write('再想想，再往前面看一下，作者有写的')
    #第二个序幕

def img_change(img,cr,cg,cb):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][cr]
            g = img_array[x,y][cg]
            b = img_array[x,y][cb]
            img_array[x,y] = (r,g,b)
    return  img
if page == '六年兴趣':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '《莲花楼》':
    page_5()