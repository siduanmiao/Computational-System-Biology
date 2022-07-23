In Vim, there are three modes of operation: Normal, Insert, and Visual.

Normal: Esc key

Insert: i

Visual: v

Insert mode is where you can insert your text in the file. This mode inserts every character you type at the current cursor location.

Visual mode allows you to select text so that you may perform certain operations (cut, copy, delete) on it.

~~~bash
vim blastparser.pl
~~~

![image-20220723163717679](Class_3%20Editors%20(vim)%20.assets/image-20220723163717679.png)

~~~bash
:help :w
~~~

`:help` can serve as a search tool.

~~~bash
:help w
~~~

it means when you press `w` in normal mode what will happen.

In vim, there are three important component: Buffer,Window and Tab

A buffer is the in-memory text of **a** file. **A buffer can show in two windows**

A window is a viewport on **a** buffer.

A tab page is a collection of **windows**.

When we edit, we load the content of file into a buffer, and a window show the buffer to us, if we open many windows, we can collect them in a Tab.

~~~bash
sp
~~~

![image-20220723165723086](Class_3%20Editors%20(vim)%20.assets/image-20220723165723086.png)

~~~bash
Ctrl+W j # move to the bottom window
Ctrl+W k # move to the up window
~~~

The cursor of each window is independent.

The new tabs

~~~bash
tabnew
~~~

![image-20220723170211756](Class_3%20Editors%20(vim)%20.assets/image-20220723170211756.png)`:q` only quit the window, not the buffer.

The movement of cursor: 

`HJKL` : one by one

`WB`: word by word

`E`: the end of the word

The edit of buffer:

`U`: undo the conduct

`D+HL`:Delete the left or right

`D+JK`: Delete the line and the up line or next line

`DD`: Delete the line

`x`: Delete the word.

`Ctrl+R`: Redo

`y`: copy `yy` for copy the line, `yw` for copy the word.

`p`: pasting

In version mode, we can move cursor to select some chucks, and press `y` to copy, and now we back to the normal mode, we can use `p` to paste.

`number + move/editing`: do the move/editing number times

