#def returnsum(dict):
    #sum = 0
    #for i in dict:
        #sum=sum+dict[i]
    #return sum
#dict={'a':100,'b':200,'c':300}
#print("sum:" ,returnsum(dict))        
    
def  returnsum(dict):
    return sum(dict.values())


dict={'a':100,'b':200,'c':300}
print("sum:" ,returnsum(dict)) 
