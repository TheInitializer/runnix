import time
with open('tree.txt', 'r') as tree_file:
    for line in tree_file:
        print line,
        time.sleep(0.0001)