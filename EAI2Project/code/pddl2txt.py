import subprocess
import os
with open('grid_problem.pddl','wb') as f:
    lines = f.readlines()
    line
f.close()
#home_dir = os.system("cd /home/adri/Downloads/planners64/planners")
out = os.popen("'./optic-clp' 'grid_domain.pddl' 'grid_problem.pddl'").read()
new_out = out.split(";;;; Solution Found")
print(new_out[1])
