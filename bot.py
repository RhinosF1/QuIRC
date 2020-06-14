import QuIRC
import random
import requests
import re
import time
import random
topic = '' #channel topic for use in channels where quotebot runs
nick = 'quirctest123'
username = 'quirc'
realname = 'realname'
bot = QuIRC.IRCConnection()
lastgreeter = ''
greetings = [
    "Hello {}!",
    "Hi {}!",
    "Hello there {}!",
    "Hi there {}!",
    "Hey {}!"]
owapikey = '' #place an api key for open weather map here
admins = ['freenode-staff', 'freenode-staff']

##FUNCTION FLAGS - SET TO 1 TO ENABLE

greetingsbot = 1
weatherbot = 0
units = '' #imperal or metric units for weaterbot output
linkbot = 1
quotebot = 1
pingbot = 1
buttbot = 0
cashortbot = 1
nspassword = ''


def getinfo():
    print('loadingconfig')
    global topic
    global nick
    global username
    global realname
    global greetings
    global greetingsbot
    global weatherbot
    global units
    global linkbot
    global quotebot
    global pingbot
    global buttbot
    global cashortbot
    global admins
    global owapikey
    global nspassword
    infofile = open('settings.csv', 'r')
    for line in infofile:
        setting = line.split(';')
        print(setting)
        if setting[0] == 'topic':
            topic = setting[1]
        if setting[0] == 'nick':
            nick = setting[1]
        if setting[0] == 'username':
           username = setting[1]
        if setting[0] == 'realname':
           realname = setting[1]
        if setting[0] == 'greetings':
            greetings = setting[1].split(',')
        if setting[0] == 'greetingsbot':
            greetingsbot = int(setting[1])
        if setting[0] == 'weatherbot':
            weatherbot = int(setting[1])
        if setting[0] == 'owapikey':
            owapikey = setting[1]
        if setting[0] == 'units':
            units = setting[1]
        if setting[0] == 'linkbot':
            linkbot = int(setting[1])
        if setting[0] == 'quotebot':
            quotebot = setting[1]
        if setting[0] == 'pingbot':
            pingbot = int(setting[1])
        if setting[0] == 'buttbot':
            buttbot = setting[1]
        if setting[0] == 'cashortbot':
            cashortbot = int(setting[1])
        if setting[0] == 'admins':
            admins = setting[1]
            admins = admins.split(',')
        if setting[0] == 'nspassword':
            nspassword = setting[1]

def on_connect(bot):
    bot.set_nick(nick)
    bot.send_user_packet(nick,realname)

def on_welcome(bot):
    global nspassword
    bot.send_message('NickServ', 'identify ' + nspassword)
    print('Authed to NickServ')
    time.sleep(10)
    bot.join_channel('#channel')
    print('Joined channels')

