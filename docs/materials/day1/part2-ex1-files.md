---
status: done
---

<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: \#008; } </style>

Monday Exercise 2.1: Work With Input and Output Files
=====================================================

The goal of this exercise is make input files available to your job on the execute machine, and return output files back. This small change significantly adds to the kinds of jobs that you can run.

Viewing a Job Sandbox
---------------------

Before you learn to transfer files to and from your job, it is good to understand a bit more about the environment in which your job runs. When the HTCondor `starter` process prepares to run your job, it creates a new directory for your job and all of its files. We call this directory the *job sandbox*, because it is your job’s private space to play. Let’s see what is in the job sandbox for a very simple job with no special input or output files.

1.  Save the script below in a file named `sandbox.sh`:

        :::bash
        #!/bin/sh
        echo 'Date: ' `date`
        echo 'Host: ' `hostname` 
        echo 'Sandbox: ' `pwd` 
        ls -alF
        # END

1.  Create a submit file for this script and submit it.
1.  When the job finishes, look at the contents of the output file.

In the output file, note the `Sandbox:` line: That is the full path to your job sandbox for the run. It was created just for your job, and it was removed as soon as your job finished.

Next, look at the output that appears after the `Sandbox:` line; it is the output from the `ls` command in the script. It shows all of the files in your job sandbox, as they existed at the end of the execution of `sandbox.sh`. The files are:

|                   |                                             |
|-------------------|---------------------------------------------|
| `.chirp.config`   | Configuration for an advanced feature       |
| `.job.ad`         | The job ClassAd                             |
| `.machine.ad`     | The machine ClassAd                         |
| `_condor_stderr`  | Saved standard error from the job           |
| `_condor_stdout`  | Saved standard output from the job          |
| `condor_exec.exe` | The executable, renamed from `sandbox.sh`   |
| `tmp/`            | A directory in which to put temporary files |

So, HTCondor wrote copies of the job and machine ads (for use by the job, if desired), transferred your executable (`sandbox.sh`), renamed it (`condor_exec.exe`), ran it, and saved its standard output and standard error into files. Notice that your submit file, which was in the same directory on the submit machine as your executable, was **not** transferred, nor were any other files that happened to be in directory with the submit file.

Now that we know something about the sandbox, we can transfer more files to and from it.

Running a Job With Input Files
------------------------------

Next, you will run a job that requires an input file. Remember, the initial job sandbox will contain only the renamed job executable, unless you tell HTCondor explicitly about every other file that needs to be transferred. Fortunately, this is easy.

Here is a simple Python script that takes the name of an input file (containing one word per line) from the command line, counts the number of times each (lowercased) word occurs in the text, and prints out the final list of words and their counts.

``` python
#!/usr/bin/env python

import os
import sys

if len(sys.argv) != 2:
    print 'Usage: %s DATA' % (os.path.basename(sys.argv[0]))
    sys.exit(1)
input_filename = sys.argv[1]

words = {}

my_file = open(input_filename, 'r')
for line in my_file:
    word = line.strip().lower()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
my_file.close()

for word in sorted(words.keys()):
    print '%8d %s' % (words[word], word)
```

1.  Save the Python script in a file named `freq.py`.
1.  Download the input file for the script (263K lines, ~1.4 MB) and save it in your submit directory:

        :::console
        username@learn $ wget http://proxy.chtc.wisc.edu/SQUID/osgschool19/mon-2.1-words.txt

1.  Create a basic submit file for the `freq.py` executable.
1.  Add a line to tell HTCondor to transfer the input file:

        :::file
        transfer_input_files = mon-2.1-words.txt

    As with all submit file commands, it does not matter where this line goes, as long as it comes before the word `queue`.

1.  Do not forget to add a line to name the input file as the argument to the Python script.
1.  Submit the job, wait for it to finish, and check the output!

If things do not work the first time, keep trying! At this point in the exercises, we are telling you less and less explicitly how to do steps that you have done before. If you get stuck, ask a neighbor or one of the instructors.

