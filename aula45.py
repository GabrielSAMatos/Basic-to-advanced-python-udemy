import sys

import aula44

aula44.hi()
print('This module is called:', __name__)
print(*sys.path, sep='\n')