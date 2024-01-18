import pickle
import product
import json
import csv
import pandas as pd
l=[]

#with open("filtered_data.json") as fp:
with open("filtered_data.csv",'r') as f:
    reader=csv.reader(f)
    keys=next(reader)
    for row in reader:
        l.append(dict(zip(keys,row)))
with open("filtered_data.json","w") as fp:
    json.dump(l,fp)

#filtered_sku_numbers = [row["SKU_number"] for _, row in df.iterrows() if float(row["StrengthFactor"]) > strengthfactor_threshold]




#pickle file
la=[]
with open("filtered_data.csv") as fp:
    read=csv.reader(fp)
    col=next(read)


    with open("SalesData.pkl","wb") as binary_file:
        for row in read:
            la.append(product.Product(','.join(row)))
        pickle.dump(la,binary_file) #dumping the sorted Data into .pkl file