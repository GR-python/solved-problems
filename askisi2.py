"""
2. Να γράψετε πρόγραμμα σε γλώσσα Python, το οποίο να υπολογίζει και να εκτυπώνει το άθροισμα 0+00+000+…+000000000 (όπου Τ το τελευταίο ψηφίο του ΑΜ σας).
"""

def askisi2(afm_last_digit):
  if  isinstance(afm_last_digit,str) and len (afm_last_digit)==1 and afm_last_digit.isdigit():
    result=0
    for i in range(1,10):
      result+=int((afm_last_digit)*i)
    return result
  else:
    print('To function argument prepei na einai sting me 1 psifio' )