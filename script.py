import numpy as np
import csv

CONTENT_TEMPLATE = "| {0} | {1} | {2}|"

def runscript():

    name, repo, grader, punctuality = np.loadtxt('gradesheet.csv',delimiter=',',unpack=True,dtype='str')
    header = "| "+name[0]+" | "+repo[0]+" | "+grader[0]+"|"
    divider = "\n| "+"----"+" | "+"----"+ " | "+"----"+ " |"

    saveReadme = open('Sheet.md', 'a')
    saveReadme.write(header)
    saveReadme.write(divider)

    for x in range(1,len(name)):
        list1 = "\n| "+name[x] + " | " + repo[x] + " | " + grader[x] + " |"
        saveReadme.write(list1)



def runscript2():
    header = "| name | repo | grader|\n"
    divider = "| ---- | ---- | ---- |\n"

    with open('gradesheet.csv', 'r+') as f:
        reader = csv.reader(f)
        for row in reader:
            content = CONTENT_TEMPLATE.format(row[0], row[1], row[2])
            # content = "| " + row[0] + " | " + row[1] + " | " + row[2] + "|"
            save_readme = open(row[0] + '_sheet.md', 'w')
            save_readme.write(header)
            save_readme.write(divider)
            save_readme.write(content)
            save_readme.close()

runscript2()
