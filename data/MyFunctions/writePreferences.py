# functions related to writing to preferences.py


def writePreferences(file_path, new_width, new_height, new_font, new_font_size, new_tooltips, new_dev):
    # converting all inputs to string
    array = [new_width, new_height, new_font, new_font_size, new_tooltips, new_dev]
    array = list(map(str, array))

    preferences = open(file_path, 'w')
    preferences.writelines([
        '\n# preferences \n',
        'width = ' + array[0] + '\n',
        'height = ' + array[1] + '\n',
        'font = "' + array[2] + '"\n',
        'font_size = ' + array[3] + '\n',
        'tooltips = ' + array[4] + '\n',
        'dev = ' + array[5] + '\n',
    ])
    preferences.close()


def writeDefaultPreferences():
    writePreferences('../MyVariables/preferences.py', 1280, 720, 'Helvetica', 12, True, True)


if __name__ == '__main__':
    writeDefaultPreferences()
    print(open('../MyVariables/preferences.py', 'r').read())
