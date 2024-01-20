
# Python3 code here creating class
class geeks: 
    def __init__(self, nam, roll): 
        self.nam = nam 
        self.roll = roll
   
# creating list       
list = [] 
  
# appending instances to list 
list.append( geeks('Akash', 2) )
list.append( geeks('Deependra', 40) )
list.append( geeks('Reaper', 44) )
  
for obj in list:
    print( obj.nam, obj.roll, sep =' ' )