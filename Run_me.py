from Discord_Automation.Discord_Browser_Automation_Class import discord_bot
from time import sleep

url_for_channel="Enter some url"
username="enter your username"
password="enter your password"

self=discord_bot(username,password)
self.login()
self.get_to_channel(url_for_channel)

# self.write_to_chat("pls balance")
# sleep(2)
#
# a=self.read_chat()
# print(a[a.find("Wallet"):a.find("Wallet")+17])
self.search_cooldown=240

#Below are the settings for the loop
self.grind_money_loop(loopnum=18000,
                      memes_on_off=True,  #Do you want to post memes or not
                      search_on_off=True,  #Do you want to search or not
                      priority_search="death",
                      give_user="@Emre", #If you want to give all your money to somebody, this user is the person you
                      # give it to
                      give_on_off=True,  #Do you want to give your money periodically to someone or not
                      rob_on_off=False,  #Do you want to answer trivia questions in the loop or not?
                      hunt_on_off=True,  #Do you want to hunt in the loop or not?
                      user_to_rob="some user")

self.write_to_chat("pls balance")
sleep(2)

# a=self.read_chat()
# print(a[a.find("Wallet"):a.find("Wallet")+17])
