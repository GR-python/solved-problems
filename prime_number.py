"""
Γράψτε πρόγραμμα, το οποίο θα δέχεται ως είσοδο έναν αριθμό
και θα εκτυπώνει αν είναι πρώτος αριθμός ή όχι
write a program that prints if a number is prime or not
"""

def protos(a):
  if a <2 :
    return False
  elif a==2:
    return True
  for i in range(2,int (math.sqrt(a)+1)):
    if not a%i:
      print (f"{a} is no prime number, because {a} = {i} * {a/i}" ) 
      return False
  print (f"{a} is a prime number")
  return True
