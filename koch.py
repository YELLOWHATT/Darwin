#!/usr/bin/env python3

# -*- coding: utf-8 -*-

__license__ = "MIT"
__version__ = "0.1.4"
__maintainer__ = "YELLOWHATT, Hydra and Artistic Memes"
__email__ = "thekoolaidmannn@gmail.com"
__status__ = "Production - Beta"
__dates__ = "11/17/18 - 01/02/19"
__type__ = "Scientific Application"
__estimated_release_date__ = "02/03/19"
__name__ = "Microbe-Log"

import wikipedia

# Readline module will be used for autocorrect or suggestions
# NEI = Not Enough Information
# Numbers are organized in binary
# A symptoms thing will be made later (possibly)

class virus:

    def __init__(self, namev, typev, speciesv, common_name_diseasev, groupv):
        self.namev = namev
        self.typev = typev
        self.speciesv = speciesv
        self.common_name_diseasev = common_name_diseasev
        self.groupv = groupv

    def __str__(self):
        return (" ".join(["Name:", self.namev, "Type:", self.typev, "Species:", self.speciesv, "Common disease name:", self.common_name_diseasev, "Group:", self.groupv]))

# RNA || ODD NUMBERS
vrs00000001 = virus("Zaire Ebola Virus", "((-)ssRNA)", "Ebola Virus", "Ebola Hemorrhagic Fever", "Group V") # 1
vrs00000011 = virus("Marburg Virus", "((-)ssRNA)", "Marburg", "Marburg Hemorrhagic Fever", "Group V") # 3
# List Separation
vrs00000010 = virus("Variola Major", "(dsDNA)", "Variola", "Small Pox", "Group I") #2
vrs00000100 = virus("Human Herpes Simplex Virus I", "(dsDNA)", "Herpes Simplex Virus I", "Herpes Virus", "Group I") # 4
# DNA || EVEN NUMBERS

class fungi:

    def __init__(self, namef, typef, speciesf):
        self.namef = namef
        self.typef = typef
        self.speciesf = speciesf

    def __str__(self):
        return(" ".join(["Name:", self.namef, "Type:", self.typef, "Species:", self.speciesf]))

fng00000001 = fungi("Synchytrium endobioticum", "Chytridiomycota", "Endobioticum") # 1
# Separation
fng00000010 = fungi("Phycomyces blakesleeanus", "Zygomycota", "Blakesleeanus") # 2
# Separation
fng00000011 = fungi("Sarcoscypha coccinea", "Ascomycota", "Coccinea") # 3
fng00001001 = fungi("Aspergillus penicillioides", "Ascomycota", "Penicillioides") # 9
# Separation
fng00000100 = fungi("Geastrum coronatum", "Basidiomycota", "Coronatum") # 4
# Separation
# Deuteromycota NEI # 5 supossed to be 5
#Separation
fng00000101 = fungi("Geosiphon pyriformis", "Gleromycota", "Pyriformis") # 5

class protozoa:

    def __init__(self, namep, typep, speciesp, common_name_diseasep):
        self.namep = namep
        self.typep = typep
        self.speciesp = speciesp
        self.common_name_diseasep = common_name_diseasep

    def __str__(self):
        return (" ".join(["Name:", self.namep, "Type:", self.typep, "Species:", self.speciesp, "Common disease name:", self.common_name_diseasep]))

# Mastigophora
proto00000001 = protozoa("", "", "", "") # 1
# Sarcodina
proto00000010 = protozoa("", "", "", "") # 2
#Separation
proto00000011 = protozoa("Toxoplasma gondii", "Apicomplexa", "Gondii", "Toxoplasmosis") # 3
proto00000100 = protozoa("Plasmodium vivax", "Apicomplexa", "Vivax", "Malaria") # 4
# Separation
proto00000101 = protozoa("Oxytricha trifallax", "Ciliophora", "Trifallax", "None") # 5

class bacteria:

    def __init__(self, nameb, typeb, speciesb, common_name_diseaseb):
        self.nameb = nameb
        self.typeb = typeb
        self.speciesb = speciesb
        self.common_name_diseaseb = common_name_diseaseb

    def __str__(self):
        return (" ".join(["Name:", self.nameb, "Type:", self.typeb, "Species:", self.speciesb, "Common disease name:", self.common_name_diseaseb]))

