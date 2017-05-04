"""
Αναπτύξτε ένα πρόγραμμα που ζητά από το χρήστη να εισάγει μια ακολουθία ψηφίων που να αποτελείται από 0 και 1 
(δυαδική ακολουθία). Αφού ολοκληρωθεί η εισαγωγή, το πρόγραμμα θα πρέπει αναγνωρίζει την 
μεγαλύτερη υποακολουθία 0 ή 1 και θα εκτυπώνει αντίστοιχο μήνυμα. 

insert binary sequence : 100110110100001110
0's have the biggest sequence. Length : 4
"""

def biggest_sequence():
  sequence=input("Insert binary sequence : ")
  len_1=0
  len_0=0
  max_0=0
  max_1=1
  flag=0
  for i in sequence:
    if i=='0':
      if flag==0:
        len_0+=1
      else:
        len_0=1
        flag=0
        if len_1>max_1:
          max_1=len_1
    elif i=='1':
      if flag==1:
        len_1+=1
      else:
        len_1=1
        flag=1
        if len_0>max_0:
          max_0=len_0
  if len_0>max_0:
          max_0=len_0
  if len_1>max_1:
          max_1=len_1
  if max_0>max_1:
    print("0's have the biggest sequence. Length : {}".format(max_0))
  elif max_1>max_0:
    print("1's have the biggest sequence. Length : {}".format(max_1))
  else: 
    print("1's and 0's have the same biggest sequence. Length : {}".format(max_1))
    
    
def biggest_sequence2():
  sequence=input("Insert binary sequence : ")
  winner=max(sequence.split('1')+ sequence.split('0'), key=len)
  print("{}'s have the biggest sequence with length : {}".format(winner[0], len(winner)))
  
  
def biggest_sequence3():
  import re
  sequence=input("Insert binary sequence : ")
  winner=max((re.findall('1+|0+', sequence)), key=len)
  print("{}'s have the biggest sequence with length : {}".format(winner[0], len(winner)))
