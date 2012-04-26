from __future__ import division, print_function


#Input Population size
pop = input('Population:')

#Define the excess plates over the population
# n is the number of numerals, a the number of letters
def extra(n,a):
    return (10**n)*(26**a)-pop

#Initiate values
# tot chosen to be initally large
numex = 0
alphex = 0
tot = pop*pop
aindex = 0
nindex = 0

#Find the fewest of each to surpass population
while 10**numex < pop:
    numex += 1
while 26**alphex < pop:
    alphex += 1

#Search through combinations for least positive excess
for a in range(alphex+1):
    for n in range(numex+1):
        excess = extra(n,a)
        if excess >=0:
            #If the excess is 0, answer has been found
            if excess==0:
                tot = excess
                nindex = n
                aindex = a
                break
            if excess < tot:
                tot = excess
                nindex = n
                aindex = a
#If pop is too small, make sure that there is one digit
if nindex==0 and aindex==0:
    nindex = 1
    tot = extra(nindex,aindex)
#Output an example
output = str()
for a in range(aindex):
    output += 'A'
for n in range(nindex):
    output += '1'
if aindex != 0 and nindex != 0:
    print('Pattern: ',nindex,'number(s), ',aindex,'letter(s)')
elif nindex !=0:
    print('Pattern: ',nindex,'number(s)')
elif aindex !=0:
    print('Pattern: ',aindex,'letter(s)')
print('Example:',output)
print('Total Plates:',tot+pop)
print('Extra:',tot)
