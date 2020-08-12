def provideAnswerResponse(selectedMenuOption):
    import textwrap
    q1 = '\nThe Saved Game Modifier facilitates editting of court members\' \
statistics in Crusader Kings II saved game files.  As of this version, it \
can modify attributes, religion, fertility, health, and wealth.  It has been \
successfully tested on saved game files for version 3.3.3.0 of the game, \
though this formatting does appear consistent in other versions.'

    q2 = '\nThis script assumes that you have installed Python 3.8.2 or a \
compatible version on your platform of choice.  It "should" work.'

    q3 = '\nI played a Half-Elf rogue in EverQuest for a number of years.  I \
was exceptionally sneaky.'

    q4a = '\nFirst and foremost, protect your kingly posterior (C.Y.A.) - Make a \
copy of your game file as a back-up.  It is easier to restore a corrupted \
game file from its original source than to find and dekerbörkulate a few \
lines of information.'

    q4b = '\nOpen your saved game file and look for the character \
that you want to edit.  This script requires that you provide between the \
fields from "att=" (attributes) and "health=" (health).  Copy all fields and \
content starting with "att=" and ending with the inclusion of wealth.'

    q4Fields = ['att={2 2 8 2 2}', 'tr={10 85 77 188 83 }', \
    'rel="hellenic_pagan"', 'secret_religion="taoist"', 'cul="pictish"', \
    'dnt=1000104328', 'dna="qcilvebuwaj"', \
    'prp="wcviik00000000000000000000000000000000"', 'fer=0.200', \
    'health=4.000', 'title="title_cupbearer"', 'job="job_spymaster"', \
    'wealth=15.00000']

    q4OutA = textwrap.wrap(q4a, width = 80, replace_whitespace = False)
    q4OutB = textwrap.wrap(q4b, width = 80, replace_whitespace = False)
    q4 = [q4OutA, q4OutB, q4Fields]

    if selectedMenuOption == 'Q1':
        fetchedAnswer = textwrap.wrap(q1, width = 80, replace_whitespace = False)
    elif selectedMenuOption == 'Q2':
        fetchedAnswer = textwrap.wrap(q2, width = 80, replace_whitespace = False)
    elif selectedMenuOption == 'Q3':
        fetchedAnswer = textwrap.wrap(q3, width = 80, replace_whitespace = False)
    elif selectedMenuOption == 'Q4':
        fetchedAnswer = q4

    return fetchedAnswer

def aboutSGM():
    '''
    About the Saved Game Modifier
    '''
    import pyinputplus as pyip
    menuList = ['Q1: What is the Saved Game Modifier?', 'Q2: Will my computer run this \
program?', 'Q3: Why the domain HalfElf.net?', 'Q4: How do I make use of the \
Saved Game Modifier?', 'Exit']

    selectedMenuOption = pyip.inputMenu(menuList, numbered = True, lettered = False)
    if selectedMenuOption == 'Exit':
        return
    else:
        selectedMenuOption = selectedMenuOption[0:2]
        fetchedAnswer = provideAnswerResponse(selectedMenuOption)

        if selectedMenuOption != 'Q4':
            for outputGroup in fetchedAnswer:
                print(outputGroup)
            print('\n')
        else:
            for outputGroup in range(len(fetchedAnswer)):
                if fetchedAnswer[outputGroup] != fetchedAnswer[-1]:
                    for thisLine in fetchedAnswer[outputGroup]:
                        print(thisLine)
                elif fetchedAnswer[outputGroup] == fetchedAnswer[-1]:
                    for thisField in fetchedAnswer[outputGroup]:
                        print('\t\t\t' + thisField)

                print('\n')
    aboutSGM()
