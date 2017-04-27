"""
Γράψτε πρόγραμμα, το οποίο θα δέχεται ως είσοδο έναν αριθμό
και θα εκτυπώνει αν είναι πρώτος αριθμός ή όχι
"""

def protos(a):
  if a <2 :
    return False
  elif a==2:
    return True
  for i in range(2,int (math.sqrt(a)+1)):
    if not a%i:
      print ("{} is no prime number, because {} = {} * {}".format(a,a,i,a/i) ) 
      return False
  print ("{} is a prime number".format(a))
  return True
