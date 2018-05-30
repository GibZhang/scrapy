# coding=utf-8
"""
存储评论内容的实体类
"""


class Comment:
    """
    评论实体类
    """

    def __init__(self, usernm, count, content):
        self.username = usernm  # 用户名
        self.count = count  # 评论点赞数
        self.content = content  # 评论内容

    def __repr__(self):
        return "###" + self.username + "————" + self.count + "————" + self.content
