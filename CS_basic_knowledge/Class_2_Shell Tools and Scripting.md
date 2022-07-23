We shouldn't use space when we defining a variable, because the space in command line of Linux is used to separating arguments.

~~~bash
[ug519111910299@mu01 lab3]$ foo= bar
bash: bar: command not found...
[ug519111910299@mu01 lab3]$ foo=bar
[ug519111910299@mu01 lab3]$ echo $foo
bar
~~~

because `foo = bar`means the program is `foo` and the first argument is `=` and the second argument is `bar`

The single quotes doesn't explain the variables with `$`, but the double quotes will.

~~~bash
[ug519111910299@mu01 lab3]$ echo "$foo"
bar
[ug519111910299@mu01 lab3]$ echo '$foo'
$foo
~~~

Functions in bash:

~~~bash
mcd(){
	mkdir -p "$1"
	cd "$1"
}
~~~

~~~bash
[ug519111910299@mu01 lab3]$ vim mcd.sh
[ug519111910299@mu01 lab3]$ source mcd.sh
[ug519111910299@mu01 lab3]$ mcd test
~~~

`$0`: the name of the script

`$1...9`: the ith argument of the command

`$?`: error code  from the previous command

`$_`: the last argument of the previous command

`$#`: the number of arguments that we are giving

`$$`: the process ID of the command that is running

`$@`: the argument list, when quoted by "", not change

`$*`: same with `$@` when not quoted, when quoted by "", means a string consisting all arguments linked by IFS. 

`!!`: the previous command

~~~bash
[ug519111910299@mu01 lab3]$ echo "hello"
hello
[ug519111910299@mu01 lab3]$ echo $?
0
[ug519111910299@mu01 lab3]$ grep foobar mcd.sh
[ug519111910299@mu01 lab3]$ echo $?
1
[ug519111910299@mu01 lab3]$ true
[ug519111910299@mu01 lab3]$ echo $?
0
[ug519111910299@mu01 lab3]$ false
[ug519111910299@mu01 lab3]$ echo $?
1
~~~

the logical operators can be used to do some sort of conditionals. 

~~~bash
[ug519111910299@mu01 lab3]$ false || echo "opps fail"
opps fail
[ug519111910299@mu01 lab3]$ echo $?
0
~~~

the `||` and `&&` means `or` and `and`

~~~bash
[ug519111910299@mu01 lab3]$ true || echo "opps fail"
[ug519111910299@mu01 lab3]$ true && echo "opps fail"
opps fail
~~~

**Note**: the `$?` is the error code of the latest command. It means if the command execute correctly rather than your requirement.

~~~bash
[ug519111910299@mu01 lab3]$ echo `s`
bash: s: command not found...

[ug519111910299@mu01 lab3]$ echo $?
0
[ug519111910299@mu01 lab3]$ s
bash: s: command not found...
[ug519111910299@mu01 lab3]$ echo $?
127
~~~

`echo` was successfully conducted.

getting the output of a command into a variable:

~~~bash
[ug519111910299@mu01 lab3]$ foo=$(pwd)
[ug519111910299@mu01 lab3]$ echo $foo
/home/ug2019/ug519111910299/bioalgorithm/lab3
[ug519111910299@mu01 lab3]$ foo=$(ls)
[ug519111910299@mu01 lab3]$ ls
mcd.sh  test  test.pbs  week6
[ug519111910299@mu01 lab3]$ echo $foo
~~~

Another way: `Process Substitution`

<(command) : conduct the command and save the output in a temporary file of `/dev/fd/`, and we can use it as the file name.

