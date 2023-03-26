import os
import creator
import renamer

##
## DEFINE WORKING DIR
##
start_dir_path = os.getcwd()
test_dir_path = os.path.join(start_dir_path, 'test_dir')

print(f'Start dir is {start_dir_path}')
print(f'Test dir is {test_dir_path}')

#os.rmdir(test_dir_path)

if not (os.path.exists(test_dir_path) and os.path.isdir(test_dir_path)):
    print(f'Create dir {test_dir_path}')
    os.mkdir(test_dir_path)

os.chdir(test_dir_path)
current_dir_path = os.getcwd()
print(f'Step into test dir {os.getcwd()}')

##
## CREATING NEW FILES AND DIRS
##
print('Create toy dirs and files')
creator.create_toy_structure(current_dir_path)
#creator.create_toy_structure2(current_dir_path)

##
## RENAMING
##
print("Originals")
renamer.show_dir_recu(path=current_dir_path, ignore=None, show='all', join=True, tab='\t')
print("\n"*2 + "Renamed")
renamer.rename_recu(path=current_dir_path, what=' ', to='_', ignore=None)
renamer.show_dir_recu(path=current_dir_path, ignore=None, show='all', join=True, tab='\t')



