import streamlit as st
from PIL import *
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区','我喜欢的UP主'])
def page_1():
    '''
    with open("TruE.mp3","rb") as f:
        mymp3 = f.read()
    st.audio(mymp3, format = "audio/mp3", start_time = 0)
    '''
    st.write('因为暂时没有找到红姐的mp3，所以下面先放个链接~')
    st.link_button('Red Mist','https://www.bilibili.com/video/BV12g411G7XK/?spm_id_from=333.337.search-card.all.click')
    st.image("殷红迷雾.jpg")
    st.write("血雾弥漫    尸横遍野")
    st.write("色彩级收尾人——殷红迷雾（Geburah，生前名kali）")
    st.write('---------------------------------------------------------')
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.write("我的电影推荐")
        st.image("默杀.png")
        st.write("默杀")
    with col3:
        st.write("我的书籍推荐")
        st.image("红星.png")
        st.write("红星照耀中国（西行漫记）")
    st.write('-----------------------------------------------------------------------------------------')
    col4, col5, col6= st.columns([1, 1, 1])
    with col4:
        st.write("我的游戏推荐")
        st.image('崩坏三.png')
        st.write("崩坏3")
        st.write("信我！一点也不刀！！！\n绝对阳光开朗，积极向上！")
        st.write('这是电脑端下载')
        st.link_button('崩坏三', 'https://act-api-takumi.mihoyo.com/event/download_porter/link/bh3_cn/bh3/pc_sembd1')
        st.write('这是官网')
        st.link_button('崩坏三', 'https://bh3.mihoyo.com/main')
    with col6:
        st.write("我的小说推荐")
        st.image("崩坏之际.png")
        st.write("崩坏之际（番茄免费小说的崩坏三同人）")
        st.write("相信我，超级甜！！！没一点点刀子！！！")
        st.link_button('开始读','https://fanqienovel.com/reader/7067230597772476960')

def page_2():
    st.write(":rainbow:图片换色小程序:rainbow:")
    uploaded_file = st.file_uploader("上传图片",type = ["png","jpeg","jpg"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        #st.write(file_name, file_type, file_size)
        img = Image.open(uploaded_file)
        st.image(img)
        tab1,tab2,tab3,tab4,tab5 = st.tabs(["原图", "改色1", "改色2", "改色3", "反色"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))
        with tab5:
            img_invert = ImageOps.invert(img)
            st.image(img_invert)
            
            

def page_3():
    st.write("智慧词典")
    with open("words_space.txt","r",encoding="utf-8") as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input("请输入要查询的单词")
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open("check_out_times.txt", "w", encoding="utf-8") as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
def page_4():
    st.write("我的留言区")
    with open("leave_messages.txt","r",encoding = 'utf-8') as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    for i in messages_list:
        if i[1] == "阿短":
            with st.chat_message("🌞"):
                st.write(i[1],":",i[2])
        elif i[1] == "编程猫":
            with st.chat_message("🍥"):
                st.write(i[1],":",i[2])
    name = st.select_slider("我是……", ["阿短", "编程猫"])
    new_message = st.text_input("想要说的话……")
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open("leave_messages.txt", "w", encoding="utf-8") as f:
            message = ""
            for i in messages_list:
                message += i[0] + '#' +i[1] +"#"+i[2]+"\n"
            message = message[:-1]
            f.write(message)
def img_change(img,cr,cg,cb):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][cr]
            g = img_array[x,y][cg]
            b = img_array[x,y][cb]
            img_array[x,y] = (b,g,r)
    return img
def page_5():
    st.write('😀这里都是我喜欢是up主啦~😀')
    go = st.selectbox('波兰球专区', ['Cat-God猫神教主'])
    st.link_button('前往','https://space.bilibili.com/331588431?spm_id_from=333.337.0.0')
    go1 = st.selectbox('MC专区', ['马里奥红叔','黑猫大少爷','萝卜吃米洛','卡慕SaMa','大炒面制造者Cen','沝沝DjKO','卡丘啊那个卡丘'])
    if go1 == '马里奥红叔':
        st.link_button('前往','https://space.bilibili.com/680447?spm_id_from=333.337.0.0')
    elif go1 == '黑猫大少爷':
        st.link_button('前往','https://space.bilibili.com/4831263?spm_id_from=333.337.0.0')
    elif go1 == '萝卜吃米洛':
        st.link_button('前往','https://space.bilibili.com/5007752?spm_id_from=333.337.0.0')
    elif go1 == '卡慕SaMa':
        st.link_button('前往','https://space.bilibili.com/9596327?spm_id_from=333.337.0.0')
    elif go1 == '大炒面制造者Cen':
        st.link_button('前往','https://space.bilibili.com/14890801?spm_id_from=333.337.0.0')
    elif go1 == '沝沝DjKO':
        st.link_button('前往','https://space.bilibili.com/108078209?spm_id_from=333.337.0.0')
    elif go1 == '卡丘啊那个卡丘':
        st.link_button('前往','https://space.bilibili.com/12481638?spm_id_from=333.337.0.0')
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '我喜欢的UP主':
    page_5()