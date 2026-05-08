# Q2.Write a script to analyze cricket stats for a team.

first_player_run = int(input("Enter First Player Scored Runs  : "))
Second_player_run = int(input("Enter Second Player Scored Runs : "))
Third_player_run = int(input("Enter Third Player Scored Runs  : "))
fourth_player_run = int(input("Enter Fourth Player Scored Runs : "))
fifth_player_run = int(input("Enter Fifth Player Scored Runs  : "))

Total_runs_scored_by_allPlayers = first_player_run + Second_player_run + Third_player_run + fourth_player_run + fifth_player_run
print(f"Total Runs Scored by All Players  : {Total_runs_scored_by_allPlayers}")
Average_Runs = Total_runs_scored_by_allPlayers/5
print(f"Average Runs : {Average_Runs}")