#CASINO TYPO
import random
import time as tm
def slprint(text):
    for i in text:
        print(i, end="",flush=True)                                             #created by Awadhraj chauhan
        tm.sleep(0.05)
    print()
slprint("WELCOME TO APNACASINO")
slprint("WE ARE HERE TO MAKE SURE YOU WIN BIG ")
slprint("To begin the game pls enter your details")
name=input("Enter your name:")
age=int(input("Enter your age:"))
if age<18:
    slprint("Sorry , you are underage and cannot enter the game")
    exit()
elif age>=100:
    print("Ohhh you still alive?")
else:
    slprint(f"WELCOME {name} LET'S WIN BIG TOGETHER")
slprint("Purchase casino currency to win the real one")
global cash
cash=0
tm.sleep(2)
def confirm():
    slprint(".")
    slprint(".")
    slprint(".")
    slprint(".")
    global he
    slprint("CONFIRM TO CONTINUE THE BET")
    he=input("CONTINUE TO THE GAME ? (yes/no):")
    if he=="yes" or he=="YES" or he=="Yes":
        pass
    else:
        slprint("CHOOSE YOUR GAME AGAIN")
        game()
                                                      #1ST GAME
def f1():
    while True:
        global cash
        slprint("WELCOME TO THE F1 FIELD")
        tm.sleep(2)
        slprint("THE RACE WILL BEGIN IN FEW MINUTES, BET ON YOUR LUCKY RACER TO WIN 10000 CASINO CASH")
        tm.sleep(2)
        slprint("BETTING WILL COST YOU 6000 casino cash and loosing bet will deduct 10000 casino cash")
        tm.sleep(2)
        print("CURRENT BALANCE",cash)
        tm.sleep(3)
        if cash<6000:
            tm.sleep(2)
            slprint("NOT ENOUGH BALANCE TO CONTINUE THE GAME")
            tm.sleep(2)
            slprint("Buy more casino cash to continue the game")
            money()                                                                             #created by Awadhraj chauhan
        
        else:
            cash=cash-6000
            slprint("TODAY's RACER'S :")
            def rac():
                slprint("1)George Russell - **MERCEDES**")
                slprint("2)kimi Antonelli - **MERCEDES**") 
                slprint("3)Max Verstappen - **RED BULL** ")
                slprint("4)Isack Hadjar - **RED BULL**")
                slprint("5)Lando Norris - **Mc Laren**")
                slprint("6)Oscar Piastri - **Mc Laren** ")
                slprint("7)Charles leclerc - **FERRARI** ")
                slprint("8)Lewis Hamilton - **FERRARI** ")
                global seloption
                seloption=int(input("ENTER THE SERIAL NUMBER OF YOUR SELECTED RACER:"))
                confirm()
            rac()
            racers=["George Russell", "Kimi Antonelli","Isack Hadjar","Lando Norris","Oscar Piastri","Charles leclerc","Lewis Hamilton","Max Verstappen"]
            if seloption<=8:
                pass
            else:
                slprint("INVALID OPTION SLECTED, TRY AGAIN")
                rac()
            sec=random.uniform(0.1,3.1)                                                    #print("f{sec:.4f}")
            tm.sleep(2)
            print("BETTING PORTALS HAVE NOW CLOSED.......SIT BACK AND ENJOY THE SHOW")
            tm.sleep(2)
            slprint("LET'S SEE YOU WIN OR LOOSE THE BET")
            tm.sleep(2)
            print(".")
            tm.sleep(1)
            print(".")
            tm.sleep(1)
            print(".")
            tm.sleep(1)
            slprint("AWADHRAJ => HELLO LADIES AND GENTELMEN I AM AWADHRAJ , TODAY'S COMMENTATOR OF THE GAME")
            tm.sleep(2)
            def venue():
                global ven
                ven=random.randint(1,4)
                if ven==1:
                    slprint("AWADHRAJ => Welcome to the Legendary streets of MONACO for the MONACO GRAND PRIX !!!!!")
                    tm.sleep(3)
                    slprint("AWADHRAJ => The jewel in Formula One's crown — the streets of Monaco! Inches separate glory from disaster as the drivers tackle the most famous street circuit in the world!")
                    tm.sleep(3)
                    slprint("AWADHRAJ => A man who needs no introduction - SIR LEWIS HAMILTON HAS ALREADY WON 3 RACES HERE")
                    tm.sleep(2)
                    slprint("AWADHRAJ => Other racers will try their best to beat lewis in this track")
                    tm.sleep(3)
                    slprint("Lewis! Lewis! Lewis! ..... Ham-il-ton! Ham-il-ton! Ham-il-ton!")
                elif ven==2:
                    slprint("AWADHRAJ => Welcome to the birthplace of Formula One, SILVERSTONE CIRCUIT ! The British Grand Prix is ready to roar into life as the world's finest drivers prepare for battle on one of motorsport's most historic tracks!")
                    tm.sleep(3)
                    slprint("AWADHRAJ => The legend and most successful racer - Lewis has already won 9 races here")
                    tm.sleep(2)
                    slprint("WILL IT BE EASY TO BEAT OUR 7 TIMES WORLD CHAMPION TODAY, DON'T THINK SO !!!!!!")
                elif ven==3:
                    slprint("AWADHRAJ => Welcome everyone to the Red bull ring, The mountains of Austria provide a stunning backdrop as Formula One returns to the Red Bull Ring! Short, fast, and unforgiving, every lap here is a flat-out sprint!")
                    tm.sleep(3)
                    slprint("AWADHRAJ => Well when the name itself is Red bull ring , you know who is the master of this track")
                    tm.sleep(3)
                    slprint("AWADHRAJ => TU TU TU TU , MAX VERSTAPPEN , TU TU TUU TU")
                    tm.sleep(3)
                    slprint("AWADHRAJ => Let us witness other drivers compete with the young beast")
                elif ven==4:
                    slprint("AWADHRAJ => Welcome to the HUNGARORING TRACK ")
                    tm.sleep(3)
                    slprint("AWADHRAJ => Nestled just outside Budapest, we arrive at the Hungaroring! A tight and twisting challenge awaits, where precision is everything and overtaking opportunities are few and far between")
                    tm.sleep(3)
                    slprint("AWADHRAJ => 8 drivers 78 laps , one winner . let us begin!!!!!!")
            venue()
            tm.sleep(3)
            slprint("AWADHRAJ => THE WEATHER IS CLOUDY TODAY , BUT OUR RACER'S ARE SHINING BRIGHTER THAN THE SUN ")
            tm.sleep(2)
            slprint("AWADHRAJ => GET READYYYY!!!! the game begins in:")
            tm.sleep(2)
            print("3")
            tm.sleep(1)
            print("2")
            tm.sleep(1)
            print("1")
            tm.sleep(1)
            print("LET'S GOOOOOOOOOOO!!!!")
            tm.sleep(3)
            slprint("LET's SEE WHO WINS TODAY")
            slprint("           **AFTER 5 mins**")
            tm.sleep(2)
            slprint("AWADHRAJ => AS ALWAYS MAX VERSTAPPEN TAKES THE LEAD OF 1.123 sec ")
            tm.sleep(1)
            slprint("AWADHRAJ => OH WAIT !! OH WAIT!! LEWIS HAMILTON OVERTAKES SOOO SMOOTH EVEN THE BUTTER QUESTIONS IT'S EXISTENCE")
            tm.sleep(2)
            slprint("AWADHRAJ => MAX and LEWIS are fighting their best to win")
            global situation
            situation=random.randint(1,3)
            if situation==1:
                slprint("AWADHRAJ => OH !! IT STARTED DRIZZLING, HOPE IT DOESN'T DISTURB THE GAME")
                tm.sleep(1)
                slprint("AWADHRAJ=> WELL THE GAME IS STILL CONTINUING , BUT THERE IS SIGN OF GAME GETTING CANCLED TODAY, LET US HOPE FOR THE BEST")
                SIT1=random.randint(1,3)
                if SIT1==1:
                    slprint("AWADHRAJ=> OH THE UNEXPECTED HAPPENS!!! IT STARTED RAINING HEAVILY AND THE TRACK ISN'T VISIBLE")
                    tm.sleep(2)
                    slprint("AWADHRAJ=> THE RACE DIRECTOR SIGNALS TO STOP THE GAME.......AS THERE IS NO SIGN OF CLEARANCE")
                    tm.sleep(2)
                    slprint("                          **IT RAINS FOR 2 HOURS STRAIGHT AND RACE GETS CANCLED**")
                    tm.sleep(4)
                    slprint("AWADHRAJ => WE ARE UNLUCKY TODAY!!! I DON'T WANT TO SAY THIS BUT")
                    slprint("AWADHRAJ => BYE FOR TODAY, SEE YOU NEXT TIME!!!!!!")
                    print(".")
                    tm.sleep(1)
                    print(".")
                    tm.sleep(1)
                    print(".")
                    tm.sleep(1)
                    print(".")
                    tm.sleep(1)
                    slprint("As the race is cancled , you loose the bet(unexpected but true)")
                    slprint("BETTER LUCK IN NEXT RACE!!!")
                    cash=cash-10000
                    slprint("YOU LOST 10000 casino cash as you have lost the bet")
                    print("CURRENT BALANCE IN TEMPORARY ACCOUNT: ",cash)
                    return
                elif SIT1==2:
                    slprint("AWADHRAJ=> Well such slight rains cannot cancle out the game, The game still continues with same energy and hunger to win the race")
                elif SIT1==3:
                    slprint("AWADHRAJ=> Well such slight rains cannot cancle out the game, The game still continues with same energy and hunger to win the race")
            elif situation==2:
                    slprint("AWADHRAJ=> The racers have turned  on their beast mode on")
                    tm.sleep(2)
                    slprint("AWADHRAJ=> Each and everyone is giving the equal competiton")
                    tm.sleep(2)
                    slprint("AWADHRAJ=> The race is pretty intresting")
                    tm.sleep(1)
                    slprint("AWADHRAJ=> Let's see who wins today as the competition is so high today")
            elif situation==3:
                    slprint("AWADHRAJ=> The racers have turned  on their beast mode on")
                    tm.sleep(2)
                    slprint("AWADHRAJ=> Each and everyone is giving the equal competiton")
                    tm.sleep(2)
                    slprint("AWADHRAJ=> OH WAIT !! OH WAIT!!! THE CARS ARE GETTING TO CLOSE TO EACAH OTHER")
                    tm.sleep(2)
                    print("                               **BOOOOOMMMMMM!!!!!!!!!!!**")
                    tm.sleep(2)
                    slprint("AWADHRAJ=> NOOOO!!!")
                    crasher1=random.choice(racers)
                    racers.remove(crasher1)
                    crasher2=random.choice(racers)
                    racers.remove(crasher2)
                    print("AWADHRAJ=>", crasher1,"and",crasher2,"have collided with each other")
                    tm.sleep(3)
                    slprint("AWADHRAJ=> .    .     .    .    .   ")
                    slprint("AWADHRAJ=> THE SAFETY CAR IS DEPLOYED")
                    slprint("AWADHRAJ=> The Track Marshals have come to distinguish the fire, with The Medical Car")
                    tm.sleep(2)
                    slprint("AWADHRAJ=> HUGE SMOKE ARISES, let us hope for the best")
                    tm.sleep(3)
                    slprint("AWADHRAJ=> The Track Marshals are helping the racers to get out of the car safely , thank god they are safe")
                    tm.sleep(2)
                    slprint("AWADHRAJ=> THIS WILL BE REMEMBERED AS A BLACK DAY IN F1 THE RACER MAY HAVE WON BUT AT THE END IT'S THE DESTINY, THE TRACK IS GETTING CLEANED.... RACE SHOULD CONTINUE SOON")
                    tm.sleep(4)
                    slprint("The race director signals to continue the game")      
            slprint("                                 **AFTER SEVERAL MINUTES**") 
            tm.sleep(2)
            seclead=random.uniform(0.1,1.2)
            leadracer=random.choice(racers)
            slprint("Only 5 laps remain")
            print(leadracer,"has the lead of",seclead,"seconds")
            slprint("Only few mins left to know the winner")
            print("                                   LAST LAP")
            slprint("THE LAST LAP REMAINS!!!!, eveyone filled woth confidence")
            tm.sleep(2)
            leadracer=random.choice(racers)
            print(leadracer,"HAS THE LEAD" )
            slprint("the lead isn't much and anyone could win now as the time gap is so small")
            winner=random.choice(racers)
    #racers=["George Russell", "Kimi Antonelli","Isack Hadjar","Lando Norris","Oscar Piastri","Charles leclerc","Lewis Hamilton","Max Verstappen"]        
            if winner=="George Russell":
                opwin=1
                slprint("AWADHRAJ => OHHHH!!! George Russell from MERCEDES has won the race and earns a new title for his team")
                tm.sleep(1)
                print("AWADHRAJ => He has a lead of",sec,"seconds")
                tm.sleep(1)
                slprint("AWADHRAJ => You know where the biggest party of the world will start today")
            elif winner=="Kimi Antonelli":
                opwin=2
                slprint("AWADHRAJ => OHHHH!!! Kimi Antonelli from MERCEDES has won the race and earns a new title for his team")
                tm.sleep(1)
                slprint("AWADHRAJ => THIS COMEBACK WILL BE REMEMBERED")
                tm.sleep(1)
                print("AWADHRAJ => He has a lead of",sec,"seconds")
                tm.sleep(1)
                slprint("AWADHRAJ => You know where the biggest party of the world will start today")
            elif winner=="Isack Hadjar":
                opwin=4
                slprint("AWADHRAJ => OHHHH!!! Isack Hadjar from RED BULL has won the race and earns a very new title for his team")
                tm.sleep(1)
                slprint("AWADHRAJ => MAX watching his teammate comeback")
                tm.sleep(1)
                print("AWADHRAJ => He has a lead of",sec,"seconds")
                tm.sleep(1)
                slprint("AWADHRAJ => You know where the biggest party of the world will start today, Isack Hadjar shows he deserve everything possible")
                tm.sleep(1)
                slprint("AWADHRAJ => HIS COMEBACK WILL BE REMEMBERED")
            elif winner=="Max Verstappen":
                opwin=3
                slprint("AWADHRAJ => OHHHH!!! Max Verstappen from RED BULL has won the race and have shown everyone why he is the best")
                tm.sleep(1)
                tm.sleep(1)
                slprint("AWADHRAJ => TU TU TU TU ! MAX VERSTAPPEN ! TU TU TU TU!!!")
                tm.sleep(1)
                print("AWADHRAJ => He has a lead of",sec,"seconds")
                tm.sleep(1)
                slprint("AWADHRAJ => You know where the biggest party of the world will start today")
            elif winner=="Lando Norris":
                opwin=5
                slprint("AWADHRAJ => OHHHH!!! Lando Norris from Mc Laren has won the race and have shown everyone why he is the best")
                tm.sleep(1)
                slprint("AWADHRAJ => Mc Laren , finally a title , they have been waiting to long for this")
                tm.sleep(1)            
                print("AWADHRAJ => He has a lead of",sec,"seconds")
                tm.sleep(1)
                slprint("AWADHRAJ => You know where the biggest party of the world will start today")
            elif winner=="Oscar Piastri":
                opwin=6
                slprint("AWADHRAJ => OHHHH!!! Oscar Piastri from Mc Laren has won the race and have shown everyone why he is the best")
                tm.sleep(1)
                slprint("AWADHRAJ => Mc Laren , finally a title , they have been waiting to long for this")
                tm.sleep(1)
                print("AWADHRAJ => He has a lead of",sec,"seconds")
                tm.sleep(1)
                slprint("AWADHRAJ => You know where the biggest party of the world will start today")
            elif winner=="Charles leclerc":
                opwin=7
                slprint("AWADHRAJ => OHHHH!!! Charles leclerc from FERRARI has won the race and have shown everyone why he is the best")
                tm.sleep(1)
                slprint("AWADHRAJ => FERRARI may have many titles but this one is some special")
                tm.sleep(1)
                print("AWADHRAJ => He has a lead of",sec,"seconds")
                tm.sleep(1)
                slprint("AWADHRAJ => You know where the biggest party of the world will start today")
            elif winner=="Lewis Hamilton":
                opwin=8
                slprint("AWADHRAJ => OHHHH!!! Lewis Hamilton from FERRARI has won the race and have shown everyone why he is the most successful racer in the world")
                tm.sleep(1)
                slprint("AWADHRAJ => Our 7 times world champion has won again , well we knew he would")
                tm.sleep(1)
                print("AWADHRAJ => He has a lead of",sec,"seconds")
                tm.sleep(1)
                slprint("AWADHRAJ => You know where the biggest party of the world will start today")
            slprint("AWADHRAJ => WE WERE VERY LUCKY TO WITNESS A RACE LIKE THIS")
            slprint("AWADHRAJ => BYE FOR TODAY, SEE YOU NEXT TIME!!!!!!")
            tm.sleep(2)
            print(".")
            tm.sleep(1)
            print(".")
            tm.sleep(1)
            print(".")
            tm.sleep(1)                                                                             #created by Awadhraj chauhan
            slprint("WELL THE GAME HAS ENDED LET'S SEE RESULTS OF YOUR BET")
            if seloption==opwin:
                slprint("CONGRATULATIONS YOUR RACER HAS WON THE RACE")
                tm.sleep(1)
                slprint("10000 CASINO CASH CREDITED YO YOUR CASINO ACCOUNT")
                cash=cash+10000
                print("CURRENT BALANCE:",cash)
            else:
                slprint("YOUR RACER HAVE LOST THE BET")
                tm.sleep(1)
                slprint("YOU LOST 10000 casino cash as you have lost the bet")
                cash=cash-10000
                print("CURRENT BALANCE:",cash)
            slprint("want to play again")
            i=input("(yes/no):").lower()
            if i=="yes":
                break
        game()
                                                                   #game2
