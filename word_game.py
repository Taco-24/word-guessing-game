from random import choice
word_list=['sloven', 'recusancy', 'scraper', 'speciation', 'pogey', 'abrasion', 'culpability', 'willfulness', 'eponym',
 'pharisaical', 'takeoff', 'heavily', 'apsis', 'sandalled', 'identicalness', 'microbar', 'saleratus', 'cause',
 'inescapably', 'ostracize', 'imbroglio', 'slipper', 'airstrip', 'bleat', 'schmeer', 'nylghai', 'abvolt', 'nonmagnetic',
 'proficiently', 'padder', 'lockbox', 'comity', 'pharaonic', 'backsliding', 'airing', 'aquaplane', 'weaverbird',
 'release', 'noisomeness', 'underlined', 'barographic', 'measuring', 'vacillation', 'carnivorous', 'potentate',
 'screechy', 'pneumothorax', 'chimaera', 'liberalize', 'metonym', 'batman', 'pointless', 'krypton', 'irrevocably',
 'radiobiology', 'jerkiness', 'picture', 'miscellanea', 'flowery', 'alarming', 'sachet', 'unmelodious', 'diatomite',
 'chloroquine', 'ichneumon', 'vinegar', 'roadless', 'trusty', 'affiance', 'twinberry', 'irresponsibly', 'farmland',
 'unwontedly', 'intradermal', 'perry', 'formalistic', 'continuant', 'origination', 'blower', 'gravitation', 'denizen',
 'purportedly', 'backbiter', 'muddled', 'handball', 'sleaze', 'tinter', 'trivialize', 'snapper', 'semen', 'pressurize',
 'subsidise', 'outface', 'guilty', 'threescore', 'amphisbaena', 'funding', 'matriarchy', 'partitionist', 'round',
 'myotonia', 'unchivalrous', 'pyroelectric', 'unconscionable', 'anathematize', 'sluttishness', 'ranter', 'anklet',
 'galleon', 'comma', 'chitinous', 'reckoning', 'believable', 'transpiration', 'savory', 'bracteal', 'grabby',
 'autoimmunity', 'sweetmeat', 'effeminate', 'brill', 'ingeniously', 'depreciation', 'scrimshaw', 'irritative',
 'pentathlon', 'warehouser', 'cretonne', 'covetousness', 'complementation', 'accumulate', 'invest', 'furnace',
 'softening', 'oppressor', 'schmuck', 'braggy', 'absorptivity', 'radio', 'soporific', 'paleobotany', 'animadvert',
 'demonic', 'conveyer', 'police', 'chastened', 'charitably', 'radiosensitivity', 'silverware', 'apochromatic',
 'musical', 'gaudiness', 'antenna', 'vellum', 'affiliate', 'craniometry', 'attain', 'silkiness', 'reeler', 'palaver',
 'sgraffito', 'cheater', 'crackerjack', 'endogamy', 'sanitate', 'atelectasis', 'polluted', 'archer',
 'companionableness', 'mutually', 'remodeled', 'pilferage', 'councilwoman', 'ruffianism', 'laudably', 'lividity',
 'philistine', 'canicular', 'amoral', 'beaklike', 'igneous', 'corrugation', 'sunscreen', 'unwelcome', 'empiric',
 'beleaguer', 'undeterminable', 'auric', 'rectify', 'musher', 'antisyphilitic', 'forthright', 'mesomorphy', 'formed',
 'savings', 'chirpily', 'permit', 'nominalistic', 'natality', 'overutilization', 'grandiloquently', 'aphagia', 'benzol',
 'mainspring', 'faltering', 'aspirate', 'pyromancy', 'evasion', 'hideaway', 'humankind', 'compatibly', 'showcase',
 'anagrammatize', 'building', 'oxford', 'handbell', 'apologetic', 'convinced', 'tender', 'solidity', 'retinene',
 'personation', 'blackcock', 'sacrificer', 'insufferable', 'tumblebug', 'acarus', 'deific', 'leptocephalus',
 'reductase']
status = True
while bool(status):
    guess_word = choice(word_list)
    chance = 5
    guessed_words = []
    guess_display = ["_" for i in guess_word]
    print(f"The word is: \n{' '.join(guess_display)}")
    print(f"Total number of chances: {chance}")

    while "_" in guess_display:
        guess = input("Enter your guess: ").lower()
        if guess in guessed_words:
            print("Already guessed this alphabet, try again.\n")
            continue
        if len(guess) > 1:
            print("You're only supposed to guess one letter at a time, please try again.\n")
            continue
        if guess in guess_word:
            for index in range(len(guess_word)):
                if guess_word[index] == guess:
                    guess_display[index] = guess
            print(f"{' '.join(guess_display)}\n")

        else:
            chance -= 1
            print(f"Wrong guess :(\nNumber of chances left: {chance}\n")
        if chance == 0:
            print("You ran out of guesses, the correct word was '{}'".format(guess_word.upper()))
            break
        guessed_words.append(guess)
    if chance > 0:
        print("Congratulations, you guessed the word correctly and it was '{}'".format(guess_word.upper()))
    status = int(input("\nPress 1 to play again or 0 to exit: "))
