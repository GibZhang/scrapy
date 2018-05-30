# coding=utf-8
from pyecharts import Bar
from MovieCommentFile import MovieCommentFile
import jieba
import jieba.analyse
from wordcloud import WordCloud
from scipy.misc import imread

def plot_data():
    movie_data = MovieCommentFile("无问东西")
    data = movie_data.read()
    laxis = []
    haxis = []
    i = 0
    for ele in data:
        votes = str(ele).split("————")
        i += 1
        laxis.append(str(i))
        haxis.append(votes[1].strip())
    bar = Bar("电影《无问东西》", "来源于豆瓣")
    bar.add("评论点赞数", laxis, haxis, mark_line=["average"], mark_point=["max", "min"])
    bar.render()


from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


def jieba_plot():
    word_list = {}
    movie_data = MovieCommentFile("无问东西")
    data = movie_data.read()
    for ele in data:
        votes = str(ele).split("————")
        for x in jieba.cut(votes[2]):
            if len(x) > 1:
                if x in word_list:
                    word_list[x] += 1
                else:
                    word_list[x] = 0
    back_color = imread('/Users/zhangjingbo/Downloads/bg.jpg')
    wc = WordCloud(font_path="/Users/zhangjingbo/Downloads/weuruan/msyh.ttf",
                   mask=back_color,
                   background_color="white", max_words=200,
                   max_font_size=80, random_state=42)
    wc.generate_from_frequencies(word_list)
    wc.to_file("%s.png" % ("无问东西云图"))


if __name__ == '__main__':
    jieba_plot()
