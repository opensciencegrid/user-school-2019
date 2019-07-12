---
status: done
---

<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: \#008; } </style>

Friday Exercise 2.1: Execute a Production Workflow
==================================================

In this exercise, you will:

-   finish testing workflow steps,
-   write the DAG for the workflow you planned, and
-   submit this workflow on `learn.chtc.wisc.edu`

There are bonus tasks in [Exercise 2.2](/materials/day5/part2-ex2-workflow-tuning), if you get through this part quickly, including running the workflow on the Open Science Grid.

Steps to Take
-------------

!!! note 
	While one person in your group works on step 1, someone else can work on step 2.

### 1. Finalize submit files

In the [previous exercise](/materials/day5/part1-ex2-plan-workflow) we ran some tests to find the optimal values for the *permutation* and *qtl* job steps.  Now we want to implement these values and confirm that they work. 

!!! note
	If your `WorkflowExercise` directory has gotten cluttered, feel free to rename it and redownload / untar a fresh copy before proceeding.  

1. Based on the values you chose in the last item of the previous exercise, modify **all** of the *permutation* and *QTL* submit files as follows: 
	- In the *permutation* submit files change the final value in the `arguments` line to the number of permutations that takes about 30 minutes to create (item 1 from the last section of the previous exercise).  
	- In the *permutation* submit file, change the `queue` statement to submit the number of jobs you chose in item 2 from the last section of the previous exercise.  
    - In *all* submit files, add or modify requests for cpus, memory and disk based on your tests.  
1. We're now going to do a final test of your modified *permutation* and *qtl* submit files for one trait.  
	1.  Submit one of these newly modified *permutation* submit files.  If your estimate of the necessary permutations per process (for a ~30-minute run time) was not close enough, modify and test the *permutation* jobs again.
	1.  Once the *permutation* jobs complete successfully, use `tarit.sh` to package the output from the test *permutation* step just above. Then run the corresponding *QTL* job. As with the just-completed *permutation* test, you will only need to submit one of the QTL submit files to confirm the approximate memory and disk needed. Make sure all of the desired output files for the QTL step are created to confirm success.
1.  Don't forget to test `taritall.sh` after a successful QTL job, to make sure it works as expected.

**After the optimized *permutation* and *QTL* tests, copy all output, error, and log files to a new directory to prepare for the production workflow.**

### 2. Create a DAG

Write a single DAG file for the workflow, including:

-   `JOB` lines for each submit file
-   `PARENT x CHILD y` lines as necessary
-   `SCRIPT PRE` and/or `SCRIPT POST` lines for the tar steps

!!! note
    You may need to think about how each `tar` step works for deciding on "PRE" or "POST" scripts for each.

If you need a refresher on what a DAG looks like, see [this exercise from Monday](/materials/day1/part4-ex3-complex-dag.md) or the [HTCondor manual](http://research.cs.wisc.edu/htcondor/manual/current/2_10DAGMan_Applications.html)

To **quickly** check that you've got the details of the DAG correct, you can modify the *permutation* submit files to run a) fewer permutations per job (in the `arguments` line) and b) fewer jobs overall (after `queue`).  

### 3. Run a production workflow

Once you have run a quick test of the DAG and you know all the steps are working together, you can submit a full-scale run of the DAG! To do so, make sure your *permutation* and *QTL* submit files have all of the appropriate values (permutations per job, number of permutation jobs, resource requests) based on your tests.  (Remember, this should be about 100,000 total permutations for each trait.)  Then submit the DAG. If you have any issues, consult the log and out files for the DAG and jobs, and modify your approach at any of the previous steps. While the full-scale DAG is running, you may wish to further detail your drawn workflow, including information regarding resource usage. Share all submit and DAG files with one another so everyone has a copy.

If you have time (even while step 3 is running smoothly), move on to the Bonus Tasks in [Exercise 2.2](/materials/day5/part2-ex2-workflow-tuning)

