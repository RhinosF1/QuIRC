print('QuIRC Setup Modifcation tool. Use !getinfo on IRC after running this to update the bot\'s cache')
####DEFAULTS###
topic = '' #channel topic for use in channels where quotebot runs
nick = 'quirctest123'
username = 'quirc'
realname = 'quirc'
lastgreeter = ''
greetings = [
    "Hello {}!",
    "Hi {}!",
    "Hello there {}!",
    "Hi there {}!",
    "Hey {}!"
]
owapikey = '' #place an api key for open weather map here
admins = ['freenode-staff', 'freenode-staff']
##FUNCTION FLAGS - SET TO 1 TO ENABLE
greetingsbot = 1
weatherbot = 0
units = 'metric'
linkbot = 1
quotebot = 1
pingbot = 1
buttbot = 0
cashortbot = 1
nspassword = ''
print('Downloading your current settings...')
###GETSETTINGS###
infofile = ('settings.csv', 'r')
for line in infofile:
        setting = line.split(';')
        if setting[0] == 'topic':
            topic = setting[1]
        if setting[0] == 'nick':
            nick = setting[1]
        if setting[0] == 'username':
            username = setting[1]
        if setting[0] == 'realname':
            realname = setting[1]
        if setting[0] == 'greetings':
            greetings = settings[1].split(',')
        if setting[0] == 'greetingsbot':
            greetingsbot = setting[1]
        if setting[0] == 'weatherbot':
            weatherbot = setting[1]
        if setting[0] == 'owapikey':
            owapikey = setting[1]
        if setting[0] == 'units':
            units = setting[1]
        if setting[0] == 'linkbot':
            linkbot = setting[1]
        if setting[0] == 'quotebot':
            quotebot = setting[1]
        if setting[0] == 'pingbot':
            greetingsbot = setting[1]
        if setting[0] == 'buttbot':
            buttbot = setting[1]
        if setting[0] == 'cashortbot':
            cashortbot = setting[1]
        if setting[0] == 'admins':
            admins = setting[1]
            admins = admins.split(',')
        if setting[0] == 'nspassword':
            nspassword = setting[1]
print('Starting tool....')
run = 1
while run == 1:
    print('----')
    print('1.nick')
    print('2.username')
    print('3.realname')
    print('4.NickServ Password')
    print('5.topic')
    print('6.greetings')
    print('7.greetingsbot')
    print('8.weatherbot')
    print('9.owapikey')
    print('10.units')
    print('11.linkbot')
    print('12.quotebot')
    print('13.pingbot')
    print('14.buttbot')
    print('15.cashortbot')
    print('16.admins')
    settoupdate = input('Which setting would you like to update?')
    if settoupdate == 1:
        nick = input('What is your bot nick? ')
    if settoupdate == 2:
        username = input('What is your bot username? ')
    if settoupdate == 3:
        realname == input('What is your bot realname? ')
    if settoupdate == 4:
        nspassword = input('What is the bot\'s NickServ Password? ')
    if settoupdate == 5:
        topic = input('What is the topic in the channel the bot runs in? ')
    if settoupdate == 6:
        print('For each gretting please add a {} where the nick of the sender should go')
        print('After each greeting, place a comma to seperate them')
        greetings = input('What greetings should be used? ')
    if settoupdate == 7:
        greetingsbot = input('Should the greetingsbot module be enabled? [1 for yes, 0 for no] ' )
    if settoupdate == 8:
        weatherbot = input('Should the weatherbot module be enabled? [1 for yes, 0 for no] ')
    if settoupdate == 9:
        owapikey = input('What is your open weather map api key? ')
    if settoupdate == 10:
        units = input('What temperature scale should the bot use? [imperial or metric]')
    if settoupdate == 11:
        linkbot = input('Should the linkbot module be enabled? [1 for yes, 0 for no] ')
    if settoupdate == 12:
        quotebot = input('Should the quotebot module be enabled? [1 for yes, 0 for no] ')
        if quotebot.isnum() == True:
            if quotebot == 1:
                print('Please gets your quotes ready, you should seperate quotes with a comma and place them in quoutes.csv ')
    if settoupdate == 13:
        pingbot = input('Should the pingbot module be enabled? (PM ONLY) [1 for yes, 0 for no] ')
    if settoupdate == 14:
        buttbot = input ('Should the buttbot module be enabled? [1 for yes, 0 for no] ')
    if settoupdate == 15:
        cashortbot = input('Should the central auth short links bot module be enabled? [1 for yes, 0 for no] ')
    if settoupdate == 16:
        admins = input('Who are the bots admins (they get access to functions which either require them to be present at the computer running the bot or that have the power to bring the botdown)? -- seperate with a comma ')
    another = input('Would you like to update anything else? y/n ').lower()
    if another == 'n':
        run = 0
print('Your settings file will now be updated')
file = open('settings.csv', 'w+')
content = ''
content = 'nick;'+str(nick)+',\n'
content = str(content)+'username;'+str(username)+';\n'
content = str(content)+'realname;'+str(realname)+';\n'
content = str(content)+'nspassword;'+str(nspassword)+';\n'
content = str(content)+'topic;'+str(topic)+';\n'
content = str(content)+'greetings;'+str(greetings)+';\n'
content = str(content)+'greetingsbot;'+str(greetingsbot)+';\n'
content = str(content)+'weatherbot;'+str(weatherbot)+';\n'
content = str(content)+'owapikey;'+str(owapikey)+';\n'
content = str(content)+'units;'+str(units)+';\n'
content = str(content)+'linkbot;'+str(linkbot)+';\n'
content = str(content)+'quotebot;'+str(quotebot)+';\n'
content = str(content)+'pingbot;'+str(pingbot)+';\n'
content = str(content)+'buttbot;'+str(buttbot)+';\n'
content = str(content)+'cashortbot;'+str(cashortbot)+';\n'
content = str(content)+'admins;'+str(admins)+';\n'
file.write(content)
print('Update Complete. Please use !getinfo to update bot\'s cache')
file.close()
