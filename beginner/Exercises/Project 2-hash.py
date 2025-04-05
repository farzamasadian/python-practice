import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    with open(f'/Users/farzam/Desktop/Python/Exercise/{input_file_name}','r') as csvfile, open(f'/Users/farzam/Desktop/Python/Exercise/{output_file_name}','w') as target:
        reader=csv.reader(csvfile) 
        writer=csv.writer(target)
        od1=OrderedDict()
        od2=OrderedDict()
        for i in range(0,10000):
            i=str(i)
            j=hashlib.sha256(str(i).encode('utf-8')).hexdigest()
            od1[j]=i
        for row in reader:
            name=row[0]
            password=str(row[1])
            for k in od1:
                if password == k:
                    od2[name]=od1[k]    
        for each in od2:
            writer.writerow([each,od2[each]])
hash_password_hack('hash project.csv','passwords.csv')

