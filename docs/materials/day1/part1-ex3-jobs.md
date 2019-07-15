---
status: done
---

<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: \#008; } </style>

Monday Exercise 1.3: Run Jobs!
==============================

The goal of this exercise is to submit jobs to HTCondor and have them run on the local pool (CHTC). This is a huge step in learning to use an HTC system!

**This exercise will take longer than the first two, short ones. It is the essential part of this exercise time. If you are having any problems getting the jobs to run, please ask the instructors! It is very important that you know how to run simple jobs.**

Running a Simple Job
--------------------

Nearly all of the time, when you want to run an HTCondor job, you first write an HTCondor submit file for it. In this section, you will run the same `hostname` command as in Exercise 1.1, but where this command will run within a job on one of the 'execute' servers in CHTC's local HTCondor pool.

Here is a simple submit file for the `hostname` command:

``` file
executable = /bin/hostname

output = simple.out
error = simple.err
log = simple.log

request_cpus = 1
request_memory = 1GB
request_disk = 1MB

queue
```

Write those lines of text in a file named `simple.sub`.

!!! note
    There is nothing magic about the name of an HTCondor submit file.
    It can be any filename you want.
    It's a good practice to always include the `.sub` extension, but it is not required.
    Ultimately, a submit file is a text file

The lines of the submit file have the following meanings:

|              |                                                                                                                                                                            |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `executable` | The name of the program to run (relative to the directory from which you submit).                                                                                          |
| `output`     | The filename where HTCondor will write the standard output from your job.                                                                                                  |
| `error`      | The filename where HTCondor will write the standard error from your job. This particular job is not likely to have any, but it is best to include this line for every job. |
| `log`        | The filename where HTCondor will write information about your job run. Technically not required, it is a **really** good idea to have a log file for every job.            |
| `request_*`  | Tells HTCondor how many `cpus` and how much `memory` and `disk` we want, which is not much, because the 'hostname' executable is pretty simple                             |
| `queue`      | Tells HTCondor to run your job with the settings above.                                                                                                                    |

Note that we are not using the `arguments` or `transfer_input_files` lines that were mentioned during lecture because the `hostname` program is all that needs to be transferred from the submit server, and we want to run it without any additional options.

Double-check your submit file, so that it matches the text above. Then, tell HTCondor to run your job:

``` console
username@learn $ condor_submit simple.sub
Submitting job(s).
1 job(s) submitted to cluster NNNN.
```

The actual cluster number will be shown instead of `NNNN`. **If, instead of the text above, there are error messages, read them carefully and then try to correct your submit file or ask for help.**

Notice that `condor_submit` returns back to the shell prompt right away. It does **not** wait for your job to run. Instead, as soon as it has finished submitting your job into the queue, the submit command finishes.

### View your job in the queue

Now, use `condor_q` and `condor_q -nobatch` to watch for your job in the queue! 

You may not even catch the job in the `R` running state, because the `hostname` command runs very quickly. When the job itself is finished, it will 'leave' the queue and no longer be listed in the `condor_q` output.

After the job finishes, check for the `hostname` output in `simple.out`, which is where job information printed to the terminal screen will be printed for the job.

``` console
username@learn $ cat simple.out
e171.chtc.wisc.edu
```

The `simple.err` file should be empty, unless there were issues running the `hostname` executable after it was transferred to the slot. The `simple.log` is more complex and will be the focus of a later exercise.

## Running a Job With Arguments

Very often, when you run a command on the command line, it includes arguments (i.e. options) after the program name, as in the below examples:

``` console
username@learn $ cat simple.out
username@learn $ sleep 60
username@learn $ dc -e '6 7 * p'
```

In an HTCondor submit file, the program (or 'executable') name goes in the `executable` statement and **all remaining arguments** go into an `arguments` statement. For example, if the full command is:

``` console
username@learn $ sleep 60
```

Then in the submit file, we would put the location of the "sleep" program (you can find it with `which sleep`) as the job `executable`, and `60` as the job `arguments`:

``` file
executable = /bin/sleep
arguments = 60
```

For the command-line command:

``` console
username@learn $ dc -e '6 7 * p'
```

We would put the following into the submit file, putting the `arguments` statement in quotes, since it contains single quotes:

``` file
executable = /usr/bin/dc
arguments = "-e '6 7 * p'"
```