# Gram Negative Bacteria || ODD NUMBERS
bac00000001 = bacteria("Eschericia Coli", "Gram Negative", "Coli", "Shiga Toxin") # 1
bac00000011 = bacteria("Pseudomonas Aeruginosa", "Gram Negatove", "Aeruginosa", "Lorem ipsum") # 3
bac00000101 = bacteria("Salmonella Enterica", "Gram Negative", "Enterica", "Lorem  ipsum") # 5
bac00000111 = bacteria("Helicobacter Pylori", "Gram Negative", "Pylori", "Stomach Ulcers") # 7
bac00001001 = bacteria("Klebsiella Pneumoniae", "Gram Negative", "Pneumoniae", "Lorem ipsum") # 9
bac00001011 = bacteria("Burkholderia Pseudomallei", "Gram Negative", "Pseudomallei", "Lorem ipsum") # 11
bac00001101 = bacteria("Enterobacter Cloacae", "Gram Negative", "Cloacae", "Lorem ipsum") # 13
bac00001111 = bacteria("Yersinia Pestis", "Gram Negative", "Pestis", "Plague") # 15
bac00010001 = bacteria("Neisseria Meningitidis", "Gram Negative", "Meningitidis", "Lorem ipsum") # 17
bac00010011 = bacteria("Prevotella Melaninogenica", "Gram Negative", "Melaninogenica", "Lorem ipsum") # 19
bac00010101 = bacteria("Salmonella Bongori", "Gram Negative", "Bongori", "Lorem ipsum") # 21
bac00010111 = bacteria("Vibrio Cholerae", "Gram Negative", "Cholerae", "Cholera") # 23
bac00011001 = bacteria("Brucellosis Canis", "Gram Negative", "Canis", "Lorem ipsum") # 25
# List Separation
bac00000010 = bacteria("Streptococcus Sanguinis", "Gram Negative", "Sanguinis", "Lorum ipsum") # 2
bac00000100 = bacteria("Staphylococcus Aureus", "Gram Positive", "Aureus", "Lorem ipsum") # 4
bac00000110 = bacteria("Clostridium Botulinum", "Gram Positive", "Botulinum", "Botulism") # 6
bac00001000 = bacteria("Clostridium Tetani", "Gram Positive", "Tetani", "Tetanus") # 8
bac00001010 = bacteria("Bacillus Anthracis", "Gram Positive", "Anthracis", "Anthrax")  # 10
bac00001100 = bacteria("Listeria Monocytogenes", "Gram Positive", "Monocytogenes", "Lorum ipsum") # 12
bac00001110 = bacteria("Clostridioides Difficile", "Gram Positive", "Difficile", "Lorum ipsum") # 14
bac00010000 = bacteria("Streptococcus Mitis", "Gram Positive", "Mitis", "Lorum ipsum") # 16
bac00010010 = bacteria("Clostridium Perfringens", "Gram Positive", "Perfringens", "Lorum ipsum") # 18
bac00010100 = bacteria("Staphylococcus Saprophyticus", "Gram Positive", "Saprophyticus", "Lorum ipsum") # 20
bac00010110 = bacteria("Corynebacterium Diphtheriae", "Gram Positive", "Diphtheriae", "Lorem ipsum") # 22
bac00011000 = bacteria("Streptococcus Pyogenes", "Gram Positive", "Pyogenes", "Lorem ipsum") # 24
bac00011010 = bacteria("Clostridium Perfringens", "Gram Positive", "Perfringens", "Lorum ipsum") # 26
bac00011100 = bacteria("Methicillin Resistant Staphylococcus Areus", "Gram Positive", "Areus", "Lorem ipsum") # 28
# Gram Positive Bacteria || EVEN NUMBERS

def bug():

    print("\nTo report a bug please emial it to this email: " + __email__)
    print("\nReturning to help menu\n")
    help()
    return

def info():

    print("\nThis is a program that helps with Microbiological information")
    print("Returning to help menu\n")
    help()
    return

def help():

    help_options = "Report a bug, Info or Exit"

    print("\nPlease enter one of the following options: " + help_options)

    help_input = str(input())

    if help_input == "Report a bug" or help_input == "report a bug" or help_input == "REPORT A BUG":

        print("Going to bug menu")
        bug()

    elif help_input == "Info" or help_input == "info" or help_input == "INFO":

        print("Going to info")
        info()

    else:

        print("Are you sure you want to exit?")
        exting = str(input())

        if exting == "Yes" or exting == "yes" or exting == "YES" or exting == "Exit" or exting == "exit" or exting == "EXIT":

            print ("Exiting")

        else:

            print("It seems you have not entered a valid input try again or enter menu to go to menu")
            new_exit = str(input())

            if new_exit == "Exit":

                print("Exiting")

            elif new_exit == "Menu":

                print("Going to menu")
                repeat2()
                return

            else:

                print("Try again")
                repeat()
                return