def on_message(
    bot,
    channel,
    sender,
    message
    ):
    global topic
    global nick
    global lastgreeter
    global greetings
    global greetingsbot
    global weatherbot
    global quotebot
    global linkbot
    global pingbot
    global buttbot
    global cashortbot
    global admins
    global owapikey
    sendernick = sender.split('!')[0]
    senderhost = sender.split('@')[1]
    if "hi " in message.lower() and greetingsbot == 1 or "hello " in message.lower() and greetingsbot == 1:
        global lastgreeter
        if lastgreeter == sender:
            print('Greetingsbot failed as sender was same as last greeter')
        else:
            print('got greeting message')
            greeting_message = random.choice(greetings).format(sendernick)
            print('picked greeting: ' + greeting_message)
            bot.send_message(channel, greeting_message)
            print('Sent greeting')
        lastgreeter = sender
    if message.lower().startswith('!opme') and sendernick in admins:
	          bot.send_line('MODE ' + channel + ' +o ' + sendernick)

    if message.lower().startswith('!deopme') and sendernick in admins:
	          bot.send_line('MODE ' + channel + ' -o ' + sendernick)

    if message.lower().startswith('!kick') and sendernick in admins:
	          arg = message.split(' ')
	          target = arg[1]
	          bot.send_line('KICK ' + channel + ' ' + target)
    if message.lower().startswith("http://") and linkbot == 1 or message.lower().startswith("https://") and linkbot == 1:
            print('Found link')
            html = requests.get(message.lower()).text
            title_match = re.search("<title>(.*?)</title>", html)
            print('Finding a title')
            if title_match:
                print(title_match.group(1))
                title = title_match.group(1)
                print(title)
                message = "Title of the URL by {}: {}".format(sendernick, title)
                print(message)
                bot.send_message(channel, message)
                print('Sent title')
    if message.split()[0] == "!weather" and weatherbot == 1:
        print('Seen weather ping')
        if len(message.split()) > 1:
            location = message.lower()
            location = location[9:]
            print('Detected location: ' + location)
            weather_data = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+location+"&APPID="+owapikey+ "&units="+units).json()
            if weather_data["cod"] == 200:
                print('Got 200 response from API')
                message = "The weather in {} is {} and {} degrees.".format(weather_data["name"], weather_data["weather"][0]["description"], weather_data["main"]["temp"])
                bot.send_message(channel, message)
                print('Sent weather to channel')
            else:
                bot.send_message(channel, sendernick + ': API Fault')
                print('API fault on !weather')
        else:
            bot.send_message(channel, "Usage: !weather Istanbul")
    for message_part in message.split():
        if message.lower() == '!pickquote' and quotebot == 1:
            print('Got !pickquote command')
            quotelist = open('quotes.csv', 'r')
            print('Getting quotes')
            quotes = quotelist.read()
            quotes = quotes.split(',')
            numq = len(quotes)
            print('Read quotes')
            numq = int(numq)-1
            picked = random.randint(0,int(numq))
            print('Picked ' + str(picked))
            pq = quotes[picked]
            print('Which is: ' + pq)
            bot.send_message(channel, 'Todays quote is: ' + str(pq))
            bot.send_message('ChanServ', 'topic ' + channel + ' ' + topic + ' | Quote of the day: ' + pq)
            print('Announced it')
    if buttbot == 1:
        message1 = message.lower()
        message1 = message.split(' ')
        newmess = ''
        print(message)
        wordsf = open('bbwords.csv', 'r')
        words = wordsf.read()
        words = words.split(',')
        print(words)
        go = random.randint(1,4)
        print(go)
        if any(x in words for x in message) and go == 1:
            print('on path')
            messlen = len(message1)
            replace = random.randint(1, messlen)
            on = 0
            while on < messlen:
                if on == replace:
                    newmess = newmess + ' butt'
                else:
                    newmess = newmess + ' ' + message1[on]
                on = on + 1
            bot.send_message(channel, newmess)
    if message.lower() == '!getinfo' and sender in admins:
        bot.set_nick(nick + '-down')
        bot.send_message(sender, 'Rebuilding')
        topic = ''
        nick = ''
        lastgreeter = ''
        greetings = ''
        owapikey = ''
        admins = ''
        greetingsbot = 0
        weatherbot = 0
        linkbot = 0
        quotebot = 0
        pingbot = 0
        buttbot = 0
        cashortbot = 0
        nspassword = ''
        time.sleep(1)
        getinfo()
        time.sleep(1)
        bot.send_message(sender, 'Rebuilt')
        bot.set_nick(nick)
    if message.lower().startswith('!wmca') and cashortbot == 1:
        user = message.split(' ')
        user = user[1]
        bot.send_message(channel, sender + ': https://meta.wikimedia.org/wiki/Special:CentralAuth/' + user)
    if message.lower().startswith('!mhca') and cashortbot == 1:
        user = message.split(' ')
        user = user[1]
        bot.send_message(channel, sender + ': https://meta.miraheze.org/wiki/Special:CentralAuth/' + user)



