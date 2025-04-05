import csv
from statistics import mean 
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    with open(f'/Users/farzam/Desktop/Python/Exercise/{input_file_name}','r') as csvfile, open(f'/Users/farzam/Desktop/Python/Exercise/{output_file_name}','w') as target:
        reader = csv.reader(csvfile)
        for row in reader:
            name=row[0]
            grades=[float(numbers) for numbers in row[1:]]
            grades_mean=mean(grades)
            writer = csv.writer(target)
            writer.writerow([name, grades_mean])

def calculate_sorted_averages(input_file_name, output_file_name):
    with open(f'/Users/farzam/Desktop/Python/Exercise/{input_file_name}','r') as csvfile, open(f'/Users/farzam/Desktop/Python/Exercise/{output_file_name}','w') as target:
        od1=OrderedDict()
        od2=OrderedDict()
        reader = csv.reader(csvfile)
        for row in reader:
            name = row[0]
            grade = float(row[1])      
            od1[name]=grade
        grades=list(od1.values())
        grades2=[]
        for i in grades:
            grades2.append(i)
        grades2.sort()
        grades=grades2
        for i in grades:
            for j in od1:
                if i == od1[j]:
                    od2[j] = i
        writer = csv.writer(target)
        for each in od2:
            writer.writerow([each,od2[each]])
 
def calculate_three_best(input_file_name, output_file_name):
    with open(f'/Users/farzam/Desktop/Python/Exercise/{input_file_name}','r') as csvfile, open(f'/Users/farzam/Desktop/Python/Exercise/{output_file_name}','w') as target:
        reader=csv.reader(csvfile)
        writer=csv.writer(target)
        od1=OrderedDict()
        for row in reader:
            name=row[0]
            grade=row[1]
            od1[name]=grade
        grades=list(od1.values())    
        n=0
        l=[]
        while n<=2:
            n+=1
            l.append(grades.pop())
        od2=OrderedDict()
        for i in l:
            for j in od1:
                if i == od1[j]:
                    od2[j] = i
        for each in od2:
            writer.writerow([each,od2[each]])

calculate_three_best('grade_mean_sorted.csv', 'three_best')

def calculate_three_worst(input_file_name, output_file_name):
    with open(f'/Users/farzam/Desktop/Python/Exercise/{input_file_name}','r') as csvfile, open(f'/Users/farzam/Desktop/Python/Exercise/{output_file_name}','w') as target:
        reader=csv.reader(csvfile)
        writer=csv.writer(target)
        od1=OrderedDict()
        for row in reader:
            name = row[0]
            grade = row[1]
            od1[name]=grade
        grades=list(od1.values())    
        n=0
        l=[]
        grades=[float(i) for i in grades]
        grades.sort(reverse=True)
        while n<=2:
            n+=1
            l.append(grades.pop())
        l=[str(i) for i in l]
        [writer.writerow([i]) for i in l]

calculate_three_worst('grade_mean_sorted.csv', 'three_worst')

    
    