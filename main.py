#!/usr/bin/python
import sys

file_path = sys.argv[1]

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


def main():
    user1 = {}
    print(file_path)
    with open(file_path, 'r', encoding='utf-8') as chat:
        chats = chat.readlines()
    s = ''
    for i in chats:
        ss = i.split(':')
        s += ss[-1]

    stopwords = set(STOPWORDS)
    stopwords.add('media')
    stopwords.add('omitted')

    word_cloud = WordCloud(collocations=False,
                           background_color='white',
                           stopwords=stopwords).generate(s)
    plt.figure(figsize=(18, 18), facecolor=None)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    for session in chats:
        try:
            int(session.split(",")[0].split("/")[0])
            int(session.split(",")[0].split("/")[1])
            if session.split(",")[0] not in user1:
                user1[session.split(",")[0]] = 1
            else:
                user1[session.split(",")[0]] = 1 + user1[session.split(",")[0]]
        except:
            pass

    x = []
    y = []
    j = 0
    n = 0

    for i in user1:
        y.append(j)
        x.append(user1[i])
        n = n + user1[i]
        j += 1
    Keymax = max(user1, key=user1.get)
    fig = plt.figure()
    fig.suptitle(file_path, fontsize=14, fontweight='bold')
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    ax.set_title(
        'total number of messages are {} in {} days. Average {} text/day. On {} max number of text were sent:{}'
        .format(n, len(user1), n // len(user1), Keymax, user1[Keymax]))

    ax.plot(y, x)
    ax.set_xlabel('days')
    ax.set_ylabel('number of messages')

    # plt.show()

    # D = user1
    # plt.bar(range(len(D)), list(D.values()), align='center')
    # plt.xticks(range(len(D)), list(D.keys()))
    plt.get_current_fig_manager().full_screen_toggle(
    )  # toggle fullscreen mode
    plt.show()

    plt.close()


main()
