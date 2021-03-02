import pickle, os

if os.path.isfile("kjøretøy"):
    print("Laster inn kjøretøy...")
    lagret_kjøretøy = open("kjøretøy", "rb")
    data = pickle.load(lagret_kjøretøy)
    lagret_kjøretøy.close()
else:
    print("Fant ingen kjøretøy")

print(data)
