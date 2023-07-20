import os   
import csv

#Reading the path
pybankpath = os.path.join("Resources/budget_data.csv") 

#Setting the variable
total_num_months = 0
total_net = 0
total_change = []
average_change = 0.00
inc_profit = 0
dec_profit = 0
best_month = 0
worst_month = 0
monthly_change = []



with open (pybankpath) as pybank_file:
    pybank_reader = csv.reader(pybank_file, delimiter= ",")
    
#Print header
    py_header = next(pybank_reader)
    print(py_header)
    
    py_first_row = next(pybank_reader)
    print(py_first_row)
    value = int(py_first_row[1])
    total_num_months = 1
    total_net = int(py_first_row[1])
    
#Finding the total amount of months

    for row in pybank_reader:
        total_num_months +=  1
        
   
    
#Finding the total net profit/losses
        total_net += int(row[1])
        
#Calculating monthly changes
      
        
        change = int(row[1]) - value
        
        
        value = int(row[1])
        
        
        monthly_change.append(row[0])
        total_change.append(change)
        
           
    
    average_change =round(sum(total_change)/(len(total_change)),2)
    
    inc_profit = max(total_change)
    dec_profit = min(total_change)
    
    inc_prof_index = total_change.index(inc_profit)
    dec_prof_index = total_change.index(dec_profit)

    best_month = monthly_change[inc_prof_index]
    worst_month = monthly_change[dec_prof_index]


# Printing the analysis result

analysis = (f"      \n"
            f" Financial Analysis  \n"
            f"-------------------------\n"
            f"          \n"
            f"Total Months: {total_num_months}   \n"
            f"          \n"
            f"Total: ${total_net}     \n"
            f"          \n"
            f"Average Change: ${average_change}      \n"
            f"          \n"
            f"Greatest Incresse in Profits: {best_month} (${inc_profit})     \n"
            f"          \n"
            f"Greatest Decrease in Profits: {worst_month} (${dec_profit})     \n" )


print(analysis)
          
#Saving and exporting file

output_file = os.path.join('Analysis/PyBank_Analysis.txt')

with open (output_file, "w") as txt_file:
    txt_file.write(analysis)              
            
            
            