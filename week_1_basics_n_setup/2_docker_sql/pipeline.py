import sys
import pandas as pd

# Adding command line arguments
print(sys.argv)

# Argument 0 will be the filename
# Argument 1 will be whatever we pass

day = sys.argv[1]


# some code using pandas

print(f'job finished successfully for day = {day}')