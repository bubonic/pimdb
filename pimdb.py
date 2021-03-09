#!/usr/bin/python3

from imdb import IMDb
import sys
import textwrap 
import random
from bs4 import BeautifulSoup
import urllib.request
import argparse
import os
from os import path

def getBasicTitleInfo(the_movie, wrapper):
    
    try: 
        print("\n")
        print("[img]%s[/img]\n" % the_movie['full-size cover url'])
        print("[size=3][color=blue]Title: %s[/color][/size]" % the_movie['title'])
        print("[color=DarkSlateBlue]Rating:[/color] [color=red]%s[/color] - [color=navy]%s votes[/color]" % (the_movie['rating'], the_movie['votes']))
        print("[color=DarkSlateBlue]Runtime:[/color] %s minutes" % the_movie['runtimes'][0])
        print("[color=DarkSlateBlue]Country:[/color] %s" % the_movie['countries'][0])
        print("[color=DarkSlateBlue]Languages:[/color] ", end=' ')
        for lang in the_movie['languages']:
            print(lang, end=', ')
        print("\n[color=DarkSlateBlue]Original Air Date:[/color] %s" % the_movie['original air date'])
        print("[color=DarkSlateBlue]Directors:[/color] ", end=' ')
        for director in the_movie['directors']:
            print(director['name'], end=', ')
    except:
        pass
    
    
    try:
        print("\n[color=DarkSlateBlue]Cinematographers: [/color]", end=' ')
        for tographer in the_movie['cinematographers']:
            print(tographer['name'], end=', ')
    except:
        pass
    
    try:     
        print("\n[color=DarkSlateBlue]Writers: [/color]", end=' ')
        writerText = ' '
        w = textwrap.TextWrapper(width=137)
        for writer in the_movie['writers']:
            #print(writer, end=', ')
            writerText = writerText + str(writer) + ', '
        writerList = w.wrap(writerText)
        for writ in writerList:
            print(writ)
    except:
        pass
    
    try: 
        print("[color=DarkSlateBlue]Producers: [/color]", end=' ')
        for prod in the_movie['producers']:
            print(prod, end=', ')
    except:
        pass
    
    try: 
        print("\n[color=DarkSlateBlue]Production Company: [/color]", end=' ')
        for prod in the_movie['production companies']:
            print(prod, end=', ')
    except:
        pass
    
    try:       
        print("\n[color=DarkSlateBlue]Genres: [/color]", end=' ')
        for genre in the_movie['genres']:
            print(genre, end=', ')
    except:
        pass
    
    try:    
        print("\n[color=DarkSlateBlue]AKAs: [/color]", end=' ')
        akaText = ' '
        for aka in the_movie['akas']:
            #print(aka, end=', ')
            akaText = akaText + str(aka) + ', '
        akaList = w.wrap(akaText)
        for aka in akaList:
            print(aka)
    except:
        pass

