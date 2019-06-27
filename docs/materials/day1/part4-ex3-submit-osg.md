---
status: in progress
---

Monday Exercise 4.3: Running jobs in the OSG
============================================

The goal of this exercise is to have your jobs running on the OSG and map their geographical locations.

Where in the world are my jobs? (Part 2)
----------------------------------------

In this version of the geolocating exercise, you will submit jobs to the OSG from `osg-learn.chtc.wisc.edu` and
hopefully getting back much more interesting results!
You will be using the same exact payload as you did in [exercise 4.1](/materials/day1/part4-ex1-submit-refresher).

### Gathering network information from the OSG

Now to create submit files that will run in the OSG!

1. If not already logged in, `ssh` into `osg-learn.chtc.wisc.edu`
1. Make a new directory for this exercise, `tuesday-4.3` and change into it
1. Use `scp` or `rsync` from [exercise 1.2](/materials/day2/part1-ex2-login-scp) to copy over the executable and input
   file from the `monday-4.1` directory from `learn`.
1. Re-create the submit file from exercise 1.1 except this time around change your submit file so that it submits **five
   hundred** jobs!
1. Submit your file and wait for the results

Mapping your jobs
-----------------

As before, you will be using <http://www.mapcustomizer.com/> from `osg-learn.chtc.wisc.edu` to visualize where your jobs
have landed in the OSG.
Copy and paste the collated results from your job output into the bulk creation text box at the bottom of the screen.
Where did your jobs end up?

Extra Challenge: Cleaning up your submit directory
--------------------------------------------------

If you run `ls` in the directory from which you submitted your job, you may see that you now have thousands of files!
Proper data management starts to become a requirement as you start to develop truly HTC workflows;
you'll want organize your submit files, code, and input data separate from your output data.

1. Try editing your submit file so that all your output and error files are saved to separate directories within your
   submit directory.
   
    !!! note "Tip"
        Experiment with fewer job submissions until you're confident you have it right, then go back to submitting 1000
        jobs!

1. Submit your file and track the status of your jobs.

Did your jobs complete successfully with output and error files saved in separate directories?
If not, can you find any useful information in the job logs or hold messages?
If you get stuck, review the [slides for submitting many jobs](/materials/day1/files/osgus18-day1-part2-many-HTCondor-jobs.pdf).
