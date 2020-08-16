#! python3
# Crusader Kings II: Saved Game Modifier
def sgmMainMenu(selectedReligion):
    from sgmModules import mAboutSGM as aboutManager
    from sgmModules import mShifterStatistics as statisticShifter
    from sgmModules import mShifterReligion as religionShifter
    from sgmModules import mUnitBooster as unitBooster
    import pyinputplus as pyip
    import pyperclip

    print('\n')
    sgmInfo = ['HalfElf.net', 'Crusader Kings II: Saved Game Modifer', 'Version 2.1.20200816a']
    for info in sgmInfo:
        print(info.center(80))

    if selectedReligion != 'noChange':
        menuList = ['Character: Update Statistics', 'Clear Selected Religion ("' + selectedReligion + '")', 'Update Army Unit', 'About This Program / Help', 'Exit']
    else:
        menuList = ['Character: Update Statistics', 'Select New Religion', 'Update Army Unit', 'About This Program / Help', 'Exit']
    print('\n')
    selectedMenuOption = pyip.inputMenu(menuList, numbered = True, lettered = False)
    if selectedMenuOption == 'Exit':
        print('Goodbye.')
        exit()
    elif selectedMenuOption == 'About This Program / Help':
        aboutManager.aboutSGM()
    elif selectedMenuOption == 'Select New Religion':
        selectedReligion = religionShifter.shiftCharacterReligion()
    elif selectedMenuOption == 'Clear Selected Religion ("' + selectedReligion + '")':
        selectedReligion = 'noChange'
    elif selectedMenuOption == 'Character: Update Statistics':
        newStatistics = statisticShifter.shiftCharacterStatistics(selectedReligion)
        pyperclip.copy(newStatistics)
        for info in infoOutput:
            print(info.center(80))
    elif selectedMenuOption == 'Update Army Unit':
        # strNUI = string, new unit info
        strNUI = unitBooster.boostUnitNumbers()
        pyperclip.copy(strNUI)

    infoOutput = []
    infoOutput.append('=' * 80)
    infoOutput.append('Processes completed successfully.')
    infoOutput.append('=' * 80 + '\n')
    for line in infoOutput:
        print(line)
    sgmMainMenu(selectedReligion)

def ck2sgm():
    sgmMainMenu('noChange')

ck2sgm()