~~~bash
[ug519111910299@mu01 bioalgorithm]$ echo <(ls)
/dev/fd/63
[ug519111910299@mu01 bioalgorithm]$ ls
lab1  lab2  lab3  PBS_learning
[ug519111910299@mu01 bioalgorithm]$ echo $(ls)
lab1 lab2 lab3 PBS_learning
[ug519111910299@mu01 bioalgorithm]$ diff <(ls) <()ls
diff: ls: No such file or directory
[ug519111910299@mu01 bioalgorithm]$ diff <(ls) <(ls)
[ug519111910299@mu01 bioalgorithm]$ diff <(ls) <(ls -l)
1,4c1,5
< lab1
< lab2
< lab3
< PBS_learning
---
> total 16
> drwxr-xr-x 6 ug519111910299 ug2019 4096 Jul 22 22:00 lab1
> drwxr-xr-x 3 ug519111910299 ug2019 4096 Mar  9 10:26 lab2
> drwxr-xr-x 4 ug519111910299 ug2019 4096 Jul 22 21:14 lab3
> drwxr-xr-x 2 ug519111910299 ug2019 4096 Mar 23 11:28 PBS_learning
[ug519111910299@mu01 bioalgorithm]$ diff $(ls) $(ls -l)
diff: extra operand 'lab3'
diff: Try 'diff --help' for more information.
~~~

The two ways is different: For `$()`, it is the same as \`\`, the output of the command directly replace the `$()`, and the `<()` will save it in the file and serve as the file name.

example:

~~~bash
#!/bin/bash
echo "Starting program at $(date)"

echo "Running program $0 with $# arguments with pid $$"

for file in "$@";do
	grep foobar "$file" > /dev/null 2> /dev/null
	if [[ "$?" -ne 0 ]]; then
	echo "File $file does not have any foobar,adding one"
    #echo "# foobar" >> "$file"
    fi
done
~~~

we can use `{}` , `*`  and so on to make patterns and simplify our command

~~~bash
[ug519111910299@mu01 bioalgorithm]$ ls
lab1  lab2  lab3  PBS_learning
[ug519111910299@mu01 bioalgorithm]$ ls lab{1,2,3}
lab1:
blastparser.pl  protein1  protein2  protein3  u1_human  worm_protein.xpd  worm_protein.xps  worm_protein.xpt

lab2:
material

lab3:
example.sh  mcd.sh  test  test.pbs  week6
~~~

 **Note:** For some commands, the pattern must use `''` to quote, otherwise it will be wrong, because the pattern is directly transfered into the long string, it might be wrong for some command.

~~~bash
[ug519111910299@mu01 bioalgorithm]$ ls lab*
lab1:
blastparser.pl  protein1  protein2  protein3  u1_human  worm_protein.xpd  worm_protein.xps  worm_protein.xpt

lab2:
material

lab3:
example.sh  mcd.sh  test  test.pbs  week6
[ug519111910299@mu01 bioalgorithm]$ find . -name 'lab*' -type d
./lab1
./lab3
./lab2
[ug519111910299@mu01 bioalgorithm]$ find . -name "lab*" -type d
./lab1
./lab3
./lab2
~~~

We can see, for `ls`, it is equal to 

~~~bash
ls lab1 lab2 lab3
~~~

for `find` , it is equal to

~~~bash
find . -name lab1 lab2 lab3 -type d
~~~

That's the wrong command, so we must use `''` to maintain the command.

The difference between `""`,`''`and not use it.

`""` and `''` can ignore special characters, for `''`, all the character remain its true meaning, for `""`, only `$`,\`,and  \ can serve as special character:

`$` : variable replace and command output replace

` : command output replace

\ : escape string

**This is very important because the following command such as `grep`,`ls`,`find` need this as the value of argument**

Other script: python

~~~python
import sys
for arg in reversed(sys.argv[1:]):
    print(arg)
~~~

~~~bash
[ug519111910299@mu01 ~]$ python3 test.py 2 3 4
4
3
2
[ug519111910299@mu01 ~]$ ./test.py
-bash: ./test.py: Permission denied
[ug519111910299@mu01 ~]$ ls
bioalgorithm  system_bio  test.py
[ug519111910299@mu01 ~]$ ls -l
total 12
drwxr-xr-x 6 ug519111910299 ug2019 4096 Mar 23 10:41 bioalgorithm
drwxr-xr-x 3 ug519111910299 ug2019 4096 May  9 19:35 system_bio
-rw-r--r-- 1 ug519111910299 ug2019   61 Jul 23 10:26 test.py
~~~

we will find that we can use `python3` to run it, but we can't `./` it, because when we use `python3`, the file is read rather than execute.

