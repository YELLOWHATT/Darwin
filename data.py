import pickle

# rolley = ["ha", "be loo", "V.V.S", "neck", "wrist", "rolley on my face", "you a old nigga", "man you washed up"]
rolley = pickle.load(open("dangerous.p", "rb"))

for word in rolley:
    print(word)

# pickle.dump(rolley, open("dangerous.p", "wb"))