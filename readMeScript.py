import os

save_path = '/Users/noahtidwell/Desktop/IDX/python/readme_gen_python'
file_name = 'README.md'
x = os.path.join(save_path, file_name)

header = '# '
subtitle = '## '

title = input("Please enter the title of your Project > ")
description = input("Please enter a detailed description of your project > ")
installation = input("Please enter a detailed description on how to install your project > ")
usage = input("Please enter how to use this project > ")
contributions = input("Please enter how others can contribute to this project > ")

file1 = open(x, 'w')

file1.write('{}{} \n'.format(header, title))
file1.write('\n {}{} \n'.format(subtitle, description))
file1.write('\n {}{} \n'.format(subtitle, installation))
file1.write('\n {}{} \n'.format(subtitle, usage))
file1.write('\n {}{} \n'.format(subtitle, contributions))
file1.close()