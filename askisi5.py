"""
Να γραφεί πρόγραμμα σε γλώσσα Python, το οποίο διαβάζει από το πληκτρολόγιο Π 
μονοψήφιους θετικούς ακεραίους αριθμούς και εκτυπώνει τους αριθμούς και το πλήθος εμφάνισής τους 
κατά αύξουσα σειρά πλήθους εμφανίσεων (όπου Π τα 2 τελευταία ψηφία του ΑΜ σας). 
"""

def repetition(am):
  a=[0,1,2,3,4,5,6,7,8,9]
  b=[0]*10
  while sum(b)<am:
    try:
      num=int(input('Dose arithmo apo 0-9 : '))
      if num in a:
        b[a.index(num)]+=1
      else:
        print('Ο αριθμός πρέπει να είναι μεταξύ 0-9')  
    except:
      pass
  c=list(zip(a,b))
  for i in sorted(c, key=lambda item:item[1], reverse=True):
    print(i)

def repetition2():
  a=[]
  b=[]
  while True:
    try:
      num=int(input('Δώσε τον {}ο ακέραιο (-1 για έξοδο): '.format(sum(b)+1)))
      if num==-1:
        break
      if num in a:
        b[a.index(num)]+=1
      else:
        a.append(num)
        b.append(0)
        b[a.index(num)]+=1
    except:
      pass
  c=list(zip(a,b))
  for i in sorted(c, key=lambda item:item[1], reverse=True):
    print(i)
