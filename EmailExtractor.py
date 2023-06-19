#Email extractor 

def extractEmails(aStr: str):
    addresses= ''
    
    #['Musil', 'Radim', 'radim.musil@o2.cz;', 'Slezák', 'Pavel', 'pavel.slezak@o2.cz;', 'Kizur', 'Michael', 'michael.kizur@o2.cz;', 'Novotný', 'Zdeněk', 'zdenek.novotny@o2.cz;', 'Chlumecký', 'Petr', 'petr.chlumecky@o2.cz']
    plainAddresses= aStr.split(' ')
    
    for x in plainAddresses:
        #'radim.musil@o2.cz;'
        if x.find('@')>-1:
            addresses +=x

    #'radim.musil@o2.cz;pavel.slezak@o2.cz;michael.kizur@o2.cz;zdenek.novotny@o2.cz;petr.chlumecky@o2.cz'
    return addresses

if __name__ ==  '__main__':
    #Musil Radim radim.musil@o2.cz; Slezák Pavel pavel.slezak@o2.cz; Kizur Michael michael.kizur@o2.cz; Novotný Zdeněk zdenek.novotny@o2.cz; Chlumecký Petr petr.chlumecky@o2.cz
    print(extractEmails(input('Input a plain text with email addresses: ')))

