import os
import random


def long_path(*path_names):
    """Join a sequence of path names together into long path name."""

    return os.path.join(os.getcwd(), *path_names)


def is_exist(*path_names):
    """Check if this path exists in the file system."""

    return os.path.exists(long_path(*path_names))


def create_toy_structure(current_dir):
    """Create a toy structure of dirs and files (10 pathes)"""

    current_dir_path = current_dir
    os.chdir(current_dir_path)

    for _ in range(10):

        obj_path = current_dir_path

        # directory nesting depth
        depth = random.randint(1, 5)
        for i in range(depth):
            obj_type = random.choice(('dir', 'dir', 'dir', 'file'))
            random_index = random.randint(0, 10)
            random_symbol = random.choice(('', ' ', '_', '-'))

            obj_name = f'{obj_type}{random_symbol}{random_index}'
            obj_name += '.txt' if obj_type == 'file' else ''

            obj_path = os.path.join(obj_path, obj_name)
            print(obj_path)

            if obj_type == 'file' and not is_exist(obj_path):
                # create file
                f = open(obj_path, 'a')
                f.close()
                break
            elif not is_exist(obj_path):
                # create dir
                os.mkdir(obj_path)



def create_toy_structure2(current_dir):
    """Create a toy structure of dirs and files"""

    current_dir_path = current_dir
    os.chdir(current_dir_path)

    for i in range(10):

        dir_name = f'd {i}' if i % 2 == 0 else f'd-{i}'
        file_name = f'file {i}' if i < 5 else f'file{i}'
        file_name += '.txt'

        if not is_exist(dir_name):
            os.mkdir(dir_name)

        if not is_exist(file_name):
            f = open(file_name, 'a')
            f.close()

        if i % 3 == 0:
            for ii in range(3):
                dir_name_ii = f'inner dir {i}' if i % 2 == 0 else f'inner-dir-{i}'
                file_name_ii = f'file {i}' if i < 5 else f'file{i}'
                file_name_ii += '.txt'

                if ii % 2 == 0:
                    if not is_exist(dir_name, dir_name_ii):
                        os.mkdir(long_path(dir_name, dir_name_ii))
                    if not is_exist(dir_name, file_name_ii):
                        f = open(long_path(dir_name, file_name_ii), 'a')
                        f.close()