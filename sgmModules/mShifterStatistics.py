def generateRandomAttributes():
    # This function generates a set of five randomly generated attribute values
    # between the values of 13 and 24 and then returns the data.  You can
    # adjust the values 13 and 24.
    import random
    attOutput = '\t\t\tatt={'
    for i in range(5):
        attOutput += str(round(random.uniform(13,24))) + ' '
        i += 1

    attOutput = attOutput[0:-1] + '}'
    return attOutput

def setModificationScope(selectedReligion):
    # Sit, Ubu, sit.  Good dog.

    # These are the statistics that this script will modify.
    modifyLines = ['att={', 'fer=', 'health=', 'prs=', 'piety=', 'wealth=']

    if selectedReligion == 'noChange':
        # The script will leave these ones alone in this version.
        skipLines = ['tr={', 'dnt=', 'dna="', 'prp="', 'lover=', 'title="', \
        'job="', 'player=', 'player_name="', 'rel=', 'secret_religion=', \
        'gov=', 'consort=', 'consort_of=', 'cul=', 'bstd=', 'claim=', '{', \
        '}', '\ttitle=', '\tpressed=yes', '\tweak=yes', 'g_cul=', 'ascul=', \
        'is_custom=yes', 'is_dynamic=yes', 'base_title=']
    elif selectedReligion != 'noChange':
        modifyLines.append('rel=')
        skipLines = ['tr={', 'dnt=', 'dna="', 'prp="', 'lover=', 'title="', \
        'job="', 'player=', 'player_name="', 'secret_religion=', 'gov=', \
        'consort=', 'consort_of=', 'cul=', 'bstd=', 'claim=', '{', '}', \
        '\ttitle=', '\tpressed=yes', '\tweak=yes', 'g_cul=', 'ascul=', \
        'is_custom=yes', 'is_dynamic=yes', 'base_title=']

    return [modifyLines, skipLines]

def shiftCharacterStatistics(selectedReligion):
    import pyinputplus as pyip
    import pyperclip
    # Iterate a string output for the return value.
    newStatistics = str()

    # Adjust fields based on whether or not religion will be changed.
    modificationScope = setModificationScope(selectedReligion)
    modifyLines = modificationScope[0]
    skipLines = modificationScope[1]

    # This question will impact prestige, piety, and wealth.
    countyLordYN = pyip.inputYesNo(' * Is this character managing a county? ')

    # Grab the attributes from memory.
    attributeInput = pyperclip.paste()

    # Make a list of the items from memory.
    attributeInputByLine = attributeInput.split('\n')

    # Look for missing attributes; add them with filler values if necessary.
    attributeLocations = {}
    for line in range(len(attributeInputByLine)):
        for modifier in modifyLines:
            if modifier in attributeInputByLine[line]:
                attributeLocations[modifier] = line
            elif modifier not in attributeInputByLine[line]:
                attributeLocations.setdefault(modifier, False)
    for attributeKey, attributeValue in attributeLocations.items():
        if attributeKey == 'rel=' and selectedReligion != 'noChange':
            attributeInputByLine.insert(2, '\t\t\trel="' + selectedReligion + '"')

        elif attributeKey == 'prs=' and attributeValue == False:
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
                elif modifier == 'rel=' and '\t\t\trel=' not in newStatistics:
                    newStatistics += '\t\t\trel="' + selectedReligion + '"\n'
                    print(newStatistics)
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

    # Return the updated statistics.
    return newStatistics