Let’s try a job submission with arguments. We will use the `sleep` command shown above, which simply does nothing for the specified number of seconds, then exits normally. It is convenient for simulating a job that takes a while to run.

Create a new submit file (you name it this time) and save the following text in it.

``` file
executable = /bin/sleep
arguments = 60

output = sleep.out
error = sleep.err
log = sleep.log

request_cpus = 1
request_memory = 1GB
request_disk = 1MB

queue
```

Except for changing a few filenames, this submit file is nearly identical to the last one. But, see the extra `arguments` line?

Submit this new job. Again, watch for it to run using `condor_q` and `condor_q -nobatch`; 
check once every 15 seconds or so. 
Once the job starts running, it will take about 1 minute to run (because of the `sleep` command, right?), 
so you should be able to see it running for a bit. 
When the job finishes, it will disappear from the queue, but there will be no output in the output or error files, because `sleep` does not produce any output.

Running a Script Job From the Submit Directory
----------------------------------------------

So far, we have been running programs (executables) that come with the standard Linux system. 
More frequently, you will want to run a program that exists within your directory 
or perhaps a simple shell script of commands that you'd like to run within a job. In this example, you will write a shell script and a submit file that runs the shell script within a job:

1. Put the following contents into a file named `test-script.sh`:

        :::bash
        #!/bin/sh
        echo 'Date: ' `date` 
        echo 'Host: ' `hostname` 
        echo 'System: ' `uname -spo` 
        echo "Program: $0" 
        echo "Args: $*"
        echo 'ls: ' `ls`
        # END

1. Add executable permissions to the file (so that it can be run as a program):

        :::console
        username@learn $ chmod +x test-script.sh

1. Test your script from the command line:

        :::console
        username@learn $ ./test-script.sh hello 42 
        Date: Mon Jul 17 10:02:20 CDT 2017 
        Host: learn.chtc.wisc.edu 
        System: Linux x86_64 GNU/Linux 
        Program: ./test-script.sh
        Args: hello 42
        ls: hostname.sub montage simple.err simple.log simple.out test-script.sh

    This step is **really** important! If you cannot run your executable from the command-line, HTCondor probably cannot run it on another machine, either. And debugging simple problems like this one is surprisingly difficult. So, if possible, test your `executable` and `arguments` as a command at the command-line first.

1. Write the submit file (this should be getting easier by now):

        :::file
        executable = test-script.sh
        arguments = foo bar baz

        output = script.out
        error = script.err
        log = script.log

        request_cpus = 1
        request_memory = 1GB
        request_disk = 1MB

        queue

    In this example, the `executable` that was named in the submit file did **not** start with a `/`, 
        so the location of the file is relative to the submit directory itself. 
        In other words, in this format the executable must be in the same directory as the submit file.

    !!! note
        As this example shows, blank lines and spaces around the = sign do not matter to HTCondor.
        Use whitespace to make things clear to **you**. What format do you prefer to read?

1.  Submit the job, wait for it to finish, and check the output (and error, which should be empty).

    What do you notice about the lines returned for "Program" and "ls"? Remember that only files pertaining
    to **this** job will be in the job working directory on the execute server. You're also seeing the effects
    of HTCondor's need to standardize some filenames when running your job, though they are named as you expect 
    in the submission directory (per the submit file contents).

## Extra Challenge

!!! note
    There are Extra Challenges throughout the school curriculum. You may be better off coming back to these after you've completed all other exercises for your current working session.

Below is a simple Python script that does something similar to the shell script above. Run this Python script using HTCondor.

```python
#!/usr/bin/env python

"""Extra Challenge for OSG User School
Written by Tim Cartwright
Submitted to CHTC by #YOUR_NAME#
"""

import getpass
import os
import platform
import socket
import sys
import time

arguments = None
if len(sys.argv) > 1:
    arguments = '"' + ' '.join(sys.argv[1:]) + '"'

print >> sys.stderr, __doc__
print 'Time    :', time.strftime('%Y-%m-%d (%a) %H:%M:%S %Z')
print 'Host    :', getpass.getuser(), '@', socket.gethostname()
uname = platform.uname()
print "System  :", uname[0], uname[2], uname[4]
print "Version :", platform.python_version()
print "Program :", sys.executable
print 'Script  :', os.path.abspath(__file__)
print 'Args    :', arguments
```