!!! note
    If you want to transfer more than one input file, list all of them on a single `transfer_input_files` command,
    separated by commas.
    For example, if there are three input files:

        transfer_input_files = a.txt, b.txt, c.txt


Transferring Output Files
-------------------------

So far, we have relied on programs that send their output to the standard output and error streams, which HTCondor captures, saves, and returns back to the submit directory. But what if your program writes one or more files for its output? How do you tell HTCondor to bring them back?

Let’s start by exploring what happens to files that a job creates in the sandbox. We will use a very simple method for creating a new file: We will copy an input file to another name.

1.  Find or create a small input file (it is fine to use any small file from a previous exercise).
1.  Create a submit file that transfers the input file and copies it to another name (as if doing `/bin/cp input.txt output.txt` on the command line)
    -   Make the output filename different than any filenames that are in your submit directory
    -   What is the `executable` line?
    -   What is the `arguments` line?
    -   How do you tell HTCondor to transfer the input file?
    -   As always, use `output`, `error`, and `log` filenames that are different from previous exercises
1.  Submit the job and wait for it to finish.

What happened? Can you tell what HTCondor did with the output file that was created (did it end up back on the submit server?), after it was created in the job sandbox? Look carefully at the list of files in your submit directory now.

Transferring Specific Output Files
----------------------------------

As you saw in the last exercise, by default HTCondor transfers files that are created in the job sandbox back to the submit directory when the job finishes. In fact, HTCondor will also transfer back **changed** input files, too. But, this only works for files that are in the top-level sandbox directory, and **not** for ones contained in subdirectories.

What if you want to bring back only **some** output files, or output files contained in subdirectories?

Here is a simple shell script that creates several files, including a copy of an input file in a new subdirectory:

``` shell
#!/bin/sh
if [ $# -ne 1 ]; then echo "Usage: $0 INPUT"; exit 1; fi
date > output-timestamp.txt
cal > output-calendar.txt
mkdir subdirectory
cp $1 subdirectory/backup-$1
```

First, let’s confirm that HTCondor does not bring back the output file in the subdirectory:

1.  Save the shell script in a file named `output.sh`.
1.  Write a submit file that transfers an input file and runs `output.sh` on it (passing the filename as an argument).
1.  Submit the job, wait for it to finish, and examine the contents of your submit directory.

Suppose you decide that you want only the timestamp output file and all files in the subdirectory, but not the calendar output file. You can tell HTCondor to transfer these specific files:

``` file
transfer_output_files = output-timestamp.txt, subdirectory/
```

!!! note
    See the trailing slash (`/`) on the subdirectory?
    That tells HTCondor to transfer back **the files** contained in the subdirectory, but not the directory itself;
    the files will be written directly into the submit directory.
    If you want HTCondor to transfer back an entire directory, leave off the trailing slash.

1.  Remove all output files from the previous run, including `output-timestamp.txt` and `output-calendar.txt`.
1.  Copy the previous submit file that ran `output.sh` and add the `transfer_output_files` line from above.
1.  Submit the job, wait for it to finish, and examine the contents of your submit directory.

Did it work as you expected?

Thinking About Progress So Far
------------------------------

At this point, you can do just about everything that you need in order to run jobs on a local HTC pool. You can identify the executable, arguments, and input files, and you can get output back from the job. This is a big achievement!

In some ways, everything after this exercise shows you how to submit multiple jobs at once and makes it easier to run certain kinds of jobs and deal with certain kinds of situations.

References
----------

There are many more details about HTCondor’s file transfer mechanism not covered here. For more information, read the ["Submitting Jobs Without a Shared Filesystem"](https://htcondor.readthedocs.io/en/v8_9_2/users-manual/submitting-a-job.html#submitting-jobs-without-a-shared-file-system-htcondor-s-file-transfer-mechanism) of the HTCondor Manual.

