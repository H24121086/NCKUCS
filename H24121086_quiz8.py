import csv

# Function to read NBA standings from CSV file
def read_nba_standings(nba_standings):
    standings = []
    with open("nba_standings.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            standings.append(row)
    return standings

# Question 1: Teams from the Eastern Conference with Home win-loss percentage lower than Away
def teams_home_win_loss_lower(standings):
    eastern_teams = [team for team in standings if team['Conference'] == 'Eastern']
    result = [team[1] for team in eastern_teams if float(team[7].split('-')[0]) / (float(team[7].split('-')[0]) + float(team[7].split('-')[1])) < float(team[8].split('-')[0]) / (float(team[8].split('-')[0]) + float(team[8].split('-')[1]))]
    return result

# Question 2: Conference with higher average difference between PF and PA
def higher_average_difference(standings):
    eastern_difference = []
    western_difference = []
    for team in standings:
        difference = int(team['PF']) - int(team['PA'])
        if team['Conference'] == 'Eastern':
            eastern_difference.append(difference)
        else:
            western_difference.append(difference)
    avg_eastern_difference = sum(eastern_difference) / len(eastern_difference)
    avg_western_difference = sum(western_difference) / len(western_difference)
    return "Eastern" if avg_eastern_difference > avg_western_difference else "Western"

# Question 3: Generate ranking list based on win percentage against other conference teams
def generate_ranking(standings):
    win_percentage = {}
    for team in standings:
        win_percentage[team['Team']] = float(team['Home'].split('-')[0]) / (float(team['Home'].split('-')[0]) + float(team['Home'].split('-')[1]))
    sorted_teams = sorted(win_percentage.items(), key=lambda x: x[1], reverse=True)
    ranking_list = [team[0] for team in sorted_teams]
    return ranking_list

# Main function to execute the program
def main():
    # Read NBA standings from CSV file
    standings = read_nba_standings('nba_standings.csv')
    
    # Question 1
    print("(1) Teams from the Eastern Conference with Home win-loss percentage lower than Away:")
    print(teams_home_win_loss_lower(standings))
    print()
    
    # Question 2
    print("(2) Conference with higher average difference between PF and PA:")
    print(higher_average_difference(standings))
    print()
    
    # Question 3
    print("(3) Ranking list of all teams based on win percentage against other conference teams:")
    print(generate_ranking(standings))

if __name__ == "__main__":
    main()