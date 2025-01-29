import os
import cProfile

print(os.environ['PATH'])

def sum():
    print(1,3)

cProfile.run('sum')





