students_by_regions_finland = {
'uusimaa': 1000000,
'nothern ostrobothina': 900000,
'eastern finlnad': 900000
} #created a dictionary with a name students_by_regions_finland and passed key and its respected values 
sort_dict=sorted(students_by_regions_finland.items(),key=lambda x:x[0])  
#the sorted function in dictionary is used to sort the key values accordingly using items() method 
print(sort_dict)