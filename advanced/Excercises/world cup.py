from collections import OrderedDict

spain=OrderedDict(wins=0, loses=0, draws=0, goaldifference=0, points=0)
iran=OrderedDict(wins=0, loses=0, draws=0, goaldifference=0, points=0) 
portugal=OrderedDict(wins=0, loses=0, draws=0, goaldifference=0, points=0)
morocco=OrderedDict(wins=0, loses=0, draws=0, goaldifference=0, points=0)
n=0
for i in range(6):
    while n==0:
        result=input()
        result=result.split('-')
        result=[int(j) for j in result]
        n+=1
        goal_difference=result[0]-result[1]
        if goal_difference>0:
            iran['wins']+=1
            iran['loses']+=0
            spain['wins']+=0
            spain['loses']+=1
            iran['points']+=3
            iran['goaldifference']+=goal_difference
            spain['goaldifference']-=goal_difference
        if goal_difference<0:
            iran['wins']+=0
            iran['loses']+=1
            spain['wins']+=1
            spain['loses']+=0
            spain['points']+=3
            spain['goaldifference']+=goal_difference
            iran['goaldifference']-=goal_difference
        if goal_difference == 0:
            spain['draws']=+1
            iran['draws']=+1
            iran['points']+=1
            spain['points']+=1
    while n==1:
        result=input()
        result=result.split('-')
        result=[int(j) for j in result]
        n+=1
        goal_difference=result[0]-result[1]
        if goal_difference>0:
            iran['wins']+=1
            iran['loses']+=0
            portugal['wins']+=0
            portugal['loses']+=1
            iran['points']+=3
            iran['goaldifference']+=goal_difference
            portugal['goaldifference']-=goal_difference
        if goal_difference<0:
            iran['wins']+=0
            iran['loses']+=1
            portugal['wins']+=1
            portugal['loses']+=0
            portugal['points']+=3
            portugal['goaldifference']+=goal_difference
            iran['goaldifference']-=goal_difference
        if goal_difference == 0:
            portugal['draws']=+1
            iran['draws']=+1
            iran['points']+=1
            portugal['points']+=1
    while n==2:
        result=input()
        result=result.split('-')
        result=[int(j) for j in result]
        n+=1
        goal_difference=result[0]-result[1]
        if goal_difference>0:
            iran['wins']+=1
            iran['loses']+=0
            morocco['wins']+=0
            morocco['loses']+=1
            iran['points']+=3
            iran['goaldifference']+=goal_difference
            morocco['goaldifference']-=goal_difference
        if goal_difference<0:
            iran['wins']+=0
            iran['loses']+=1
            morocco['wins']+=1
            morocco['loses']+=0
            morocco['points']+=3
            morocco['goaldifference']+=goal_difference
            iran['goaldifference']-=goal_difference
        if goal_difference == 0:
            morocco['draws']=+1
            iran['draws']=+1
            iran['points']+=1
            morocco['points']+=1
    while n==3:
        result=input()
        result=result.split('-')
        result=[int(j) for j in result]
        n+=1
        goal_difference=result[0]-result[1]
        if goal_difference>0:
            spain['wins']+=1
            spain['loses']+=0
            portugal['wins']+=0
            portugal['loses']+=1
            spain['points']+=3
            spain['goaldifference']+=goal_difference
            portugal['goaldifference']-=goal_difference
        if goal_difference<0:
            spain['wins']+=0
            spain['loses']+=1
            portugal['wins']+=1
            portugal['loses']+=0
            portugal['points']+=3
            portugal['goaldifference']+=goal_difference
            spain['goaldifference']-=goal_difference
        if goal_difference == 0:
            portugal['draws']=+1
            spain['draws']=+1
            spain['points']+=1
            portugal['points']+=1
    while n==4:
        result=input()
        result=result.split('-')
        result=[int(j) for j in result]
        n+=1
        goal_difference=result[0]-result[1]
        if goal_difference>0:
            spain['wins']+=1
            spain['loses']+=0
            morocco['wins']+=0
            morocco['loses']+=1
            spain['points']+=3
            spain['goaldifference']+=goal_difference
            morocco['goaldifference']-=goal_difference
        if goal_difference<0:
            spain['wins']+=0
            spain['loses']+=1
            morocco['wins']+=1
            morocco['loses']+=0
            morocco['points']+=3
            morocco['goaldifference']+=goal_difference
            spain['goaldifference']-=goal_difference
        if goal_difference == 0:
            morocco['draws']=+1
            spain['draws']=+1
            spain['points']+=1
            morocco['points']+=1
    while n==5:
        result=input()
        result=result.split('-')
        result=[int(j) for j in result]
        n+=1
        goal_difference=result[0]-result[1]
        if goal_difference>0:
            portugal['wins']+=1
            portugal['loses']+=0
            morocco['wins']+=0
            morocco['loses']+=1
            portugal['points']+=3
            portugal['goaldifference']+=goal_difference
            morocco['goaldifference']-=goal_difference
        if goal_difference<0:
            portugal['wins']+=0
            portugal['loses']+=1
            morocco['wins']+=1
            morocco['loses']+=0
            morocco['points']+=3
            morocco['goaldifference']+=goal_difference
            portugal['goaldifference']-=goal_difference
        if goal_difference == 0:
            morocco['draws']=+1
            portugal['draws']=+1
            portugal['points']+=1
            morocco['points']+=1

iran_new=dict()
spain_new=dict()
portugal_new=dict()
morocco_new=dict()

for each in iran:
    iran_new[each]=iran[each]
for each in spain:
    spain_new[each]=spain[each]
for each in portugal:
    portugal_new[each]=portugal[each]
for each in morocco:
    morocco_new[each]=morocco[each]

country_list=[('Iran',iran_new),('Spain',spain_new),('Portugal',portugal_new),('Morocco',morocco_new)]

sorted_list = sorted(country_list, key=lambda x: (-x[1]['points'], -x[1]['wins'], x[0]))
for each in sorted_list:
    print(each[0],each[1])