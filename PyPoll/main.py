import os
import csv

#Reading the Path

pypollpath = os.path.join("Resources/election_data.csv")

#Setting variables to store results

total_votes = 0
list_of_candidates = []
winner = ''
candidate_votes = {}


#Reading CSV file

with open (pypollpath, 'r') as election:
    election_reader = csv.reader(election, delimiter= ',')
    
    #Skipping header line
    
    header = next(election_reader)
    #print(header)
    
    #Finding the total amount of candidates
    
    for row in election_reader:
        total_votes += 1
        candidate = row[2]

        if candidate not in list_of_candidates:
            list_of_candidates.append(candidate)
            
            candidate_votes[candidate] = 0
        
        candidate_votes[candidate]= candidate_votes[candidate] + 1 
        
  
      
     #Setting votes per candidate
     
    votes_per_candidate = [*candidate_votes.values()] 
 
      
    perc_candidate1 = round((candidate_votes[list_of_candidates[0]]/total_votes)*100,3)
    perc_candidate2 = round((candidate_votes[list_of_candidates[1]]/total_votes)*100,3)  
    perc_candidate3 = round((candidate_votes[list_of_candidates[2]]/total_votes)*100,3)    
    

    
    winner = max(candidate_votes, key=candidate_votes.get)
    
    
    #Printing the analysis result
    
    analysis_result = (f"                            \n"
      f"Election Results \n"
      f"                            \n"
      f"----------------------------\n"
      f"                            \n"
      f"Total Votes: {total_votes} \n"
      f"                            \n"
      f"----------------------------\n"
      f"                            \n"
      f"{list_of_candidates[0]}: {perc_candidate1}% ({votes_per_candidate[0]})\n"
      f"{list_of_candidates[1]}: {perc_candidate2}% ({votes_per_candidate[1]})\n"
      f"{list_of_candidates[2]}: {perc_candidate3}% ({votes_per_candidate[2]})\n"
      f"                            \n"
      f"----------------------------\n"
      f"                            \n"
      f"Winner: {winner}"
      f"                            \n"
      f"                            \n"
      f"----------------------------\n")
     
    
    print (analysis_result)
    
 #Converting to txt and exporting
 
pypoll_file = os.path.join('Analysis/pypoll_results.text')   

with open(pypoll_file, "w") as txt_file:
    txt_file.write(analysis_result)