from tqdm import tqdm
from mutagen.oggvorbis import OggVorbis
import mutagen.mp3
import mutagen.flac
import os

mp3flactable = { #list so i can use mp3 tag names for flacs
    'TIT2': 'TITLE', #and oggs
    'TPE1': 'ARTIST',
    'TPE2': 'ALBUMARTIST',
    'TALB': 'ALBUM'}


def main(list, replace, musicpath):

    counter = 0
    for x in os.listdir(musicpath):
        counter = counter + 1
    print(counter)

    for item in tqdm(os.listdir(musicpath), desc='Naming...', unit='songs'):
        def gettag(key:str, file:str):
            if item.rsplit('.')[-1] == 'mp3': #splits it on the '.' and checks the last one if its mp3 or flac
                file = mutagen.mp3.Open(file)
                name = file.get(key)
                try:
                    return name
                except TypeError:
                    tqdm.write('uh oh')
                    return 'Unknown'
            elif item.rsplit('.')[-1] == 'flac': # same as above
                file = mutagen.flac.Open(file)
                name = file.get(mp3flactable[key])
                try: #trys to return it
                    return name[0]
                except TypeError: #but it might not work.
                    tqdm.write('ruhroh smth went wrong.')
                    return 'Unknown'
            elif item.rsplit('.')[-1] == 'ogg':
                file = OggVorbis(file) # ayyy ogg.
                name = file.tags.get(mp3flactable[key])
                try:
                    return name[0]
                except TypeError:
                    tqdm.write('ruhroh smth went wrong.')
                    return 'Unknown'

        def charremove(string, blist, replace): #makes sure theres no bad chars so micheal doesn't crash the script
            final = [string]
            if blist in ('d', '', ['\\', '/', ':', '?', '"', '<', '>', '|']): #checks if you say default
                dlist = ['\\', '/', ':', '?', '"', '<', '>', '|'] #instead of the list but still works for custom lists
            else:
                dlist = blist.split(' ')
            for l in string: # goes through the string
                for i in dlist: # then the list
                    if i in l: # and if the char in the string is the same as the list then:
                        tqdm.write(f'Uh oh, {l} was found in {string}.\nReplacing...') #replaces it.
                        final[0] = final[0].replace(i, replace)
            return final[0] #im sure i can do it better but tbh this is all i came up with.
#and i HATE debugging it.
        filetype = item.rsplit('.')[-1] # same as gettag()
        tqdm.write(f'{filetype} file') #prints it to be nice :)
        if filetype in ('flac', 'mp3', 'ogg'): #makes sure it's a mp3 or flac
            title = gettag('TIT2', f'{musicpath}/'+item) #and gets the tags,
            artist = gettag('TPE1', f'{musicpath}/'+item) #makes sure they are good,
            newname = charremove(f'{title} - {artist}.{filetype}', list, replace)
            os.rename(f'{musicpath}/{item}', f'{musicpath}/{newname}') # and renames it to Title - Artist
            tqdm.write(f'Renamed {item} to {newname}')
        else:
            tqdm.write('Sorry, at the moment EUTS2-MU only supports .mp3 and .flac')