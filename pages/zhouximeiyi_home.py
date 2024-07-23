import streamlit as st
from PIL import Image, ImageOps

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区', '我的家乡介绍'])

def page_1():
    '''我的兴趣推荐'''
    st.write('Taylor Swift - You need to calm down')
    with open('4.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    #st.image('slogan.png')
    st.write('我的电影推荐')
    st.image('1.png')
    st.write('名侦探柯南挺好看的，现在剧场版也有20多部了:sunglasses:~')
    st.write('其它动漫（元气囝仔、银之匙、虫师、世界第一初恋、萤火之森...）也很不错。。')
    st.write('我的游戏推荐')
    st.image('2.jpg')
    st.write('原神有着古风仙魔的美妙世界，其中的地图丰富多彩，每处都被精心设计，角色也拥有丰富的个性和背景故事。:rainbow:')
    st.write('我的书籍推荐')
    st.image('3.jpg')
    st.write('《嫌疑人X的献身》、《解忧杂货铺》、《额尔古纳河右岸》')
    st.write('我的习题集推荐')
    st.write('额.. 数学的《名校题库》')
    
def page_2():
    '''我的图片处理工具'''
    st.write('Taylor Swift - You need to calm down')
    with open('4.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write(":sparkles:图片换色小程序:sparkles:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        # st.write(file_name, file_type, file_size)
        img = Image.open(uploaded_file)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["原图", "改色1", "改色2", "改色3", "反色"])
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
    st.write('Taylor Swift - You need to calm down')
    with open('4.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write('我的智慧词典')
    st.write('有彩蛋哦~')
    st.write('提示：1.什么时候会吃蛋糕')
    st.write('     2.北方冬天会怎样')
    st.write('     3.你会什么语言编程')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    print(words_list)
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
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
        if word=='python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')
    
def page_4():
    '''我的留言区'''
    st.write('Taylor Swift - You need to calm down')
    with open('4.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write('我的留言区')

    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1], ':', i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1], ':', i[2])
    name = st.selectbox('我是...', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话...')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
        
        

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (b, g, r)
    return img

def page_5():
    '''我的家乡介绍'''
    st.write('Taylor Swift - You need to calm down')
    with open('4.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write('我的家乡介绍')
    #col1, col2, col3, col4 = st.columns([1, 1, 1, 1])    
    #st.image('4.jpg')
    st.write('成都市（Chengdu），简称“蓉”，别称蓉城、锦城，是四川省省会、副省级市、特大城市、成渝地区双城经济圈核心城市，国务院批复确定的中国西部地区重要的中心城市，国家重要的高新技术产业基地、商贸物流中心和综合交通枢纽。全市下辖12个市辖区、3个县、代管5个县级市。常住人口2093.78万人（2020年）陕西诸省市交界。')
    st.write('更多信息：https://baike.so.com/doc/24231950-25023317.html')
    st.write('有名景点')
    st.write('杜甫草堂')
    col1, col2,  = st.columns([1, 2])
    with col1:
        st.image('5.jpg')
        st.write('更多信息：https://baike.so.com/doc/5391457-5628187.html')
    with col2:
        st.write('杜甫草堂位于四川省成都市青羊区西门外的浣花溪畔，是中国唐代伟大现实主义诗人杜甫流寓成都时的故居。草堂完整保留着清代嘉庆重建时的格局，总面积近300亩。园林是非常独特的“混“少陵草堂”碑亭合式”中国古典园林。其中大廨、诗史堂、工部祠3座主要纪念性建筑物，坐落在中轴线上，幽深宁静。草堂占地面积近300亩，完整保留着明弘治十三年（公元1500年）和清嘉庆十六年（公元1811年）修葺扩建时的建筑格局，建筑古朴典雅、园林清幽秀丽，是中国文学史上的一块圣地。1955年成立杜甫纪念馆，1985年更名为成都杜甫草堂博物馆。')    
    st.write('春熙路')
    col1, col2,  = st.columns([1, 2])
    with col1:
        st.image('6.jpg')
        st.write('更多信息：https://baike.so.com/doc/5390891-5627555.html')
    with col2:
        st.write('春熙路位于成都市中心，是一条历史悠久，热闹繁华的商业街，外地人到成都来如果不逛逛春熙路，就好比到北京不去王府井，到上海不到南京路一样令人遗憾。春熙路不仅仅是一条街，而是指北新街以东、总府路以南、红星路以西、东大街以北、南新街、中新街及其临街区域。春熙路不仅是成都的时尚中心，美女打望地，也是美味小吃云集之所，钟水饺、赖汤圆、夫妻肺片、韩包子、龙抄手，还有街边的麻辣烧烤和串串香，价格指数和美味指数的对比一定让你在大饱口福的同时，丝毫不担心钱包的迅速缩水。春熙路主街的交汇处是著名的中山广场，屹立着孙中山铜像。北口还有用花岗石雕制而成的成都风俗浮雕艺术墙，描绘了唐代成都的庙会、花会、灯会、采桑等各个景观。')
    st.write('熊猫基地')
    col1, col2,  = st.columns([1, 2])
    with col1:
        st.image('7.jpg')
        st.write('更多信息：https://baike.so.com/doc/5357001-5592513.html')
    with col2:
        st.write('成都大熊猫繁育基地位处成都市北郊斧头山，距市区10公里，有一条宽阔的熊猫大道与市区相连，现已成为国内开展大熊猫等珍稀濒危野生动物移地保护的主要基地之一。常年饲养有大熊猫、小熊猫、黑颈鹤、白鹳和白天鹅、黑天鹅、雁、鸳鸯及孔雀等动物。在由68科300多种高等植物所构成的基地人工生态植被内栖息着野生鸟类29科90多种（有花花哦~）。现在的基地，翠竹葱茏，绿树成荫，鸟语花香，空气清新，自然山野风光和优美人工景观巧妙融合，各种珍稀濒危动物在其中悠然自得地生息繁衍。')
    st.write('武侯祠')
    col1, col2,  = st.columns([1, 2])
    with col1:
        st.image('8.jpg')
        st.write('更多信息：https://baike.so.com/doc/5342081-5577524.html')
    with col2:
        st.write('武侯祠(汉昭烈庙)位于四川省成都市武侯区，肇始于公元223年修建刘备惠陵时，它是中国唯一的一座君臣合祀祠庙和最负盛名的诸葛亮、刘备及蜀汉英雄纪念地，也是全国影响最大的三国遗迹博物馆。1961年国务院公布武侯祠为首批全国重点文物保护单位，2008年评选为首批国家一级博物馆。成都武侯祠现占地15万平方米，由三国历史遗迹区(文物区)、西区(三国文化体验区)以及锦里民俗区(锦里)三部分组成，享有"三国圣地"的美誉。')

    st.write('成都美食')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.write('火锅')
        st.image('9.jpg')
    with col2:
        st.write('钵钵鸡')
        st.image('10.jpg')
    with col3:
        st.write('龙抄手')
        st.image('11.jpg')
    with col4:
        st.write('麻婆豆腐')
        st.image('12.jpg')
    st.write('有机会的话一定要尝尝:rainbow:~')
        
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '我的家乡介绍':
    page_5()