import csv
# Create a Datamanager instances and load the fitered dataset
class DataManager:
    def __init__(self):
        filename = "filtered_data.csv"
        
        
        with open(filename,'r') as input:
            self.reader = csv.DictReader(input)
            
            self.header = next(self.reader)
            self.list_csv=[x for x in self.reader]
     
     # Display the loaded data
    def display(self):

        lengths = [key for key in self.header.keys()]
        values = [value for value in self.header.values()]

        File_width = len(lengths[0])+5
        SkU_width = len(lengths[1])+5
        Sold_width = len(lengths[2])+5
        ReleaseNum_width = len(lengths[3])+5
        Strength_width = len(lengths[4])+8
        Price_width = len(lengths[5])+5
        Release_width = len(lengths[6])+5
        Item_width = len(lengths[7])+5
        User_width = len(lengths[8])+5
        net_width = len(lengths[9])+5
        print("-" * (10+File_width + SkU_width + Sold_width + ReleaseNum_width+ Strength_width + Price_width + Release_width + Item_width + User_width + net_width + 10))

        print("{:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}}".format("File_type",File_width, "SKU_number", SkU_width,"Sold_Flag",Sold_width,"ReleaseNumber",ReleaseNum_width,"StrengthFactor",Strength_width,"PriceReg",Price_width,"ReleaseYear",Release_width,"ItemCount",Item_width,"LowUserPrice",User_width,"LowNetPrice",net_width))
        print("-" * (10+File_width + Sold_width + Strength_width + Price_width + Release_width + Item_width + User_width + net_width + 10))
        # print("{:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} ".format(values[0],File_width,values[1],SKU_width,values[2],Sold_width,values[3],ReleaseNum_width,values[4],Strength_width,values[5],Price_width,values[6],Release_width,values[5],Item_width,values[6],User_width,values[7],net_width))
        count=0
        for row in self.list_csv:
            count+=1
            if(count == 5):
                break
            print("{:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}}".format(row['File_Type'],File_width,row['SoldFlag'],Sold_width,row['StrengthFactor'],Strength_width,row['PriceReg'],Price_width,row['ReleaseYear'],Release_width,row['ItemCount'],Item_width,row['LowUserPrice'],User_width,row['LowNetPrice'],net_width))
        print("-" * (10+File_width + Sold_width + Strength_width + Price_width + Release_width + Item_width + User_width + net_width + 10))
        
# Sort data based on a column
    def sort(self,col):
        self.list_csv=sorted(self.list_csv,key=lambda x: float(x[col]))

        rows = [list(row.values()) for row in self.list_csv]
# filter data based on a certain condition
    def filter(self, column_name, condition):

        #self.data = [self.list_csv[0]] + [row for row in self.list_csv[1:] if row[column_name] == condition]
        self.list_csv=[row for row in self.list_csv if float(row[column_name]) == float(condition)]


        
d=DataManager()
d.display()
d.sort("ReleaseYear")
d.display()
d.filter("ItemCount",20)
print(f"Sorted data after function:")
d.display()


