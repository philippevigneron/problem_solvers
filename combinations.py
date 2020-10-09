from datetime import datetime
iteration_nb = 17
moves = [1,2]
solutions = 0
start = datetime.now()

def take_a_step(step):
  if (sum(step) >= iteration_nb): 
    print(step)
    global solutions
    solutions+=1
  for j in moves:
    newstep = []
    newstep.extend(step)
    newstep.append(j)
    if (sum(newstep) <= iteration_nb): 
      take_a_step(newstep)

for i in moves:
  newstep = []
  newstep.append(i)
  take_a_step(newstep)
end = datetime.now()
print('Computation time: ',round((end-start).total_seconds(),3))
print('# of solutions: ',solutions)
