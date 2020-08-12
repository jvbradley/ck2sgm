#! python3
# Crusader Kings II: Saved Game Modifier
def sgmMainMenu(selectedReligion):
    from sgmModules import mAboutSGM as aboutManager
    # This is a work in progress.  The aim of this script is to incorporate
    # religions under the logic of adjusting character statistics.
    from sgmModules import mShifterStatistics as statisticShifter
    from sgmModules import mShifterReligion as religionShifter
    import pyinputplus as pyip
    import pyperclip

    print('\n')
    sgmInfo = ['HalfElf.net', 'Crusader Kings II: Saved Game Modifer', 'Version 2.0.20200812a']
    for info in sgmInfo:
        print(info.center(80))

    if selectedReligion == 'noChange':
        menuList = ['Character: Update Statistics', 'Queue New Religion', 'About This Program / Help', 'Exit']
    else:
        menuList = ['Character: Update Statistics', 'Queue New Religion (Current: ' + selectedReligion + ')', 'About This Program / Help', 'Exit']
    print('\n')
    selectedMenuOption = pyip.inputMenu(menuList, numbered = True, lettered = False)
    if selectedMenuOption == 'Exit':
        print('Goodbye.')
        exit()
    elif selectedMenuOption == 'About This Program / Help':
        aboutManager.aboutSGM()
    elif selectedMenuOption == 'Queue New Religion':
        selectedReligion = religionShifter.shiftCharacterReligion()
    elif selectedMenuOption == 'Character: Update Statistics':
        newStatistics = statisticShifter.shiftCharacterStatistics(selectedReligion)
        pyperclip.copy(newStatistics)
        infoOutput = []
        infoOutput.append('=' * 80)
        infoOutput.append('Processes completed successfully.')
        infoOutput.append('The updated character statistics are now in memory.')
        infoOutput.append('=' * 80 + '\n')
        for info in infoOutput:
            print(info.center(80))

    sgmMainMenu(selectedReligion)

def ck2sgm():
    sgmMainMenu('noChange')

ck2sgm()
