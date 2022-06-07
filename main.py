import random
import discord
import re
import sqlite3

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")

    async def on_message(self, message):
        # datetime object for dob
        # have the bot run on correct timezone
        args = message.content.split()
        if args[0] == "$birthday":
            if args[1] == "add":
                if len(args) < 4:
                    # throw error here
                    await message.reply("Not enough arguments!")
                dob = args[2].date()
                print(f"DOB: {dob}")
                name = " ".join(args[3:])
                print(f"name: {name}")
            elif args[1] == "delete":
                # DELETE
            else:
                # HELP OPTION FOR USERS


        cursor = self.db.cursor()
        cursor.execute('''
        INSERT INTO people (people_id, name, dob)
            VALUES (?,?,?)
        ''', [id], name, dob)




client = MyClient()
with open('secretbdaybot.txt') as f:
    content = f.read()
client.run(content)

