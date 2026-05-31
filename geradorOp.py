import csv
#import collections import deque
def LastRow():
    with open("ops.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)
            
            if rows:
                lastRow = rows[-1] 
                lastRow_ = int(lastRow[0]) + 1
                #print(lastRow_
            
