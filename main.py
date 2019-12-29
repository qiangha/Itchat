def starter():
    #pip install itchat

    import time
    import itchat
    from friend_sex import analyseSex
    from friend_location import analyseLocation
    from friend_word_cloud import draw_word_cloud
    import warnings
    warnings.filterwarnings("ignore")

    f= open("birthday_wishes.txt","r")
    for line in f:
        print(line)
        time.sleep(1.5)

    itchat.auto_login()
    friends = itchat.get_friends(update=True)
    # gender of friends 
    analyseSex(friends)
    # location of friends
    analyseLocation(friends)
    #draw wordcloud
    draw_word_cloud()

if __name__ == "__main__":
    starter()