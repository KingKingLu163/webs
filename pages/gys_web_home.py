import streamlit as st
from PIL import Image,ImageOps

# "工作室名称：搬运工的天堂"
# "根据地使用范围：个人使用"

page=st.sidebar.radio("(洗)首页", ['视频搬运', '图片处理工具搬运', '词典搬运', '评论区','神秘界面'])

def page_1():
    st.image("数码.png")
    st.write("数码区视频搬运")
    go1=st.selectbox("选择播放视频",['我做了苹果放弃的产品……','我做了一个自己打字的键盘……','首次公开！带你逛我们工作室'])
    if go1=='我做了苹果放弃的产品……':
        st.link_button('播放1视频','https://www.bilibili.com/video/BV19v411M7Rs/?spm_id_from=333.999.0.0')
    elif go1=='我做了一个自己打字的键盘……':
        st.link_button('播放2视频','https://www.bilibili.com/video/BV1W14y1b7Mq/?spm_id_from=333.999.0.0')
    elif go1=='首次公开！带你逛我们工作室':
        st.link_button('播放3视频','https://www.bilibili.com/video/BV1oC411B7wu/?spm_id_from=333.999.0.0')
    st.write("--------------------")
    st.image("数学.png")
    st.write("数学区视频搬运")
    go2=st.selectbox("选择播放视频",['为什么1/89的小数部分藏着斐波那契数列？','刘谦春晚魔术背后是什么数学原理？','所有数都是无理数？'])
    if go2=='为什么1/89的小数部分藏着斐波那契数列？':
        st.link_button('播放1视频','https://www.bilibili.com/video/BV1Lr421F7Ku/?spm_id_from=333.337.search-card.all.click')
    elif go2=='刘谦春晚魔术背后是什么数学原理？':
        st.link_button('播放2视频','https://www.bilibili.com/video/BV1FA4m157um/?spm_id_from=333.337.search-card.all.click')
    elif go2=='所有数都是无理数？':
        st.link_button('播放3视频','https://www.bilibili.com/video/BV1wH4y1D7Lu/?spm_id_from=333.337.search-card.all.click')
    st.write("--------------------")
    st.image("科普.png")
    st.write("科普区视频搬运")
    go3=st.selectbox("选择播放视频",['时间有四种方向','宇宙最极端的三种生命形式','星舰意味着什么？'])
    if go3=='时间有四种方向':
        st.link_button('播放1视频','https://www.bilibili.com/video/BV1xa4y1E74M/?spm_id_from=333.337.search-card.all.click')
    elif go3=='宇宙最极端的三种生命形式':
        st.link_button('播放2视频','https://www.bilibili.com/video/BV1nN411Y7Jz/?spm_id_from=333.788')
    elif go3=='星舰意味着什么？':
        st.link_button('播放3视频','https://www.bilibili.com/video/BV1eT411n7vs/?spm_id_from=333.999.0.0')
    st.write("--------------------")
    st.image("手工.png")
    st.write("手工区视频搬运")
    go4=st.selectbox("选择播放视频",['魔刀千刃制作','原神雷电将军武器极致还原','黄金爪子刀制作'])
    if go4=='魔刀千刃制作':
        st.link_button('播放1视频','https://www.bilibili.com/video/BV1tJ411W7hw/?spm_id_from=333.337.search-card.all.click')
    elif go4=='原神雷电将军武器极致还原':
        st.link_button('播放2视频','https://www.bilibili.com/video/BV1rh411W7nH/?spm_id_from=333.337.search-card.all.click')
    elif go4=='黄金爪子刀制作':
        st.link_button('播放3视频','https://www.bilibili.com/video/BV1Je4y1V7uA/?spm_id_from=333.337.search-card.all.click')
    st.write("--------------------")
    st.image("桌游.png")
    st.write("桌游区视频搬运")
    go5=st.selectbox("选择播放视频",['师生对线战棋版！','自制战棋桌游《骑士与魔法》完全体！','自制桌游《迷你篮球赛》'])
    if go5=='师生对线战棋版！':
        st.link_button('播放1视频','https://www.bilibili.com/video/BV1qj421d7Ej/?spm_id_from=333.999.0.0')
    elif go5=='自制战棋桌游《骑士与魔法》完全体！':
        st.link_button('播放2视频','https://www.bilibili.com/video/BV1UK4y1z7gF/?spm_id_from=333.337.search-card.all.click')
    elif go5=='自制桌游《迷你篮球赛》':
        st.link_button('播放3视频','https://www.bilibili.com/video/BV1De411f7r9/?spm_id_from=333.999.0.0')
    st.write("--------------------")

def img_change(img,rc,gc,bc):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img

def page_2():
    st.write(":level_slider:图片处理工具:level_slider:")
    uploaded_file=st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        st.write(file_name,file_type,file_size)
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4,tab5=st.tabs(["原图","改色1","改色2","改色3","改色4"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
        with tab5:
            img_invert=ImageOps.invert(img)
            st.image(img_invert)

def page_3():
    st.write("词典")
    with open("words_space.txt","r",encoding="utf-8") as f:
        words_list=f.read().split("\n")
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    with open("check_out_times.txt",'r',encoding='utf-8') as f:
        times_list=f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    word=st.text_input("请输入要查询的单词（一次一词，首字母非大写，暂时不支持查询人名）")
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open("check_out_times.txt","w",encoding="utf-8") as f:
            message=''
            for k,v in times_dict.items():
                message+=str(k)+'#'+str(v)+'\n'
            message=message[:-1]
            f.write(message)
        st.write("查询次数:",times_dict[n])
        if word=="snow":
            st.snow()
        if word=="python":
            st.code('''# 恭喜你触发彩蛋，这是一行Python代码:print('hello world')''')
        if word=="plant" or word=="zombie":
            st.code('''# 恭喜你触发彩蛋，小屋创造者特别喜欢玩植物大战僵尸。''')

def page_4():
    st.write("评论区，欢迎大家来发帖")
    with open("leave_messages.txt",'r',encoding='utf-8') as f:
        messages_list=f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split('#')
    for i in messages_list:
        if i[1]=="浏览者":
            with st.chat_message('✨'):
                st.write(i[1],':',i[2])
        elif i[1]=="作者":
            with st.chat_message('❗'):
                st.write(i[1],':',i[2])
    name=st.selectbox("我是……",['浏览者','作者'])
    new_message=st.text_input("想要说的话……")
    if st.button('评论'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open("leave_messages.txt","w",encoding="utf-8") as f:
            message=''
            for i in messages_list:
                message+=i[0]+'#'+i[1]+'#'+i[2]+'\n'
            message=message[:-1]
            f.write(message)

def page_5():
    w=st.selectbox("选择作者录制的视频",["土豆雷、大嘴花狂喜，高建国、蔡徐坤的悲哀","土豆雷和荔枝寄出强大，蔡徐坤排雷兵意念合一"])
    if w=="土豆雷、大嘴花狂喜，高建国、蔡徐坤的悲哀":
        st.video("蔡徐坤处刑视频.mp4")
    elif w=="土豆雷和荔枝寄出强大，蔡徐坤排雷兵意念合一":
        st.video("土豆雷处刑视频.mp4")

if page == '视频搬运':
    page_1()
elif page == '图片处理工具搬运':
    page_2()
elif page == '词典搬运':
    page_3()
elif page == '评论区':
    page_4()
elif page=='神秘界面':
    page_5()
