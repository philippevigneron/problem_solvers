steps = 10
kinds = [1,3,5]

def take_a_step(step):
  if (sum(step) >= steps): print('{0}'.format(step))
  for j in kinds:
    newstep = []
    newstep.extend(step)
    newstep.append(j)
    if (sum(newstep) <= steps): 
      take_a_step(newstep)

for i in kinds:
  newstep = []
  newstep.append(i)
  take_a_step(newstep)
