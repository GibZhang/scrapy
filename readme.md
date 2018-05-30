## 爬取豆瓣电影《无问西东》影评信息
*获取其他电影的影评，只需要修改电影名称即可*
### 要点
* 用selenium模拟登录豆瓣
* 影评数据保存在文件中
* 数据清洗并保存在mysql中
* 用echarts可视化分析评论数密度分布
* 用jieba分词
* 用WordCloud做云图


**1、用selenium模拟登录豆瓣**

- 使用selenium的webdriver

        def __init__(self, url, username, password):
            self.url = url
            self.username = username
            self.password = password
            self.driver = webdriver.Safari()


        
- 获取用户名、密码元素

        def login(self):
            """
            模拟登录
            :param url:  登录url
            :param username: 用户名
            :param password:  密码
            :return:
            """
            time.sleep(3)
            self.driver.get(self.url)
            elem_username = self.driver.find_element_by_name("form_email")
            elem_username.send_keys(self.username)
            elem_passowrd = self.driver.find_element_by_name("form_password")
            elem_passowrd.send_keys(self.password)
- 利用pytesseract自动识别验证码

        def get_confirm_code(self, file):
            """
            从图片中识别出验证码
            :return:
            """
            image = Image.open(file) //读取验证码图片
            text = ""
            try:
                text = pytesseract.image_to_string(image) //图片识别
            except Exception as e: 
                print(e)
            return text
**2、数据保存到文件**
![数据文件截图](https://raw.githubusercontent.com/GibZhang/scrapy/master/fileshoot.png)

**3、数据简单清洗**

**4、数据保存到mysql**
- python操作mysql太简单了，不做赘述

**5、用echarts可视化分析**

        bar = Bar("电影《无问东西》", "来源于豆瓣")
        bar.add("评论点赞数", laxis, haxis, mark_line=["average"], mark_point=["max", "min"])
        bar.render()
        
 ![echart评论点赞数目密度](https://github.com/GibZhang/scrapy/blob/master/echart.png)

**6、用jieba分词处理**

        for ele in data:
            text = str(ele).split("————")
            for x in jieba.cut(text):
                if len(x) > 1:
                    if x in word_list:
                        word_list[x] += 1
                    else:
                        word_list[x] = 0
**7、用WordCloud做云图**

 ![评论词频云图](https://github.com/GibZhang/scrapy/blob/master/moviecloud.png)
**8、简单分析总结**

   从评论云图中可以看出，这个电影是具有明显的时代特征，章子怡、黄晓明、王力宏、张震等在评论中出现频率较高，大多数人比较喜欢这个电影，
   故事背景应该与清华大学有关，同时比较有趣的是有很多关于片尾和彩蛋的评论，那么大家千万不要错过这个电影片尾的彩蛋哦

