#!/usr/bin/python3
import tweepy
import subprocess as s
import sys

consumer_key="CONSUMER KEY HERE"
consumer_secret="CONSUMER SECRET HERE"

access_token="ACCESS TOKEN HERE"
access_token_secret="ACCESS TOKEN SECRET HERE"

MAXWAIT = 800000

api = None

apiready = False

def postTweetPureText(text,status=None):
    tamano = len(text)
    while (len(text)>280):
        status= api.update_status(status=text[0,279],in_reply_to_status_id =status).id_str
        text=text[279,len(text)]

    status= api.update_status(status=text,in_reply_to_status_id =status).id_str
    return status


def postTweetDecode(text):
    status=None
    for t in text.split("||"):
        status=postTweetPureText(t,status)
        print(t)


def getname():
    if apiready:
        return api.me().name+"[@"+api.me().screen_name+"]"
    else:
        return "default"
def postTweet(text):
    #if apiready:
    cont =0
    while apiready == False:
        if cont ==MAXWAIT:
              s.call(['notify-send','InstaTweet','Still loading try again'])
              sys.exit(0)
        cont+=1
        
    
    tamano = len(text)
    if tamano <0:
        s.call(['notify-send','InstaTweet','The tweet is too long or too short'])
        return
    elif text.find("||")==-1:
        postTweetPureText(text)
        return
    else:
        postTweetDecode(text) 
        return
    # else:
    #     s.call(['notify-send','InstaTweet','Still loading try again'])

def loadapi():
    global apiready
    global api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    apiready = True
    
def getimage():
    print(api.me().profile_image_url_https)    

def checkoptions(tokens):
    for i in range(0,len(tokens)):
        if tokens[i] == "-t":
            postTweet(tokens[i+1])
        if tokens[i] == "-n":
            print(getname())
        if tokens[i] == "-i":
            getimage()

loadapi()
checkoptions(sys.argv)