s=input("Введіть рядок: ")
s=min(s.split(),key=len)
print("Найкоротше слово", s)
wordlen=len(s)
i=None
while wordlen!=0:
    x=s[wordlen-1]
    if i is None:
        i=x
    else:
        i=i+x
    wordlen=wordlen-1
if s==i:
    print("Слово",s,"- поліндром")
else:
    print("Слово",s,"- не поліндром")
print(s, i)