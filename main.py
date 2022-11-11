import discord
import os
from collections import Counter
import sys
import random
import time

file = discord.File("PP/Shy_Guy_Sry.png", filename="image.png")

prefix = '!'
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

imageOrText = ['image', 'text']

path = "cat"
files = os.listdir(path)

LaraPath = "lara"
LaraFiles = os.listdir(LaraPath)


class Bcolors:
    ENDC = '\033[0m'
    OKGREEN = '\033[92m'
    OKCYAN = '\033[96m'
    PINK = '\033[95m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'

    def disable(self):
        self.OKGREEN = ''


# Ready-up
@client.event
async def on_ready():
    activity = discord.Game(name="sorry..", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('------')
    print(f"{Bcolors.OKCYAN}Activity: {Bcolors.PINK}{activity}")
    print(f"{Bcolors.OKCYAN}Bot Name: {Bcolors.PINK}{client.user.name}")
    print(f"{Bcolors.OKGREEN}Bot Ready!{Bcolors.ENDC}")
    print('------')



@client.event
async def on_message(message):
    if message.content == prefix + 'sorry' or message.content == prefix + 'Sorry':
        filename = open('counter.txt', 'r')
        with open('counter.txt', 'a') as w:
            w.write('sorry ')
        textFile = filename.read()
        wordCount = (textFile.split())
        new_string = f'{len(wordCount)}'
        print("Sorry Counter:", len(wordCount))
        embedVar = discord.Embed(title=new_string, description="Er hat sich schon wieder entschuldigt...",
                                 color=0x9b59b6)
        embedVar.set_author(name="SHYLY - SORRY COUNTER",
                            icon_url="https://cdn.discordapp.com/avatars/368418491566522371/1bd2b869d9d0a2c56253650648752c29.webp?size=80")
        file = discord.File("PP/Shy_Guy_Sry.png", filename="image.png")
        embedVar.set_thumbnail(url="attachment://image.png")
        await message.channel.send(file=file, embed=embedVar)
        freq = Counter(wordCount)
        filename.close()
        print('------')


    # Test Command
    elif message.content == prefix + 'test' or message.content == prefix + 'Test':
        print('test')
        await message.channel.send('Test')
        print('------')

    # Hallo
    elif message.content == 'Hallo' or message.content == 'hallo':
        print('test')
        await message.channel.send('Hallo!')
        print('------')

    # Hallo
    elif message.content == 'ok' or message.content == 'Ok':
        print('test')
        await message.channel.send('ok..')
        print('------')

    # hs command
    elif ' hs' in message.content:
        print('hs')
        await message.channel.send('Lügen darf man nicht sagen!')
        print('------')

    # hs command
    elif message.content == 'hs':
        await message.channel.send('SELBER!')

    # hs command
    elif message.content == 'huso':
        await message.channel.send('DU!')

    # hs command
    elif ' huso' in message.content:
        await message.channel.send('DU!')

    # hug mention command
    elif message.content.startswith(prefix + 'hug '):
        text = message.content.split(' ')[1:]
        emptystr = ""
        for i in text:
            emptystr += i + ''
            await message.channel.send(emptystr + ' Fühl dich gedrückt von {}'.format(message.author.name) + '!')

    # hug mention command
    elif message.content == prefix + 'hug':
        await message.channel.send('Fühl dich von mir gedrückt! {}'.format(message.author.mention))

    # huso mention command
    elif message.content.startswith(prefix + 'huso '):
        text = message.content.split(' ')[1:]
        emptystr = ""
        for i in text:
            emptystr += i + ''
            await message.channel.send(emptystr + ' ich soll dir HUS0 von {}'.format(message.author.name) + ' sagen!!!')

    # huso mention command
    elif message.content.startswith(prefix + 'hs '):
        text = message.content.split(' ')[1:]
        emptystr = ""
        for i in text:
            emptystr += i + ''
            await message.channel.send(emptystr + ' ich soll dir HUS0 von {}'.format(message.author.name) + ' sagen!!!')

    # break bot
    elif message.content == prefix + 'break':
        await message.channel.send('ok, bye!')
        sys.exit("break")

    # random cat
    elif message.content == prefix + 'cat':
        d = random.choice(files)
        CatPic = discord.File(f"cat/{d}", filename="image.png")
        embedCat = discord.Embed(color=0x7289da)
        embedCat.set_author(name="CAT",
                            icon_url="https://i.pinimg.com/564x/b0/33/6d/b0336de8b6ca431d44e0ad5ed76b1dd8.jpg")
        embedCat.set_image(url="attachment://image.png")
        await message.channel.send(file=CatPic, embed=embedCat)
        print('Random Cat: ' + f"cat/{d}")
        print('------')

    # random lara pic
    elif message.content == prefix + 'lara':
        d = random.choice(LaraFiles)
        LaraPic = discord.File(f"lara/{d}", filename="image.png")
        embedLara = discord.Embed(color=0xe91e63)
        embedLara.set_author(name="LARA - HOT IMAGE",
                             icon_url="https://i.pinimg.com/564x/1b/ad/52/1bad5289a0df3e8375ce0ff098047b2a.jpg")
        embedLara.set_image(url="attachment://image.png")
        print('Random Lara pic: ' + f"lara/{d}")
        print('------')
        await message.channel.send(file=LaraPic, embed=embedLara)

    # ! league command
    elif message.content == prefix + 'league':
        leftImgHints = 2
        leftTextHints = 2
        ImgAsStringL = str(leftImgHints)
        TextAsStringL = str(leftTextHints)

        LeaguePath = "league"
        Leaguefiles = os.listdir(LeaguePath)
        d = random.choice(Leaguefiles)
        Lfile = discord.File(f"league/{d}", filename="image.png")
        embedLeague = discord.Embed(title="Erkenne den League Character!",
                                    description='Achtung, alles klein schreiben! \n  \n ```Hints: \n!hint image - Left: ' +
                                                ImgAsStringL + '\n!hint text - Left: ' + TextAsStringL + '```',
                                    color=0x206694)
        embedLeague.set_author(name="LEAGUE - WHO'S THAT?", icon_url="https://i.imgur.com/vgERB5I.png")
        embedLeague.set_image(url="attachment://image.png")
        CharPath = f"league/{d}".replace('.jpg', '')
        leagueCharProg = CharPath.replace('league/', '')
        if 'second' in leagueCharProg:
            leagueChar = leagueCharProg.replace(' second', '')
        #  print("Second picture")
        elif 'third' in leagueCharProg:
            leagueChar = leagueCharProg.replace(' third', '')
        # print("third picture")
        else:
            leagueChar = leagueCharProg
        #  print("first picture")

        usedHelp = leagueCharProg
        print(usedHelp)

        NoneList = leagueChar + ""
        SecondList = leagueChar + " second"
        ThirdList = leagueChar + " third"
        second = " second"
        third = " third"
        UsedCounter = 0
        helpTitle = 'YOU NEED HELP?'
        helpColor = 0xf1c40f
        helpDesc = 'Hier ein anderes Bild:'
        Text = 0

        await message.channel.send(file=Lfile, embed=embedLeague)
        print("LEAGUE QUIZ")
        print("LOOP STARTED")
        print("Correct answer:", leagueChar)
        print("___")

        def check(m):
            return m.content and m.channel == message.channel and m.author != 'Sorry ShyGuy#5937'

        while message.content == '!league':
            print("Waiting for answer...")
            print("____")
            msg = await client.wait_for('message', check=check)
            print("LEAGUE QUIZ")
            print("Answer was entered")
            print("Checking answer..")

            if msg.content == leagueChar:
                print(f"{Bcolors.OKGREEN}Answer: Right{Bcolors.ENDC}")
                embedLeague = discord.Embed(title="RICHTIG!", description="Die Antwort: " + leagueChar, color=0x2ecc71)
                fullCharPath = "full/" + leagueChar + '.jpg'
                print(fullCharPath)
                fullChar = discord.File(fullCharPath, filename="image.png")
                embedLeague.set_author(name="LEAGUE - WHO'S THAT?", icon_url="https://i.imgur.com/vgERB5I.png")

                embedLeague.set_image(url="attachment://image.png")
                await message.channel.send(file=fullChar, embed=embedLeague)

                print(f"{Bcolors.OKBLUE}Loop ended{Bcolors.ENDC}")
                print("____")
                break

            elif msg.content == prefix + 'hint image':

                print(f"{Bcolors.OKGREEN}HINT{Bcolors.ENDC}")

                if UsedCounter == 2:
                    print('Verbraucht')
                    helpDesc = 'Für diesen Character gibt es leider keine weiteren Hints... \n'
                    helpTitle = 'KEINE HINTS MEHR!'
                    helpChar = leagueCharProg
                    UsedCounter = UsedCounter + 1

                elif UsedCounter == 3:
                    print('Verbraucht')
                    helpDesc = 'WIE GESAGT: KEINE HINTS MEHR!!!...'
                    helpTitle = 'KEINE HINTS MEHR!'
                    helpChar = leagueCharProg

                elif 'second' in usedHelp:
                    print('elif')
                    helpChar = usedHelp.replace(usedHelp, ThirdList)
                    print('usedHelp Variable - Used before: ' + usedHelp)
                    usedHelp = leagueChar + third
                    print('usedHelp Variable - Using now: ' + usedHelp)
                    print(helpChar)
                    leftImgHints = leftImgHints - 1
                    ImgAsString = str(leftImgHints)
                    TextAsString = str(leftTextHints)
                    helpDesc = '```Hints: \n!hint image - Left: ' + ImgAsString + '\n!hint text - Left: ' + TextAsString + '```' + '\n Hier ein anderes Bild:'
                    UsedCounter = UsedCounter + 1

                elif 'third' in usedHelp:
                    print('elif')

                    helpChar = usedHelp.replace(usedHelp, NoneList)
                    print('usedHelp Variable - Used before: ' + usedHelp)
                    usedHelp = leagueChar
                    print('usedHelp Variable - Using now: ' + usedHelp)
                    print(helpChar)
                    UsedCounter = UsedCounter + 1
                    leftImgHints = leftImgHints - 1
                    ImgAsString = str(leftImgHints)
                    TextAsString = str(leftTextHints)

                    helpDesc = '```Hints: \n!hint image - Left: ' + ImgAsString + '\n!hint text - Left: ' + TextAsString + '```' + '\n Hier ein anderes Bild:'

                else:
                    print('else')

                    helpChar = usedHelp.replace(usedHelp, SecondList)
                    print('HelpChar Variable - new: ' + usedHelp)
                    print('usedHelp Variable - Used before: ' + usedHelp)
                    usedHelp = leagueChar + second
                    print('usedHelp Variable - Using now: ' + usedHelp)
                    print(helpChar)
                    UsedCounter = UsedCounter + 1
                    leftImgHints = leftImgHints - 1
                    ImgAsString = str(leftImgHints)
                    TextAsString = str(leftTextHints)
                    helpDesc = '```Hints: \n!hint image - Left: ' + ImgAsString + '\n!hint text - Left: ' + TextAsString + '```' + '\n Hier ein anderes Bild:'

                embedLeague = discord.Embed(title=helpTitle, description=helpDesc, color=helpColor)
                FixPath = helpChar.replace('\u200b', '')
                helpCharPath = 'C:/Users/nilss/Desktop/DC-BOT/BOT-SorryCounter/' + 'league/' + FixPath + '.jpg'
                test = os.getcwd()
                print('HelpCharPath: ' + helpCharPath)
                print(test)
                time.sleep(0.1)
                fullChar = discord.File(helpCharPath, filename="image.png")
                embedLeague.set_author(name="LEAGUE - WHO'S THAT?", icon_url="https://i.imgur.com/vgERB5I.png")

                if UsedCounter < 3:
                    embedLeague.set_image(url="attachment://image.png")
                    await message.channel.send(file=fullChar, embed=embedLeague)

                else:
                    await message.channel.send(embed=embedLeague)

            elif msg.content == prefix + 'league':
                embedLeague = discord.Embed(title="Versuch abgebrochen",
                                            description="Neue challenge öffnet sich gleich...", color=0xe74c3c)
                embedLeague.set_author(name="LEAGUE - WHO'S THAT?", icon_url="https://i.imgur.com/vgERB5I.png")
                await message.channel.send(embed=embedLeague)
                time.sleep(1)
                break

            elif msg.content == prefix + 'hint ' + 'text':
                if Text == 0:
                    leftTextHints = leftTextHints - 1
                    ImgAsString = str(leftImgHints)
                    TextAsString = str(leftTextHints)
                    print('text hint')
                    helpDesc = '```Hints: \n!hint image - Left: ' + ImgAsString + '\n!hint text - Left: ' + TextAsString + '```' + '\n \n Der Character Name beginnt mit: '
                    helpTitle = 'TEXT HINT:'
                    Text = Text + 1
                    embedLeague2 = discord.Embed(title=helpTitle, description=helpDesc, color=helpColor)
                    embedLeague2.add_field(name=(leagueChar[0]), value='\u200b', inline=False)
                    embedLeague2.set_author(name="LEAGUE - WHO'S THAT?", icon_url="https://i.imgur.com/vgERB5I.png")
                    await message.channel.send(embed=embedLeague2)

                elif Text == 1:
                    leftTextHints = leftTextHints - 1
                    ImgAsString = str(leftImgHints)
                    TextAsString = str(leftTextHints)
                    print('text hint 2')
                    helpDesc = '```Hints: \n!hint image - Left: ' + ImgAsString + '\n!hint text - Left: ' + TextAsString + '```' + '\n \n Der Character Name beginnt mit:'
                    helpTitle = 'TEXT HINT:'
                    Text = Text + 1
                    embedLeague3 = discord.Embed(title=helpTitle, description=helpDesc, color=helpColor)
                    embedLeague3.add_field(name=(leagueChar[0]) + (leagueChar[1]), value='\u200b', inline=False)
                    embedLeague3.set_author(name="LEAGUE - WHO'S THAT?", icon_url="https://i.imgur.com/vgERB5I.png")
                    await message.channel.send(embed=embedLeague3)
                else:
                    print('text hint verbraucht')
                    helpDesc = 'Soviel kann ich dir jetzt auch nicht verraten... \n Versuch es mal mit !hint image wenn du trotzdem nicht weiterkommst!'
                    helpTitle = 'TEXT HINTS VERBRAUCHT!'
                    embedLeague = discord.Embed(title=helpTitle, description=helpDesc, color=helpColor)
                    embedLeague.set_author(name="LEAGUE - WHO'S THAT?", icon_url="https://i.imgur.com/vgERB5I.png")
                    await message.channel.send(embed=embedLeague)

            else:
                print(f"{Bcolors.WARNING}Answer: False{Bcolors.ENDC}")

                embedLeague = discord.Embed(title="FALSCH!", description="Versuch's nochmal!", color=0xe74c3c)
                embedLeague.set_author(name="LEAGUE - WHO'S THAT?", icon_url="https://i.imgur.com/vgERB5I.png")
                await message.channel.send(embed=embedLeague)
                print("____")

    elif message.content == prefix + 'lara quiz':

        LaraQPath = "laraQ"
        LeagueQfiles = os.listdir(LaraQPath)
        d = random.choice(LeagueQfiles)
        Lfile = discord.File(f"laraQ/{d}", filename="image.png")
        embedLeague = discord.Embed(title="Wer ist das?",
                                    description='Achtung, alles klein schreiben!',
                                    color=0x206694)
        embedLeague.set_author(name="LARA - WHO'S THAT?", icon_url="https://twibbon.blob.core.windows.net/twibbon/2020/33/bd7892d2-7be2-482b-9b32-f4f85faf0cd7.png")
        embedLeague.set_image(url="attachment://image.png")
        CharPath = f"laraQ/{d}".replace('.jpg', '')
        LaraCharProg = CharPath.replace('laraQ/', '')

        if 'second' in LaraCharProg:
            LaraChar = LaraCharProg.replace(' second', '')
            #  print("Second picture")
        elif 'third' in LaraCharProg:
            LaraChar = LaraCharProg.replace(' third', '')
            # print("third picture")
        else:
            LaraChar = LaraCharProg
            #  print("first picture")

        usedHelp = LaraCharProg
        print(usedHelp)

        NoneList = LaraChar + ""
        SecondList = LaraChar + " second"
        ThirdList = LaraChar + " third"
        second = " second"
        third = " third"
        UsedCounter = 0
        helpTitle = 'YOU NEED HELP?'
        helpColor = 0xf1c40f
        helpDesc = 'Hier ein anderes Bild:'
        Text = 0

        await message.channel.send(file=Lfile, embed=embedLeague)
        print("LEAGUE QUIZ")
        print("LOOP STARTED")
        print("Correct answer:", LaraChar)
        print("___")

        def check(m):
            return m.content and m.channel == message.channel and m.author != 'Sorry ShyGuy#5937'

        while message.content == '!lara quiz':
            print("Waiting for answer...")
            print("____")
            msg = await client.wait_for('message', check=check)
            print("LEAGUE QUIZ")
            print("Answer was entered")
            print("Checking answer..")

            if msg.content == LaraChar:
                print(f"{Bcolors.OKGREEN}Answer: Right{Bcolors.ENDC}")
                embedLeague = discord.Embed(title="RICHTIG!", description="Die Antwort: " + LaraChar, color=0x2ecc71)
                fullLaraPath = "fullLara/" + LaraChar + '.jpg'
                print(fullLaraPath)
                fullChar = discord.File(fullLaraPath, filename="image.png")
                embedLeague.set_author(name="LARA - WHO'S THAT?", icon_url="https://twibbon.blob.core.windows.net/twibbon/2020/33/bd7892d2-7be2-482b-9b32-f4f85faf0cd7.png")
                embedLeague.set_image(url="attachment://image.png")
                await message.channel.send(file=fullChar, embed=embedLeague)

                print(f"{Bcolors.OKBLUE}Loop ended{Bcolors.ENDC}")
                print("____")
                break

client.run(os.environ.get('DISCORD_TOKEN'))
