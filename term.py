from blessed import Terminal
term = Terminal()

class pcs: # buncha colors for the script
    clear = term.normal
    grey = term.bright_black
    mint = term.mediumspringgreen #(to use once.)
    indent = term.mediumpurple('>> ')

def inputcheck():
    inputvar = input()
    if inputvar in ('/help', 'help'): #checks if you ask for help
        print('\n' \
             f'{pcs.indent}ETS2MU (or Euro Truck Simulator 2 Music Utility for long) is a utility used\n' \
             f'{pcs.indent}to rename files to their title made for the radio in ETS2 but also for\n' \
             f'{pcs.indent}whatever you want too!\n' \
             f'{pcs.indent}Here\'s a list of the commands and what they do.\n' \
             f'{pcs.indent}ps, you don\'t need to use a /')
        print('\n' \
            f'{pcs.indent}/help           Opens this menu.\n' \
            f'{pcs.indent}/quit, /exit    Exits this code.\n' \
            f'{pcs.indent}/runmain        The purpose of this code!\n') #and (hopefully) helps.
        inputcheck()
    elif inputvar in ('quit', '/quit', 'exit', '/exit'): #quiting
        print(f'{pcs.indent}Quitting...')
        return
    elif inputvar in ('die.', 'die', '/die', 'kys'):
        print(f'{pcs.indent}*sigh*\n'+f'{pcs.indent}Quitting...')
    elif inputvar in ('runmain', '/runmain'): #and the main bit
        print(f'{pcs.indent}One sec...')
        import renamer
        print(f"{pcs.indent}All right, what is your replace list? (use d if you don't know.)")
        rlist = input()
        print(f"{pcs.indent}And what will be your replace? (continue if you don't know.)")
        replace = input()
        print(f"{pcs.indent}And where is your music? (use the path to it like C:\\thing)")
        path = input()+'/'
        renamer.main(rlist, replace, path)
    else:
        print('No command triggered.')
        inputcheck()

print(f'{pcs.indent}Welcome to{pcs.mint} ETS2MU {pcs.grey}(i know, bad name.)\n'
     +f'{pcs.indent}What would you like to do?\n{pcs.indent}ps: say "help" for help.\n') # the start text

inputcheck()
