import math
import argparse
import matplotlib.pyplot as plt

#this is our function
def f(x): 
    return x*(x-1)

#define our variables for the derivaive
x=1

#this list will allow us to store our deltas he gave us
delta= [10**-2,10**-4,10**-6,10**-8,10**-12]

#this new list will be all the new values we input into our equation
values=[]

#this loop will allow us to cycle through our delta array
for i in delta:
    d=(f(x+i)-f(x))/i
    
#allows us to add unto our values list
    values.append(d)
print(values)

#this plots our values as a function of delta, but since its super small we need to have it scaled to logartihmic form
plt.loglog(delta,values, color = args.x)

parser = argparse.ArgumentParser()
parser.add_argument("x",
                    type = str,
                    help = "add a color for the line")

args = parser.parse_args()