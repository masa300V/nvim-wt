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

    if cnt == 0:
        print("Starting new Neovim instance.")

        subprocess.Popen("C:\\Users\\masa300V\\AppData\\Local\\Microsoft\\WindowsApps\\wt.exe -p \"Neovim\"")
        sleep(3)

        hoge = subprocess.Popen("pipelist64.exe", stdout=subprocess.PIPE, text=True).stdout.readlines()
        for are in hoge:
            if re.search(r'nvim', are):
                num = re.sub(r'^nvim-([0-9]*)-[0-9].*$', r'\1', are).strip('\n')
                if oyo.get(num, True):
                    servername = "\\\\.\\pipe\\nvim-" + num + "-0"
                    print('Using new nvim %s.' % servername)
    elif cnt > 1:
        print("Multiple existing Neovim instances.")
        sleep(3)
        return
    else:
        print("Using the existing Neovim instance.")
        servername = "\\\\.\\pipe\\nvim-" + num0 + "-0"

    try:
        nvim = neovim.attach("socket", path=servername)
    except Exception:
        print("Neovim not found")
        return 1

    if len(sys.argv) <= 1:
        return

    path = sys.argv[1]
    nvim.command(':e %s' % os.path.abspath(path))

    nvim.close()


if __name__ == "__main__":
    ret = main()
    sys.exit(ret)

