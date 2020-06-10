####DEFAULTS###
topic = ''
nick = 'quirctest123'
lastgreeter = ''
greetings = [
    "Hello {}!",
    "Hi {}!",
    "Hello there {}!",
    "Hi there {}!",
    "Hey {}!"
]
owapikey = ''
admins = ['freenode-staff', 'freenode-staff']
greetingsbot = 1
weatherbot = 0
linkbot = 1
quotebot = 1
pingbot = 1
buttbot = 0
cashortbot = 1
##RUN THIS SCRIPT AFTER INSTALLING THIS -- THIS WILL ALLOW YOU TO SETUP A WORKING SETTINGS FILE
##WHEN ENABLING BOTS - YOU MUST ANSWER 1 (ON) OR 0 (OFF)
print('Thanks for downloading QuIRC\'s QuIRC Bot Scripts')
print('This will create your settings file for you')
print('----')
nick = input('What is your bot nick? ')
nspassword = input('What is the bot\'s NickServ Password? ')
username = input('What is your bot user name? ')
realname = input('What is your bot real name? ')
topic = input('What is the topic in the channel the bot runs in? ')
print('For each gretting please add a {} where the nick of the sender should go')
print('After each greeting, place a comma to seperate them')
greetings = input('What greetings should be used? ')
greetingsbot = input('Should the greetingsbot module be enabled? [1 for yes, 0 for no] ')
weatherbot = input('Should the weatherbot module be enabled? [1 for yes, 0 for no] ')
if weatherbot.isdigit() == True:
  if weatherbot == 1:
    owapikey = input('What is your open weather map api key? ')
linkbot = input('Should the linkbot module be enabled? [1 for yes, 0 for no] ')
quotebot = input('Should the quotebot module be enabled? [1 for, 0 for no] ')
if quotebot.isdigit() == True:
  if quotebot == 1:
   print('Please gets your quotes ready, you should seperate quotes with a comma and place them in quoutes.csv')
pingbot = input('Should the pingbot module be enabled? (PM ONLY) [1 for yes, 0 for no l] ')
buttbot = input ('Should the buttbot module be enabled? [1 for yes, 0 for no] ')
cashortbot = input('Should the central auth short links bot module be enabled? [1 for yes, 0 for no] ')
admins = input('Who are the bots admins (they get access to functions which either require them to be present at the computer running the bot or that have the power to bring the botdown)? -- seperate with a comma ')
print('Your settings file will now be created')
file = open('settings.csv', 'w+')
content = ''
content = 'nick;'+str(nick)+';\n'
content = str(content)+'nspassword;'+str(nspassword)+';\n'
content = str(content)+'username;'+str(username)+';\n'
content = str(content)+'realname;'+str(realname)+';\n'
content = str(content)+'topic;'+str(topic)+';\n'
content = str(content)+'greetings;'+str(greetings)+';\n'
content = str(content)+'greetingsbot;'+str(greetingsbot)+';\n'
content = str(content)+'weatherbot;'+str(weatherbot)+';\n'
content = str(content)+'owapikey;'+str(owapikey)+';\n'
content = str(content)+'linkbot;'+str(linkbot)+';\n'
content = str(content)+'quotebot;'+str(quotebot)+';\n'
content = str(content)+'pingbot;'+str(pingbot)+';\n'
content = str(content)+'buttbot;'+str(buttbot)+';\n'
content = str(content)+'cashortbot;'+str(cashortbot)+';\n'
content = str(content)+'admins;'+str(admins)+';\n'
file.write(content)
print('Setup Complete. The bot may now be ran using bot.py')
file.close()