def repeat():

    print("You have entered an incorrect input please try again")
    print("Would you like to exit or continue?")
    continue_with_program = str(input())

    if continue_with_program == "No" or continue_with_program == "no" or continue_with_program == "NO":

        print("Ok continuing program")
        repeat2()
        return

    else:

        print("Are you sure you would like to exit")
        yes_exit = str(input())

        if yes_exit == "No" or yes_exit == "NO" or yes_exit == "no":

            print("OK")
            print("Going back to repeat")
            repeat()

        elif yes_exit != "No" or yes_exit != "NO" or yes_exit != "n":

            print("Exiting")

def v():

    dna_based = [vrs00000010, vrs00000100]
    rna_based = [vrs00000001, vrs00000011]

    print("\nPlease enter a Nucleic type, Name, or a Species\n")
    print("If you would like to find more information on a Viral species enter Wikipedia\n")

    VTS = str(input())
    print("\n\n############")

    rna_based.sort(key = lambda x: x.namev)
    dna_based.sort(key = lambda x: x.namev)

    if VTS == "Rna" or VTS == "RNA" or VTS == "rna":

        for rna_based in rna_based:

            print("\n")
            print(rna_based)
            print("\n")
        input("This is the end of the program press enter to exit...")

    elif VTS == "Dna" or VTS == "dna" or VTS == "DNA":

        for dna_based in dna_based:

            print("\n")
            print(dna_based)
            print("\n")
        input("This is the end of the program pres enter to exit...")

    elif VTS == "Wikipedia" or VTS == "WIKIPEDIA" or VTS == "wikipedia":

        print("\nEnter the name of a Virus to find more about it\n")
        wiki_virus = str(input())
        print("\n")
        print(wikipedia.summary(wiki_virus, sentences = 7))
        print("\nWould you like to return to the menu or exit?")

        newexit = str(input())

        if newexit == "Exit" or newexit == "exit":

            print("Exiting...")

        elif newexit == "Menu" or newexit == "menu":

            print("Returning to menu...")
            repeat2()
            return

        else:

            repeat()

    else:

        for rna_virus, dna_virus in rna_based, dna_based:

            if rna_virus.namev == VTS or rna_virus.speciesv == VTS or rna_virus.typev == VTS or rna_virus.common_name_diseasev == VTS or rna_virus.groupv == VTS:

                print("\n")
                print(rna_virus, "\n" * 2)
                print(dna_virus, "\n" * 2)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue")
                repeat2()
                return

            else:

                pass

        repeat()

