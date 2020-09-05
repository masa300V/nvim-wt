# nvim-wt
Neovim wrapper for Windows Terminal

## scripts
<dl>
  <dt>nvim-wt-new</dt>
  <dd>Open a file in new nvim by opening new windows terminal</dd>
  <dt>nvim-wt-reuse</dt>
  <dd>Open a file in existing nvim on existing windows terminal</dd>
  <dt>nvim-wt-defx</dt>
  <dd>Open a file in new nvim by opening new windows terminal, then start Defx</dd>
  <dt>nvim-wt-diff</dt>
  <dd>Compare 2 files in new nvim by opening new windows terminal</dd>
</dl>

## requirements
* [Neovim](https://neovim.io/ "Neovim")
* [Windows Terminal](https://github.com/microsoft/terminal "Windows Terminal")  
Setup windows terminal (wt.exe) to start nvim.exe.  See example wt.exe configuration [settings.json](https://github.com/masa300V/nvim-wt/blob/master/settings.json "Windows Terminal setting").
* [Phython](https://www.python.org/ "Python")
* [pynvim](https://github.com/neovim/pynvim "pynvim")
* [Pipelist](https://docs.microsoft.com/en-us/sysinternals/downloads/pipelist "pipelist")  
Install pipelist64.exe (or pipelist.exe) in your PATH.

## expected usage
Convert these scripts into .exe files by the pyinstaller command.  Then, place the .exe files in your "send to" folder or register to your shell context menu like gvim.

## (many) limitations
* Extreme redundancy on these 3 scripts.  
Great Python programmers can make them one script with command line options.
* No check of mulitple nvim.exe instances.  
With the pynvim interface, these scripts can ping all nvim.exe instances to select your target nvim.exe.  
For example, all nvim.exe found by the pipelist show a message "nvim-wt requests to open a file, hit regurn key to chose this nvim".
* Long wait time for new Windows Terminal  
Waiting for 3 seconds to ensure nvim.exe is running on new wt.exe...  This is purely limitation of me don't know how to control processes from the Python.

## background
I switched my editor software from Vim to Neovim early 2020.
Since then, I kept looking for a good GUI like gvim.
After spending days to understand a concept of Neovim, why I can't find a good GUI, I realized that Neovim is designed for terminals.  So I changed my quest for a great terminal program (not for great Neovim GUI).
...and "Bingo!", I found Neovim works great in windows terminal.

In the Windows Terminal, I can use my mouse with Neovim and I can use basic copy/cut/paste operations.  Yes, those are all I was looking for.

## a request for improvements
I generated these scripts by patch-working flagments of codes I could find online.
Because I'm a very poor Python programmer, I don't have any skillset to improve these programs.

**If you find these useful, please folk and upgrade!!**
Then, let me know so to copy your improved vesion 😁

## disclaimer
* These are free software scripts.
* Use these scrypts by your own risk, nobody takes any responsibilty of damages caused by using these scripts.
* Please kindly advise any misuse of somebody's outputs.
