"""
2. Να γράψετε πρόγραμμα σε γλώσσα Python, το οποίο να υπολογίζει και να εκτυπώνει το άθροισμα
T+TT+TTT+…+TTTTTTTTT(9 φορές) (όπου Τ το τελευταίο ψηφίο του ΑΜ σας).
"""

def askisi2(afm_last_digit):
  afm_last_digit_str=str(afm_last_digit)
  result=0
  for i in range(1,10):
    result+=int((afm_last_digit_str)*i)
  return result
  
def askisi(a):
  result=0
  for i in range(1,10):
    number=0
    j=0
    while j<i:
      number=number+a*10**j
      j+=1
    result+=number
  return result
