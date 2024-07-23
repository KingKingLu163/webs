'''
工作室名字：
根据地用户：个人使用
根据地用途：数据收集
最喜欢现有模块：智慧词典
原创模块：



'''

import streamlit as st
from PIL import Image,ImageOps,ImageEnhance
page = st.sidebar.radio('我的首页',['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区', 'streamlit知识库'])
def page_1():
    a1 = st.write('我的游戏推荐')
    st.image("原神.png")
    a2 = st.write('原神最近玩的有点上头')
    a = st.link_button("点击下载", "https://ys.mihoyo.com/")
    fg1 = st.write("------------------------")
    b1 = st.write('我的动漫推荐')
    st.image("柯南.jpg")
    b2 = st.write('柯南也是越看越上头')
    b = st.link_button("点击下载", "http://www.ytv.co.jp/conan/")
    fg2 = st.write("------------------------")
    cs1, ds1 = st.columns([1, 1])
    with cs1:
        c1 = st.write('我的书籍推荐')
        st.image("新华字典.png")
        c2 = st.write('这本书可以查到你想要的所有书')
        c = st.link_button("点击查询", "https://baike.baidu.com/item/%E6%96%B0%E5%8D%8E%E5%AD%97%E5%85%B8/310045?fr=ge_ala")
    with ds1:
        d1 = st.write('我的电影推荐')
        st.image('抓娃娃.jpeg')
        d2 = st.write('《抓娃娃》这部电影看完之后会让你怀疑人生')
        d = st.link_button("点击下载", "https://www.1905.com/mdb/film/2257907/")
def img_change(img, rc, rg, rb):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][rg]
            b = img_array[x, y][rb]
            img_array[x, y] = (b, g, r)
    return img
def page_2():
    st.write(':rainbow:图片换色小程序:rainbow:')
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        st.write(file_name, file_type, file_size)
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["原图", "改色1", "改色2", "改色3", "反色", "亮度"])
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
        with tab6:
            e = ImageEnhance.Brightness(img)
            e = e.enhance(1.2)
            st.image(e)            
def page_3():
    st.write("我的智慧词典")
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    print(words_list)
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open("check_out_time.txt", "r", encoding='utf-8') as f:
        times_list = f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_time.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + "#" + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write("查询的次数为", times_dict[n])
        if word == 'birthday':
            st.balloons()
        if word == 'snow':
            st.snow()
        if word == "python":
            st.code('''
                    # 恭喜你触发隐藏彩蛋， 这是一行python代码
                    print('Hello World!)''')
    elif word == '':
        pass
    else:
        st.code('''
                # 你哪来的这么多单词''')
        
def page_4():
    st.write("我的留言区")
    with open("leave_messages.txt", "r", encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    for i in messages_list:
        if i[1] == "阿短":
            with st.chat_message('🌞'):
                st.write(i[1], ":", i[2])
        elif i[1] == "编程猫":
            with st.chat_message('🍥'):
                st.write(i[1], ":", i[2])
    name = st.selectbox('我是......', ["阿短", "编程猫"])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + "#" + i[1] + "#" + i[2] + "\n"
            message = message[:-1]
            f.write(message)
def page_5():
    with open("streamlit_word_space.txt", "r", encoding='utf-8') as f:
        word_list = f.read().split('\n')
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split('#')
    
    word_dict = {}
    for i in word_list:
        word_dict[i[1]] = [int(i[0]), i[2]]
    words = st.text_input("请输入要解释的语句:")
    if words in word_dict:
        st.write(word_dict[words])
    elif words == '':
        pass
    else:
        st.write('抱歉，无法查询，敬请谅解')
        
        
    
            

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == 'streamlit知识库':
    page_5()
else:
    pass



