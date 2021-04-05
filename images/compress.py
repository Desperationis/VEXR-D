import os
import sys

filename = sys.argv[-1]
print(filename.split(".")[-1])
if filename.split(".")[-1] == 'png':
    os.system("convert {0}.png -quality 50% -resize 1024x {0}.jpg".format(filename.split(".")[0]))
    print("double")

else:
    os.system("convert {0} -quality 50% -resize 1024x {0}".format(filename, filename))
    print("single")
