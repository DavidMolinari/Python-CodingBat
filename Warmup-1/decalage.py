''' TP Cryoptographie
Meh
'''

# A. Occurence d'une lettre dans un message :

'''
a. Lister les variables utilisées ainsi que leur type.
message = variable de type chaine de caractere
n = variable de type entier
i et cpt = variables de type entier

b. Il manque l'incrépentation du compteur i pour permettre de boucler
jusqu'à la longueur de message, donc l'instruction : i = i + 1

c. Cet algorithme permet de compter le nombre de fois où la lettre 'a'
est dans le mesage.

e. pour prendre e compte le A en majusculre, on ajoute une condition
    de plus : if (message[i] == 'a' or message[i] == 'A') '''



# Fontion qui retourne le nombre d'occurence de la lettre a/A
def occurence_lettre(message):
    n = len(message)
    i = 0
    cpt = 0
    while (i < n):
        if (message[i] == 'a' or message[i] == 'A') :
            cpt = cpt + 1
        i = i + 1
    print(cpt)
# Fonction qui retourne sous forme d'un tableau, le nombre d'occurencs
# de toutes les lettres de l'alphabet

def occurence(message):
    a = "abcdefghijklmnopqrstuvwxyz"
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tab = [0]*len(a)
    lettremax = ""
    meh = 0
    nb = 0
    n = len(message)
    for i in range(0, n):
        for j in range (0, len(a)):
            if message[i] == a[j] or message[i] == A[j]:
                tab[j] = tab[j]+1
            if (tab[j] > nb):
                nb = tab[j]
                lettremax=message[i]
    print(nb, " = ", lettremax)
    print(tab)



    
''' Codage Affine '''

def decalage(message, meh):
    a = "abcdefghijklmnopqrstuvwxyz"
    nouvelIndice = 0
    newA = ""
    for i in range(0, len(message)):
        indice = message[i]
        nouvelIndice = (i + meh)%26  
        newA = newA + a[nouvelIndice]
        
        
    print(newA)



def meh(message):
    a = ("abcdefghijklmnopqrstuvwxyz")
    p = ("?,. !:")
    nouveau = [0]*len(message)
    nouvmeh = 0
    for i in range(len(message)):
        for j in range (len(a)):
            if message[i] == a[j]:
                nouveau[i] = a[(j-3)%26]
            else:
                for k in range(len(p)):
                    if message[i] == p[k]:
                        nouveau[i] = p[k]
                    
        print (nouveau[i], end="")

def occurence2(message):
    a = "abcdefghijklmnopqrstuvwxyz"
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tab = [0]*len(a)
    lettremax = ""
    meh = 0
    nb = 0
    n = len(message)
    for i in range(0, n):
        for j in range (0, len(a)):
            if message[i] == a[j] or message[i] == A[j]:
                tab[j] = tab[j]+1
            if (tab[j] > nb):
                nb = tab[j]
                lettremax=message[i]
    return (lettremax)




''' Programme principal  '''
'''
print("Occurences de la lettre a dans : J'aime les ananas :")
occ1 = occurence_lettre("J'aime les ananas !")
print("Occurences de la lettre a dans : Avez vous appris votre cours ?  :")
occ2 = occurence_lettre('Avez vous appris votre cours ? ')


print("Occurence de toutes les lettres de d'alphabet")
occurence("Portez ce vieux whisky au juge blond qui fume")
'''

'''decalage("aaaaaa", 3)'''


print(occurence2("ath bpiwtbpixfitj, r'thi qxtc !"))

