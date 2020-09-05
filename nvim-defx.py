import os
import sys
import neovim
import subprocess
import re
from time import sleep


def main():

    oyo = {}
    cnt = 0

    hoge = subprocess.Popen("pipelist64.exe", stdout=subprocess.PIPE, text=True).stdout.readlines()
    print("Searching Neovim instances...")
    for are in hoge:
        if re.search(r'nvim', are):
            num0 = re.sub(r'^nvim-([0-9]*)-[0-9].*$', r'\1', are).strip('\n')
            print("\t" + are, end="")
            oyo[num0] = False
            cnt += 1

    print("Starting new Neovim instance.")

    subprocess.Popen("C:\\Users\\masa300V\\AppData\\Local\\Microsoft\\WindowsApps\\wt.exe -p \"Neovim\"")
    sleep(3)

    hoge = subprocess.Popen("pipelist64.exe", stdout=subprocess.PIPE, text=True).stdout.readlines()
    for are in hoge:
        if re.search(r'nvim', are):
            num = re.sub(r'^nvim-([0-9]*)-[0-9].*$', r'\1', are).strip('\n')
            if oyo.get(num, True):
                print('Using new nvim %s.' % num)
                servername = "\\\\.\\pipe\\nvim-" + num + "-0"
                print(servername)

    try:
        nvim = neovim.attach("socket", path=servername)
    except Exception:
        print("Neovim not found")
        return 1

    if len(sys.argv) > 2:
        return

    if len(sys.argv) == 1:
        path = os.path.abspath(os.getcwd())

    if len(sys.argv) == 2:
        path = os.path.abspath(sys.argv[1])

    print(path)

    path2 = re.sub(r' ', r'\ ', path.replace(os.path.sep, '/'))
    print(':Defx %s' % path2)
    nvim.command(':Defx %s' % path2)

    nvim.close()

if __name__ == "__main__":
    ret = main()
    sys.exit(ret)