def getPlotInfo(ia, the_movie, imdbTT, wrapper):
    the_movie2 =' '
    plot = max(the_movie['plot'], key=len).lstrip(' ')
    plot = plot.split("::")[0]
    plotList = wrapper.wrap(text=plot)
    print("\n\n[b][color=DarkRed][size=4]PLOT[/size][/color][/b]\n" )
    for s in plotList:
        print(s)
    
    try:
        the_movie2 = ia.get_movie(imdbTT, info=['critic reviews', 'external reviews', 'goofs', 'keywords', 'locations', 'reviews', 'quotes', 'technical', 'synopsis', 'awards', 'recommendations', 'photographs', 'metascore' ])
        the_movie2.infoset2keys
    except Exception as e:
        print(str(e))
    
    '''
    print(sorted(the_movie2.keys()))
    print(the_movie2['synopsis'])
    print("Continue (y/n): ", end='')
    answer = input()
    if answer.upper() == "N":
        exit
    else:
        exit
    '''
    j=1
    try:
        awards = the_movie2['awards']
        #print(the_movie2['awards'])
        print("\n[b][color=DarkSlateBlue]Awards: [/color][/b]")
        for award in the_movie2['awards']:
            #print(award)
            if j < 7:
                try:
                    notes = award['notes']
                except:
                    notes = ''
                    pass
                try:
                    category = award['category']
                except:
                    category = ''
                    pass
                try:
                    actor = award['to'][0]
                    name = actor['name']
                except:
                    name = ''
                    pass
                print("%s.) [b][color=black]%s[/color][/b], %s, %s, %s, %s, %s " % (j,award['award'], award['year'], award['result'], notes, category, name))
                j += 1
            else:
                break
    except:
        pass
    
    try:
        metascore = the_movie2['metascore']
        print("\n[b][color=DarkSlateBlue]Metascore: [/color][/b]%s" % metascore, end=' ')
    except:
        pass
    
    j=0
    try: 
        recommendations = the_movie2['recommendations']
        if recommendations:
            print("\n[b][color=DarkSlateBlue]Recommendations: [/color][/b]", end=' ')
            recommendText = ' '
            for r in recommendations:
                if j < 6:
                    recommendText = recommendText + "[i]" + str(r) + "[/i], "              
                    #print("[i]%s[/i]" % r, end=', ')
                    j += 1
                else:
                    break
            w = textwrap.TextWrapper(width=159)
            rList = w.wrap(recommendText)
            for r in rList:
                print(r)
            
    except:
        pass
    
    try:
        photos = the_movie2['photographs']
        if photos:
            print("\n\nPhotos: ")
            for photo in photos:
                print("\n %s" % photo)
    except:
        pass
    
    #ia.update(the_movie2,'all')
    
    
    try: 
        synopsis = the_movie2['synopsis'][0]
        synopList = wrapper.wrap(text=synopsis)
        print("\n\n[b][color=orange][size=3]Synopsis[/size][/color][/b]\n" )
        for s in synopList:
            print(s)
    except:
        pass
    
    
    try:
        if the_movie2['keywords']:
            j=0
            keywordText = ' '
            print("\n\n[color=black][b]Keywords:[/color][/b] ", end=' ')
            for keyword in the_movie2['keywords']:
                if j < 15:
                    keywordText = keywordText + ', ' + str(keyword)
                    #print(keyword, end=', ')
                    j += 1
                else:
                    break
            w = textwrap.TextWrapper(width=137)
            kList = w.wrap(keywordText)
            
            for keyword in kList:
                print(keyword)
    except:
        pass
            
    
    try: 
        j=0
        locationText = ' '
        if the_movie2['locations']:
            print("\n\n[color=black][b]Locations: [/b][/color]", end=' ')
            for location in the_movie2['locations']:
                if j < 6:
                    locationText = locationText + ', ' + str(location)
                    j += 1
                    
                else:
                    break
            locList = w.wrap(locationText)
            
            for loc in locList:
                print(loc)
    except:
        pass
        
    try:
        wrapper = textwrap.TextWrapper(width=137)
        j=1
        if the_movie2['goofs']:
            print("\n\n[color=red][size=2]Goofs:[/size][/color] " )
            for goof in the_movie2['goofs']:
                if j < 6:
                    goofCat = goof['category']
                    goofText = goof['text'].replace('\\', '').rstrip()
                    goofText = goofCat + ": " + goofText
                    goofTextList = wrapper.wrap(text=goofText)
                    print("%s.) " % (j), end=' ')
                    for s in goofTextList:
                        print(s)
                                                
                    j += 1
                else:
                    break 
        
    except:
        print()
    
    
    try: 
        j=1
        wrapper = textwrap.TextWrapper(width=137)
        if the_movie2['quotes']:
            print("\n[b][size=3][color=magenta]Quotes:[/color][/size][/b] " )
            for quote in the_movie2['quotes']:
                for q in quote:
                    if j < 7:
                        q = q.replace('\\', '')
                        qList = wrapper.wrap(text=q)
                        print("%s.)" % j, end=' ')
                        for s in qList:
                            print(s)
                        j += 1
                    else:
                        break
        
    except:
        print()
    
    return the_movie2
  
def getTechSpecs(the_movie2):
    try: 
        print("\n[color=indigo]Technical Information: [/color]")
        print("Runtime: %s" % the_movie2['technical']['runtime'][0])
        print("Sound Mix: %s" % the_movie2['technical']['sound mix'][0])
        print("Color: %s" % the_movie2['technical']['color'][0])
        print("Aspect Ratio: %s" % the_movie2['technical']['aspect ratio'][0])
        print("Film: %s" % the_movie2['technical']['negative format'][0])
    
    except:
        pass


def getCastInfo(the_movie):
    cast = []
    roles = []

    aText="Actor"
    rText="Role"
    space=' '
    castINFO = the_movie.get("cast")
    
    k=0
    for member in castINFO: 
        cast.insert(k, member['name'])
        roles.insert(k, member.currentRole)  
        k += 1
        
    k = 0
    
    maxCastLen = len(max(cast, key=len))
    maxCastChars = maxCastLen + 10 
    
    print("\n\n")
    print("[b][size=3]%-*s%s[/size][/b]" %(maxCastLen+23, aText, rText))
    #print("[b][size=2]%s  \t\t\t %s[/size][/b]" %(aText, rText))
    print("[pre]-----------" + maxCastLen*space + "----------")
    
    for member in cast:
        NumOfSpaces = maxCastChars - len(member) 
        print("%s%s - %s"  % (member,NumOfSpaces*space,roles[k]), end='\n')
        #print("%s \t\t\t-  %s" % (member, roles[k]), end='\n')
        k += 1
        #print()
        #print("ACTOR: %s \t\t - %s" % (cast[k], roles[k]))
    # show all information sets that can be fetched for a movie
    print("[/pre]")
 
