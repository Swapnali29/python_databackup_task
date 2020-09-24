#### Python Backup Cleaner
#
# Buckets 1 and 2 contain backup of code and database respectively.
# Each file name contains the date it was backed up on.
#
# Your task is to **delete** the files from these buckets that do not fit the below criteria.
#
# Following files are to be kept and rest are to be deleted:
# 1. backups of last 5 days
# 2. backups of last 4 Saturdays
# 3. backups of last day of each month
#
# Code should be scalable in nature i.e. addition of any new buckets should **not** require any changes to the core logic of the code
#
# Note: You cannot create any new files in bucket1 and bucket2 folders.
#
# An Object-Oriented Approach is expected in the solution.
import os

list1 = ['code_backup_2020-8-22.txt',
         'code_backup_2020-8-29.txt',
         'code_backup_2020-8-31.txt',
         'code_backup_2020-9-5.txt',
         'code_backup_2020-9-12.txt',
         'code_backup_2020-9-13.txt',
         'code_backup_2020-9-14.txt',
         'code_backup_2020-9-15.txt',
         'code_backup_2020-9-16.txt',
         'code_backup_2020-9-17.txt', ]

res1 = list(map(lambda x: x, list1))
#print(res)
for root, dirs, files in os.walk(r'C:\Users\SURAJ\Downloads\Python-Data-Backup-Task\Python Data Backup Task\bucket1'):
    for name in files:
        path = os.path.join(root, name)
        if os.path.isfile(path):
            if name not in res1:
                #print(path)
                os.remove(path)



list2 = ['db_backup_2020-6-30.txt',
         'db_backup_2020-7-31.txt',
         'db_backup_2020-8-22.txt',
         'db_backup_2020-8-29.txt',
         'db_backup_2020-8-31.txt',
         'db_backup_2020-9-5.txt',
         'db_backup_2020-9-12.txt',
         'db_backup_2020-9-13.txt',
         'db_backup_2020-9-14.txt',
         'db_backup_2020-9-15.txt',
         'db_backup_2020-9-16.txt',
         'db_backup_2020-9-17.txt', ]

res2 = list(map(lambda x: x, list2))
#print(res2)
for root, dirs, files in os.walk(r'C:\Users\SURAJ\Downloads\Python-Data-Backup-Task\Python Data Backup Task\bucket2'):
    for name in files:
        path = os.path.join(root, name)
        if os.path.isfile(path):
            if name not in res2:
                #print(path)
                os.remove(path)

