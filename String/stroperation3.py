#string searching for text
word="this is actually a good thing to start with it"
#searching pattern good in word
print(word.find('good'))
#returns the first position in word where pattern ocurs
print(word.find('good',0,10))
#return -1 if no occurance of pattern within that limit
#index also used, raise value error if pattern not found
print(word.index('good'))
print(word.index('good',0,10))
#replace
print(word)
print(word.replace('good','awesome'))
# replaces good by awesome


