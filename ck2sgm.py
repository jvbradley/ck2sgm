#! python3
# Crusader Kings II: Saved Game Modifier
def sgmMainMenu(shiftReligionYN, newCharacterReligion):
    # This is a work in progress.  The aim of this script is to incorporate
    # religions under the logic of adjusting character statistics.
    from sgmModules import mShifterStatistics as statisticShifter
    import pyinputplus as pyip
    import pyperclip

    sgmInfo = ['HalfElf.net', 'Crusader Kings II: Saved Game Modifer', 'Version 1.20200806a']
    sgmInfo.append('Session religion shift: ' + str(shiftReligionYN) + '\n')
    print('\n')
    for info in sgmInfo:
        print(info.center(80))

    menuList = ['Update Another Character', 'Exit']
    selectedMenuOption = pyip.inputMenu(menuList, numbered = True, lettered = False)
    if selectedMenuOption == 'Exit':
        print('Goodbye.')
        exit()
    elif selectedMenuOption == 'Update Another Character':
        newStatistics = statisticShifter.shiftCharacterStatistics(shiftReligionYN, newCharacterReligion)
        pyperclip.copy(newStatistics)
        infoOutput = []
        infoOutput.append('=' * 80)
        infoOutput.append('Processes completed successfully.')
        infoOutput.append('The updated character statistics are now in memory.')
        infoOutput.append('=' * 80 + '\n')
        for info in infoOutput:
            print(info.center(80))

        sgmMainMenu(shiftReligionYN, newCharacterReligion)

def ck2sgm():
    from sgmModules import mShifterReligion as religionShifter
    import pyinputplus as pyip
    shiftReligionYN = pyip.inputYesNo(' * Set/adjust character religions in this session? ')
    if shiftReligionYN == 'yes':
        newCharacterReligion = religionShifter.shiftCharacterReligion()
    elif shiftReligionYN == 'no':
        newCharacterReligion = False

    sgmMainMenu(shiftReligionYN, newCharacterReligion)

ck2sgm()
