import shutil
import os
import datetime


SETUP_FILE = 'user.txt'


def setup():
    print ('Enter your Chrome bookmark directory.')
    print (r'Standard one is: C:\Users\<USER>\AppData\Local\Google\Chrome\User Data\Default')
    bookmarkfolder = input('> ')

    print ('Enter the folder you want to save the backup files in.')
    print (r'For example: C:\Users\<USER>\Desktop\Chrome Bookmarks')
    backupfolder = input('> ')

    with open(SETUP_FILE, 'w') as txt:
        txt.write(bookmarkfolder + '\n' + backupfolder + '\n')

    copy()


def copy():
    with open(SETUP_FILE, 'r') as txt:
        user_list = [line.strip() for line in txt]

    shutil.copy(user_list[0] + r'\Bookmarks', user_list[1])

    new_name = datetime.date.today().strftime('Bookmarks%Y%m%d')
    try:
        os.rename('Bookmarks', new_name)
    except WindowsError:
        os.remove(new_name)
        os.rename('Bookmarks', new_name)


def checksetup():
    try:
        with open(SETUP_FILE, 'r') as txt:
            txt.seek(0)
            line = txt.readline()

        if '\\' in line:
            copy()
        else:
            setup()
    except FileNotFoundError:
        setup()


if __name__ == "__main__":
    checksetup()
