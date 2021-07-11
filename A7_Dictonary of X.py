def func_create_myDict():
    i='y'
    myDict = dict()

    while (i=='y' or i=='Y'):
        word = input("\nEnter word : ")
        meaning = input("Enter meaning of word : ")
        myDict.update({word : meaning})
        print() #Move Control to next line
        i=input("Do u want to enter more words (Y/N) : ")
    return myDict

def func_create_synonym_dict(myDict):
    synonym_dict = dict()
    for i in myDict:
        list_synonym = []
        for j in myDict:
            if(i!=j and myDict[i]==myDict[j]):
                if i not in sum(list(synonym_dict.values()),[]) :#flattening list
                    list_synonym.append(j)
                    new=myDict[j]
        if (list_synonym != []):
            list_synonym.append(new)
            synonym_dict[i]=list_synonym        
    return synonym_dict

def find_meaning_of_word(myDict):
    word=input("\nEnter a word to find its meaning : ")
    meaning=myDict[word]
    print("\nMeaning of word --> \"",word,"\" is --> ",meaning)
    
def find_synonym_of_word_iterative(synonym_dict,x):
    synDict = list(synonym_dict.items())
    
    synonym_list =[]
   
    if x in synonym_dict.keys():
        return synonym_dict[x]
    
    else:
        for i in synDict:
            for j in i:
                for k in j:
                    if(k==x):
                        key_list=list(synonym_dict.keys())
                        value_list=list(synonym_dict.values())
                        position=value_list.index(j)
                        key_of_j=(key_list[position])
                        j.append(key_of_j)
                        synonym_list=j
        if x in synonym_list:
            synonym_list.remove(x)
        return synonym_list
     
def main():
    
    myDict = dict()
    synonym_dict = dict()

    myDict = func_create_myDict()
    
    synonym_dict = func_create_synonym_dict(myDict)
    
    print("\nmyDict : ",myDict)
    print("\nsynonym_dict : ",synonym_dict)
    
    find_meaning_of_word(myDict)
    
    word = input("\nEnter word to find synonym : ")
    syn =[]
    syn =find_synonym_of_word_iterative(synonym_dict,word)
    print("\nSynonyms of --> ",word," are --> ",syn)

    
main()  

