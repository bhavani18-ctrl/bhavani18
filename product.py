class Product:
    def __init__(self, line):
        # Split the csv line into a line of values
        values = line.split(',')
        
        #Assign values into attributes
        self.File_type = values[0]
        self.SKU_number = int(values[1])
        self.SoldFlag = values[2]
        self.ReleaseNumber = int(values[3])
        self.StrengthFactor = float(values[4])
        self.PriceReg = float(values[5])
        self.ReleaseYear = int(values[6])
        self.ItemCount = int(values[7])
        self.LowUserPrice = float(values[8])
        self.LowNetPrice = float(values[9])

p=Product("0,1,2,3,4,5,6,7,8,9")  
print(p.File_type,p.ItemCount)