import os

MAX_DEPTH = 3  # max depth of recursion

q = 'LICENSE'  # file to find
os.chdir('/Volumes/350GB/Projects/')  # starting directory to search
exclude_path = ['node_modules', 'bower_components']  # exclude going into these folders

Q = [(0, f) for f in os.listdir('.')]  # depth and filename

while len(Q) > 0:
    d, f = Q.pop(0)
    if not os.path.isdir(f):
        if os.path.basename(f) == q:
            print f
    else:
        if d < MAX_DEPTH and not os.path.basename(f) in exclude_path:
            c = os.listdir(f)
            for f1 in c:
                Q.append((d + 1, os.path.join(f, f1)))
