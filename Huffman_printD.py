# ALGRORITHME DE HUFFMAN : COMPRESSION DE DONNEES

def TableDeFrequence (texte):

    print('')
    print('------------------------------------------')
    print('TableDeFrequence : début')
    print('')
    print('texte = ALACAZAM')
    print('')

    table={}
    for c in texte:
        if c in table:
            table[c]=table[c]+1
            print(table)
        else:
            table[c]=1
            print(table)

    print('')
    print('TableDeFrequence : fin')
    print('------------------------------------------')
    print('')
    print('')
    print('')

    return table





def Arbre(table):

    print('')
    print('------------------------------------------')
    print('Arbre : début')
    print('')

    if table=={}:
        return {}
    else:
        import operator
        tas = []
        for k in table:
            tas.append((table[k], k))
        tas = sorted(tas)
        print ('1. tas trié : ',tas)
        print('')

    # construction de l'arbre, un tuple correspond à un noeud

        while len(tas) >= 2:
            (freq1, LettreGauche) = tas[0]
            del tas[0]
            (freq2, LettreDroite) = tas[0]
            del tas[0]
            SF = freq1+freq2
            Noeud = {0: LettreGauche,1: LettreDroite}
            tas.append((SF, Noeud))
            tas.sort(key=operator.itemgetter(0))
            print ('2. nouveau tas trié : ',tas)

    print('')
    arbre = tas[0][1]
    print('Arbre = ',arbre)

    print('')
    print('Arbre : fin')
    print('------------------------------------------')
    print('')
    print('')
    print('')

    return arbre

def code_huffman(arbre):

    code = {}
    ParcoursArbre(arbre,'',code)

    print('')
    print('')
    print('code final = ',code)
    print('')
    print('')
    print('Parcours de larbre : fin')
    print('------------------------------------------')
    print('')
    print('')
    print('')

    return code



def ParcoursArbre(arbre, historique, code):

    print('')
    print('------------------------------------------')
    print('parcours de l arbre: début')
    print('')
    print('')
    print('préfixe = ', historique)
    for k in arbre:
        print('k =', k)
        print('arbre = ', arbre)
        print('')


        if isinstance(arbre[k],str) == True:
            print('La valeur de la clef k est un caractere')
            ClefCaractere = historique+str(k)
            code[ClefCaractere] = arbre[k]
            print('caractere = ',code[ClefCaractere])
            print('on lui associe donc son code : ')
            print('code actuel = ', code)
            print('')
        else:
            print('la valeur de la clef k n est pas un caractere,')
            print('on relance donc la fonction en prenant pour nouvel arbre le dictionnaire de la clef k')
            NouveauPrefixe = historique+str(k)
            ParcoursArbre(arbre[k],NouveauPrefixe,code)





def encodage(texte, code):
    print('')
    print('------------------------------------------')
    print('Encodage : début')
    print('')

    print('texte = ',texte)
    print('')
    print('code = ',code)

    codeInverse = DictionnaireInverse(code)
    print('code inverse = ',codeInverse)
    print ('')
    texte_binaire = ''
    compteur = 1
    for c in texte:
        print('index de la lettre dans le texte : ',compteur,' lettre = ',c)
        texte_binaire = texte_binaire + codeInverse[c]
        print('texte binaire actuel : ',texte_binaire)
        compteur+=1
        print('')
    print('texte binaire final :',texte_binaire)

    print('')
    print('encodage : fin')
    print('------------------------------------------')
    print('')
    print('')
    print('')

    return texte_binaire


def DictionnaireInverse(d):

    print('')
    print('------------------------------------------')
    print('DictionnaireInverse : début')
    print('')

    D_inverse = {}
    print(D_inverse)
    print(d)
    for k in d:
        print ('k = ',k)
        valeur = d[k]
        print ('valeur = ',valeur)
        print('')
        if valeur not in D_inverse:
            print('la valeur n est pas dans le dictionnaire inverse')
            D_inverse[valeur] = k
            print('la valeur de la clef',valeur, 'devient donc',k)
            print('')
        else:
            print('la valeur est deja dans le dictionnaire inverse')
            D_inverse[valeur].append(k)
            print('D_inverse')
            print('')

    print(D_inverse)
    print('')
    print('DictionnaireInverse : fin')
    print('------------------------------------------')
    print('')

    return D_inverse




def decodage(code, texte_binaire):

    print('')
    print('------------------------------------------')
    print('Décodage : début')
    print('')

    print('code = ' ,code)
    print('texte binaire =',texte_binaire)
    print('')

    texte = ''
    tampon = ''
    for b in texte_binaire:
        tampon = tampon+b
        print ('code = ',tampon)
        if tampon in code:
            print('ce code existe et correspond à',code[tampon])
            texte = texte+code[tampon]
            print('texte actuel : ' ,texte)
            tampon = ''
            print('')
    print('texte alphabétique final : ',texte)

    print('')
    print('decodage : fin')
    print('------------------------------------------')
    print('')
    print('')
    print('')

    return texte

def TexteAleatoire(n) :
    import random
    Alphabet = "abcdefghijklmnopqrstuvwxyz "
    texte = ""
    for k in range(n):
        texte  = texte + Alphabet[random.randint(0, len(Alphabet) - 1)]
    return texte

import random
NombreAleatoire = (random.randint(1, 1000))
TexteAleatoire = TexteAleatoire(20)


te = 'ALLEZ LES BLEUS'
t = TableDeFrequence(te)
a = Arbre(t)
c = code_huffman(a)
e = encodage(te,c)
d = decodage(c,e)


if len(te) == 0 :
    l= 0
else :
    l = len(e)/len(te)

NbitASCII = 8 * len(te)

if len(te) == 0 :
    TC = 0
else :
    TC = (1 - (len(e) / NbitASCII)) * 100


def H(t):
    import math
    H = 0
    for k in t :
        p1 = t[k]
        p2 = len(te)
        p = p1/p2
        H = H + p*math.log(1/(p),2)
    return H

H = H(t)




print('')
print('')
print('--------------------------------------------------')
print('En résumé : ')
print('')

print('Texte alphabétique :          ',te)
print('Table de fréquence :          ',t)
print('Arbre binaire :               ',a)
print('Codage :                      ',c)
print('Texte binaire :               ',e)
print('Texte alphabétique décodé :   ',d)
print('')
print('Taux de compression :              ',TC,'%')
print('Entropie =                         ',H)
print('longueur moyenne de la séquence =  ',l)
print('--------------------------------------------------')