def f():

    chytridiomycota = [fng00000001]
    zygomycota = [fng00000010]
    ascomycota = [fng00000011, fng00001001]
    basidiomycota = [fng00000100]
    glomeromycota = [fng00000101]

    chytridiomycota.sort(key = lambda x: x.namef)
    zygomycota.sort(key = lambda x: x.namef)
    ascomycota.sort(key = lambda x: x.namef)
    basidiomycota.sort(key = lambda x: x.namef)
    glomeromycota.sort(key = lambda x: x.namef)

    print("\nPlease enter a Fungi name, Species, or Type\n")
    print("If you would like to find more information on a Fungal species enter Wikipedia\n")

    FTS = str(input())
    print("\n\n############\n\n")

    if FTS == "Chytridiomycota" or FTS == "chytridiomycota" or FTS == "CHYTRIDIOMYCOTA":

        for chytridiomycota in chytridiomycota:

            print("\n")
            print(chytridiomycota)
            print("\n")
        input("This is the end of the program press enter to exit...")

    elif FTS == "Zygomycota" or FTS == "zygomycota" or FTS == "ZYGOMYCOTA":

        for zygomycota in zygomycota:

            print("\n")
            print(zygomycota)
            print("\n")
        input("This is the end of the program press enter to exit...")

    elif FTS == "Ascomycota" or FTS == "ascomycota" or FTS == "ASCOMYCOTA":

        for ascomycota in ascomycota:

            print("\n")
            print(ascomycota)
            print("\n")
        input("This is the end of the program press enter to exit...")

    elif FTS == "Basidiomycota" or FTS == "basidiomycota" or FTS == "BASIDIOMYCOTA":

        for basidiomycota in basidiomycota:

            print("\n")
            print(basidiomycota)
            print("\n")
        input("This is the end of the program press enter to exit...")

    elif FTS == "Glomeromycota" or FTS == "glomeromycota" or FTS == "GLOMEROMYCOTA":

        for glomeromycota in glomeromycota:
            print("\n")
            print(glomeromycota)
            print("\n")
        input("This is the end of the program press enter to exit...")

    elif FTS == "Wikipedia" or FTS == "wikipedia" or FTS == "WIKIPEDIA":

        print("Enter the name of the Fungi to find more about it\n")
        wiki_fungi = str(input())
        print("\n")
        print(wikipedia.summary(wiki_fungi, sentences = 7))
        print("\nWould you like to return to the menu or exit?")

        next = str(input())

        if nexit == "Exit" or nexit == "exit" or nexit == "EXIT":

            print("Exiting...")

        elif nexit == "Menu" or nexit == "menu" or nexit == "MENU":

            print("Returning to menu...")
            repeat2()
            return

        else:

            repeat()

    else:

        for chytridiomycota in chytridiomycota:

            if chytridiomycota.namef == FTS or chytridiomycota.speciesf == FTS or chytridiomycota.typef == FTS:

                print(chytridiomycota)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue\n")
                repeat2()
                return

        for zygomycota in  zygomycota:

            if zygomycota.namef == FTS or zygomycota.speciesf == FTS or zygomycota.typef == FTS:

                print(zygomycota)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue\n")
                repeat2()
                return

        for ascomycota in ascomycota:

            if ascomycota.namef == FTS or ascomycota.speciesf == FTS or ascomycota.typef == FTS:

                print(ascomycota)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue\n")
                repeat2()
                return

        for basidiomycota in basidiomycota:

            if basidiomycota.namef == FTS or basidiomycota.speciesf == FTS or basidiomycota.typef == FTS:

                print(basidiomycota)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue\n")
                repeat2()
                return

        for glomeromycota in glomeromycota:

            if glomeromycota.namef == FTS or glomeromycota.speciesf == FTS or glomeromycota.typef == FTS:

                print(basidiomycota)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue\n")
                repeat2()
                return

        repeat()

def p():

    mastigophora = [proto00000001]
    sarcodina = [proto00000010]
    apicomplexa = [proto00000011, proto00000100]
    ciliophora = [proto00000101]

    mastigophora.sort(key = lambda x: x.namep)
    sarcodina.sort(key = lambda x: x.namep)
    apicomplexa.sort(key = lambda x: x.namep)
    ciliophora.sort(key = lambda x: x.namep)

    print("\nPlease enter a Protozoan name, Species, or Causative agent\n")
    print("If you would like to find more information on a viral species enter Wikipedia\n")

    PTS = str(input())
    print("\n\n############\n\n")

    if PTS == "Mastigophora" or PTS == "mastigophora" or PTS == "MASTIGOPHORA":

        for mastigophora in mastigophora:

            print("\n")
            print(mastigophora)
            print("\n")
        input("This is the end of the program press enter to exit...")

    elif PTS == "Wikipedia" or PTS == "WIKIPEDIA" or PTS == "wikipedia":

        print("\nEnter the name of a Protozoan to find more about it\n")
        wiki_protozoa = str(input())
        print("\n")
        print(wikipedia.summary(wiki_protozoa, sentences = 7))
        print("\nWould you like to return to the menu or exit?")

        nexit = str(input())

        if nexit == "Exit" or nexit == "exit" or nexit == "EXIT":

            print("Exiting...")

        elif nexit == "Menu" or nexit == "menu" or nexit == "MENU":

            print("Returning to menu...")
            repeat2()
            return

        else:

            repeat()

    elif PTS == "Sarcodina" or PTS == "sarcodina" or PTS == "SARCODINA":

        for sarcodina in sarcodina:

            print("\n")
            print(sarcodina)
            print("\n")
        input("This is the end of the program press enter to exit...")

    elif PTS == "Apicomplexa" or PTS == "apicomplexa" or PTS == "APICOMPLEXA":

        for apicomplexa in apicomplexa:

            print("\n")
            print(apicomplexa)
            print("\n")
        input("This is the end of the program press enter to exit...")

    elif PTS == "Ciliophora" or PTS == "ciliophora" or PTS == "CILIOPHORA":

        for ciliophora in ciliophora:

            print("\n")
            print(ciliophora)
            print("\n")
        input("This is the end of the program press enter to exit...")

    else:

        for mastigophora in mastigophora:

            if mastigophora.namep == PTS or mastigophora.speciesp == PTS or mastigophora.typep == PTS or mastigophora.common_name_diseasep == PTS:

                print(mastigophora)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue\n")
                repeat2()
                return

        for sarcodina in sarcodina:

            if sarcodina.namep == PTS or sarcodina.speciesp == PTS or sarcodina.typep == PTS or sarcodina.common_name_diseasep == PTS:

                print(sarcodina)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue\n")
                repeat2()
                return

        for apicomplexa in apicomplexa:

            if apicomplexa.namep == PTS or apicomplexa.speciesp == PTS or apicomplexa.typep == PTS or apicomplexa.common_name_diseasep == PTS:

                print(apicomplexa)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue\n")
                repeat2()
                return

        for ciliophora in ciliophora:

            if ciliophora.namep == PTS or ciliophora.speciesp == PTS or ciliophora.typep == PTS or ciliophora.common_name_diseasep == PTS:

                print(ciliophora)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue\n")
                repeat2()
                return

