
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from time import *
from random import *



class discord_bot:
    def __init__(self , usrnm="",psw="",login=True):
        if login==True:

            self.browser = webdriver.Chrome(r"chromedriver.exe")
            self.thingtodo = ActionChains(self.browser)
            self.usrnm=usrnm
            self.psw=psw


            #These are the cooldowns for each action that you can do in dank memer:
            self.search_cooldown=30
            self.beg_cooldown=45
            self.trivia_cooldown=45
            self.meme_cooldown=60
            self.hunt_cooldown=60
            self.blackjack_cooldown=10
            self.rob_cooldown=120

    def wait_for_page(self,intensity=1):
        servers = self.browser.find_elements_by_class_name("listItem-2P_4kh")

        while len(servers) < 5:
            sleep(intensity)
            servers = self.browser.find_elements_by_class_name("listItem-2P_4kh")

        sleep(intensity+1)


    def login(self):
        self.browser.get("https://discord.com/login")

        #Waiting to load
        email = self.browser.find_elements_by_name("email")
        while len(email)<1:
            email = self.browser.find_elements_by_name("email")
        sleep(uniform(0.9,1.5))

        #Send username
        email[0].click()
        email[0].send_keys(self.usrnm)

        sleep(0.5)
        password = self.browser.find_elements_by_name("password")
        while len(password) < 1:
            password = self.browser.find_elements_by_name("password")

        sleep(0.5)
        password[0].click()
        sleep(2)
        password[0].send_keys(self.psw)
        sleep(0.5)
        password[0].send_keys(Keys.ENTER)

        self.wait_for_page(1)
        sleep(1)



    def get_to_channel(self,url=""):
        self.browser.get(url)
        self.wait_for_page(1)
        sleep(1)

    def read_chat(self, how_many_lines=1):
        """Reads 'how_many_lines' from the chat. The counting starts from the bottonm.
        Returns either an array of messages, or only one message. By default, this function returns the last message
        in the chat as a string. """
        messages = self.browser.find_elements_by_class_name("message-2qnXI6")

        while len(messages) < how_many_lines + 3:
            messages = self.browser.find_elements_by_class_name("message-2qnXI6")


        if how_many_lines==0:
            asd=[]
            for i in messages:
                asd.append(i.text)
            return asd

        else:
            message = messages[-how_many_lines].text

            return message

    def write_to_chat(self,text):
        """Writes a given text to the chat."""
        textbox = self.browser.find_element_by_class_name("slateTextArea-1Mkdgw")
        sleep(0.5)
        textbox.click()

        sleep(0.5)
        textbox.send_keys(text)
        sleep(0.5)
        textbox.send_keys(Keys.ENTER)
        sleep(0.5)
        #Checking to see if it's sent
        do=True
        while do:
            try:

                if self.read_chat()!=text:
                    do=False

            except:
                pass



    def beg(self):
        """Activates the beg command in dank memer"""
        self.write_to_chat("pls beg")

        r="pls beg"
        while "pls beg" in r:
            r=self.read_chat()


        sleep(1)



    def search(self,priority="net gain"):
        """Activates the search command in dank memer. Then, depending on what the judgement_formula returns,
        picks somewhere to search. It is very important here that the character does not die when searching
        somewhere. In a case where that happens, virtually everything done up until that point is lost."""
        from Discord_Automation.Search import judgement_formula

        self.write_to_chat("pls search")
        sleep(1)
        response="pls search"
        while "pls search" in response:
            response = self.read_chat()


        sleep(2)

        response = response.split("\n")[-1].split(", ")
        response = judgement_formula(response[0],response[1],response[2],priority)
        print(response)
        #
        # while "area51" in response:
        #     response=choice(response)

        sleep(1)

        self.write_to_chat(response)
        sleep(0.5)

    def post_meme(self):
        """Activates the post meme command in dank memer"""
        self.write_to_chat("pls postmeme")
        r="pls postmeme"
        while "pls postmeme" in r:
            r=self.read_chat()


        sleep(1)
        self.write_to_chat(choice(["n","e","r","d"]))

    def hunt(self):
        """Activates the hunt command in dank memer"""
        self.write_to_chat("pls hunt")
        r="pls hunt"
        while "pls hunt" in r:
            r=self.read_chat()
        sleep(1)

    def trivia(self):
        """Activates the trivia command in dank memer. Recently, the rules were changed. No currency is currently
        given if you give the correct answer for trivia. Due to this, it is generally not advised to use this
        command (it's mostly a waste of time when trying to automate mining dank memer currency). """
        self.write_to_chat("pls trivia")
        r="pls trivia"
        while "pls trivia" in r:
            r=self.read_chat()
        sleep(1)
        self.write_to_chat(choice(["a","b","c","d"]))

    def rob(self, user):
        """Activates the rob command in dank memer. Robs a given user_to_rob. This is especially good if you are in a
        and one of the people there has lots of money. If the user_to_rob has robbing on, that means they are OK with people
        attempting to rob them. If they are not OK, they will have disabled this feature on their account. """
        self.write_to_chat("pls withdraw 500")
        r = "pls withdraw 500"

        while "pls withdraw 500" in r:
            r = self.read_chat()

        sleep(0.8)
        self.write_to_chat("pls rob " + user)
        sleep(1)

        self.write_to_chat("pls deposit all")
        sleep(1)

    def stable_beg(self):
        """This is a stable version of the beg function. If there's a problem with the internet, the program does not
        crash."""
        try:
            self.beg()

        except:
            pass
        beg_time_initial = perf_counter()
        return beg_time_initial

    def stable_search(self,priority="net gain"):
        """This is a stable version of the search function. If there's a problem with the internet, the program does
        not crash."""
        try:
            self.search(priority=priority)
        except:
            pass
        search_time_initial = perf_counter()

        return(search_time_initial)
    def stable_postmeme(self):
        """This is a stable version of the postmeme function. If there's a problem with the internet, the program does
        not crash."""
        try:
            self.post_meme()
        except:
            pass
        return perf_counter()

    def stable_hunt(self):
        """This is a stable version of the hunt function. If there's a problem with the internet, the program does
        not crash."""
        try:
            self.hunt()
        except:
            pass

        sleep(1)
        return(perf_counter())

    def stable_trivia(self):
        """This is a stable version of the trivia function. If there's a problem with the internet, the program does
        not crash."""
        try:
            self.trivia()
        except:
            pass

        sleep(1)
        return(perf_counter()) #Returns the time trivia was done

    def stable_rob(self,user):
        """This is a stable version of the rob function. If there's a problem with the internet, the program does
        not crash."""
        try:
            self.rob(user=user)
        except:
            pass
        sleep(1)
        return perf_counter()

    def check_for_event(self):
        """This function reads the chat to see if there is a surprise dank memer event. If there is,
        the bot responds."""
        a=self.read_chat(0)
        event=False
        finmes=""
        next=False
        for m in a:
            if next==True:
                finmes=m
                break

            elif "event" in m:
                event=True
                next=True


        if event==True:
            finmes+=" "
            t1=finmes[finmes.find("Type")+5:-1]

            self.write_to_chat(t1)

            t2=finmes[finmes.find("type")+5:-1]
            self.write_to_chat(t2)

            for i in range(5):
                self.write_to_chat(t2)
                sleep(0.8)
                self.write_to_chat(t1)
                sleep(0.8)

            return True

        else:
            return False

    def grind_money_loop(self, loopnum, search_on_off, memes_on_off, trivia_on_off=False, give_on_off=False, give_user="",
                         priority_search="net gain", hunt_on_off=False, rob_on_off=False, user_to_rob=""):

        """This is the loop where everything comes together. If you wish to use this, just activate the loop,
        configure the setings, sit back, and enjoy all the currency coming your way. On average, with the right
        settings and dank memer being generous, this loop can grind around 100k coins per hour. """
        beg_time=self.stable_beg()
        if search_on_off:
            search_time=self.stable_search(priority_search)
        if memes_on_off:
            meme_time=self.stable_postmeme()

        hunt_time=self.stable_hunt()
        if trivia_on_off==True:
            trivia_time=self.stable_trivia()
        deposit_time=perf_counter()
        if rob_on_off:
            rob_time=self.stable_rob(user=user_to_rob)


        total=0
        start=perf_counter()
        while perf_counter()-start<loopnum:

            if perf_counter()-beg_time>self.beg_cooldown+2:
                print("begging")

                beg_time = self.stable_beg()
                total+=1

            if search_on_off==True:
                if perf_counter()-search_time>self.search_cooldown:
                    print("searching")

                    search_time = self.stable_search(priority_search)
                    total+=1

            if rob_on_off==True:
                if perf_counter()-rob_time>self.rob_cooldown:
                    print("robbing")

                    rob_time=self.stable_rob(user=user_to_rob)

            if memes_on_off==True:
                if perf_counter()-meme_time>self.meme_cooldown:
                    print("posting meme")

                    meme_time = self.stable_postmeme()
                    total+=1
            if hunt_on_off==True:
                if perf_counter()-hunt_time>self.hunt_cooldown:
                    print("hunting")

                    hunt_time = self.stable_hunt()
                    total+=1

            if trivia_on_off==True:
                if perf_counter()-trivia_time>self.trivia_cooldown:
                    print("triviaing")

                    trivia_time=self.stable_trivia()
                    total+=1
                    sleep(1.3)

            elif perf_counter()-deposit_time>100:
                print("depositing")
                self.write_to_chat("pls deposit all")
                sleep(1)
                deposit_time=perf_counter()

                if give_on_off==True:
                    print("giving")
                    self.write_to_chat("pls give "+ give_user+ " all")
                    sleep(1)

    @staticmethod
    def filter_blackjack(string):
        """Parses the blackjack text dank memer sends. Returns the parsed version."""
        update = []
        for l in string:
            try:
                l = int(l)
                update.append(l)
            except:
                if l in ["K","Q","J"]:
                    update.append(10)
                elif l in ["A"]:
                    update.append(1)

        update2 = []
        for i in range(len(update)):
            if update[i] == 0 and update[i - 1] == 1:
                update2.pop()
                update2.append(10)
            else:
                update2.append(update[i])
        return update2

    def responde_blackjack(self,wager):
        """Responds to dank memer after activating the blackjack command."""
        from Blackjack import Blackjack_Minimax as bg
        response=self.read_chat()
        response = response.split("\n")
        go_on=True
        while go_on==True:
            response = self.read_chat()
            response = response.split("\n")
            go_on=False
            for x in response:
                if "pls blackjack" + str(wager) in x or "Slow it down, cmon" in x:
                    go_on=True
        cards = []
        for x in response:
            if "Cards" in x:
                cards.append(x+" ")
        print("response :\n" + str(response))
        print("cards:")
        print(cards)
        my_cards=self.filter_blackjack(cards[0])
        dank_card=self.filter_blackjack(cards[1])
        print(my_cards,dank_card)
        move=bg.get_move(my_cards,dank_card)

        self.write_to_chat(move)


        #wait for response:
        init=True
        while init:
            response = self.read_chat()
            if "blackjack game"  in response:
                init = False

        if "You win" in response:
            return 1

        elif "You lose!" in response:
            return 0

        else:
            return 2


    def blackjack(self,wager,shouldiwithdraw):
        """Plays blackjack with dank memer. All decisions made are with 100% accuracy since a minimax algorithm I
        wrote is imported."""
        if shouldiwithdraw==True:
            r="pls withdraw " + str(wager)
            self.write_to_chat(r)
            response=self.read_chat()
            while r in response:
                response=self.read_chat()

        self.write_to_chat("pls blackjack " + str(wager))

        goingon=2
        while goingon==2:
            goingon=self.responde_blackjack(wager=wager)
            # 1 means we have won the game, 0 means we lost, 2 means the game is still going

        return goingon

    def blackjack_loop(self,starting_wager,how_much_to_win,withdraw=True,):
        """Initiates a blackjack loop."""

        from time import perf_counter
        money_won=0
        n=1
        lastr=False

        startedblack=perf_counter()
        while money_won<how_much_to_win:
            if lastr==True:
                n=1

            if perf_counter()-startedblack>=self.blackjack_cooldown:
                didiwin=self.blackjack(starting_wager*n,withdraw)
                if didiwin==1:
                    lastr=True
                    money_won+=starting_wager*n
                else:
                    lastr=False
                    money_won-=starting_wager*n

                startedblack=perf_counter()
                n+=1

                print("Our money won is: " + str(money_won))