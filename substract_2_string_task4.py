class String():

    def __init__(self,st):
        self.data = st
    def __del__(self):
        print('Deleted')

    
    def __sub__(self,obj):
        for i in obj.data:
            
            if(i in self.data):
                n = len(self.data)
                ind = self.data.index(i)
                self.data = self.data[:ind:]+self.data[ind+1::]

        return self.data        

string1 = input("Enter first string : ")
string2 = input("Enter second string : ")
s1 = String(string1)
s2 = String(string2)
print("difference (first string - second string) = ",s1-s2)
