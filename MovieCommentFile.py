# coding=utf-8
"""
保存电影影评的文件
"""


class MovieCommentFile:
    def __init__(self, movie):
        self.path = "/Volumes/USBDISK/" + movie + ".txt"

    def write(self, data):
        with open(self.path, 'w') as file:
            for comment in data:
                file.write(comment)

    def read(self):
        data = []
        with open(self.path, 'r') as file:
            flag = True
            tmp = ''
            while flag:
                sepfi = True
                while sepfi:
                    elem = file.readline()
                    if elem == '':
                        flag = False
                        sepfi = False
                    else:
                        if elem.lstrip().startswith("###"):
                            data.append(tmp)
                            sepfi = False
                            tmp = elem
                        else:
                            tmp += elem
        return data
