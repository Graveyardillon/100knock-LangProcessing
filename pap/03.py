s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
l = []

for i in s.replace(",", " ").split():
  l.append(len(i))

print(l)