text1 = open('D:\Git\sliderAnalysis\oldoutput.txt')
list3=text1.read().split('  ')
so = set(list3)
text1.close()

text = open('D:\Git\sliderAnalysis\input.txt','r')
list1 = text.readlines()
list2=[]
list4=[]
list5=[]

for i  in list1:
    i=i[:-1]
    k = i.split(' ')
    for j  in k:
        if 4 < len(j) < 12:
            list2.append(j)

for i in list2:
    if i[-1]==',':
        i = i[:-1]
        list4.append(i)
    elif i[-1]=='.':
        i = i[:-1]
        list4.append(i)
    elif i[-1]=='?':
        i = i[:-1]
        list4.append(i)
    elif i[-1]=='"':
        i=i[:-1]
        list4.append(i) 
    elif i[0]=='"':
        i=i[:-1]
        list4.append(i) 
    else:
        list4.append(i)  
        
text.close()
        
s1 = set(list4)
s3 = s1 - so
out = open('D:\Git\sliderAnalysis\output1.txt','w')
for i in s3:
    out.write(i)
    out.write("  ")

out.close()     
   