def on_pm(bot, sender, message):
    global topic
    global nick
    global lastgreeter
    global greetings
    global greetingsbot
    global weatherbot
    global quotebot
    global linkbot
    global pingbot
    global buttbot
    global cashortbot
    global admins
    global owapikey
    print('Got PM')
    if message.lower() == 'ping' and pingbot == 1:
        print('Got ping message over PM')
        bot.send_message(sender, 'PONG')
        print('PONGed user back')
    if "hi " in message.lower() and greetingsbot == 1 or "hello " in message.lower() and greetingsbot == 1:
        global lastgreeter
        print('got greeting message')
        greeting_message = random.choice(greetings).format(sender)
        print('picked greeting: ' + greeting_message)
        bot.send_message(sender, greeting_message)
        print('Sent greeting')
    for message_part in message.split():
        if message_part.startswith("http://") and linkbot == 1 or message_part.startswith("https://") and linkbot == 1:
            print('Found link')
            html = requests.get(message_part).text
            title_match = re.search("<title>(.*?)</title>", html)
            print('Finding a title')
            if title_match:
                print(title_match.group(1))
                title = title_match.group(1)
                title = title.encode("ascii", "replace")
                print(title)
                message = "Title of the URL by {}: {}".format(sender, title)
                message = message.encode("ascii", "replace")
                print(message)
                bot.send_message(sender, message)
                print('Sent title')
    if message.split()[0] == "weather" and weatherbot == 1:
        print('Seen weather ping')
        if len(message.split()) > 1:
            location = message.lower()
            location = location[8:]
            print('Detected location: ' + location)
            weather_data = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+location+"&APPID="+owapikey+ "&units=metric").json()
            if weather_data["cod"] == 200:
                print('Got 200 response from API')
                message = "The weather in {} is {} and {} degrees.".format(weather_data["name"], weather_data["weather"][0]["description"], weather_data["main"]["temp"])
                message = message.encode("ascii", "replace")
                bot.send_message(sender, message)
                print('Sent weather to channel')
            else:
                bot.send_message(sender, sender + ': API Fault')
                print('API fault on weather')
        else:
            bot.send_message(sender, "Usage: weather Istanbul")
    if buttbot == 1:
        message1 = message.lower()
        message1 = message.split(' ')
        newmess = ''
        print(message)
        wordsf = open('bbwords.csv', 'r')
        words = wordsf.read()
        words = words.split(',')
        print(words)
        go = random.randint(1,4)
        print(go)
        if any(x in words for x in message) and go == 1:
            print('on path')
            messlen = len(message1)
            replace = random.randint(1, messlen)
            on = 0
            while on < messlen:
                if on == replace:
                    newmess = newmess + ' butt'
                else:
                    newmess = newmess + ' ' + message1[on]
                on = on + 1
            bot.send_message(sender, newmess)
    if message.lower() == 'getinfo' and sender in admins:
        bot.set_nick(nick + '-down')
        bot.send_message(sender, 'Rebuilding')
        topic = ''
        nick = ''
        lastgreeter = ''
        greetings = ''
        owapikey = ''
        admins = ''
        greetingsbot = 0
        weatherbot = 0
        linkbot = 0
        quotebot = 0
        pingbot = 0
        buttbot = 0
        cashortbot = 0
        nspassword = ''
        time.sleep(1)
        getinfo()
        time.sleep(1)
        bot.send_message(sender, 'Rebuilt')
        bot.set_nick(nick)
    if message.lower().startswith('wmca') and cashortbot == 1:
        user = message.split(' ')
        user = user[1]
        bot.send_message(sender, sender + ': https://meta.wikimedia.org/wiki/Special:CentralAuth/' + user)
    if message.lower().startswith('mhca') and cashortbot == 1:
        user = message.split(' ')
        user = user[1]
        bot.send_message(sender, sender + ': https://meta.miraheze.org/wiki/Special:CentralAuth/' + user)

getinfo()
bot.on_private_message.append(on_pm)
bot.on_connect.append(on_connect)
bot.on_welcome.append(on_welcome)
bot.on_public_message.append(on_message)
print('Starting...')

bot.connect("chat.freenode.net")
print('Connected')
bot.run_loop()
