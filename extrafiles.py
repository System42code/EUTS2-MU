#        this is for extra utilites that would be too long to be in the main files.
#                                you can mostly just ignore this.

#                                        -- functions --

def readsettings(section, setting):
    import configparser
    config = configparser.ConfigParser()
    config.read('settings.ini')

    return config[section][setting]
def changesettings(section, setting, value):
    import configparser
    config = configparser.ConfigParser()
    config.read('settings.ini')
    config[section] = {setting : value}

    with open('settings.ini', 'w') as configfile:
        config.write(configfile)
    print(config['Finding']['recursive_search'])
changesettings('', '')