"""
Ο υπολογισμός του ετήσιου φόρου αριθμού μισθωτών υπαλλήλων 
με βάση το ετήσιο ακαθάριστο εισόδημά τους ως εξής:
• Φόρος t% για εισόδημα μέχρι και 15000 € (όπου t εισάγεται από το χρηστη)
• Φόρος p% για το υπόλοιπο εισόδημα (όπου p εισάγεται από το χρηστη)

Να γράψετε πρόγραμμα σε γλώσσα python, το οποίο:
i. Διαβάζει τις ετήσιες ακαθάριστες αποδοχές των υπαλλήλων με χρήση αμυντικού προγραμματισμού 
   (δηλ. δεν πρέπει να γίνονται δεκτές αρνητικές τιμές).
ii. Εκτυπώνει τον ετήσιο φόρο για κάθε υπάλληλο.
iii. Εκτυπώνει το μηνιαίο καθαρό μισθό κάθε υπαλλήλου (θεωρώντας 12 μισθούς ανά έτος).
iv. Εκτυπώνει το μεγαλύτερο καθαρό ετήσιο εισόδημα και τον αντίστοιχο φόρο.
"""

def foros():
  t=int(input('Εισάγετε τον φορολογικό συντελεστή για εισοδήματα μικρότερα ή ίσα των 15.000€ : '))
  p=int(input('Εισάγετε τον φορολογικό συντελεστή για το υπόλοιπο εισόδημα άνω των 15.000€ : '))
  apodoxes=[]
  ar_ipallilou=0
  while True:
    try:
      apodoxi=float(input('Δώσε τις ετήσιες αποδοχές του {}ου υπαλλήλου (0 για έξοδο): '.format(ar_ipallilou+1)))
      if apodoxi>0:
        apodoxes.append(apodoxi)
        ar_ipallilou+=1
      elif apodoxi==0:
        break
      else:
        print("Οι αποδοχές πρέπει να είναι αριθμός μεγαλύτερος του 0")
    except:
      print('Πρέπει να πληκτρολογήσετε αρθμό')
    
  foroi=[]
  for i in apodoxes:
    if i<=15000:
      foros=(t/100)*i
    else:
      foros=((t/100)*15000)+(p/100)*(i-15000)
    foroi.append(foros)
  
  kathares_apodoxes=[apodoxes[i]-foroi[i] for i in range(len(apodoxes))]
  
  for i in range(len(foroi)):
    print('Ο {}ος υπάλληλος έχει φόρο {:.2f}€'.format( i+1, foroi[i]))
  
  for i in range(len(kathares_apodoxes)):
    print('Ο {}ος υπάλληλος έχει μηνιαίο μισθό {:.2f}€'.format(i+1, kathares_apodoxes[i]/12))
  
  print ('Το μεγαλύτερο καθαρό εισόδημα είναι {:.2f}€ μετά από φόρο {:.2f}€'.format( max(kathares_apodoxes),
          foroi[kathares_apodoxes.index(max(kathares_apodoxes))]))
          
"""
An object oriented approach
"""

class Ipallilos:
  ipalliloi=[]
  def __init__(self, am, onoma, etisies_apodoxes):
    self.am=am
    self.onoma=onoma
    self.etisies_apodoxes=etisies_apodoxes
    self.upologise_foro()
    type(self).ipalliloi.append(self)
  def __repr__(self):
    return "AM :{}, Ονοματεπώνυμο :{}".format(self.am, self.onoma)
  def upologise_foro(self):
    if self.etisies_apodoxes<=15000:
      self.foros=( 10/100)*self.etisies_apodoxes
    else:
      self.foros=((10/100)*15000)+(20/100)*(self.etisies_apodoxes-15000)
  @property
  def arithmos(self):
    return len(type(self.ipalliloi))
  
    
    
  
