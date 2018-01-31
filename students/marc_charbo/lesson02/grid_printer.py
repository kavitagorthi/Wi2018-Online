#!/usr/bin/env python3

print ('print grid')

minus = "-"
plus = "+"
bar = "|"
space = " "

grid_size = 2

for i in range(grid_size+1):
    if(i%grid_size==0):
        for j in range(grid_size+1):
            if(j%grid_size==0):
                print (plus,end=' ')    
            else:
                print (minus,end=' ')
        print (" ")
    else:
        for k in range(grid_size+1):
            if(k%grid_size==0):
                print (bar,end=' ')    
            else:
                print (space,end=' ')
        print (" ")
