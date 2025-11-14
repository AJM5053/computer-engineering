# This is my first text based adventure game
print('The Haunted Library')
print('You are in the libary late at night finishing an assignment')
print('You here a loud *CLINK* from the ancient manuscripts section')
print('This sends a shiver down your spine but also piques your curiosity')
print('Do you want to:')
print('1. Investigate the sound')
print('2. Head for the exit')

# This function will be used for making choices throughout the game
def get_choice():
    choice = input('Enter 1 or 2: ')
    while choice not in ['1', '2']:
        print('Invalid choice, try again')
        choice = input('Enter 1 or 2: ')
    return choice

choice1 = get_choice()

if choice1 == '1':
    print('\nYou cautiously explore the accient manuscrips section')
    print('An old, dusty book shakes from a shelf and lands on the floor in front of you...')
    print('Do you want to:')
    print('1. Pick up the book')
    print('2. Splash some water on it')

    choice2 = get_choice()

    if choice2 == '1':
        print('\nThe book shoots open in your hands. A terrifying spirit in white robes and gold chains appears!!')
        print('You close your eyes in hope that all of this is a bad dream. The spirit decides to speak')
        print('"Those who look into the eyes of Lemures shall be rewarded"')
        print('Do you want to:')
        print('1. Look into the eyes of Lemures')
        print('2. Run away')

        choice3 = get_choice()

        if choice3 == '1':
            print('\nYou reluctantly open your eyes and stare into the huge green orbs that are eyes of the spirit')
            print('A strange sensation overwhelmes you as the spirit gets closer and closer. You pass out')
            print('Upon waking up, the book is back on the shelf and Lemures is gone. You feel a lot smarter than before you passed out')
            print('Perhaps finishing that assignment will be a breeze now')
            print('🧠 Ending: Knowledge is Power 🧠')

        else:
            print('\nYou scream in fear and dash in the opposite direction. The spirit speaks again')
            print('"HOW DARE YOU TURN AWAY FROM LEMURES!!')
            print('The spirit catches up with you. You are doomed')
            print('It drags you back towards the book, then inside...')
            print('You will be missed')
            print('💀 Ending: Gone Forever 💀')

    else:
        print('\nYou take out your water bottle and splash the book')
        print('A loud screech comes from the book and a spirit appears before you!!')
        print('It looks angry and speaks to you')
        print('"YOU WILL SUFFER FOR ATTEMPTING TO HARM LEMURES!!"')
        print('Do you want to:')
        print('1. Beg for mercy')
        print('2. Attack Lemures')

        choice4 = get_choice()

        if choice4 == '1':
            print('\nTerrified for your life, you start begging to the spirit on your knees')
            print('Lemures looks displeased and speaks again')
            print('Disgraceful!! Lemures has no time for worms')
            print('After slowly raising your head, you notice the spirit has vanished and the book is back on the shelf')
            print('You celebrate avoiding harm while wiping tears off your face')
            print('🥲 Ending: Pathetic Survivor 🥲')

        else:
            print('\nYou gather up all your courage and charge at the spirit like a gladiator')
            print('You throw a punch only for it to go through Lemures, no surprise there')
            print('Lemures puts a nasty grin on and speaks')
            print('"Brave, but foolish..."')
            print('With a single hand movement from the spirit, you go flying out the window and land on concrete')
            print('That was really stupid and now both of your legs are broken, good effort though')
            print('🚑 Ending: Ouch 🚑')

else:
    print('\nStartled by the noise, you decide you want to leave')
    print('You reach the exit but the doors refuse to open, even when you press the button')
    print('This could be a simple malfunction but you sense something paranormal is the cause')
    print('Freaked out, you start to get desperate')
    print('Do you want to: ')
    print('1. Look for another exit')
    print('2. Smash a window to get out')

    choice5 = get_choice()

    if choice5 == '1':
        print('\nYou run around the library in a panic to find another exit')
        print('While you search, more strange noises echo from the ancient manuscripts section. Time is running out...')
        print('You eventually find a backdoor exit near the admin office')
        print('However, you realise that your bag is missing. You left it at the main exit while trying to get the button to work')
        print('What a pain. You want to leave but that bag has all your notes in...')
        print('Do you want to: ')
        print('1. Leave without your bag')
        print('2. Go back for it')

        choice6 = get_choice()

        if choice6 == '1':
            print('You decide the notes are not important and go to leave')
            print('The door is locked so you start kicking it with all your strength')
            print('Something is irritated by all the noise and charges at you, a spirit of some sort!!')
            print('You are cornered. The spirit devours you in rage then returns to the ancient manuscripts section')
            print('What a horrible way to go...')
            print('🍴 Ending: Spirit dinner 🍴')

        else:
            print('You run back to the main enterance quickly, your bag is still there')
            print('You turn to head back to the backdoor exit with your bag when you hear the main doors open')
            print('It was a campus security officer doing his routine check of the libary, he asks')
            print('"Are you alright mate?"')
            print('Without a second thought, you run past him and leave the library')
            print('That was quite rude of you but oh well, you escaped')
            print('😅 Ending: Lucky Escape 😅')
    else:
        print('You pick up a chair and throw it at the nearest window')
        print('The window is loudly shattered, irritating whatever is up there in the ancient manuscripts section')
        print('Before you can dash out the window, you get grabbed!!')
        print('"What the hell have you done??"')
        print('It is a campus security officer. You might be in trouble here...')
        print('Do you want to: ')
        print('1. Explain the situation to him')
        print('2. Force him off you')

        choice7 = get_choice()

        if choice7 == '1':
            print('You try your best to explain the paranormal things that happened tonight')
            print('The officer laughs in your face')
            print('"Someone has had too much to drink tonight. Now, come with me')
            print('You get escorted to the security office where you have to explain yourself')
            print('You might be in a lot of trouble here...')
            print('😒 Ending: Naughty Student 😒')

        else:
            print('You push the officer hard enough to escape his grip')
            print('You dash out the window you smahsed to make your escape, you hear the officer shout')
            print('OI, GET BACK HERE!!')
            print('Before you get far, you hear a scream come from the officer you just evaded')
            print('It seems he was in the wrong place at the wrong time...')
            print('🏃 Ending: Get Outta There 🏃')