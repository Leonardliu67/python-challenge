import os
import csv


os.chdir("C:\\Users\\liush\\Documents\\UTBC\\Assignment 3\\PyPoll\\Resources")
os.getcwd()

counter = 0




c_1 = 0
c_2 = 0
c_3 = 0
total_cand_list = []
candi_list =[]
df_poll = os.path.join("..","Resources","election_data.csv")

with open(df_poll) as poll_file:
    df_poll_1 = csv.reader(poll_file, delimiter=",")
    for row in df_poll_1:
        if row[0] == "Ballot ID" :
            counter = 0
        else: 
            counter = counter + 1 
        
        if row[2] != "Candidate":
            candi_list.append(row[2])




        

    total_cand_list = list(set(candi_list))
    
    c_n1 = total_cand_list[0]
    c_n2 = total_cand_list[1]
    c_n3 = total_cand_list[2]

             
    

    for name in candi_list:
        if total_cand_list[0] == name:
            c_1 +=1
        elif total_cand_list[1] == name:
            c_2 += 1
        elif total_cand_list[2] == name:
            c_3 += 1

    c1_pctg = round((c_1 / (c_1 + c_2 + c_3)) * 100,2)
    c2_pctg = round((c_2 / (c_1 + c_2 + c_3)) * 100,2)
    c3_pctg = round(100 - c1_pctg - c2_pctg,2)
    
    
    
    print("Election Results \n"
    "-------------------------------------")
    
    print("Total Votes :" + str(counter))

    print(c_n1 +":"+str(c1_pctg)+"%" + str(c_1))
    print(c_n2 +":"+str(c2_pctg)+"%" + str(c_2))
    print(c_n3 +":"+str(c3_pctg)+"%" + str(c_3))

    print()
    
    
    w_d = {}
    keys = [c_n1,c_n2,c_n3]
    values =[c1_pctg , c2_pctg, c3_pctg]
    for name in keys:
        for value in values:
            w_d[name] = value
            values.remove(value)
            break
    
    # max_val = max(w_d)
    # print(max_val)

    print("Winner: " + (max(w_d, key = w_d.get)))
   





        
       

