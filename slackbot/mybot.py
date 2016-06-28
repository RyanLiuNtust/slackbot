from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import json
import libs.web_crawler as web_crawler
import libs.str
import random

def random_reply(str_list):
    return random.sample(str_list, 1)[0]

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

@respond_to('I love you', re.IGNORECASE)
def love(message):
    message.reply('I love you too!')

@listen_to('Can someone help me?', re.IGNORECASE)
def help(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')

    # Message is sent on the channel
    # message.send('I can help everybody!')

@respond_to('web (.*) (.*)', re.IGNORECASE)
def web(message, keyword=None, web_type=None):
    # refer to https://api.slack.com/docs/message-attachments
    support_types = ['github', 'google']
    keyword = libs.str.str_encode(keyword)
    web_type = web_type.lower()
    if web_type == 'github':
        link = 'https://www.github.com/{}'.format(keyword)
        w = web_crawler.web()
        p = w.get_all_property(link)
        attachments = [
        {
            'fallback': 'Fallback text',
            'title': '{}'.format(p['title']),
            'thumb_url': '{}'.format(p['img']),
            'title_link': '{}'.format(link),
            'text': '{}'.format(p['desc']),
            'color': '#59afe1'
        }]
        message.send_webapi('', json.dumps(attachments))

    elif web_type == 'google':
        w = web_crawler.web()
        n_results = 3
        results = w.google_search(keyword, n_results)
        attachments = []
        for result in results:
            attachments.append({
                'fallback': 'Fallback text',
                'title': '{}'.format(result['title']),
                'thumb_url': '{}'.format(result['img']),
                'title_link': '{}'.format(result['link']),
                'text': '{}'.format(result['desc']),
                'color': '#59afe1'
            })
        message.send_webapi('',json.dumps(attachments))
    else:
        message.reply('Unknown type {}, only supports {}'.format(web_type, support_types))

@listen_to('joan', re.IGNORECASE)
def joan(message):
    replies = ['https://www.youtube.com/watch?v=GJ26gAc7BtU', 
               'https://www.youtube.com/watch?v=xHsSWiLsIRY',
               'https://www.youtube.com/watch?v=1YpLiiSNR5g',
               'https://www.youtube.com/watch?v=Njmg4CcljGg',
               'https://i.imgur.com/tNHKqGg.jpg',
               'http://www.101media.com.tw/img/file/1408577407wnxij.jpg',
               'http://whatscap.ristury.com/java/WhatsCAP/content/photo/v1/80890_WM.jpg',
               '87']
    message.reply(random_reply(replies))


@respond_to('joan', re.IGNORECASE)
def joan_reply(message):
    replies = ['who is joan?', 
               'Oh, I know she is {}'.format(random.sample(['good',
                                                            'bad',
                                                            'oh my god...',
                                                            '....en, no comment!!',
                                                            'https://i.ytimg.com/vi/reg9Xxa7eIs/hqdefault.jpg'], 1)[0])]
    message.reply(random_reply(replies))

@respond_to('123', re.IGNORECASE)
def one_two_three(message):
    replies = ['456', '123', '=6', 'https://www.youtube.com/watch?v=tc2oZzTi8RY']
    message.reply(random_reply(replies))

@respond_to('(.*)x(.*)', re.IGNORECASE)
def mul(message, a, b):
    result = str(float(a) * float(b))
    reply = '{} x {} = {}'.format(a, b, result)
    message.reply(reply)

@respond_to('(.*)/(.*)', re.IGNORECASE)
def div(message, a, b):
    result = str(float(a) / float(b))
    reply = '{} / {} = {}'.format(a, b, result)
    message.reply(reply)

@respond_to('(.*) add (.*)', re.IGNORECASE)
def add(message, a, b):
    print a, b
    result = str(float(a) + float(b))
    reply = '{} + {} = {}'.format(a, b, result)
    message.reply(reply)

@respond_to('(.*)-(.*)', re.IGNORECASE)
def sub(message, a, b):
    result = str(float(a) - (float(b)))
    reply = '{} - {} = {}'.format(a, b, result)
    message.reply(reply)

@respond_to('(.*) power (.*)', re.IGNORECASE)
def power(message, a, b):
    result = str(float(a) ** float(b))
    reply = '{} ** {} = {}'.format(a, b, result)
    message.reply(reply)

