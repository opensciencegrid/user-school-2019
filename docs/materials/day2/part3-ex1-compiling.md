---
status: done
---

<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: \#008; } </style>

Tuesday Exercise 3.1: Compiling Programs for Portability
==========================================================

The goal of this exercise is to compile and statically link a piece of code and then submit it as a job. This exercise should take 5-10 minutes.

Background
----------

There is a large amount of scientific software that is available as source code. Source code is usually a group of text files (code) meant to be downloaded and then compiled into a *binary file* which a computer can understand. Sometimes the source code depends on other pieces of code called libraries. If the source code is linked *statically*, these libraries are bundled into the compilation with the source code, creating a *static binary* which can be run on any computer with the same operating system.

Our Software Example
--------------------

For this compiling example, we will use a script written in C. C code depends on libraries and therefore will benefit from being statically linked.

Our C code prints 7 rows of Pascal's triangle.

1.  Log into the OSG submit node `training.osgconnect.net`. Create a directory for this exercise and `cd` into it.
1.  Copy and paste the following code into a file named `pascal.c`.

		:::c++
		#include "stdio.h"

		long factorial(int);

		int main()
		{
		int i, n, c;
		n=7;
		for (i = 0; i < n; i++){
		  for (c = 0; c <= (n - i - 2); c++)
		  printf(" ");
			  for (c = 0 ; c <= i; c++)
				 printf("%ld ",factorial(i)/(factorial(c)*factorial(i-c)));
			  printf("\n");
		   }
		   return 0;
		}

		long factorial(int n)
		{
		   int c;
		   long result = 1;
		   for (c = 1; c <= n; c++)
				 result = result*c;
		   return result;
		}

Compiling
---------

In order to use this code in a job, we will first need to statically compile the code. Recall the slide from the lecture - where *can* we compile and where *should* we compile? In particular:

-   Where is the compiler available?
-   How computationally intensive will this compilation be?    

<!--hiding-->


1.  Think about these questions before moving on. Where do you think we should compile?

1. Most linux servers (including our submit node) have the `gcc` (GNU compiler collection) installed, so we already have a compiler on the submit node. Furthermore, this is a simple piece of C code, so the compilation will not be computationally intensive. Thus, we should be able to compile directly on the submit node. 

1. Compile the code, using the command: 

        :::console
        username@training $ gcc -static pascal.c -o pascal

	Note that we have added the `-static` option to make sure that the compiled binary includes the necessary libraries. This will allow the code to run on any Linux machine, no matter where those libraries are located. 

1. Verify that the compiled binary was statically linked:

        :::console
        username@training $ file pascal

The Linux `file` command provides information about the *type* or *kind* of file that is given as an argument. In this case, you should get output like this:

```console
username@host $ file pascal
pascal: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), %BLUE%statically linked%ENDCOLOR%,
for GNU/Linux 2.6.18, not stripped
```

Note the blue text, which clearly states that this executable (software) is statically linked. The same command run on a non-statically linked executable file would include the text `dynamically linked (uses shared libs)` instead. So with this simple verification step, which could even be run on files that you did not compile yourself, you have some further reassurance that it is safe to use on other Linux machines. (Bonus exercise: Try the `file` command on lots of other files)

Submit the Job
--------------

Now that our code is compiled, we can use it to submit a job.

1.  Think about what submit file lines we need to use to run this job:
    -   Are there input files?
    -   Are there command line arguments?
    -   Where is its output written?

1.  Based on what you thought about in 1., find a submit file from earlier in the week that you can modify to run our compiled `pascal` code.

1. Copy it to the directory with the `pascal` binary and make those changes. 

1. Submit the job using `condor_submit`. 

1. Once the job has run and left the queue, you should be able to see the results (seven rows of Pascal's triangle) in the `.out` file created by the job.

