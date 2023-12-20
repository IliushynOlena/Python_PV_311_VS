import random
print("\t\tWelcome to the game ")
print("\t\tRock Paper Scissors ")

user = 0
bot = 0

user_score = 0
bot_score = 0
while True:
    user_score = 0
    bot_score = 0
    for item in range(3):
        #print("--------------------------- Round [{}]--------------------".format(item+1))
        print(f"--------------------------- Round [{item+1}]--------------------")
        while True:
            user = input("\t[r] - rock;\n\t[p] - paper; \n\t[s] - scissors;\n\tEnter your choice :")
            user = user.lower()
            if user == 'r' or user == 'p' or user == 's':
                break
            else:
                print("Try again! Enter new symbol ")
                
        bot = random.choice('rps')
        print("\t User \t  Bot")
        print(f"\t [{user}]\t [{bot}]")
        if user == 'r' and bot == 's' or user == 'p' and bot == 'r' or user == 's' and bot == 'p':
            user_score += 1
        elif bot == 'r' and user == 's' or bot == 'p' and user == 'r' or bot == 's' and user == 'p':
            bot_score += 1
    if user_score > bot_score:
        print("================= You are winner =================")
    elif bot_score > user_score:
        print("================= Bot is winner =================")
    else :
        print("====================Draw=======================")
        
    while True:
        user_choice = input("Play again ? [y] - YES; [n] - NO : ")
        user_choice = user_choice.lower()
        if user_choice == 'y' or user_choice == 'n':
            break
        else :
            print("Enter your choice !!!")
    if user_choice == 'n':
        break
        