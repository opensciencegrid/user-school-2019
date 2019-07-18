---
status: tested
---

Thursday Exercise 1.2: File Compression and Testing Resource Requirements
==================================================


The objective of this exercise is to refresh yourself on HTCondor file transfer, to implement file compression, and to
begin examining the memory and disk space used by your jobs in order to plan larger batches, which we'll tackle in later
exercises today.

Setup
-----

The executable we'll use in this exercise and later today is the same `blastx` executable from previous exercises.

1. Log in to `training.osgconnect.net`
1. Navigate to your local scratch directory:

        :::console
        user@training $ cd /local-scratch/<USERNAME>

    Replacing `<USERNAME>` with your username

1. Change into the `thurs-blast-data` folder that you created in the previous exercise.

### Review: HTCondor File Transfer

![OSG data transfer](/materials/day4/files/osgus18-day4-part2-ex2-data-transfer.jpg)

Recall that OSG does **NOT** have a shared filesystem!
Instead, HTCondor *transfers* your executable and input files (specified with the `executable` and
`transfer_input_files` submit file directives, respectively) to a working directory on the execute node, regardless of
how these files were arranged on the submit node.
In this exercise we'll use the same `blastx` example job that we used previously, but modify the submit file and test
how much memory and disk space it uses on the execute node.

Start with a test submit file
-----------------------------

We've started a submit file for you, below, which you'll add to in the remaining steps.

``` file
executable = 
transfer_input_files = 
output = test.out
error = test.err
log = test.log
request_memory = 
request_disk = 
request_cpus = 1
requirements = (OpSys == "LINUX")
queue
```

### Implement file compression

In our first blast job from yesterday, the database files in the `pdbaa` directory were all transferred, as is, but we
could instead transfer them as a single, compressed file using `tar`.
For this version of the job, let's compress our blast database files to send them to the submit node as a single
`tar.gz` file (otherwise known as a tarball), by following the below steps:

1. Change into the `pdbaa` directory and compress the database files into a single file called `pdbaa_files.tar.gz`
   using the `tar` command.
   Note that this file will be different from the `pdbaa.tar.gz` file that you used earlier, because it will only
   contain the `pdbaa` files, and not the `pdbaa` directory, itself.)

   Remember, a typical command for creating a tar file is:

        :::console
        user@training $ tar -cvzf <COMPRESSED FILENAME> <LIST OF FILES OR DIRECTORIES>


    Replacing `<COMPRESSED FILENAME>` with the name of the tarball that you'd like to create and
    `<LIST OF FILES OR DIRECTORIES>` with a space-separated list of files and/or directories that you want to 
    Move the tarball to the `thur-blast-data` directory.

2. Create a wrapper script that will first decompress the `pdbaa_files.tar.gz` file, and then run blast.

    Because this file will now be our submit file `executable`, we'll also end up transferring the `blastx` executable
    with `transfer_input_files`.
    In the `thur-blast-data` directory, create a new file, called `blast_wrapper.sh`, with the following contents:

        :::file
        #!/bin/bash
        
        tar -xzvf pdbaa_files.tar.gz
        
        ./blastx -db pdbaa -query mouse.fa -out mouse.fa.result
        
        rm pdbaa.*

    !!! warning "Extra Files!"
        The last line removes the resulting database files that came from `pdbaa_files.tar.gz`, as these files would
        otherwise be copied back to the submit server as perceived output since they're "new" files that HTCondor
        didn't transfer over as input.

### List the executable and input files

Make sure to update the submit file with the following:

-   Add the new `executable` (the wrapper script you created above)
-   In `transfer_input_files`, list the `blastx` binary, the `pdbaa_files.tar.gz` file, and the input query file.

!!! note "Commas, commas everywhere!"
    Remember that `transfer_input_files` accepts a comma separated list of files, and that you need to list the full
    location of the `blastx` executable (`blastx`).
    There will be no arguments, since the arguments to the `blastx` command are now captured in the wrapper script.

### Predict memory and disk requests from your data

Also, think about how much memory and disk to request for this job.
It's good to start with values that are a little higher than you think a test job will need, but think about:

-   How much memory `blastx` would use if it loaded all of the database files *and* the query input file into memory.
-   How much disk space will be necessary on the execute server for the executable, all input files, and all output
    files (hint: the log file only exists on the submit node).
-   whether you'd like to request some extra memory or disk space, just in case

Look at the `log` file for your `blastx` job from Tuesday, and compare the memory and disk "Usage" to what you predicted
from the files.
Make sure to update the submit file with more accurate memory and disk requests (you may still want to request slightly
more than the job actually used).

Run the test job
----------------

Once you have finished editing the submit file, go ahead and submit the job.
It should take a few minutes to complete, and then you can check to make sure that no unwanted files (especially the
`pdbaa` database files) were copied back at the end of the job.

Run a **`du -sh`** on the directory with this job's input.
How does it compare to the directory from Tuesday, and why?

When you've completed the above, continue with the [next exercise](/materials/day4/part1-ex3-blast-split).


