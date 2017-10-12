# ALGRORITHME DE HUFFMAN : COMPRESSION DE DONNEES

def TableDeFrequence (texte):
    """
 Construction d'une table de fréquences
    @ Entrée: un texte
    @ type: string
    @ Sortie: un dictionnaire qui pour chaque caractère présent dans le texte lui associe sa fréquence
    @ type: dict
    """

    table={}                                  # crée un dictionnaire vide
    for c in texte:                           # pour chaque caractère dans le texte
        if c in table:                        # si le caractère est déjà dans le texte
            table[c]=table[c]+1               # la valeur de la clef [nom du caractère] est incrémanté de 1
        else:
            table[c]=1                        # sinon crée la clef [nom du caractère] et l'assimile a la valeur = 1
    return table                              # cette fonction crée une clef pour chaque caractère different




def Arbre(table):
    """
Construction d'un arbre de Huffman
    @ Entrée: un dictionnaire (la table de fréquence) . les clefs sont les caractères, les valeurs sont leur fréquence
    @ type: dict
    @ Sortie: un dictionnaire structuré sous forme d'arbre binaire. les feuilles sont les caractères
    @ type: dict
    """

    if table=={}:
        return {}
    else:
        tas = []
        for k in table:                          # transforme le dictionnaire de fréquences en liste de fréquences.
            tas.append((table[k], k))            # ce qui permet d'utiliser les index du type list
                                                 # cette liste est composée de couples de la forme (fréquence,caractère).
        tas = sorted(tas)                        # trie la liste par ordre croissant de fréquence


    # construction de l'arbre, un couple correspond à un noeud

        while len(tas) >= 2:                                 # arrêt à 1 car un arbre binaire ne contient qu'un seul noeud père
            (freq1, LettreGauche) = tas[0]
            del tas[0]                                       # supprime le couple de plus petite frequence du tas (car la tas est triée)
            (freq2, LettreDroite) = tas[0]
            del tas[0]                                       # supprime le nouveau couple de plus petite frequence du tas
            SF = freq1+freq2
            Noeud = {0: LettreGauche,1: LettreDroite}
            tas.append((SF, Noeud))                          # ajoute au tas le couple composé des sommes de frequences des plus 'petits' couples (index 1 du couple)
                                                             # et qui a chacune des 2 lettres associe leur placement dans l'arbre (fils gauche/droit) (index2 du couple)
            import operator
            tas.sort(key=operator.itemgetter(0))             # trie la liste par ordre croissant de fréquence (car certains tuples de la liste sont de la forme
                                                             # (int,dict) et d'autre de la forme (int,string)
                                                             # <!> le module operator permet donc de ne comparer que les premiers éléments du couple entre eux afin de les trier
                                                             # necessaire car python ne peut comparer un type dict et un type string

    arbre = tas[0][1]
    return arbre

#######################################################################################
# Les deux prochaines fonctions sont dépendantes l'une de l'autre

def ParcoursArbre(arbre):
    """
fonction qui associe à chaque caractere son code
        @ Entrée : un dictionnaire stucturé sous forme d'arbre binaire
        @ type: dict
        @ Sortie: dictionnaire du type clefs = code d'un caractere, valeur = ce caractere
           on a donc type(clef) = string, type(valeur) = string
        @ type: dict
          """
    code = {}
    SousParcours(arbre,'',code)        # parcours l'arbre en associant à chaque caractère son code
    return code


def SousParcours(arbre, pref, code):
    """
fonction permettant de parcourir l'arbre
<!> cette fonction ne fait que calculer de maniere recursive, elle ne renvoie rien, d'ou sa dépendance avec la fonction précédente
    @ Entrées:
    @ arbre : un dictionnaire stucturé sous forme d'arbre binaire
    @ type: dict
    @ pref : une chaîne de caractère initialement vide, dans la recursivité : enregistre le chemin pris pour arriver à un caractère
    @ type : string
    @ code : un dictionnaire initialement vide, dans la résurvité : enregistre les différents codes de chaque caractères
    @ type : dict

      """
    for k in arbre:                                           # pour k parcourant les CLEFS de l'arbre
        if isinstance(arbre[k], str) == True:                 # si la valeur de la clef k est une chaine de caractère
            ClefCaractere = pref + str(k)                     # le code de ce caractère est défini comme le chemin parcouru + l'endroit où l'on se situe
            code[ClefCaractere] = arbre[k]                    # le dictionnaire 'code' enregistre donc ce code
        else:                                                 # si la valeur de la clef k est un dictionnaire
            NoeudSuivant = arbre [k]                          # on se place dans le noeud suivant
            NouveauPrefixe = pref + str(k)                    # on enregistre le chemin prit dans l'arbre
            SousParcours(NoeudSuivant,NouveauPrefixe,code)    # on refais la même chose dans le nouveau noeud

# La fonction s'arrête lorsque tous les noeuds ont été explorés
# Fin de la dépendance
##############################################################################



