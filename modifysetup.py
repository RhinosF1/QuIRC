print('QuIRC Setup Modifcation tool. Use !getinfo on IRC after running this to update the bot\'s cache')
####DEFAULTS###
topic = '' #channel topic for use in channels where quotebot runs
nick = 'quirctest123'
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
        if setting[0] == 'greetings':
            greetings = settings[1].split(',')
        if setting[0] == 'greetingsbot':
            greetingsbot = setting[1]
        if setting[0] == 'weatherbot':
            weatherbot = setting[1]
        if setting[0] == 'owapikey':
            owapikey = setting[1]
        if setting[0] == 'quotebot':
            quotebot = setting[1]
        if setting[0] == 'linkbot':
            linkbot = setting[1]
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
    print('2.NickServ Password')
    print('3.topic')
    print('4.greetings')
    print('5.greetingsbot')
    print('6.weatherbot')
    print('7.owapikey')
    print('8.quotebot')
    print('9.pingbot')
    print('10.buttbot')
    print('11.cashortbot')
    print('12.admins')
    settoupdate = input('Which setting would you like to update?')
    if settoupdate == 1:
        nick = input('What is your bot nick? ')
    if settoupdate == 2:
        nspassword = input('What is the bot\'s NickServ Password? ')
    if settoupdate == 3:
        topic = input('What is the topic in the channel the bot runs in? ')
    if settoupdate == 4:
        print('For each gretting please add a {} where the nick of the sender should go')
        print('After each greeting, place a comma to seperate them')
        greetings = input('What greetings should be used? ')
    if settoupdate == 5:
        greetingsbot = input('Should the greetingsbot module be enabled?' )
    if settoupdate == 6:
        weatherbot = input('Should the weatherbot module be enabled? ')
    if settoupdate == 7:
        owapikey = input('What is your open weather map api key? ')
    if settoupdate == 8:
        quotebot = input('Should the quotebot module be enabled? ')
        if quotebot.isnum() == True:
            if quotebot == 1:
                print('Please gets your quotes ready, you should seperate quotes with a comma and place them in quoutes.csv ')
    if settoupdate == 9:
        pingbot = input('Should the pingbot module be enabled? (PM ONLY) ')
    if settoupdate == 10:
        buttbot = input ('Should the buttbot module be enabled? ')
    if settoupdate == 11:
        cashortbot = input('Should the central auth short links bot module be enabled? ')
    if settoupdate == 12:
        admins = input('Who are the bots admins (they get access to functions which either require them to be present at the computer running the bot or that have the power to bring the botdown)? -- seperate with a comma ')
    another = input('Would you like to update anything else? y/n ').lower()
    if another == 'n':
        run = 0
print('Your settings file will now be updated')
file = open('settings.csv', 'w+')
content = ''
content = 'nick;'+str(nick)+',\n'
content = str(content)+'nspassword;'+str(nspassword)+';\n'
content = str(content)+'topic;'+str(topic)+';\n'
content = str(content)+'greetings;'+str(greetings)+';\n'
content = str(content)+'greetingsbot;'+str(greetingsbot)+';\n'
content = str(content)+'weatherbot;'+str(weatherbot)+';\n'
content = str(content)+'owapikey;'+str(owapikey)+';\n'
content = str(content)+'quotebot;'+str(quotebot)+';\n'
content = str(content)+'pingbot;'+str(pingbot)+';\n'
content = str(content)+'buttbot;'+str(buttbot)+';\n'
content = str(content)+'cashortbot;'+str(cashortbot)+';\n'
content = str(content)+'admins;'+str(admins)+';\n'
file.write(content)
print('Update Complete. Please use !getinfo to update bot\'s cache')
file.close()
