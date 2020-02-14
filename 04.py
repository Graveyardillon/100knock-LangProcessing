s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Mght Also Sign Peace Security Clause. Arthur King Can."
d = {}

for index, j in enumerate(s.replace(".", " ").split()):
  if index == 0 or index == 4 or index == 5 or index == 6 or index == 7 or index == 8 or index == 14 or index == 15 or index == 18:
    tmp = {str(index): j[0]}
  else:
    tmp = {str(index): j[0:2]}
  
  d.update(tmp)

print(d)