def g_s():

    gram_pos = [bac00000010, bac00000100, bac00000110, bac00001000, bac00001010, bac00001100,
                bac00001110, bac00010000, bac00010010, bac00010100, bac00010110, bac00011000,
                bac00011010, bac00011100] # || EVEN NUMBERS

    gram_neg = [bac00000001, bac00000011, bac00000101, bac00000111, bac00001001, bac00001011,
                bac00001101, bac00001111, bac00010001, bac00010011, bac00010101, bac00010111,
                bac00011001] # || ODD NUMBERS

    gram_pos.sort(key = lambda x: x.nameb)
    gram_neg.sort(key = lambda x: x.nameb)

    print("\nPlease enter a Gram stain, Name, Species or a Common name / disease\n")
    print("If you would like to find more information on a bacterial species enter Wikipedia\n")

    NTS = str(input())
    print("\n\n############\n\n")

    if NTS == "Gram Positive" or NTS == "Gram positive" or NTS == "gram positive":

        for gram_pos in gram_pos:
            print("\n")
            print(gram_pos)
            print("\n")
        input("This is the end of the program press enter to exit...")

    elif NTS == "Gram Negative" or NTS == "Gram negative" or NTS == "gram negative":

        for gram_neg in gram_neg:

            print("\n")
            print(gram_neg)
            print("\n")
        input("This is the end of the program press enter to exit...")

    elif NTS == "Wikipedia" or NTS == "WIKIPEDIA" or NTS == "wikipedia":

        print("\nEnter the name of a Bacteria to find more about it\n")
        wiki_bacteria = str(input())
        print("\n")
        print(wikipedia.summary(wiki_bacteria, sentences = 7))
        print("\nWould you like to return to the menu or exit?")

        nexit = str(input())

        if nexit == "Exit" or nexit == "exit":

            print("Exitting...")

        elif nexit == "Menu" or nexit == "menu":

            print("Returning to menu...")
            repeat2()
            return

        else:

            repeat()

    else:

        for gram_pos in gram_pos:

            if gram_pos.nameb == NTS or gram_pos.speciesb == NTS or gram_pos.common_name_diseaseb == NTS:

                print(gram_pos)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue\n")
                repeat2()
                return

        for gram_neg in gram_neg:

            if gram_neg.nameb == NTS or gram_neg.speciesb == NTS or gram_pos.common_name_diseaseb == NTS:

                print(gram_neg)
                print("\nGoing back to Main Menu\n")
                input("Press any key to continue\n")
                repeat2()
                return

        repeat()

microbes = "Bacteria, Virus, Protozoa, Fungi, Bug, or Help"

print("Welcome!")
print("\nYou are using version " + __version__ + " of " + __name__)

def repeat2():

    print("\nPlease select if you would like to view, " + microbes + "\n")
    view = str(input())

    if view == "Virus" or view == "virus" or view == "VIRUS":

        print("\nGoing to Virus menu")
        v()

    elif view == "Protozoa" or view == "PROTOZOA" or view == "protozoa":

        print("\nGoing to Protozoa menu")
        p()

    elif view == "Help" or view == "help" or view == "HELP":

        print("\nGoing to Help menu")
        help()

    elif view == "Fungi" or view == "fungi" or view == "FUNGI":

        print("\nGoing to Fungi menu")
        f()

    elif view == "Bacteria" or view == "bacteria" or view == "BACTERIA":

        print("\nGoing to Bacteria menu")
        g_s()

    else:

        print("\nYou have entered an incorrect input please try again...\n")
        input("Press enter when you are ready...")
        repeat2()

repeat2()
