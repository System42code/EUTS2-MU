#        this is for extra utilites that would be **way** too long to be in the main files.
#                              and also where the settings are stored.
#                                 you can mostly just ignore this.

#                                         -- settings --

no  = 'i got nothing to put (right now...) so yeah.'

#                                        -- functions --

def quotechecker(inputvar:str):   # when you input something with quotes and spaces, some work needs to happen.
    print('yeah you made it!')
    splitvar    = inputvar.split()
    illegallist = []
    returnum    = ''

    if "'" in inputvar: # sees whats wrong
        illegalchar = "'"
        print(f'{illegalchar} in inputvar.')
    if '"' in inputvar:
        illegalchar = '"'
        print(f'{illegalchar} in inputvar.')
    for e in range(len(splitvar)):
        if illegalchar in splitvar[e]:
            illegallist.append(e)
            print(f'HERE! {str(illegallist)}')
    iternum = illegallist[0]
    while iternum < illegallist[-1] - 1:
        iternum = iternum+1
        illegallist.insert(-1, iternum)
    iternum = 0
    for i in illegallist:
        returnum = returnum+splitvar[illegallist[iternum]]+' '
        iternum = iternum+1
    return returnum