import os

save_path = '/Users/noahtidwell/Desktop/readme_gen_python'
file_name = 'README.md'
x = os.path.join(save_path, file_name)

header = '# '
subtitle = '## '
space = ''
dscript = "Decription:"
install = 'Installation:'
use = 'Usage:'
contribute = 'Contributions:'

title = input("Please enter the title of your Project > ")
description = input("Please enter a detailed description of your project > ")
installation = input("Please enter a detailed description on how to install your project > ")
usage = input("Please enter how to use this project > ")
contributions = input("Please enter how others can contribute to this project > ")

file1 = open(x, 'w')

file1.write('{}{} \n'.format(header, title))
file1.write('\n {}{} \n'.format(subtitle, dscript))
file1.write('{}{} \n'.format(space, description))
file1.write('\n {}{} \n'.format(subtitle, install))
file1.write('{}{} \n'.format(space, installation))
file1.write('\n {}{} \n'.format(subtitle, use))
file1.write('{}{} \n'.format(space, usage))
file1.write('\n {}{} \n'.format(subtitle, contribute))
file1.write('{}{} \n'.format(space, contributions))
file1.close()