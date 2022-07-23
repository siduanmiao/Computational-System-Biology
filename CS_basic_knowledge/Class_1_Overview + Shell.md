Shell : A program for us to interact with our computer.

\$PATH: the directory our computer search for program.

back to the previous directory:

~~~bash
[ug519111910299@mu01 ~]$ cd -
/home
~~~

~~~bash
drwxr-xr-x
~~~

the first keys : d=directory -=normal file l=soft links

the next 3 keys: for owner

the middle 3 keys: for groups that own this file

the last 3 keys : for everyone else

For files:

* r :read the contents
* w :change the contents
* x :execute the file

For directories:

* r :to see the list of files in the directory
* w :rename,create or remove files
* x :enter the directory(cd), if you want to get to a file, you must have the permission of this directory and all parent directory.

if you have the w in file but not in directory, you can empty it but you can't delete it.

\> ：redirection and rewrite

\> \>:   redirection and append

~~~bash
[ug519111910299@mu01 sys]$ ls
block  bus  class  dev  devices  firmware  fs  hypervisor  kernel  module  power
~~~

this is the kernel parameters of this computer.

when we use redirection, the programs don't know each other, so if we use

~~~bash
sudo echo 500 > bright_ness
~~~

we don't have the permission of bright_ness, even we use the sudo, only the echo is sudo, the file don't know you have the permission,so **Permission denied**

~~~bash
echo 500 > sudo tee birght_ness
~~~

we all know, the `tee` can write the input to the next file while writing it to your screen.

**Note: the redirection and pipeline all need stdin and stdout**

~~~bash
[ug519111910299@mu01 lab1]$ echo < blastparser.pl 

[ug519111910299@mu01 lab1]$ history | echo

[ug519111910299@mu01 lab1]$ echo blastparser.pl 
blastparser.pl
~~~

because for `echo`, `echo` prints all of its arguments. It does not read from `stdin`. So the second `echo` prints all of its arguments (none) and exits, ignoring the content on `stdin`.

What's more, we should know that all the content of Linux is file, the pipeline and the stdin stdout is all file and filename:

~~~bash
[ug519111910299@mu01 lab1]$ echo "sssd" | grep ss
sssd
[ug519111910299@mu01 lab1]$ grep ss sssd
grep: sssd: No such file or directory
[ug519111910299@mu01 lab1]$ grep ss $(echo sssd)
grep: sssd: No such file or directory
[ug519111910299@mu01 lab1]$ grep ss <(echo sssd)
sssd
~~~

**The difference between `-` and `--`**

for `--` , we use `=` to link the argument and value

for `-`, we can integrate all the argument without values. For those with values, we can't integrate them and the blank between argument and values is optional.