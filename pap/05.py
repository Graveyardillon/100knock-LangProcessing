SENTENCE = "I am an NLPer"
N = 2

def ngram(s):
  c = []
  w = []
  sp = s.split()
  for i in range(len(s)):
    c.append(s[i:i+N])
  
  for i in range(len(sp)):
    w.append(sp[i:i+N])
  
  print(c)
  print(w)

ngram(SENTENCE)