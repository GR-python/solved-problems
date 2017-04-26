"""
Γράψτε πρόγραμμα, το οποίο θα δέχεται ως είσοδο έναν αριθμό
και θα εκτυπώνει αν είναι πρώτος αριθμός ή όχι
write a program that prints if a number is prime or not
"""

def protos(a): 
  counter = 2 
  while counter*counter < a: 
    if a % counter == 0: 
      print (f"{a} is no prime number, because {a} = {counter} * {a/counter}" ) 
      return False
    counter += 1 
  print (f"{a} is a prime number")
  return True
