text1 = open('D:\Git\sliderAnalysis\oldoutput.txt')
list3=text1.read().split('  ')
oldput = set(list3)
text1.close()
text2 = open('D:\Git\sliderAnalysis\output.txt')
Loutput=text2.read().split('  ')
output=set(Loutput)
text2.close()

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
        
input = set(list4)
output = input - oldput
#output2 = output1 - output上下文修改了代码，这里还没改
out = open('D:\Git\sliderAnalysis\output.txt','w')
for i in output:
    out.write(i)
    out.write("  ")

out.close()    

out2 = open('D:\Git\sliderAnalysis\output2.txt','w')
for i in output2:
    out2.write(i)
    out2.write("  ")
 
out2.close() 
 
   


