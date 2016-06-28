from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import json
import libs.web_crawler as web_crawler
import libs.str

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

@respond_to('I love you')
def love(message):
    message.reply('I love you too!')

@listen_to('Can someone help me?')
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
