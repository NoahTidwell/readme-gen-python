import os

save_path = '/Users/noahtidwell/Desktop/readme_gen_python'
file_name = 'README.md'
x = os.path.join(save_path, file_name)

header = '# '
subtitle = '## '
title = input("Please enter the title of your Project > ")
description = input("Please enter a detailed description of your project > ")
installation = input("Please enter a detailed description on how to install your project > ")
usage = input("Please enter how to use this project > ")
contributions = input("Please enter how others can contribute to this project > ")

t1 = format(f'{header}{title}')
desc = format(f'{subtitle} Description:\n{description} /n')
install = format(f'{subtitle} Installation:\n{installation} /n')
use = format(f'{subtitle} Usage:\n{usage} /n')
contribute = format(f'{subtitle} Contributions:\n{contributions}')

output = t1+'\n'+'\n'+desc+'\n'+'\n'+install+'\n'+'\n'+use+'\n'+'\n'+contribute

file1 = open(x, 'w')
file1.write(output)
file1.close()