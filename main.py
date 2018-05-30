# coding=utf-8
from DataSpider import DataSpider
from MovieCommentFile import MovieCommentFile
from pyecharts import Bar
def main():
    """
    测试
    :return:
    """
    dataSpider = DataSpider('https://www.douban.com/accounts/login?source=movie', '****',
                            '****')
    data = dataSpider.get_data("无问东西")
    moviefile = MovieCommentFile("无问东西")
    moviefile.write(data)


if __name__ == '__main__':
    main()
