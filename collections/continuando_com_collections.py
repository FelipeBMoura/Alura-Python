usuarios_data_science = [15, 23, 43, 56]

usuarios_machine_learning = [13, 23, 43, 42]

assistiram = usuarios_data_science.copy()

assistiram.extend(usuarios_data_science)

print(assistiram)

print(set(assistiram))

print(set([1, 2, 3, 4, 1]))

print({1, 2, 3, 4, 1})

print(type({1, 2, 3, 4, 1}))

usuarios_data_science = {15, 23, 43, 56}

usuarios_machine_learning = {13, 23, 56, 42}

# usuarios_machine_learning[3]  # no set não existe posição. Dará TypeError

for usuario in set(assistiram):
    print(usuario)

print(usuarios_data_science | usuarios_machine_learning)

print(usuarios_data_science & usuarios_machine_learning)

print(usuarios_data_science - usuarios_machine_learning)
