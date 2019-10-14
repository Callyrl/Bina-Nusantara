#%%
# part A

import csv
import matplotlib.pyplot as plt 
import datetime as dt
import statistics as st

path = "activity.csv"

dict = {}
dictinterval = {}
dictinterval_weekdays = {}
dictinterval_weekends = {}

NA = 0

with open(path) as file:
    reader = csv.reader(file, delimiter = ",")
    header = next(reader)
    
    for row in reader:
        steps = row[0]
        intervals = row[2]
        
        if (steps != "NA"):
            date = row[1]
            dates = int(dt.datetime.strptime(date, "%Y-%m-%d").day)
            interval = int(row[2])
            
            dict.setdefault(str(date), [])
            dict[str(date)].append(int(steps))
            
            dictinterval.setdefault(interval, [])
            dictinterval[interval].append(int(steps))
            
            if (dates % 7 == 0):
                dictinterval_weekends.setdefault(interval, [])
                dictinterval_weekends[interval].append(int(steps))
            else:
                dictinterval_weekdays.setdefault(interval, [])
                dictinterval_weekdays[interval].append(int(steps))
                
        else:
            NA += 1

listdate = []
listtotal = []
listaverage = []
                
for i in dict.keys():
    listdate.append(i)
    listtotal.append(sum(dict.get(i)))
    listaverage.append(st.mean(dict.get(i)))
    
plt.hist(listtotal, bins = 20)
plt.title("Total steps daily")
plt.xlabel("Snumber of Steps")
plt.ylabel("Frequency")
plt.yticks(range(0,25,5))   
plt.show()    
      
print("Mean Steps:", st.mean(listtotal))
print("Median Steps:", st.median(sorted(listtotal)))

#%%
#%%
#part B

with open(path) as file:
    reader = csv.reader(file)
    header = next(reader)
    
    listinterval = []
    listinterval_mean = []
    
    for i in dictinterval.keys():
        listinterval.append(i)
    for i in dictinterval.values():
        listinterval_mean.append(st.mean(i))
    
    plt.plot(listinterval, listinterval_mean)
    plt.title("Average number of steps in interval")
    plt.xlabel("Interval")
    plt.ylabel("Average steps") 
    plt.show()    
    
maximum = []
for i in range(len(steps)):
    if steps[i] == max(steps):
        maximum.append(intervals[i])
    else:
        continue
    
print("Maximum steps: ", maximum)

#%%
#%%
# part C 

import pandas as pd

path = "activity.csv"
  
print("No. of missing values:", NA)
df = pd.read_csv(path)
df.to_csv("copyof_" + "file.csv")
replace = ["NA", 0]

dict = {}
dictinterval2 = {}
dictinterval_weekdays2 = {}
dictinterval_weekends2 = {}

filecopy = r"copyof_file.csv"
with open(filecopy, 'ab') as file:
    writer = csv.writer(file)
    writer.writerows(replace)
    
    reader2 = csv.reader(file)
    header2 = next(reader2)
    
    for row in reader2:
        steps2 = row[0]
        date2 = row[1]
        dates2 = int(dt.datetime.strptime(date2, "%Y-%m-%d").day)
        interval2 = row[2]
            
        dict.setdefault(str(date2), [])
        dict[str(date2)].append(int(steps2))
            
        dictinterval.setdefault(interval2, [])
        dictinterval[interval2].append(int(steps2))
        
        if (dates2 % 7 == 0):
            dictinterval_weekends.setdefault(interval2, [])
            dictinterval_weekends[interval2].append(int(steps2))
        else:
            dictinterval_weekdays.setdefault(interval2, [])
            dictinterval_weekdays[interval2].append(int(steps2))

listdate2 = []
listtotal2 = []
listaverage2 = []
                
for i in dict.keys():
    listdate2.append(i)
    listtotal2.append(sum(dict.get(i)))
    listaverage2.append(st.mean(dict.get(i)))
    
plt.hist(listtotal2, bins = 20)
plt.title("Total steps daily")
plt.xlabel("Snumber of Steps")
plt.ylabel("Frequency")
plt.yticks(range(0,25,5))   
plt.show()    
      
print("Mean Steps:", st.mean(listtotal2))
print("Median Steps:", st.median(sorted(listtotal2)))
#%%


