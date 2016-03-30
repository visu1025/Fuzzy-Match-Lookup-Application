#author: Venkatga Kasi Viswanath Yeleswarapu
#Fuzzy search of excel sheet
#written in Python 3.4.3 might not be compatible with other versions of Python
import csv
from difflib import SequenceMatcher as SM
#thresholds for key words and names
THETA1=0.60 #threshold for names
THETA=0.60 #threshold for key words

print('--------------------------------------', end='\n')
print('Press 1 if you want to search by name', end='\n')
print('Press 2 if you want to search by key word', end='\n')
print('Press QUIT to end the search', end='\n')
print('--------------------------------------', end='\n') 
choice=input('Enter your choice:')
choice=choice.upper()
print(end='\n')
while (choice!='QUIT'): 
   
    if choice=='1':
       
        print('searching by name', end='\n')
        Name=input('enter the name of the professor\n')
        print('--------------------------------------', end='\n') 
    if choice=='2':
       
        print('searching by keyword', end='\n')
        Key=input('Enter the keyword\n')
        print('--------------------------------------', end='\n') 
       
    with open('projectdatabase.csv','rU') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if choice=='1':
                fullName= row['Name (First)'] + row['Name (Last)']
                if SM(None, Name , fullName).ratio() > THETA1:
                    print(row['Name (First)'], row['Name (Last)'],end='\n')
                    print(row['Keyword Phrase 1'], row['Keyword Phrase 2'], row['Keyword Phrase 3'], row['Keyword Phrase 4'], row['Keyword Phrase 5'], row['Keyword Phrase 6'])
                    print(end='\n')
                else:
                    if SM(None, Name , row['Name (First)']).ratio() > THETA1:
                        print(row['Name (First)'], row['Name (Last)'],end='\n')
                        print(row['Keyword Phrase 1'], row['Keyword Phrase 2'], row['Keyword Phrase 3'], row['Keyword Phrase 4'], row['Keyword Phrase 5'], row['Keyword Phrase 6'])
                        print(end='\n')
                
                    if SM(None, Name, row['Name (Last)']).ratio() > THETA1:
                        print(row['Name (First)'], row['Name (Last)'],end='\n')
                        print(row['Keyword Phrase 1'], row['Keyword Phrase 2'], row['Keyword Phrase 3'], row['Keyword Phrase 4'], row['Keyword Phrase 5'], row['Keyword Phrase 6'])
                        print(end='\n')
            if choice=='2':
                keyWords=Key.split()
                max=len(keyWords)
                
                Phrases1=row['Keyword Phrase 1'].split()
                Phrases2=row['Keyword Phrase 2'].split()
                Phrases3=row['Keyword Phrase 3'].split()
                Phrases4=row['Keyword Phrase 4'].split()
                Phrases5=row['Keyword Phrase 5'].split()
                Phrases6=row['Keyword Phrase 6'].split()
                found=[0,0,0,0,0,0]
                i=0
                for keyWord in keyWords:
                    keyWord=keyWord.upper()
                    
                    
                    for Phrase1 in Phrases1:
                        Phrase1=Phrase1.upper()
                        
                        if SM(None, keyWord, Phrase1).ratio() > THETA:
                            found[0]+=1
                            if (found[0]==max):
                                print(row['Name (First)'], row['Name (Last)'], row['Keyword Phrase 1'])
                                print(end='\n')
                            
                            break
                    for Phrase2 in Phrases2:
                        Phrase2=Phrase2.upper()
                        if SM(None, keyWord, Phrase2).ratio() > THETA:
                            found[1]+=1
                            if (found[1]==max):
                                print(row['Name (First)'], row['Name (Last)'], row['Keyword Phrase 2'])
                                print(end='\n')
                            
                            break
                    for Phrase3 in Phrases3:
                        Phrase3=Phrase3.upper()
                        if SM(None, keyWord, Phrase3).ratio() > THETA:
                            found[2]+=1
                            if (found[2]==max):
                                print(row['Name (First)'], row['Name (Last)'], row['Keyword Phrase 3'])
                                print(end='\n')
                            
                            break
                    for Phrase4 in Phrases4:
                        Phrase4=Phrase4.upper()
                        if SM(None, keyWord, Phrase4).ratio() > THETA:
                            found[3]+=1
                            if (found[3]==max):

                                print(row['Name (First)'], row['Name (Last)'], row['Keyword Phrase 4'])
                                print(end='\n')
                            
                            break
                    for Phrase5 in Phrases5:
                        Phrase5=Phrase5.upper()
                        if SM(None, keyWord, Phrase5).ratio() > THETA:
                            found[4]+=1
                            if (found[4]==max):
                                print(row['Name (First)'], row['Name (Last)'], row['Keyword Phrase 5'])
                                print(end='\n')
                            
                            break
                    for Phrase6 in Phrases6:
                        Phrase6=Phrase6.upper()
                        if SM(None, keyWord, Phrase6).ratio() > THETA:
                            found[5]+=1
                            if (found[5]==max):
                                print(row['Name (First)'], row['Name (Last)'], row['Keyword Phrase 6'])
                                print(end='\n')
                            break

    print('--------------------------------------', end='\n') 
    choice=input('Enter your choice\n');
    choice=choice.upper()
    print('--------------------------------------', end='\n') 
