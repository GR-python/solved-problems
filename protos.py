"""
Γράψτε πρόγραμμα, το οποίο θα δέχεται ως είσοδο έναν αριθμό
και θα εκτυπώνει αν είναι πρώτος αριθμός ή όχι
"""

def protos(a): 
  counter = 2 
  while counter*counter < a: 
    if a % counter == 0: 
      print (f"{a} is no prime number, because {a} = {counter} * {a/counter}" ) 
      return 
    counter += 1 
  print (f"{a} is a prime number")
