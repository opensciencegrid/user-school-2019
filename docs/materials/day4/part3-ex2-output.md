---
status: in progress
---

Thursday Exercise 3.2: Large Output Data
========================================

In this exercise, we will run a job that produces a very large output file, based on a few parameters. This exercise should take 15-20 minutes.

Background
----------

This exercise will be the reverse of the previous exercise! Instead of large input/small output, we will be using a program  that has no input except for a few arguments on the command line, but produces a file that is several GB in size.  As before, we will need to write a shell script that runs the program and handles the data.

The Program
-----------

If you haven't already, log in to `learn.chtc.wisc.edu`. Download the software package and untar it.

``` console
user@learn $ wget http://proxy.chtc.wisc.edu/SQUID/osgschool18/motif-flanks.tar.gz
user@learn $ tar -xzf motif-flanks.tar.gz
```

Use the `cd` command to enter the unpacked `motif-flanks` directory. Take a look at the README file and then do the following:

1.  Compile the code. 
2. Run the program without any arguments. 
3. Based on the README, what is the largest amount of data we might expect?

This program generates all permutations of nucleotide sequences  surrounding a given DNA motif. We can choose the length of permutation we want both  before and after a motif of our choice. To use this program on the command line and save the output to a FASTA file, we can use the command:

``` console
user@learn $ ./motif-flanks 2 AGTTCATGCCT 2 > sequences.fa
```

According to the usage information and README, the two numerical arguments can add up to 13, at most, and the middle sequence can be any  DNA sequence up to 20 characters. The largest output we can expect is around 4 GB.

Test Job
--------

Having output of up to 4 GB means two things: we will want to run a smaller  test before we run the program at its peak, and the output data will need to go into a shared location like Gluster, instead of returning  to the submit server.

First, we'll create a shell script to serve as the job's executable.

1.  What commands do you need to put in the script? What do you need to do with the `sequences.fa` file before the job exits?
2.  Our script needs to run the `motif-flanks` command as shown above, redirecting the output to a file called `sequences.fa`. Then, after that command completes, the `sequences.fa` file should be moved to your Gluster directory, as it is too large to return to the  submit server as usual.
1.  Write the script and then check it against the script below. Yours might look slightly different. 

``` file
#!/bin/sh

./motif-flanks 4 GATTTTCGATC 4 > sequences.fa
mv sequences.fa /mnt/gluster/%RED%username%ENDCOLOR%/
```

!!! note 
    Note that the two arguments in the script (4 and 4) are much smaller than the total possible for the software (two values that add up to 13). This is because we want to run a smaller test before submitting a job with the largest possible combination of arguments.

Next, create a submit file for this job, based on other submit files from the school. Some important considerations:

1.  We're writing our file to the job's working directory, so make sure to request several GB of disk space. (`request_disk` in the submit file)
2.  Add a line to the file that ensures your job will land on computers that have access to Gluster (see the file from the [last exercise](part4-ex1-input.md)).
3.  The `executable` will be the script you wrote above.

Once you have a submit file that does all these things, submit the test job.

Once the job has completed, do the following:

1.  Check the directory where you submitted the job. Has the `sequences.fa` file returned there, accidentally?
2.  Check your Gluster directory. Did the `sequences.fa` file get copied there successfully?
3.  Check file size. How big is the `sequences.fa` file? You can use the `ls -lh` command with the filename to find out.

If your job successfully copied the `sequences.fa` file to Gluster and did **not** return it to your submission directory on  the submit server, congratulations! Everything is working as it should and you can now submit a full job.

Final Job
---------

Having done a test, it should be straightforward to run a "full scale" job. Edit your `run_motif.sh` executable so that the `motif-flanks` command  uses larger numerical arguments:

``` file
./motif-flanks 6 GATTTTCGATC 7 > sequences.fa
```

Then submit your job. When it completes, check the size of the output file in Gluster.


