# Dropping columns : The columns i am removing order, marketing_type, new_release_flag, soldcount

# Reason to dropping : 
# 1)Oder : Order is identfying the sequential number but in dataset already 
# sku_number is identifying the data. So the order can be ignored.

# 2)marketing_type : Marketing_type is how the data is marketed, it has more 
# meaning to idetify the data indepently for each type. So the marketing_type can be ignored.
    
# 3)New_release_flag : New_release_flag is product of any future release.So it can be ignored.

# 4)sold count : The sold count information is already in sold flag. 
#             So the sold count can be ignored.

# Important columns : Strength Factor, Price_reg 

# 1) SolD flag: The Sold flag represents the sold happens in last month. 

# 2)SKU_number : It represents the unique indentifier.

# 2) Price Reg : The price reg represents the price of the product. So the price reg is important.