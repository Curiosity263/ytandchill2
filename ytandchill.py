import discord
import time
from random import randint
import os
import asyncio
from itertools import cycle

client = discord.Client()

@client.event
async def on_ready():
   await client.change_presence(activity=discord.Game(name='Use [help'))
   print("The bot is ready!")

@client.event
async def on_message(message):
   if message.author == client.user:
       return
   if message.content =='[hello':
       await message.channel.send('Hello!')
   if message.content == '[help':
       embed = discord.Embed(title='**Help**',description='''
`[help fun` - Help about the fun commands
`[help utility` - Help about utility commands''', color = 0x00ff00)
       await message.channel.send(embed=embed)
   if message.content == '[help fun':
       embed1 = discord.Embed(title="**Fun Commands**", description="""
**[hello** - Feeling lonely? Say hello to the bot!(Damn, you got desperate)

**[penis** - I can tell you the length of your penis

**[iq** - I can also tell what your IQ is, test me

**[gender** - Try me! I even know your gender

**[f in the chat** - Responds with f

**[8ball** - 8ball decides for you, think of a yes or no question, then type [8ball to see your answer

**[coinflip** - Flip a coin!

**[roll** - Roll a dice!

**[howgay** - Tells you how gay you are

There is also 3 keys and gates that you can unlock to find a prize at the end decipher this to get the hint ->([hint info).!""", color=0x00ff00)
       await message.channel.send(embed=embed1)
   if message.content == '[help utility':
       embed2 = discord.Embed(title="**Utility commands**",description="""
**[info** - General info about the bot

**[creator info** - Info about the developer of the bot

**[rules** - prints a simplified version fo the rules
""", color=0x00ff00)
       await message.channel.send(embed=embed2)
   if message.content == '[creator info':
       await message.channel.send('This bot is made by the YouTube and Chill staff team, while being founded by Average Alan!')
   if message.content == '[coinflip':
       coin = randint(1,2)
       if coin == 1:
         await message.channel.send('Heads')
       if coin == 2:
         await message.channel.send('Tails')
   if message.content == '[rules':
       embed = discord.Embed(title = '**YOUTUBE AND CHILL RULES**', description = '''
**GENERAL RULES**
────────────────
Respect everyone you meet, especially the staff
No spamming (although the meat is good)
Use tickets properly
Do not threat others. (e.g DDOS, etc.)
Do not swear at anyone, and do not swear excessively
Dont DM/ping people for sub4sub, especially staff
Obey Discord TOS and Community Guidelines
- TOS: https://discordapp.com/terms
- Community Guidelines: https://discordapp.com/guidelines
────────────────
**VOICE CHAT RULES**
────────────────
Do not make unnecessary sounds.
Do not play any bass boost/earrape music or sounds in voice chats.
Dont Troll
Do not use profanity
Do not play any music regarding 18+ content
Respect others while they are talking.
────────────────
**PROMOTION RULES**
────────────────
No promoting in designated channel
No spam promotion.
You can only promote in any channels if you reached 100 invites.
Do not ping while promoting
Do not DM anyone for promotion
Do not sub4sub scam or you will be reported''', color = 0x00ff00)
       await message.channel.send(embed=embed)
   if message.content == '[info':
       embed = discord.Embed(title='**Info about Youtube and Chill bot**', description='''
      
       - Started June 8th 2019
       - Running at 99% uptime since June 12 2019
       - Coding language used: python
       - Running on repl.it with UptimeRobot to keep the code alive 99% of time
       - Average minumum latency: 10.21 ms
       - Average maximum latency: 133.08 ms ''', color=0x00ff00)
       await message.channel.send(embed=embed)
   if message.content == '[hint info':
       embed = discord.Embed(title='**Get the hint by solving this**', description='''
The number is a 6 digit number
The sum of the numbers is **21**
2 of the numbers are the same
The number is an employee number from a movie and a book
The second last number is one of the most basic numbers in math
Type the command like so (Dont include the <>), [<number>''', color = 0xff0000)
       await message.channel.send(embed = embed)
   if message.content == '[655321':
       embed= discord.Embed(title='**Congratulations!**',description =
'''You have found the Copper key, copy this access code and riddle down!
284034
The Copper gate is where all the sentences abate
The Copper gate also needs a mate
The message to the gate is a single character.
And you might need help.
Finding the character, is very fun.
''', color = 0x00ff00)
       await message.author.send(embed=embed)
       await message.delete()
   if message.content == '[wholesome and gloves':
       embed = discord.Embed(title='**Congratulations!**',description =
'''You have found the Jade key! Your access code is 655321.
To find the Jade gate, you must find out the total range for the penis command is. [<lower number> to <higher number>''', color = 0x00ff00)
       await message.author.send(embed=embed)
       await message.delete()
   if message.content == '[-50 to 200':
       embed = discord.Embed(title='**Congratulations!**',description =
'''You have succesfully found the Jade gate! Your code is 913746.
Solve these riddles:
1. This old one falls forever, but never moves at all. He has not lungs nor throat, but still a mighty roaring call. What is it?
2. There is an ancient invention still used in some parts of the world today that allows people to see through walls. What is it?''', color = 0x00ff00)
       await message.author.send(embed=embed)
       await message.delete()
   if message.content == '[waterfall and window':
       embed = discord.Embed(title='**Congratulations!**',description =
'''You have succesfully found the crystal key! Your code is 273926. To find the crystal gate....

Discover which character nickname can get you to the crystal gate, get ready. Because only player one is an option.''', color = 0x00ff00)
       await message.author.send(embed=embed)
       await message.delete()
   if message.content == '[Parzival':
       embed = discord.Embed(title = '**Congratulations!**', description =
'''Code: 173926
Submit your answer to Average Alan, iJeneral_TV or Blitz_Alex
Solve these:
1. When does Christmas come before Thanksgiving?
2. An 8 letter word can have a letter taken away and it still makes a word.
Take another letter away and it still makes a word. Keep on doing that until you have one letter left. What is the word?''', color = 0x00ff00)
       await message.author.send(embed=embed)
       await message.delete()
   if message.content == '[!]':
       embed = discord.Embed(title='**Congratulations!**' , description =
'''You have found the Copper gate!
Code = 430482
Solve these 2 riddles:
1. What is it that when you take away the whole, you still have some left over?
2. They have not flesh, nor feathers, nor scales, nor bone. Yet they have fingers and thumbs of their own. What are they?
Type both answers like this, [<answer1> and <answer2>''', color = 0x00ff00)
       await message.author.send(embed=embed)
       await message.delete()
   if message.content == '[penis':
       spenus = randint(-50,200)
       spenus = int(spenus)
       if spenus > 0:
         spenus = str(spenus)
         await message.channel.send('Your penis is '+spenus+' cm long')
       else:
         spenus = str(spenus)
         await message.channel.send('Ha noob, your penis actually goes inwards, measuring at '+spenus+'cm long')
   if ('nigga') in message.content:
      await message.delete()
   if ('Nigga') in message.content:
      await message.delete()
   if ('Nigger') in message.content:
      await message.delete()
   if ('nigger') in message.content:
      await message.delete()
   if message.content == '[f in the chat':
       fchat = randint(5,15)
       for i in range(fchat):
           await message.channel.send('f')
           time.sleep(0.2)
   if message.content == '[iq':
       iq = randint(-50,500)
       iq = int(iq)
       if iq > 100:
         iq = str(iq)
         await message.channel.send('You have a staggering IQ of '+iq)
       else:
         iq = str(iq)
         await message.channel.send('Lol, ur so dumb, your iq is only '+iq)
   if message.content == '[gender':
       gender = randint(1,7)
       if gender == 1:
           await message.channel.send('You are male')
       if gender == 2:
           await message.channel.send('You are female')
       if gender == 3:
           await message.channel.send('You are James Charles')      
       if gender == 4:
           await message.channel.send('You are non-binary')
       if gender == 5:
          await message.channel.send('You are an attack helicopter')  
       if gender == 6:
          await message.channel.send('You are T-Series')
       if gender == 7:
          await message.channel.send('You are genderless')
   if message.content == '[roll':
       gender = randint(1,6)
       if gender == 1:
           await message.channel.send('Thats a 1')
       if gender == 2:
           await message.channel.send('Thats a 2')
       if gender == 3:
           await message.channel.send('Thats a 3')      
       if gender == 4:
           await message.channel.send('Thats a 4')
       if gender == 5:
          await message.channel.send('Thats a 5')  
       if gender == 6:
          await message.channel.send('Thats a 6')
   if message.content == '[8ball':
       ball = randint(1,12)
       if ball == 1:
         await message.channel.send('It is certain')
       if ball == 2:
         await message.channel.send('It is decidely so')
       if ball == 3:
         await message.channel.send('Without a doubt')
       if ball == 4:
         await message.channel.send('My sources say no')
       if ball == 5:
         await message.channel.send('You may rely on it')
       if ball == 6:
         await message.channel.send('As I see it, yes, Most Likely')
       if ball == 7:
         await message.channel.send('Outlook not good')
       if ball == 8:
         await message.channel.send('My reply is no')
       if ball == 9:
         await message.channel.send('Very doubtful')
       if ball == 10:
         await message.channel.send('Reply hazy, try again')
       if ball == 11:
         await message.channel.send('Ask again later')
       if ball == 12:
         await message.channel.send('Cannot predict now')
   if message.content == '[free nitro':
       embed = discord.Embed(title = '**NiTRo gENeRaTEd**', description = ''' www.bitly.com/iJeneral_TV''', color = 0x00ff00)
       await message.author.send(embed=embed) 
   if message.content == '[howgay':
       gay = randint(1,100)
       gay = str(gay)
       embed = discord.Embed(title = '', description = 'You are '+gay+'% gay :gay_pride_flag:', color = 0xff0000)
       await message.channel.send(embed=embed)
   if message.content == '[roll':
       number = randint(1,10)       
       number = str(number)       
       await message.channel.send('You rolled a '+number)


TOKEN = 'NTY3NDE4MDc2OTU4ODE4MzE0.XQkCeQ.BG7iZA3_s9Zur4EAiIIK-flc31g'
client.run(TOKEN)
