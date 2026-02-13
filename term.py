from blessed import Terminal
term = Terminal()

class pcs: # buncha colors for the script
    clear = term.normal
    grey = term.bright_black
    mint = term.mediumspringgreen #(to use once.)
    indent = term.mediumpurple('>> ')

def inputcheck():
    inputvar = input()
    if inputvar.replace('/', '') =='help': #checks if you ask for help
        print(f'\n{pcs.indent}EUTS2-MU (or Euro Truck Simulator 2 Music Utility for long) is a utility used\n{pcs.indent}to rename files to their title made for the radio in Euro Truck Simulator 2 but also for\n{pcs.indent}whatever you want too!\n{pcs.indent}Here\'s a list of the commands and what they do.\n{pcs.indent}ps, you don\'t need to use a /')
        print(f'\n{pcs.indent}/help           Opens this menu.\n{pcs.indent}/extrahelp      More technical stuff\n{pcs.indent}/quit, /exit    Exits this code.\n{pcs.indent}/runmain        Takes a replacelist, a optional replace, and the path to the folder containing the music seperated by commas. (like runmain d, (musicpath)\n') #and (hopefully) helps.
        inputcheck()
    if inputvar.replace('/', '') == 'extrahelp':
        print(f'\n{pcs.indent}Welcome. So, here\'s a list of info.\n{pcs.indent}replacelist: So, Windows has certain characters that can\'t be used in a file name, \n{pcs.indent}and if I say for it to use say, a \\ it will through a error and crash the code.\n{pcs.indent}So, we add a list including all the characters we can\'t have seperated by spaces (eg,/ \\ < >)\n{pcs.indent}And, other OSes might block different characters\n{pcs.indent}(after all, not all OSes are Windows clones.) so, you can use different lists!\n{pcs.indent}And that\'s what a replacelist is!\n\n{pcs.indent}replace: Well, what will you replace the \\ with?\n')
        inputcheck()
    elif inputvar.replace('/', '') in ('quit', 'exit'): #quiting
        print(f'{pcs.indent}Quitting...')
        exit()
    elif inputvar.replace('/', '') in ('die.', 'die', 'kys'):
        print(f'{pcs.indent}*sigh*\n{pcs.indent}Quitting...')
        exit()
    elif inputvar.split(' ')[0].replace('/', '').replace(',', '') == 'runmain': # and the main bit
        valnum = inputvar.count(',') +1
        values = inputvar.split(maxsplit=valnum)
        print(values)
        if valnum > 3 or valnum < 2:
            print(f'{pcs.indent}Expected 2 or 3 values, got {valnum}.\n{pcs.indent}pss hey, make sure to seperate your values with commas.')
            inputcheck()
        else:
            if valnum == 2:
                print('One sec...')
                import renamer
                renamer.main(values[1].replace(',',''), '', values[-1].replace('"',''))
            elif valnum == 3:
                print('One sec...')
                import renamer
                renamer.main(values[1].replace(',',''), values[2], values[-1].replace('"',''))
        print('you good :thumbs_up:')
    else:
        print('No command triggered.')
        inputcheck()

print(f'{pcs.indent}Welcome to{pcs.mint} EUTS2-MU {pcs.grey}(i know, bad name.)\n'
     +f'{pcs.indent}What would you like to do?\n{pcs.indent}ps: say "help" for help.\n') # the start text

inputcheck()