def encodage(texte,code):
    """
fonction qui transforme le texte en texte binaire suivant la méthode de Huffman
    @ Entrées :
    @ texte : un texte
    @ type : string
    @ code : un dictionnaire du type clefs = code d'un caractère, valeur = ce caractere
             type(clefs) = string, type(valeur) = string
    @ type : dict

    @ Sortie: le texte binaire correspondant au texte alphabétique
    @ type: string
    """

    codeInverse = DictionnaireInverse(code)                         # inverse les clefs et les valeurs du dictionnaire de code
    texteBinaire = ''                                               # car on cherche a acceder aux clefs
    for k in texte:                                                 # pour une variable k parcourant chaque caractère du texte alphabétique
        texteBinaire = texteBinaire + codeInverse[k]                # ajoute le code de k au texte binaire (concatène les strings)
    return texteBinaire



def DictionnaireInverse(d):
    """
       fonction qui inverse les clefs et les valeurs d'un dictionnaire
        @ Entrée : un dictionnaire
        @ Type : dict
        @ Sortie : le même dictionnaire avec les clefs et valeurs inversées
        @ Type : dict (ou string si la fonction est utilisé dans un autre cadre que le code d'Huffman)
    """
    D_inverse = {}
    for k in d:                                 # pour k parcourant le dictionnaire
        valeur = d[k]
        if valeur not in D_inverse:             # si la valeur de la clef k n'est pas dans le dictionnaire inverse
            D_inverse[valeur] = k               # crée le dictionnaire inverse en associant les clefs aux valeurs et les valeurs aux clefs
        else :                                  # pas besoin de definir un else car toutes les valeurs sont différentes
            return 'deux valeurs du dictionnaire sont identiques'
    return D_inverse



def decodage(code, texteBinaire):
    """
fonction qui retranspose le texte binaire en son texte alphabétique d'origine
    @ Entrées :
    @ texteBinaire : le texte binaire résultant de la fonction encodage (suite de 0 et 1)
    @ type : string
    @ code : dictionnaire du type clefs = code d'un caractére, valeur = ce caractère
          type(clefs) = string, type(valeur) = string
    @ type : dict

    @ Sortie: le texte correspondant au texte binaire
    @ type: string
        """

    texte = ''
    clef = ''
    for k in texteBinaire:                      # pour une variable parcourant le texte binaire
        clef = clef+k                           # on construit une clef a partir du premier bit du texte binaire
        if clef in code:                        # on test si la clef appartient au dictionnaire representant le code
            texte = texte+code[clef]            # dans l'affirmative on ajoute au texte la lettre correspondante a la clef, sinon on ajoute le 2ème bit a la clef et on retest
            clef = ''                           # reinitialisation de la clef
    return texte




def CodeHuffman(texte):
    """
Fonction qui associe à un texte son texte binaire selon la méthode de Huffman
        @ Entree: un texte
        @ type: string
        @ Sortie: le texte en binaire
        @ type: string
        """

    t = TableDeFrequence(texte)
    a = Arbre(t)
    c = ParcoursArbre(a)
    e = encodage(texte, c)
    return e


def decodeHuffman(texte,texte_binaire):
    """
    Fonction qui associe à un texte binaire son texte d'origine selon la méthode d'Huffman
            @ Entrée: un texte binaire
            @ type: string
            @ Sortie: le texte correspondant
            @ type: string
            """

    t = TableDeFrequence(texte)
    a = Arbre(t)
    c = ParcoursArbre(a)
    d = decodage(c, texte_binaire)
    return d

def TexteAleatoire(n) :
    import random
    Alphabet = "abcdefghijklmnopqrstuvwxyz "
    texte = ""
    for k in range(n):
        texte  = texte + Alphabet[random.randint(0, len(Alphabet) - 1)]
    return texte

import random
NombreAleatoire = (random.randint(1, 1000))
TexteAleatoire = TexteAleatoire(NombreAleatoire)

texte = TexteAleatoire


def H(t):
    import math
    H = 0
    for k in t :
        p1 = t[k]
        p2 = len(texte)
        p = p1/p2
        H = H + p*math.log(1/(p),2)
    return H




t = TableDeFrequence(texte)
a = Arbre(t)
c = ParcoursArbre(a)
e = encodage(texte,c)
d = decodage(c,e)
H = H(t)

if len(texte) == 0 :
    l= 0
else :
    l = len(e)/len(texte)

NbitASCII = 8 * len(texte)

if len(texte) == 0 :
    TC = 0
else :
    TC = (1 - (len(e) / NbitASCII)) * 100


print(texte)
print(CodeHuffman(texte))
texteBinaire = (CodeHuffman(texte))
print(decodeHuffman(texte,texteBinaire))

print('')
print('longueur du texte : ',len(texte))
print('')
print('Taux de compression :              ',TC,'%')
print('Entropie =                         ',H)
print('longueur moyenne de la séquence =  ',l)