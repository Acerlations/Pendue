from random import randint


def word_list():
    listed_word = ["Courageux", "Prince", "Niveau", "Amour", "Parfumerie", "Historique", "Chariot", "Insecticide",
                   "Tremblement", "Batteries", "Chaussons", "Scientifique", "Imprimeur", "Stupide", "Professionnel",
                   "Chanteurs","Semaine","Rampant","Coiffeur","Routes","Insomnie","Galerie","Gomme","Inspecter",
                   "Nucléaire","Alligator","Assistant","Rencontrer","Hydrophobe","Ornithorynque","Schisme",
                   "Caïman","Dimanche","Kiwi","Grenouille","Enveloppe","Kamikaze","Antigel","Mensonge",
                   "Obstacle","Mouette","Chevalet", "Unique", "Spectre", "Physique", "Bonjour", "Antigel"]
    return listed_word[randint(0, len(listed_word)-1)]


def removeDupes(mystring):
    newstring = ""
    mystring = mystring.lower()
    for i in mystring:
        if i not in newstring:
            newstring += i
    return newstring


def randomletter(string):
    liste = list(string)
    maxi = len(liste) - 1
    return liste[randint(0, maxi)]


def hideword(word):
    word_del_dupe = removeDupes(word)
    randomword = randomletter(word_del_dupe)
    # print(f"Lettre random : {randomword}")
    liste = list(word)
    hide = ""
    for i in liste:
        if i == " ":
            i = " "
        elif i == "-":
            i = "-"
        elif i != randomword:
            i = "_"
        hide += i
    return hide


def afficher(text):
    return print(text)


def verif(mystring, fonction_name):
    if mystring.isdigit():
        afficher("Mettez que des lettres ou mots")
        return fonction_name()
    elif not mystring.strip():
        afficher("C'est vide ?!")
        return fonction_name()


def init():
    word = input("Mot: ")
    if len(word) < 2:
        afficher("Mettez un mot")
        return init()
    verif(word, play)
    return word


def nb_coups(word):
    return len(removeDupes(word))


def guess():
    propo = input("Proposition: ")
    propo = propo.lower()
    verif(propo, guess)
    return propo


def gamemode():
    demande = input("Vous voulez faire deviner un mot ou avoir un mot au hasard [deviner/hasard]: ")
    if demande == "deviner":
        return init()
    if demande == "hasard":
        return word_list()
    else:
        afficher("Je ne comprend pas votre demannde mettez deviner pour faire trouver un mot ou mettez hasard pour avoir un mot au hasard")
    

def play():
    word = gamemode()
    nb_coups_restant = nb_coups(word)
    word = word.lower()
    hidden_word = hideword(word)
    afficher(hidden_word)
    propo = guess()
    while word != propo or nb_coups_restant != 0:
        if len(propo) >= 2 and word != propo:
            nb_coups_restant -= 1
            afficher(f"Mauvais Mot attention il vous reste {nb_coups_restant} coup(s)")
            propo = guess()
        elif word == propo:
            break
        else:
            word_try = letter_finder(word, propo)
            if len(word_try) >= 1:
                hidden_word = aply_letter(word_try, hidden_word, word)
                if word == hidden_word:
                    break
                afficher(f"{hidden_word}")
                propo = guess()
                word_try = letter_finder(word, propo)
            else:
                nb_coups_restant -= 1
                afficher(f"Mauvaise lettre attention il vous reste {nb_coups_restant} coup(s)")
                propo = guess()
    if word == propo or word == hidden_word:
        afficher(f"C'est gagné bravo, c'était {word}")
    else:
        afficher(f"C'est perdue, c'était {word}")


def aply_letter(letter, hidden_word, word):
    word_liste = list(word)
    hidden_word_liste = list(hidden_word)
    one_letter = letter[0]
    for i in word:
        if i == one_letter:
            hidden_word_liste[word_liste.index(i)] = i
            word_liste[word_liste.index(i)] = None
    hidden_word_liste = ''.join(hidden_word_liste)
    return hidden_word_liste


def letter_finder(word, propo):
    word = list(word)
    liste_word_found = []
    for i in word:
        if i == propo:
            i = propo
            liste_word_found.append(i)
    return liste_word_found


play()