def getThreeRandomReviews(the_movie2):
    randomReview = []
    print("\n")
    try: 
        wrapper = textwrap.TextWrapper(width=145)
        k=0
        for j in range(3):
            print("[b][color=SlateGray][size=3]Review:[/size][/color][/b]")
            r = random.randint(0,len(the_movie2['reviews'])-1)
            while 1 == 1:
                if r in randomReview:
                    r = random.randint(0,len(the_movie2['reviews'])-1)
                    continue
                else:
                    randomReview.insert(k, r)
                    k += 1
                    break
            review =  the_movie2['reviews'][r]['content']
            reviewList = wrapper.wrap(text=review)
            for s in reviewList:
                print(s)
            print("[i]Date: %s[/i]" % the_movie2['reviews'][r]['date'])
            print("\n\n")
    except:
        print()
        
def dlPosters(tt, the_movie, posters):
    imdbTT = tt
    URL="https://www.imdb.com/title/tt" + imdbTT +"/mediaindex/"
    web = urllib.request.urlopen(URL)
    HTML = web.read()
    
    web.close()
    
    soup = BeautifulSoup(HTML, features="html.parser")
    block = soup.find('div', {'class' : 'media_index_thumb_list'})
    imgBlocks = soup.find_all('img')
    
    headerRow = soup.find_all('div', {'class' : 'desc' })[0]
    numPhotos = int(headerRow.getText().split(' ')[-2])
    
    if numPhotos > 48:
        pages = int(int(numPhotos) / int(48)) + 1
        x = 2
        print("Number of pages: %s" % pages)
        while x <= pages:
            URL="https://www.imdb.com/title/tt" + imdbTT +"/mediaindex?page=" + str(x)
            web = urllib.request.urlopen(URL)
            HTML = web.read()
            soup = BeautifulSoup(HTML, features="html.parser")
            block = soup.find('div', {'class' : 'media_index_thumb_list'})
            imgBlocks2 = soup.find_all('img')
            for img in imgBlocks2:
                imgBlocks.append(img)
            x += 1
    
    
    web.close()
    
    k=0
    
    print("Number of Posters: %s" % numPhotos)
    
    if not posters:
        print("Would you like to download the posters (y/n):", end=' ')
        option=input()
    else:
        option = "Y"
    
    
    if option.upper() == "Y":
        parentDir = the_movie['title'].replace(' ', '').replace('/', '')
        posterDir = 'Posters' 
        cwd = os.getcwd()
        if not path.exists(parentDir):
            os.mkdir(parentDir)
        os.chdir(parentDir)
        if not path.exists(posterDir):
            os.mkdir(posterDir)
        os.chdir(posterDir)
        for img in imgBlocks:
            if k < numPhotos: 
                urlPre = img['src'].split('._')[0]
                url = urlPre + ".jpg"
                file_name = "Poster-" + str(k) + ".jpg"
                file_path = path.join(cwd, parentDir, posterDir, str(file_name))
                if path.isfile(path.abspath(file_path)):
                    print("File Exists... Skipping...")
                    k += 1
                    continue
                try: 
                    u = urllib.request.urlopen(url)
                    f = open(file_name, 'wb')
                except (OSError, urllib.error.URLError, Exception) as e:
                    print("Error retrieving %s-th poster... (%s)" % (k, str(e)))
                    print("Skipping....")
                    k += 1
                    continue 
                meta = u.info()
                file_size = int(meta.get("Content-Length"))
                print("Downloading: %s Bytes: %s" % (file_name, file_size))
                
                file_size_dl = 0
                block_sz = 8192
                while True:
                    buffer = u.read(block_sz)
                    if not buffer:
                        break
                
                    file_size_dl += len(buffer)
                    f.write(buffer)
                    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
                    status = status + chr(8)*(len(status)+1)
                    print(status)
                k += 1
            else: 
                break
        try:
            f.close()
        except Exception as e:
            print(str(e))
    
    else:
        print("Goodbye.")
    os.system("cd " + parentDir + '/' + posterDir)
#imdbTT=sys.argv[1].split('tt')[-1].split('/', 1)[0]

def main():
    
    parser = argparse.ArgumentParser(description="PyIMDB - Get a range of IMDB info for title")
    parser.add_argument('-p', '--posters', action='store_true', default=False, help='Automatically Download all IMDB Posters without being prompted')
    parser.add_argument('imdburl', metavar='url', nargs='+')
    
    args = parser.parse_args()
    TT=args.imdburl[0].split('tt')[-1].split('/', 1)[0]
    ia = IMDb()
    the_movie= ia.get_movie(TT)
    
    wrapper = textwrap.TextWrapper(width=145) 
    
    getBasicTitleInfo(the_movie, wrapper)
    the_movie2 = getPlotInfo(ia, the_movie, TT, wrapper)
    getTechSpecs(the_movie2)
    getCastInfo(the_movie)
    getThreeRandomReviews(the_movie2)
    
    if args.posters:
        dlPosters(TT, the_movie, True)
    else:
        dlPosters(TT, the_movie, False)
        

if __name__ == '__main__':
    main()