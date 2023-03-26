# file-system-names
This project is for recursively renaming files and folders according to a template.

## Description of modules
The file `run.py` shows the basic steps of working with models: creating random files and folders (module `creator.py`) in the test directory, printing the contents of all directories on the screen and renaming them according to the template (module `renamer.py`).

## Example of work.
Take the project
```
$ git clone git@github.com:alexande-popov/file-system-names.git
$ cd file-system-names
```
Try to run an example `run.py`
```
$ python run.py
```
or work manually.

Import working modules.
```python
>>> import os
>>> import creator
>>> import renamer
```
Define a working directory
```python
>>> os.mkdir('test_dir')
>>> os.chdir('test_dir')
>>> current_dir_path = os.getcwd()
```
Create new structure of dirs and files by random.
```python
>>> creator.create_toy_structure(current_dir_path)
```
Show recursively all inner dirs and files inside `test_dir`.
```python
renamer.show_dir_recu(path=current_dir_path, ignore=None, show='all', join=True, tab='\t')
```
```
.\file-system-names\test_dir
.\file-system-names\test_dir\dir 0
.\file-system-names\test_dir\dir 1
.\file-system-names\test_dir\dir 9
.\file-system-names\test_dir\dir-4
.\file-system-names\test_dir\dir0
.\file-system-names\test_dir\dir7
.\file-system-names\test_dir\dir_1
                ...
```
```python
>>> r = renamer.rename_recu(path=current_dir_path, what=' ', to='_', ignore=None)
```
Return of `rename_recu` 
The result of the `rename_recu` work is changing pathes-names according to the template. We replace `what=' '` to `to='_'`. If the rename fails, this object is returned.
```
>>> r
['.\\file-system-names\\test_dir\\dir 1']
```
As you can see, the folder `dir 1` could not be renamed, because the name `dir_1` is already reserved. Let's see the result now
```python
>>> renamer.show_dir_recu(path=current_dir_path, ignore=None, show='all', join=True, tab='\t')
```
```
.\file-system-names\test_dir
.\file-system-names\test_dir\dir 1
.\file-system-names\test_dir\dir-4
.\file-system-names\test_dir\dir0
.\file-system-names\test_dir\dir7
.\file-system-names\test_dir\dir_0
.\file-system-names\test_dir\dir_1
.\file-system-names\test_dir\dir 1
.\file-system-names\test_dir\dir 1\dir_0
               ...
```
