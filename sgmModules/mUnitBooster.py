def bootCamp(troopSection):
    '''
    This module only builds units of each type composed of 20,000 soldiers
    each.  I'll customize the inputs at a later time.
    '''
    tabFive = '\t' * 5
    tabSix = '\t' * 6
    tabSeven = '\t' * 7
    newRecruits = [tabSix + '{']
    for newTroops in troopSection:
        newRecruits.append(tabSeven + newTroops + '20000.000')

    newRecruits.append(tabSix + '}')
    newRecruits.append(tabFive + '}')
    return newRecruits

def boostUnitNumbers():
    '''
    This script updates army units.  It operates on information from the
    clipboard, and pastes the updated information back into your clipboard.
    You can just paste over the section of the file from which you copied the
    original information.

    Start with the line in your saved game file that is tabbed five times and
    reads 'sub_unit='.  Copy from that line to the closing curly bracket at the
    end of that sub-unit's section in the file, also indended five times.

    Other visual clues for the end of section for sub-unit include either a
    'location=' field or another 'sub_unit=' field immediately following.
    '''
    tabSix = '\t' * 6
    import pyperclip, pprint
    # These are the statistics that this script will modify.
    troopSection = ['li=', 'hi=', 'pi=', 'lc=', 'hc=', 'ar=', 'horse_archers=']

    # The script will leave these ones alone in this version.
    skipLines = ['sub_unit=', '{', 'id=', 'type=', '}', 'leader=', \
    'owner=', 'date=', 'troops=', 'morale=']
    unitInfo = pyperclip.paste()
    unitInfoByLine = unitInfo.split('\n')
    newUnitInfo = []

    for thisLine in unitInfoByLine:
        if 'morale=' in thisLine:
            newUnitInfo.append(tabSix + 'morale=1.000')
        elif 'troops=' in thisLine:
            print(' * I don\'t know what I\'ve been told ...')
            newRecruits = bootCamp(troopSection)
            for newUnit in newRecruits:
                newUnitInfo.append(newUnit)
            break
        else:
            newUnitInfo.append(thisLine)

    # String: new unit information will be returned
    strNUI = str()
    for lineItem in newUnitInfo:
        strNUI += lineItem + '\n'

    strNUI = strNUI[0:-1]
    return strNUI
