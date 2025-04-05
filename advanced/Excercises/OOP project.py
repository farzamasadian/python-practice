import random 

class Human:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
class Footballer(Human):
    def team_assignment(self,team):
        self.team=team        
    def get_team(self):
        return self.team

# teams=['A','B']
# team=random.choice(teams)

team_a=[]
team_b=[]
teams=[]
for i in range(22):
    n=input('Player\'s name: ')
    teams.append(n)
random.shuffle(teams)

teams = [Footballer(i) for i in teams]
for i in teams[:11]:
    team_a.append(i)
for j in teams[11:]:
    team_b.append(j)

# team_a = [team_a.append(i) for i in teams[:11]]
# team_b = [team_b.append(i) for i in teams[11:21]]

for i in team_a:
    i.team_assignment('A')
    print(i.get_name(), i.get_team())
for i in team_b:
    i.team_assignment('B')
    print(i.get_name(), i.get_team())