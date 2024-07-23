import turtle
import streamlit as st
from PIL import Image,ImageOps
import base64
import streamlit as st

def bar_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def page_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )


page_bg('a.jpg')

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区','跳转按钮_应用'])

def page_1():
    '''我的推荐'''
    with open('音乐.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write('业余的爱好')

    # 图片处理
    imgs_name_lst = ['阿甘正传.jpg', '三体.png', '我的世界1.jpg', '羽毛球.jpg']
    imgs_lst = []
    for i in imgs_name_lst:
        img = Image.open(i)
        img = img.resize((500, 400))
        imgs_lst.append(img)
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.image(imgs_lst[0])
        st.write('《阿甘正传》')
        st.write('一个非常励志的电影，非常建议观看')
    with col2:
        st.image(imgs_lst[1])
        st.write('《三体》')
        st.write('科幻小说，充满科幻的色彩')
    with col3:
        st.image(imgs_lst[2])
        st.write('《我的世界》')
        st.write('充满乐趣的游戏，在里面可以体验大自然的生活')
    with col4:
        st.image(imgs_lst[3])
        st.write('羽毛球')
        st.write('我最爱的运动，锻炼手臂力量')


def page_2():
    '''我的图片处理工具'''
    st.write(':rainbow:图片换色小程序:rainbow:')
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        #st.write(file_name,file_name,file_size)
        img = Image.open(uploaded_file)
        
        tab1,tab2,tab3,tab4,tab5 = st.tabs(['原图','改色1','改色2','改色3','反色'])
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

def page_3():
    '''我的智慧词典'''
    st.write('我的智慧词典')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] =  words_list[i].split('#')
    words_dict = {}    
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] =  times_list[i].split('#')
    times_dict = {}    
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
        
    word = st.text_input('请输入要查询的单词：')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
                
        if word == 'birthday':
            st.balloons()
        if word == 'snow':
            st.snow()
        if word == 'python':
            st.code('''
                    #恭喜你触发彩蛋， 这是一行python代码
                    print('hello world')''')
        if word == 'wbh':
            st.balloons()
            st.code('''#恭喜你触发彩蛋#''')
def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] =  messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🎱'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('💯'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是...',['阿短','编程猫'])
    new_message = st.text_input('想要说的话...')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
                
def img_change(img,cr,cg,cb):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][cr]
            g = img_array[x, y][cg]
            b = img_array[x, y][cb]
            img_array[x, y] = (r, g, b)
    return img

def page_5():
    '''跳转按钮_应用'''
    import streamlit as st
    
    # 跳转按钮link_button()
    st.link_button('百度首页', 'https://www.baidu.com/')
    
    # 如何创建跳转按钮
    # 普通的按钮需要编写if判断触发效果，跳转按钮需要吗？
    
    # 应用：兴趣推广_分享链接指引
    st.write('----')
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['我的贴吧', '我的bilibili'])
    if go == '我的贴吧':
        st.link_button('帮我盖楼', 'https://www.baidu.com/')
    elif go == '我的bilibili':
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')
        
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '跳转按钮_应用':
    page_5()