def guess():
    while True:
        global cash
        gnum=random.randint(1,10)
        slprint("Rules are simple , you need to guess number in 3 chances and if you loose , 5000 casino cash will be deducted")
        slprint("Entry fees is 2500 casino cash")
        tm.sleep(2)
        print("CURRENT BALANCE:",cash)
        tm.sleep(3)
        confirm()
        if cash>=2500:
            cash=cash-2500
        else:
            slprint("Insufficent balance in the account to continue the game")
            tm.sleep(2)
            slprint("Buy more cash to continue the game....")
            tm.sleep(2)
            money()
        slprint(".    .     .     .     .     .     .   ")
        slprint("Let's begin , GUESS THE NUMBER")
        oneguess=int(input("What's that number ?:"))
        if oneguess!=gnum:
            slprint("OHH WRONG ANSWER , YOU STILL HAVE A CHANCE TO WIN")
            slprint("COM'ON YOU CAN DO ITTTT!!!!!!!!")
            twoguess=int(input("What's that number ?:"))
            if twoguess!=gnum:
                slprint("YEAHHHH!!!!")
                tm.sleep(2)
                slprint("JUST KIDDING....WRONG ANSWER")
                tm.sleep(1)
                slprint("Last chance.. don't let the bet go away from your hands")
                threeguess=int(input("What's that number ?:"))
                if threeguess!=gnum:
                    slprint("FINALLYYY!!!")
                    tm.sleep(2)
                    slprint("You get a streak of giving wrong answers")
                    slprint("I can feel the pain .....")
                    print("THE ANSWER WAS =>",gnum)
                    slprint("AS PER RULES THE 5000 casino cash IS DEDUCTED FROM THE BALANCE")
                    cash=cash-5000
                    tm.sleep(2)
                    print("CURRENT BALNCE:",cash)
                else:
                    slprint("OHHH SHIT !!! , IT WAS SO CLOSE.....")
                    tm.sleep(2)
                    slprint("...TO THE WRONG ANSWER")
                    slprint("LET'S GOOOO!!! You won the bet")
                    slprint("AS PER RULES THE 5000 casino cash CREDITED TO THE BALANCE")
                    cash=cash+5000
                    tm.sleep(2)
                    print("CURRENT BALNCE:",cash)                                                   #created by Awadhraj chauhan
            else:
                    slprint("OHHH SHIT !!! , IT WAS SO CLOSE.....")
                    tm.sleep(2)
                    slprint("...TO THE WRONG ANSWER")
                    slprint("LET'S GOOOO!!! You won the bet")
                    slprint("AS PER RULES THE 500 casino cash CREDITED TO THE BALANCE")
                    cash=cash+5000
                    tm.sleep(2)
                    print("CURRENT BALNCE:",cash)
        else:
            slprint("IN THE VERY 1ST GUESS , THAT'S IMPRESSIVE!")
            slprint("LET'S GOOOO!!! You won the bet")
            slprint("AS PER RULES THE 500 casino cash CREDITED TO THE BALANCE")
            cash=cash+5000
            tm.sleep(2)
            print("CURRENT BALNCE:",cash)
        slprint("want to play again")
        i=input("(yes/no):").lower()
        if i!="yes":
            break
    game()
        
                                                                            #game 3
