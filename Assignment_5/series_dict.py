# create a pandas series from dictionary
# create a pandas series from lists


import pandas as pd

# pandas series from dictionary
data1={101:"bhumi",102:"chetan",103:"aditya",104:"ali",105:"badal"}
series_dict=pd.Series(data1)
print("Pandas series from dictionary:")
print(series_dict)

# pandas series from lists
data2=["Naruto","Obito","Kakashi","Rin","Itachi"]
series_list=pd.Series(data2,index=[101,102,103,104,105])
print("")
print("Pandas series from lists:")
print(series_list)

print("")
print("Element of 101 Index in series_dict is:",series_dict[101])       # access the element of 101 index from series_dict
print("")
print("Element of 101 to 103 Index from series_list:")                  # access the element from label 101 to 103 from series list
print(series_list[0:3])