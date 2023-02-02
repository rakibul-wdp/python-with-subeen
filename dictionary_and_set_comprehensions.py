li = [(1, 'One'), (2, 'Two'), (3, 'Three')]
dt = {k:v for k, v in li}
# print(dt)

dt = {v:k for k, v in li}
# print(dt)

s = 'aldksjflasjdlajsdlfjalsdfjaldsjfdlfj'
unique_letters = {a for a in s}
# print(unique_letters)

colors_choice = [('Abul', 'Blue'), ('Babul', 'Red'), ('Cabul', 'Yellow'), ('Dabul', 'Blue'), ('Ebul', 'Blue')]
colors_dt = {name:color for name, color in colors_choice}
# print(colors_dt)

colors_set = {color for color in dt.values()}
# print(colors_set)

colors_set = {color for color in colors_dt.values()}
print(colors_set)