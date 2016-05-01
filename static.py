import os

total = 0

for x in range(2009, 2016):
        for root, dirs, files in os.walk(str(x)+'/'):
                for filename in files:
                        stat = os.stat(root+filename)
                        if stat.st_size != 1741:
                                total += 1
                        else:
                                os.remove(root+filename)
                                print('removed 1 file')
        print(str(x)+' : '+str(total))
        total = 0
