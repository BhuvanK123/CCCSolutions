#Variables
P = int(input())#when we want the program to notify us after P number of people have been infected
N = int(input())#the number of people who have the disease on Day 0
R = int(input())#the number of people spread each day

infected = N #number of people infected at that instance
infected_total = N #total number of people infected
days = 0 #the number of days passed

for i in range (1000000000):
    if infected_total > P:
        print(days)
        break
    
    infected = infected * R
    infected_total += infected
    days+=1