def luckydraw():
    slprint("Welcome to the **LUCK IN THE DRAW??**")
    tm.sleep(1)
    slprint("Luck is needed to win this......talent and hardwork doesn't work here")
    slprint("Want to test your Luck?")
    tm.sleep(2)
    slprint("Entry fees is 3000 casino cash per draw")
    tm.sleep(2)
    print("CURRENT BALANCE:",cash)
    tm.sleep(3)
    global spin
    def spin():
        confirm()
        while True:
            global cash
            if cash>=3000:
                cash=cash-3000
            else:
                slprint("Insufficent balance in the account to continue the game")
                tm.sleep(2)
                slprint("Buy more cash to continue the game....")
                tm.sleep(2)
                money()
            X=random.randint(133,10000)
            slprint("OKAY THEN......")
            tm.sleep(2)
            slprint("The rules are simple....you get a chance to draw...it could be a reward and a debt trap too")
            tm.sleep(2)
            slprint("Here is the list of things in **LUCK IN THE DRAW??**......You'll be getting one of these things")
            tm.sleep(2)
            slprint("1)Jackpot of **GOLD** worth 150000 casino cash")
            slprint("2)Loss of 1000 casino cash")
            tm.sleep(1)
            print("3)lottery of",X,"casino cash")
            tm.sleep(1)
            slprint("4)Loss of *just* 100000 casino cash")
            slprint("5)get a chance to draw again")
            tm.sleep(1)
            slprint("6)Nothing...Well it's fine as you didn't loose too")
            tm.sleep(3)
            options=[1,2,3,4,5,6]
            weights=[10,55,40,14,40,35]
            draw=random.choices(options,weights=weights,k=1)[0]
            slprint("AND THE DRAW YOU GOT IS................")
            if draw==1:
                slprint("OHHHHHHHH!!!!!!!!!!!")
                tm.sleep(1)
                slprint("The amount of luck you have is CRAZYY.....You have just hit a JACKPOT!!!!")
                tm.sleep(1)
                slprint("You have won Gold worth upto 150000 casino cash")
                cash=cash+150000
                tm.sleep(1)
                slprint("That makes your balance:")
                tm.sleep(2)
                print("CURRENT BALANCE:",cash)
            elif draw==2:
                slprint("Welll...")
                tm.sleep(1)
                slprint("You lost 1000 casino cash...")
                tm.sleep(1)
                slprint("The luck maybe bad but isn't worst ....let's hope for the best in next draw")
                cash=cash-1000
                print("CURRENT BALANCE:",cash)
            elif draw==3:
                slprint("Congratulations .....")
                tm.sleep(1)
                print("You won a lottery of",X,"casino cash")
                tm.sleep(1)
                cash=cash+X
                slprint("That makes your balance:")
                tm.sleep(2)
                print("CURRENT BALANCE:",cash)
            elif draw==4:
                slprint("OHHHHH THE JACKPOT.....")
                tm.sleep(1)
                slprint("OF LOOSING THE HIGHEST AMOUNT 100000 casino cash")
                cash=cash-100000
                tm.sleep(1)
                slprint("That makes your balance:")
                tm.sleep(2)
                print("CURRENT BALANCE:",cash)
                if cash<3000:
                    tm.sleep(1)
                    slprint("You need to buy more casino cash in order to continue")
                    tm.sleep(1)
                    money()
                else:
                    tm.sleep(1)
                    slprint("HARD LUCK BRO")
            elif draw==5:
                slprint("You get to a chance to draw more 1 times ..")
                tm.sleep(1)                                                             #created by Awadhraj chauhan
                slprint("And the lucky draw you got is.......")
                weights=[10,55,40,14,0,35]
                draw1=random.choices(options,weights=weights,k=1)[0]
                if draw1==1:
                    slprint("OHHHHHHHH!!!!!!!!!!!")
                    tm.sleep(1)
                    slprint("The amount of luck you have is CRAZYY.....You have just hit a JACKPOT!!!!")
                    tm.sleep(1)
                    slprint("You have won Gold worth upto 150000 casino cash")
                    cash=cash+150000
                    tm.sleep(1)
                    slprint("That makes your balance:")
                    tm.sleep(2)
                    print("CURRENT BALANCE:",cash)
                elif draw1==2:
                    slprint("Welll...")
                    tm.sleep(1)
                    slprint("You lost 1000 casino cash...")
                    tm.sleep(1)
                    slprint("The luck maybe bad but isn't worst ....let's hope for the best in next draw")
                    cash=cash-1000
                    print("CURRENT BALANCE:",cash)
                elif draw1==3:
                    slprint("Congratulations .....")
                    tm.sleep(1)
                    print("You won a lottery of",X,"casino cash")
                    tm.sleep(1)
                    cash=cash+X
                    slprint("That makes your balance:")
                    tm.sleep(2)
                    print("CURRENT BALANCE:",cash)
                elif draw1==4:
                    slprint("OHHHHH THE JACKPOT.....")
                    tm.sleep(1)
                    slprint("OF LOOSING THE HIGHEST AMOUNT 100000 casino cash")
                    cash=cash-100000
                    tm.sleep(1)
                    slprint("That makes your balance:")
                    tm.sleep(2)
                    print("CURRENT BALANCE:",cash)                                                      #created by Awadhraj chauhan
                    if cash>3000:
                        tm.sleep(1)
                        slprint("You need to buy more casino cash in order to continue")
                        tm.sleep(1)
                        money()
                    else:
                        tm.sleep(1)
                        slprint("HARD LUCK BRO")
                elif draw1==6:
                    slprint("YOO WON........")
                    tm.sleep(1)
                    slprint("NOTHING")                                                  #created by Awadhraj chauhan
                    tm.sleep(1)
                    slprint("Well it's better than loosing something")
                    slprint("That makes your balance:")
                    tm.sleep(2)
                    print("CURRENT BALANCE:",cash)
                slprint(".")
                tm.sleep(1)
                slprint(".")
                tm.sleep(1)
                slprint(".")
                tm.sleep(1)
                slprint("Let's draw again?")
                o=input("READY(yes/no):").lower()
                if o!="yes":
                    break
            elif draw==6:
                slprint("YOO WON........")
                tm.sleep(1)
                slprint("NOTHING")
                tm.sleep(1)
                slprint("Well it's better than loosing something")
                slprint("That makes your balance:")
                tm.sleep(2)
                print("CURRENT BALANCE:",cash)
            slprint(".")
            tm.sleep(1)
            slprint(".")
            tm.sleep(1)
            slprint(".")
            tm.sleep(1)
            slprint("Let's draw again?")
            o=input("READY(yes/no):").lower()
            if o!="yes":
                break
        game()
    spin()


                                                                                    #gameslection
