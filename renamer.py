import os


def get_current_dir(verbose=False):
    """Get the current working directory"""
    path = os.getcwd()
    if verbose:
        print(f'I\'m here: {path}')
    return path


def change_dir(root=None, cd=None):
    """Change working directory

    Use root for full path.
    Or use the 'cd'-notation for changing the current dir.
    """
    if root:
        path = root
    elif cd:
        path = os.path.join(get_current_dir(), cd)
    else:
        path = get_current_dir()
    os.chdir(path)


def show_dir(path=None, ignore=None):
    """Show directory.

    If ignore it excludes listed objects from showing.
    Examples: ignore=['.md', '.py']; ignore='.md .py'
    """
    if path is None:
        path = os.getcwd()

    if ignore:
        ignore_tup = tuple(ignore.split()) if isinstance(ignore, str) else tuple(ignore)

    res = sorted(os.listdir(path))

    for item in res:

        if ignore:
            if any([x in item for x in ignore_tup]):
                continue

        print(item)


def show_dir_recu(path=None, ignore=None, show='all', join=True, tab='\t'):
    """Show directory recursively.

    If ignore it excludes listed objects from showing.
    Examples: ignore=['.md', '.py']; ignore='.md .py'
    """

    if path is None:
        path = os.getcwd()

    if ignore:
        # convert ignore-param in tuple
        ignore_tup = tuple(ignore.split()) if isinstance(ignore, str) else tuple(ignore)
        # is there item from ignore_tup in path_string?
        check_ignore = lambda path_str: any([x in path_str for x in ignore_tup])

    for root, dirs, files in os.walk(path):

        if ignore:
            if check_ignore(root):
                continue

        print(root)

        if show == 'root':
            continue

        if show == 'dirs' or show == 'all':
            for _dir in dirs:
                if ignore:
                    if check_ignore(_dir):
                        continue
                if join:
                    print(os.path.join(root, _dir))
                else:
                    print(f'{tab}{_dir}')

        if show == 'files' or show == 'all':
            for _file in files:
                if ignore:
                    if check_ignore(_file):
                        continue
                if join:
                    print(os.path.join(root, _file))
                else:
                    print(f'{tab}{_file}')


def rename_with(src, what, to):
    """Rename string"""

    # check if the strings or correct to str
    src, what, to = list(map(lambda x: str(x) if not isinstance(x, str) else x, [src, what, to]))

    return src.replace(what, to)


def show_renamed(path=None, what=None, to=None, ignore=None):
    if path is None:
        path = os.getcwd()

    if ignore:
        # convert ignore-param in tuple
        ignore_tup = tuple(ignore.split()) if isinstance(ignore, str) else tuple(ignore)
        # is there item from ignore_tup in path_string?
        check_ignore = lambda path_str: any([x in path_str for x in ignore_tup])

    for root, dirs, files in os.walk(path, topdown = False):

        if ignore:
            if check_ignore(root):
                continue

        for _file in files:
            if ignore:
                if check_ignore(_file):
                    continue
            new_file_name = rename_with(_file, what, to)
            print(os.path.join(root, new_file_name))

        for _dir in dirs:
            if ignore:
                if check_ignore(_dir):
                    continue
            new_dir_name = rename_with(_dir, what, to)
            print(os.path.join(root, new_dir_name))

# path = get_current_dir(verbose=True)
# show_dir(path, ignore=[])
# print()
#
# change_dir(cd='../Coursera_Diving_into_Python')
# path = get_current_dir(verbose=True)

#show_dir_recu(path, ignore=['.git', '.py'], show='all')
#show_renamed(path, what='_', to='-',ignore=['.git',])


