#!/usr/bin/env python3
# Author: Mark Legrove
# Author ID: mlegrove
# Date Created: 2025/05/12

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')