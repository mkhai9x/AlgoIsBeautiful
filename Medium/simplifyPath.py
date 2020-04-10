'''
Given an absolute path for a file (Unix-style), simplify it.
r in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory.
Furthermore, a double period .. moves the directory up a level.

Note that the returned canonical path must always begin with a slash /, a
nd there must be only a single slash / between two directory names.
The last directory name (if it exists) must not end with a trailing /.
Also, the canonical path must be the shortest string representing the absolute path.
'''


def simplifyPath(path):
    # split the path by / character into a list
    list_folder = path.split('/')
    # using stack
    folders = list()
    i = 0
    while i < len(list_folder):
        # We ignore all the '' and '/' characters
        if list_folder[i] != '' and list_folder[i] != '/':
            if list_folder[i] != '.':
                if len(folders) != 0 and list_folder[i] == '..':
                    folders.pop()
                elif list_folder[i] != '..':
                    folders.append(list_folder[i])
        i += 1
    string = '/'
    for i in folders:
        if folders[-1] != i:
            string = string + i + '/'
        else:
            string = string + i
    return string


assert simplifyPath("/../") == "/"

assert simplifyPath("/home//foo/") == "/home/foo"

assert simplifyPath("/a/./b/../../c/") == "/c"

assert simplifyPath("/a/../../b/../c//.//") == "/c"

assert simplifyPath("/a//b////c/d//././/..") == "/a/b/c"
