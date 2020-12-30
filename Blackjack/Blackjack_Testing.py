from Discord_Automation.Discord_Browser_Automation_Class import discord_bot
username="some username"
password="some password"
self=discord_bot(username,password)
self.login()
self.get_to_channel()
self.blackjack_loop(500,10000)