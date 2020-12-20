# Importing modules
import discord
import asyncio
import time
import random
from datetime import datetime
from selenium import webdriver

# id = 776890242359623740
messages = joined = 0
lc = ["Roma", "Napoli", "Venezia", "Milano", "Aosta", "Genova", "Torino", "Bologna", "Trieste", "Trento",
      "Firenze", "Perugia", "l'Aquila", "Potenza", "Catanzaro", "Ancona", "Campobasso", "Bari", "Cagliari",
      "Palermo"]


# Reading the bot's token in another file
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()


async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("src/stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined} \n")

                messages = 0
                joined = 0

                await asyncio.sleep(60)
        except Exception as e:
            print(e)
            await asyncio.sleep(60)


# Waving who enters in the server
@client.event
async def on_members_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "benvenuto":
            await client.send_message(f"""Benvenuto nel server {member.mention}!""")


# Writing how many users are there in the server with command "!users"
@client.event
async def on_message(message):
    global messages
    messages += 1

    id = client.get_guild(776890242359623740)

    if message.content == "!help":
        embed = discord.Embed(title="Comandi di 1tsBotto")
        embed.add_field(name="!città", value="Tutte le città di cui puoi riceverne il meteo")
        embed.add_field(name="!dado", value="Simulare l'estrazione di un numero dal dado (da 1 a 6)")
        embed.add_field(name="!github, !gh", value="Scopri i nostri profili GitHub!")
        embed.add_field(name="!help", value="Tutti i comandi")
        embed.add_field(name="!hpsoundtrack", value="Riproduci su Google Chrome la colonna sonora di Harry Potter")
        embed.add_field(name="!random 10, 100, 1000", value="Generare un numero casuale")
        embed.add_field(name="!search:twitch", value="Apre la schermata home di Twitch su Google Chrrome")
        embed.add_field(name="!search:youtube, !search:yt", value="Aprono la schermata home di YouTube su Google Chrome")
        embed.add_field(name="!time", value="L'orario attuale")
        embed.add_field(name="!users", value="Numero totale di utenti nel server")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!github":
        embed = discord.Embed(title="Profili di GitHub")
        embed.add_field(name="1tsN1c0", value="https://github.com/1tsN1c0")
        embed.add_field(name="Udrk", value="https://github.com/Udrk")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!gh":
        embed = discord.Embed(title="Profili di GitHub")
        embed.add_field(name="1tsN1c0", value="https://github.com/1tsN1c0")
        embed.add_field(name="Udrk", value="https://github.com/Udrk")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!tw":
        url = 'https://twitter.com/N1c01ts'
        browser = webdriver.Chrome()
        browser.get(url)
        embed = discord.Embed(title="Profili di Twitter")
        embed.add_field(name="1tsN1c0", value="https://twitter.com/N1c01ts")
        embed.add_field(name="Notifica", value="Aperto su una scheda di Google Chrome il mio profilo Twitter!")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!twitter":
        url = 'https://twitter.com/N1c01ts'
        browser = webdriver.Chrome()
        browser.get(url)
        embed = discord.Embed(title="Profili di Twitter")
        embed.add_field(name="1tsN1c0", value="https://twitter.com/N1c01ts")
        embed.add_field(name="Notifica", value="Aperto su una scheda di Google Chrome il mio profilo Twitter!")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!search:youtube":
        url = 'https://youtube.com'
        browser = webdriver.Chrome()
        browser.get(url)
        embed = discord.Embed()
        embed.add_field(name="Notifica", value="Aperto YouTube in una scheda di Chrome")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!search:yt":
        url = 'https://youtube.com'
        browser = webdriver.Chrome()
        browser.get(url)
        embed = discord.Embed()
        embed.add_field(name="Notifica", value="Aperto YouTube in una scheda di Chrome")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!search:twitch":
        url = 'https://twitch.tv'
        browser = webdriver.Chrome()
        browser.get(url)
        embed = discord.Embed()
        embed.add_field(name="Notifica", value="Aperto Twitch in una scheda di Chrome")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!social":
        embed = discord.Embed(title="Dove trovarmi sui social:")
        embed.add_field(name="Discord", value="1tsN1c0#0385")
        embed.add_field(name="GitHub", value="https://github.com/1tsN1c0")
        embed.add_field(name="Telegram", value="https://t.me/1tsN1c0")
        embed.add_field(name="Twitter", value="https://twitter.com/N1c01ts")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!hpsoundtrack":
        url = "https://www.youtube.com/results?search_query=harry+potter+complete+soundtrack"
        browser = webdriver.Chrome()
        browser.get(url)
        browser.find_element_by_xpath('//*[@id="img"]').click()
        embed = discord.Embed()
        embed.add_field(name="Notifica:", value="Riproducendo la Soundtrack di Harry Potter completa su YouTube!")
        await message.channel.send(content=None, embed=embed)

    elif message.content in lc:
        url = "https://www.meteo.it/"
        browser = webdriver.Chrome()
        browser.get(url)
        input_element = browser.find_element_by_id("search-input")
        input_element.send_keys(message.content)
        embed = discord.Embed()
        embed.add_field(name="Notifica", value="""Aperto su Google Chrome la scheda meteo! Basta che schiacci invio!""")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!città":
        embed = discord.Embed()
        embed.add_field(name="Città", value="""Roma, Napoli, Venezia, Milano, Aosta, Genova, Torino, Bologna, Trieste, 
        Trento, Firenze, Perugia, l'Aquila, Potenza, Catanzaro, Ancona, Campobasso, Bari, Cagliari, Palermo""")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!users":
        embed = discord.Embed()
        embed.add_field(name="Numero di membri", value=f"""AL momento, nel server ci sono {id.member_count} persone""")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!time":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        embed = discord.Embed()
        embed.add_field(name="Orario", value=f"""L'ora èttuale è {current_time}""")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!random 10":
        embed = discord.Embed(title="Generatore random di numeri")
        embed.add_field(name="Result:", value=f"""{random.randint(1, 10)}""")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!random 100":
        embed = discord.Embed(title="Generatore random di numeri")
        embed.add_field(name="Result:", value=f"""{random.randint(1, 100)}""")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!random 1000":
        embed = discord.Embed(title="Generatore random di numeri")
        embed.add_field(name="Result:", value=f"""{random.randint(1, 1000)}""")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!dado":
        embed = discord.Embed(title="Estrazione del dado")
        embed.add_field(name="Result", value=f"""{random.randint(1, 6)}""")
        await message.channel.send(content=None, embed=embed)

    elif message.content == "!wikipedia":
        url = 'https://it.wikipedia.org/wiki/Pagina_principale'
        browser = webdriver.Chrome()
        browser.get(url)
        browser.find_element_by_xpath('//*[@id="n-randompage"]/a').click()
        embed = discord.Embed()
        embed.add_field(name="Notifica", value="Un articolo a caso di Wikipedia aperto su Google Chrome!")
        await message.channel.send(content=None, embed=embed)

    else:
        print(f"""{message.author} ha provato ad eseguire il comando {message.content} nel canale {message.channel}""")


# Running the bot
client.loop.create_task(update_stats())
client.run(token)
