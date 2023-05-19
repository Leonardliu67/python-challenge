import os
import csv


os.chdir("C:\\Users\\liush\\Documents\\UTBC\\Assignment 3\\PyBank\\Resources")
os.getcwd()

df_bank = os.path.join("..","Resources","budget_data.csv")
counter = 0
p_total = 0
p_list = []
dif_list =[]



with open(df_bank) as bank_file:
    df_bank1 = csv.reader(bank_file, delimiter=",")
    for row in df_bank1:
        if row[0] == "Date" :
            counter = 0
        else: 
            counter = counter + 1 
        if row[1] == 'Profit/Losses':
            p_total = 0
        else:
            row[1] != " "
            p_total = p_total + int(row[1])
            p_list.append(int(row[1]))
        
    
    #for i in dif_list:
    length = len(p_list) - 1
    print(length)
    for i in range (0,length):

        dif_list.append(p_list[i+1] - p_list[i])
    print(dif_list)    
       
    avg_change = round(sum(dif_list) / len(dif_list),2)

    max_dif = max(dif_list)
    min_dif = min(dif_list)

    print(max_dif)
    print(min_dif)
    print(avg_change)
    print(counter)
    print(p_total)       
    
    #print(f"total count:   {counter}")
    #print(f"Total Profit/Losses:  + {p_total}")
