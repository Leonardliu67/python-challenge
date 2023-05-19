import os
import csv

#get current dir
os.getcwd()

#open file 
df_bank = os.path.join("..","Resources","budget_data.csv")
counter = 0
p_total = 0
p_list = []
dif_list =[]

#use counter to go through all rows in file, find total month and total net loss/gain

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
        
    
    
#make a list to find the largest and smallest change
    length = len(p_list) - 1
    
    for i in range (0,length):

        dif_list.append(p_list[i+1] - p_list[i])
   
       
    avg_change = round(sum(dif_list) / len(dif_list),2)

    max_dif = max(dif_list)
    min_dif = min(dif_list)

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months:  {counter}")
    print(f"Total:  ${p_total}")
    print(f"Average Change:  ${avg_change}")
    print(f"Greatest Increase in Profits:  (${max_dif})")
    print(f"Greatest Decrease in Losses:   (${min_dif})")
    

    

budget_file = os.path.join("Output", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {counter}\n")
    outfile.write(f"Total:  ${p_total}\n")
    outfile.write(f"Average Change:  ${avg_change}\n")
    outfile.write(f"Greatest Increase in Profits:   (${max_dif})\n")
    outfile.write(f"Greatest Decrease in Losses:  (${min_dif})\n")