"""
2. Να γράψετε πρόγραμμα σε γλώσσα Python, το οποίο να υπολογίζει και να εκτυπώνει το άθροισμα
T+TT+TTT+…+TTTTTTTTT(9 φορές) (όπου Τ το τελευταίο ψηφίο του ΑΜ σας).
"""

def askisi2(afm_last_digit):#To function argument prepei na einai sting me 1 psifio
  result=0
  for i in range(1,10):
    result+=int((afm_last_digit)*i)
  return result
  
