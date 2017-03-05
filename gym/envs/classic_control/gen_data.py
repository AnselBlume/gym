"""
Generates data with periodicity
"""
from random import randint

cylinder_profile  = [
  #id, periodicity, start phase, current phase
  [0, 30, 0, 0],
  [1, 0, 0, 0],
  [2, 0, 0, 0],
  [3, 120, 0, 0],
  [5, 180, 0, 0],
  [6, 0, 0, 0],
  [7, 0, 0, 0],
  [8, 30, 0, 0],
  [9, 0, 0, 0],
  [10, 360, 0, 0]
]


temp = 0
max_temp = 10
offset = 0

num_days = 360

for didx in range(0,num_days):

  for cidx in range(0,10):

    if ( cylinder_profile[cidx][1] == 0 ) :
      #Generate temp for an aperiodic cylinder
      temp = randint(0,10)
    else :
      #Generate temp for a periodic cylinder
      period = cylinder_profile[cidx][1]
      cur_phase = cylinder_profile[cidx][3]
  
      if (period >= cur_phase) :
        offset = period - cur_phase
      else:
        offset = cur_phase - period
  
      temp = max_temp - offset 
      if (temp < 0 ) :
        temp = 0
      #print " period %d, offset %d, temp %d" %(period, offset, temp) 
   

    # Convert day to date

    print "%d,%d,%d" % (cidx,temp,didx)


