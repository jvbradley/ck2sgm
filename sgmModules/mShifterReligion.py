def shiftCharacterReligion():
    '''
    This script intends to facilitate adjusting the religion of NPC characters.
    It may be used in conjunction with the Statistic Shifter.

    Source: https://ck2.paradoxwikis.com/Religion

    It'll look pretty in a future version, I'm sure.
    '''
    import pyinputplus as pyip

    ck2Religions = {\
    'judaism': [\
        ['jewish', 'samaritan', 'karaite']], \
    'indian': [\
        ['hindu', 'buddhist', 'jain', 'taoist']], \
    'mazdan': [\
        ['zoroastrian', 'khurmazta', 'mazdaki', 'manichean']], \
    'islam': [\
        ['sunni', 'yizadi', 'zikri'], \
        ['shia', 'druze', 'hurufi', 'qarmatian'], \
        ['ibadi', 'kharijite']],
    'christianity': [\
        ['catholic', 'cathar', 'fraticelli', 'waldensian', 'lollard'], \
        ['orthodox', 'bogomilist', 'monothelite', 'iconoclast', 'paulician'], \
        ['miaphysite', 'monophysite'], ['nestorian', 'messalian']],
    'pagan': [\
        ['norse_pagan', 'norse_pagan_reformed'], \
        ['tengri_pagan', 'tengri_pagan_reformed'], \
        ['aztec', 'aztec_reformed'], \
        ['slavic_pagan', 'slavic_pagan_reformed'], \
        ['finnish_pagan', 'finnish_pagan_reformed'], \
        ['baltic_pagan', 'baltic_pagan_reformed'], \
        ['west_african_pagan', 'west_african_pagan_reformed'], \
        ['hellenic_pagan', 'hellenic_pagan_reformed'], \
        ['zun_pagan', 'zun_pagan_reformed']]}

    infoOutput = ['\n\n', 'SHIFT-O-MATIC', \
    'From the following menu,', \
    'select a major religion family.\n']

    for info in infoOutput:
        print(info.center(80))
    menuReligionFamilies = []
    for religionFamily in ck2Religions.keys():
        menuReligionFamilies.append(religionFamily)

    selectedReligionFamily = pyip.inputMenu(menuReligionFamilies, numbered = True, lettered = False)
    menuReligionOptions = []
    for religionGroup in ck2Religions[selectedReligionFamily]:
        for religionIndex in range(len(religionGroup)):
            if religionIndex == 0 and selectedReligionFamily != 'indian' \
            and selectedReligionFamily != 'pagan':
                menuReligionOptions.append(religionGroup[religionIndex] + ' *')
            else:
                menuReligionOptions.append(religionGroup[religionIndex])

    explainAstro = ['\n', 'An asterisk denotes the non-heretical,', \
    'or "primary", branch of the religion.\n']

    for astro in explainAstro:
        print(astro.center(80))

    selectedRelgion = pyip.inputMenu(menuReligionOptions, numbered = True, lettered = False)
    if selectedRelgion[-1] == '*':
        return selectedRelgion[0:-2]
    else:
        return selectedRelgion
