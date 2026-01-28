from blessed import Terminal
term = Terminal()

class pcs: # buncha colors for the script
    clear = term.normal
    grey = term.bright_black
    mint = term.mediumspringgreen #(to use once.)
    indent = term.mediumpurple('>> ')

end = False
def inputcheck():
    inputvar = input()
    if inputvar.replace('/', '') =='help': #checks if you ask for help
        print(f'\n{pcs.indent}EUST2-MU (or Euro Truck Simulator 2 Music Utility for long) is a utility used\n{pcs.indent}to rename files to their title made for the radio in Euro Truck Simulator 2 but also for\n{pcs.indent}whatever you want too!\n{pcs.indent}Here\'s a list of the commands and what they do.\n{pcs.indent}ps, you don\'t need to use a /')
        print(f'\n{pcs.indent}/help           Opens this menu.\n{pcs.indent}/extrahelp      More technical stuff\n{pcs.indent}/quit, /exit    Exits this code.\n{pcs.indent}/runmain        The purpose of this code!\n') #and (hopefully) helps.
        inputcheck()
    if inputvar.replace('/', '') == 'extrahelp':
        print(f'\n{pcs.indent}Welcome. So, here\'s a list of info.\n{pcs.indent}replacelist: So, Windows has certain characters that can\'t be used in a file name, \n{pcs.indent}and if I say for it to use say, a \\ it will through a error and crash the code.\n{pcs.indent}So, we add a list including all the characters we can\'t have seperated by spaces (eg,/ \\ < >)\n{pcs.indent}And, other OSes might block different characters\n{pcs.indent}(after all, not all OSes are Windows clones.) so, you can use different lists!\n{pcs.indent}And that\'s what a replacelist is!\n\n{pcs.indent}replace: Well, what will you replace the \\ with?\n')
        inputcheck()
    elif inputvar.replace('/', '') in ('quit', 'exit'): #quiting
        print(f'{pcs.indent}Quitting...')
        globals()['end'] = True
        return
    elif inputvar.replace('/', '') in ('die.', 'die', 'kys'):
        print(f'{pcs.indent}*sigh*\n{pcs.indent}Quitting...')
        globals()['end'] = True
        return
    elif inputvar.split(' ')[0].replace('/', '') == 'runmain': # and the main bit
        values = inputvar.split(' ')
        valnum = str(values).count(',')
        if valnum > 3 or valnum < 2:
            print(f'{pcs.indent}Expected 2 or 3 values, got {valnum}.')
            inputcheck()
        else:
            print('One sec...')
            import renamer
            if valnum == 2:
                renamer.main(values[1], '', values[2]+'\\')
            elif valnum == 3:
                renamer.main(values[1], values[2], values[3]+'\\')
    else:
        if end == True:
            return
        print(inputvar)
        print('No command triggered.')
        inputcheck()

print(f'{pcs.indent}Welcome to{pcs.mint} EUST2-MU {pcs.grey}(i know, bad name.)\n'
     +f'{pcs.indent}What would you like to do?\n{pcs.indent}ps: say "help" for help.\n') # the start text

inputcheck()