def game():
    slprint("WHAT WOULD YOU LIKE TO PLAY")
    tm.sleep(1)
    slprint("1) *F1* RACING CAR BET")
    tm.sleep(1)
    slprint("2)Guess the number between 1 to 10 (in 3 chances)")
    tm.sleep(1)
    slprint("3)Luck in the draw??")
    tm.sleep(3)
    slprint("4)PRESS 4 TO EXIT")
    tm.sleep(1)
    global gameoption
    gameoption=int(input("ENTER THE NUMBER OF THE CATEGORY YOU LIKE:"))
    if gameoption<=4:
        if gameoption==1:
            f1()
        elif gameoption==2:
            guess()
        elif gameoption==3:
            luckydraw()
        elif gameoption==4:
            if cash<0:
                slprint("Make sure the balance isn't pending...pay all the debt")
                slprint("Buy more cash before you leave ")
                money()
            else:
                checkout()
    else:
        slprint("INVALID OPTION SELECTED...CHOOSE AGAIN")
        game()

def money():
    slprint(" **NOTE** => YOU CAN ONLY PURCHASE CASINO CASH WORTH UPTO 200000 RUPEES")
    tm.sleep(2)
    slprint("The casino cash will be credited in your temporary casino account")
    tm.sleep(3)
    while True:
        dmcash=int(input("Enter the amount money you want to buy casino cash with:"))
        tm.sleep(2)
        global cash
        if dmcash<=0:
            slprint("INVALID AMOUNT OF PURCHASE MADE")
        elif dmcash>200000:
            slprint("INVALID AMOUNT PURCHASE MADE")
        else:
            cash+=2*dmcash
            print(cash,"casino cash is credited to your temporary casino account")
            tm.sleep(2)
            slprint("LET'S PLAY")
            tm.sleep(2)
            print("CURRENT BALANCE IN TEMPORARY ACCOUNT:",cash)
            game()
def checkout():
    print(".")
    tm.sleep(1)
    print(".")
    tm.sleep(1)
    print(".")
    tm.sleep(1)
    print(".")
    tm.sleep(1)
    slprint("Hello there welcome to th casino counter....")
    tm.sleep(1)
    slprint("Hope you enjoyed the game")
    tm.sleep(1)
    slprint("The casino cash balance in the account is . . . . . ")
    print("Balance =>",cash)
    global coin
    coin=cash//2
    tm.sleep(2)
    print("Here is your",coin,"Rupees you get")
    tm.sleep(1)
    slprint("Thankyou...visit again")
    exit()
money()
checkout()
