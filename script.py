import numpy as np

def runscript():

    name, repo, grader, punctuality = np.loadtxt('gradesheet.csv',delimiter=',',unpack=True,dtype='str')
    header = "| "+name[0]+" | "+repo[0]+" | "+grader[0]+"|"
    divider = "\n| "+"----"+" | "+"----"+ " | "+"----"+ " |"

    saveReadme = open('README.md', 'a')
    saveReadme.write(header)
    saveReadme.write(divider)

    for x in range(1,len(name)):
        list1 = "\n| "+name[x] + " | " + repo[x] + " | " + grader[x] + " |"
        saveReadme.write(list1)

runscript()
