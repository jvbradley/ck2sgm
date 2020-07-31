#! /usr/bin/python
'''
Crusader Kings II: Statistic Shifter

This script facilitates editting of court members' statistics in Crusader Kings
II saved game files.  It has been successfully tested on saved game files for
version 3.3.3.0 of the game, though this formatting does appear consistent in
other versions.

This script assumes that you have installed Python 3.8.2 or a compatible
version on your platform of choice.  To use this script, copy an NPC's
information between the lines entitled 'att={ ...' and 'wealth={ ...', as
demonstrated below:

            att={2 2 8 2 2}
            tr={10 85 77 188 83 }
            rel="hellenic_pagan"
            secret_religion="taoist"
            cul="pictish"
            dnt=1000104328
            dna="qcilvebuwaj"
            prp="wcviik00000000000000000000000000000000"
            fer=0.200
            health=4.000
            title="title_cupbearer"
            job="job_spymaster"
            wealth=15.00000

This script will accommodate can accommodate optional fields as well, such as
titles, jobs, and consort status.  The script manages white space and line
breaks in the data to ensure consistency with the current structure of the file.
As this script makes no claims of warranty or guarantee, ALWAYS MAKE A BACK-UP
OF YOUR SAVED GAMNE FILE BEFORE YOU MODIFY IT.
'''
def generateRandomAttributes():
    # This function generates a set of five randomly generated attribute values
    # between the values of 14 and 24 and then returns the data.  You can
    # adjust the values 14 and 24.
    import random
    attOutput = '\t\t\tatt={'
    for i in range(5):
        attOutput += str(round(random.uniform(14,24))) + ' '
        i += 1

    attOutput = attOutput[0:-1] + '}'
    return attOutput

def statShifter():
    import pyinputplus as pyip
    import pyperclip
    introText1 = 'Crusader Kings II: Statistic Shifter'
    introText2 = 'Version 1.01.20200730a\n'
    print('\n' + introText1.center(80))
    print(introText2.center(80))

    # Grab the attributes from memory.
    attributeInput = pyperclip.paste()

    # Make a list of the items from memory.
    attributeInputByLine = attributeInput.split('\n')

    # These are the statistics that this script will modify.
    modifyLines = ['att={', 'fer=', 'health=', 'prs=', 'piety=', 'wealth=']

    # The script will leave these ones alone in this version.
    skipLines = ['tr={', 'dnt=', 'dna="', 'prp="', 'lover=', 'title="', 'job="', 'player=', 'player_name="', 'rel=', 'gov=', 'consort=', 'consort_of=', 'cul=', 'bstd=']

    # This question will impact prestige, piety, and wealth.
    countyLordYN = pyip.inputYesNo(' * Is this character managing a county? ')

    # Look for missing attributes; add them with filler values if necessary.
    attributeLocations = {}
    for line in range(len(attributeInputByLine)):
        for modifier in modifyLines:
            if modifier in attributeInputByLine[line]:
                attributeLocations[modifier] = line
            elif modifier not in attributeInputByLine[line]:
                attributeLocations.setdefault(modifier, False)
    for attributeKey, attributeValue in attributeLocations.items():
        if attributeKey == 'prs=' and attributeValue == False:
            attributeInputByLine.insert(attributeLocations['health='] + 1, '\t\t\tprs=1.000\n')
        elif attributeKey == 'piety=' and attributeValue == False and attributeLocations['wealth='] != False:
            attributeInputByLine.insert(attributeLocations['health='] + 2, '\t\t\tpiety=1.000\n')
        elif attributeKey == 'piety=' and attributeValue == False and attributeLocations['wealth='] == False:
            attributeInputByLine.insert(attributeLocations['health='] + 2, '\t\t\tpiety=1.000\n')
        elif attributeKey == 'wealth=' and attributeValue == False:
            attributeInputByLine.append('\t\t\twealth=15.00000\n')


    for line in attributeInputByLine:
        # While iterating through the attribute lines, these lines will be
        # blindly passed 'as-is' into the output.
        for skip in skipLines:
            if '\t\t\t' + skip in line:
                newStatistics += line + '\n'
        # End skip logic

        # Itterate through the items, one line at a time.
        for modifier in modifyLines:
            # Check if this current line is a field that we want to adjust.
            if '\t\t\t' + modifier in line:
                if modifier == 'att={':
                    newStatistics = str(generateRandomAttributes()) + '\n'
                elif modifier == 'fer=':
                    newStatistics += '\t\t\tfer=1.500\n'
                elif modifier == 'health=':
                    newStatistics += '\t\t\thealth=6.900\n'
                elif modifier == 'prs=':
                    if countyLordYN == 'yes':
                        newStatistics += '\t\t\tprs=2750.000\n'
                    elif countyLordYN == 'no':
                        newStatistics += '\t\t\tprs=750.000\n'
                elif modifier == 'piety=':
                    if countyLordYN == 'yes':
                        newStatistics += '\t\t\tpiety=1500.000\n'
                    elif countyLordYN == 'no':
                        newStatistics += '\t\t\tpiety=500.000\n'
                elif modifier == 'wealth=':
                    if countyLordYN == 'yes':
                        newStatistics += '\t\t\twealth=125000.00000'
                    elif countyLordYN == 'no':
                        newStatistics += '\t\t\twealth=400.00000'
            # This ends the logic for field adjustments.
    # End iteration of statistics.

    # Drop the updated statistics into memory, readying it for pasting.
    pyperclip.copy(newStatistics)
    print(' * Process complete.')
    exit()

statShifter()
