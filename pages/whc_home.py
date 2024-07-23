'''
本工作室叫做：诸葛好奇de工作室
根据地用户：个人
'''
import streamlit as st
from PIL import Image, ImageOps

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区','我喜欢的小动物']) 

def page_1():
    '''我的兴趣推荐'''
    with open('大鱼.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time = 0)

    st.title('我的影视剧推荐（ > _ < )')
    x1, x2= st.columns([2, 2])
    with x1:
        st.image('1.png')
    with x2:
        st.image('15.jpg')
    st.title('我的游戏推荐:很好玩的沙盒游戏~')
    st.image('2.png')
    st.title('我的书籍推荐（个人很喜欢狼）')
    z1, z2= st.columns([1, 2])
    with z1:
        st.image('3.png')
    with z2:
        st.image('16.jpg')
        
    # with x4:
    #     x4 = st.write('我的习题集推荐:无（其实不怎么做(・ω・｀ll)）')
    #     st.write('')
    #     st.write('----------------------------')

def page_2():
    '''我的图片处理工具'''
    st.write(':rainbuw:图片换色小程序：rainbow:')
    uploaded_file = st.file_uploader('上传图片', type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        #获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size

        st.write(file_name, file_type, file_size)
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4, tab5 = st.tabs(['原图', '改色1', '改色2', '改色3', '反色'])
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
    '''我的智慧词典'''
    st.write('我的智慧词典')
    #从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding = 'utf-8')as f:
        words_list = f.read().split('\n')
        
    # 将列表中的每一项内容进行分割， 分为‘单词，编号，解释’
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询， 分为‘单词，编号，解释’
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并储存在列表中
        with open('check_out_times.txt', 'r', encoding='utf-8')as f:
            times_list = f.read().split('\n')
        #将列表转为字典
        for i in range(len(times_list)):
            times_list[i] = times_list[i].split('#')
        times_dict = {}
        for i in times_list:
            times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_list:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8')as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询的次数为', times_dict[n])
        if word == 'birthday':
            st.balloons()
        if word == 'snow':
            st.snow()
    
def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容， 并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8')as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('😃'):
                st.write(i[1], ':', i[2])
        elif i[1] == '编程猫':
            with st.chat_message('😆'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是......', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8')as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
def img_change(img, r, g, b):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][0] 
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            img_array[x, y] = (b, g, r)
    return img

def page_5():
    '''我喜欢的小动物'''
    st.title('小猫')
    y1, y2 = st.columns([2, 2])
    with y1:
        st.image('6.jpg')
        st.image('8.webp')
    with y2:
        st.image('7.jpg')
    st.title('小狗')
    st.image('9.webp')
    st.image('10.webp')
    st.title('熊猫')
    a1, a2 = st.columns([2, 3])
    with a1:
        st.image('13.webp')
        st.image('14.webp')
    with a2:
        st.image('11.webp')
        st.image('12.webp')
    
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '我喜欢的小动物':
    page_5()