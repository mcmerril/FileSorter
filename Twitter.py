import os
from pip._vendor.distlib.compat import raw_input

target_folder = os.environ.get('OriginalFolderPath')                #Folder containing unsorted files
source_folder = os.environ.get('TargetFolderPath') + '//'           #Parent folder path containing subfolders
class1 = 'Class100'
class2 = 'Class200'
classNames = ["Class100", "Class200", "Class300"]                                                     #Temporary list of class names
subFolderNames = ["HW", "Projects", "Notes", "Random"]
endAddy = '//'


def move_files(sourceFolder, targetFolder, className):
    global target_folder
    target_folder = os.environ.get('PathForFileSorter')

    try:
        for path, dir, files in os.walk(source_folder):
            if files:
                for file in files:
                    if className in file and not os.path.isfile(target_folder + file):
                        endAddy = '\\' + className + '//'                                                               #endAddy is used for when we need to assign specific new folder
                        target_folder = target_folder + endAddy                                                         #Sets the new target_folder
                        os.rename(path + '\\' + file, target_folder + file)                                             #Renames the address and puts into proper folder

    except Exception as e:
        print(e)

def move_files_subFolder(sourceFolder, targetFolder, className, subName):
    global target_folder

    try:
        for path, dir, files in os.walk(source_folder):
            if files:
                for file in files:
                    if className in file and subName in file and not os.path.isfile(target_folder + file):
                        endAddy = '\\' + className + '\\' + subName + '//'                                              #endAddy is used for when we need to assign specific new folder
                        target_folder = target_folder + endAddy                                                         #Sets the new target_folder
                        os.rename(path + '\\' + file, target_folder + file)                                             #Renames the address and puts into proper folder

    except Exception as e:
        print(e)

def match_folder(listOf):                                                                                               #List of is the list of :Classes:Sub categories: ect
    global target_folder

    for i in listOf:                                                                                                    #For all classes
        for j in subFolderNames:
            try:
                for path, dir, files in os.walk(source_folder):                                                         #For all files in the source folder
                    if files:
                        for file in files:
                            target_folder = os.environ.get('PathForFileSorter')
                            if i in file and j in file and not os.path.isdir(target_folder + '\\' + i + '\\' + j):      #Checks if both the class and sub-folder exist in the file, but, there is no folder for the subfolder
                                move_files(source_folder, target_folder, i)                                             #If so it just places into the class folder

                            elif i in file and j in file:                                                               #Similar to above but assumes there is a subfolder and pplaces it within
                                move_files_subFolder(source_folder, target_folder, i, j)

                            elif i in file:                                                                             #Defalt, just in case there is only the class name in the file
                                move_files(source_folder, target_folder, i)

            except Exception as e:
                print(e)

def find_Choice(x):                                                                                                     #Makeshift switch statement for user input
    if x is 'S':
        print('\nFiles have now been sorted!\n')
        match_folder(classNames)                                                                                        #Calls the sorting methods and sorts files

    elif x is 'A':
        print('How many classes do you want to add?')
        num_classes = raw_input()
        total = int(num_classes)
        stTotal = total
        i = 1
        while total is not 0:
            print('\nEnter class number ', i ,' out of ', stTotal)
            add_class(raw_input())                                                                                      #Adds the class a user inputs
            total = total - 1
            i = i + 1

    elif x is 'B':
        print('What class do you want to add to?')
        addToName = raw_input()
        print('How many sub-folders do you want to add to',addToName,'?')
        num_subFolders = int(raw_input())
        total = num_subFolders
        i = 1
        while num_subFolders is not 0:
            print('\nEnter folder name ', i , ' of ', total)
            add_subFolder(raw_input(), addToName)                                                                       #Adds the subfolder to class folder
            i = i + 1
            num_subFolders = num_subFolders - 1


    elif x is 'P':
        print('Now printing all classes and their respective sub-folders')
        print_All()

    elif x is 'D':
        print('Which class would you like to load the default sub-folders?')
        addToName = raw_input()
        print('Adding HW, Projects, Notes, and Random sub-folders to', addToName,'\n')
        add_subFolder('HW',addToName)
        add_subFolder('Projects',addToName)
        add_subFolder('Notes',addToName)
        add_subFolder('Random',addToName)
        print('\n\nSub-folders successfully created!')

    elif x is 'Q':
        print('Thank You.')

    else:
        print('Please input a valid character (Case Sensitive)')

def add_class(className):                                                                                               #Accepts a classname to create a new folder to store

    dirName =  os.environ.get('PathForFileSorter') + '\\' + className

    if not os.path.exists(dirName):                                                                                     #Creates a folder if none does not already exist
        os.mkdir(dirName)
        print("Directory ", dirName, " Created\n")
    else:
        print("Directory ", dirName, " already exists\n")

def add_subFolder(newSubFolder,className):

    dirName =  os.environ.get('PathForFileSorter') + '\\' + className + '\\' + newSubFolder

    if not os.path.exists(dirName):                                                                                     #Creates an address to overlaying class
        os.mkdir(dirName)
        print("Directory ", dirName, " Created\n")
    else:
        print("Directory ", dirName, " already exists\n")

def print_All():
    print('Printing all main classes and subclasses of each class')

def main_Menu():
    print('\nThank you for using my file sorting program!')
    choice = ''

    while choice is not 'Q':
        print('\tPlease make a selection (Case Sensitive):')
        print('\t(S) Sort the files in your source folder.')
        print('\t(A) Add classes to your target folder.')
        print('\t(B) Add sub-folder for a specific target folder class.')
        print('\t(D) Add the default sub-folders to a class (HW, Projects, Notes, Random).')
        print('\t(P) Print all classes currently in use and sub-folders.')
        print('\t(Q) Quit.')
        choice = raw_input()                                                                                            #Input from user as a string
        find_Choice(choice)


    #f = open('Classes.txt', 'a')
    #f.write('CSE310')
    #f.close


main_Menu()                                                                                                             #Calls the Main Menu