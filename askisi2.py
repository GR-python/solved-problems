"""
Να γράψετε πρόγραμμα, το οποίο να υπολογίζει και να εκτυπώνει το άθροισμα
T+TT+TTT+…+TTTTTTTTT(9 φορές) (όπου Τ το τελευταίο ψηφίο του ΑΜ σας).
"""

def askisi2(afm_last_digit):
  if afm_last_digit in range(10):
    afm_last_digit_str=str(afm_last_digit)
    result=0
    for i in range(1,10):
      result+=int((afm_last_digit_str)*i)#Δημιουργούμαι κάθε φορά το T[1-9] ως str και μετά το μετατρέπω σε int 
    return result
  else:
    return f'To {afm_last_digit} πρέπει να είναι αριθμός 0-9'
  
def askisi(a):
  result=0
  for i in range(1,10):
    number=0
    j=0
    while j<i:
      number=number+a*10**j#Δημιουργούμαι κάθε φορά τον ακέραιο πχ 22222(5 φορές το 2) ώς 2+2*10**1+2*10**2+2*10**3+2*10**4
      j+=1
    result+=number
  return result
#Στις δύο παραπάνω λύσεις μου δεν χρησιμοποιώ το print(result) που ζητάει η άσκηση αλλά το return result.
#Έλεγχο εισόδου του argument μπορούμε να επαναλάβουμε το ίδιο και στην δεύτερη άσκηση.
