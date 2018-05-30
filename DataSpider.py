# coding=utf-8
"""
模拟登录
"""
from selenium import webdriver
import time
from PIL import Image
import pytesseract
from selenium.common.exceptions import NoSuchElementException
from urllib import request
import ssl
from Comment import Comment

ssl._create_default_https_context = ssl._create_unverified_context


class DataSpider:
    """
    完成从豆瓣爬取数据
    """

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Safari()

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
        try:
            elem_code = self.driver.find_element_by_id("captcha_image")
        except NoSuchElementException as e:
            print(e)
        else:
            code_file = "/Users/zhangjingbo/Workspaces/PycharmProjects/scrapy/code.jpeg"
            request.urlretrieve(elem_code.get_attribute("src"), filename=code_file)
            code_text = self.get_confirm_code(code_file)
            self.driver.find_element_by_id("captcha_field").send_keys(code_text)
        elem_submit = self.driver.find_element_by_name("login")
        elem_submit.click()
        time.sleep(3)

    def get_data(self, movie):
        """
        获取评论
        :return:
        """
        # 执行登录操作
        self.login()
        # 搜索相关影片
        link = self.search(self.driver, movie)
        self.driver.get(link)
        comment_list = []
        flag = True
        while flag:
            try:
                comment_list = comment_list + self.get_comments()
                next = self.driver.find_element_by_class_name("next")
                if next.get_attribute("href") == None:
                    flag = False
                else:
                    next.click()
            except NoSuchElementException as e:
                print(e)
        return comment_list

    def search(self, driver, movie):
        driver.get("https://movie.douban.com/subject_search?search_text=" + movie + "&cat=1002")
        # elem_search_text = driver.find_element_by_id("inp-query")
        # elem_search_text.send_keys(movie)
        # elem_tmp = driver.find_element_by_class_name("inp-btn")
        # elem_tmp.find_element_by_tag_name("input").click()
        # 获取第一条搜索结果
        elems = driver.find_elements_by_class_name("detail")
        elem_root = elems[0].find_element_by_class_name("title")
        link = elem_root.find_element_by_tag_name("a").get_attribute("href")
        return link + "comments?status=P"

    def get_confirm_code(self, file):
        """
        从图片中识别出验证码
        :return:
        """
        image = Image.open(file)
        text = ""
        try:
            text = pytesseract.image_to_string(image)
        except Exception as e:
            print(e)
        return text

    def get_comments(self):
        """
        解析评论内容，并返回当前页list
        :return:
        """
        time.sleep(3)
        elems = self.driver.find_elements_by_class_name("comment-item")
        comments = []
        for elem in elems:
            username = elem.find_element_by_class_name("avatar").find_element_by_tag_name("a").get_attribute("title")
            content = elem.find_element_by_class_name("comment").find_element_by_tag_name("p").text
            vote = elem.find_element_by_class_name("comment").find_element_by_class_name("votes").text
            comment = Comment(username, vote, content)
            comments.append(repr(comment))
        return comments

    def __del__(self):
        self.driver.close()
        self.driver.quit()
