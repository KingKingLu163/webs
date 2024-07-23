'''我的主页'''
import streamlit as st
from PIL import Image, ImageOps

#import base64

#def bar_bg(img):
    #last = 'jpg'
    #st.markdown(
        #f"""
        #<style>
        #[data-testid='stSidebar'] > div:first-child {{
            #background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        #}}
        #</style>
        #""",
        #unsafe_allow_html = True,
    #)

#def page_bg(img):
    #last = 'jpg'
    #st.markdown(
        #f"""
        #<style>
        #.stApp {{
           #background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            #background-size: cover
       #}}
        #</style>
       #""",
        #unsafe_allow_html = True,
    #)

#bar_bg('天象奇景.jpg')
#page_bg('天象奇景.jpg')


#'''
#工作室名字：
#根据地用户：个人
#'''

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区','自定义页面'])
def page_1():
    '''我的兴趣推荐'''
    with open ('霞光.mp3','rb')as f:
        mymp3 = f.read()
    st. audio(mymp3,format='audio/mp3', start_time=0)
    st.write('我的电影推荐')
    st.write('16.jpg')
    st.write('我的游戏推荐')
    st.write('ec.jpg')


    imgs_name_lst = ['16.jpg', 'ec.jpg']
    imgs_lst = []
    for i in imgs_name_lst:
        img = Image.open(i)
        img = img.resize((400, 300))
        imgs_lst.append(img)

    col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
    with col1:
        st.image(imgs_lst[0])
        st.write('16.jpg')
        st.write('《速度与激情》是以赛车题材动作犯罪类电影系列，截至2024年7月，这一系列共上映了11部电影。')
    with col2:
        st.image(imgs_lst[1])
        st.write('ec.jpg')
        st.write('荒野乱斗作为一款海外游戏，在2020年在中国上市，被腾讯公司收购')



def page_2():
    '''我的图片处理工具'''
    st.write(":sunglass:图片处理工小程序:sunglass:")
    uploaded_file = st.file_uploader("上传图片", type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        #st.write( file_name ,file_type,)file_size
        st.write(file_name, file_type, file_size)
        img = Image.open(uploaded_file)

        tab1,tab2,tab3,tab4,tab5 = st.tabs(["原图","改色1","改色2","改色3","反色"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
        with tab5:
            img_invert = ImageOps.invert(img)
            st.image(img_invert)

def img_change(img,cr,cg,cb):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][cr]
            g = img_array[x,y][cg]
            b = img_array[x,y][cb]
            img_array[x,y] = (r,g,b)
    return img
    

def page_3():
    '''我的智慧词典'''
    st.write('智慧词典')
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    print(words_list)
    
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open('check_out_time.txt.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
        
        word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word[0]]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_time.txt.txt','r',encoding='utf-8') as f:
            message = ''
            for k , v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:1]
            f.write(message)
            
        st.write('查询次数',times_dict[n])
        
        if word == 'birthday':
            st.balloons()
        if word == 'snow':
            st.snow()
        
def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    for i in messages_list:
        if i [1] == '阿短':
            with st.chat_message('🍬'):
                st.write(i[1],':',i[2])
        if i [1] == '编程猫':
            with st.chat_message('🎃'):
                st.write(i[1],':',i[2])
    name=st.selectbox('我是......',['阿短','编程猫'])
    new_messages=st.text_input('想要说的话......')
    if st.button('评论'):
        messages_list.append([str(int(messages_list[-1][0])+1),
name, new_messages])
        with open('leave_messages.txt','r',encoding='utf-8') as f:
            message = ''
        for i in messages_list:
            message += i(0) + '#' + str(v) + '\n'
        message = message[:1]
        f.write(message)

def page_5():
    '''自定义页面'''
    st.write('自定义页面')
    with open ('我喜欢的音乐.mp3','rb')as f:
        mymp3 = f.read()
    st. audio(mymp3,format='audio/mp3', start_time=0)
    st.write('b站我喜欢的up主')
    st.image('bd.jpg')
    st.image('xc.jpg')
    st.write('游戏up主')
    st.image('ff.png')
    
    
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '自定义页面':
    page_5()
