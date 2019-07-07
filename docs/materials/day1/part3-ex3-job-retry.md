---
status: done
---

<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: \#008; } </style>

Monday Exercise 3.3: Retries
============================

The goal of this exercise is to demonstrate running a job that intermittently fails and thus could benefit from having HTCondor automatically retry it.

This first part of the exercise should take only a few minutes, and is designed to setup the next exercises.

Bad Job
-------

Let’s assume that a colleague has shared with you a program, and it fails once in a while. In the real world, we would probably just fix the program, but what if you cannot change the software? Unfortunately, this situation happens more often than we would like.

Below is a simple Python script that fails once in a while. We will not fix it, but use it to simulate a program that can fail and that we **cannot** fix.

``` file
#!/usr/bin/env python

# murphy.py simulates a real program with real problems
import random
import sys
import time

# Create a random number seeded by system entropy
r = random.SystemRandom()

# One time in three, simulate a runtime error
if (r.randint(0,2) == 0):
    # intentionally print no output
    sys.exit(15)
else:
    time.sleep(3)
    print "All work done correctly"

# By convention, zero exit code means success
sys.exit(0)
```

Even if you are not a Python expert, you may be able to figure out what this program does.

Let’s see what happens when a program like this one is run in HTCondor.

1.  In a new directory for this exercise, save the script above as `murphy.py`.
1.  Write a submit file for the script; `queue 20` instances of the job and be sure to ask for 20 MB of memory and disk.
1.  Submit the file and wait for the jobs to finish.

What output do you expect? What output did you get? If you are curious about the exit code from the job, it is saved in completed jobs in `condor_history` in the `ExitCode` attribute. The following command will show the `ExitCode` for a given cluster of jobs:

``` console
username@learn $ condor_history %RED%<CLUSTER>%ENDCOLOR% -af ProcId ExitCode
```

(Be sure to replace `<cluster>` with your actual cluster ID)

How many of the jobs succeeded? How many failed?

Retrying Failed Jobs
--------------------

Now let’s see if we can solve the problem of jobs that fail once in a while. In this particular case, if HTCondor runs a failed job again, it has a good chance of succeeding. Not all failing jobs are like this, but in this case it is a reasonable assumption.

From the lecture materials, implement the `max_retries` feature to retry any job with a non-zero exit code up to 5 times, then resubmit the jobs. Did your change work?

After the jobs have finished, examine the log file(s) to see what happened in detail. Did any jobs need to be restarted? Another way to see how many restarts there were is to look at the `NumJobStarts` attribute of a completed job with the `condor_history` command, in the same way you looked at the `ExitCode` attribute earlier. Does the number of retries seem correct? For those jobs which did need to be retried, what is their `ExitCode`; and what about the `ExitCode` from earlier execution attempts?

A (Too) Long Running Job
------------------------

Sometimes, an ill-behaved job will get stuck in a loop and run forever, instead of exiting with a failure code, and it may just need to be re-run (or run on a different execute server) to complete without getting stuck. We can modify our Python program to simulate this kind of bad job with the following file:

``` file
#!/usr/bin/env python

# murphy.py simulate a real program with real problems
import random
import sys
import time

# Create a random number seeded by system entropy
r = random.SystemRandom()

# One time in three, simulate an infinite loop
if (r.randint(0,2) == 0):
        # intentionally print no output
        time.sleep(3600)
        sys.exit(15)
else:
        time.sleep(3)
        print "All work done correctly"

# By convention, zero exit code means success
sys.exit(0)
```

Again, you may be able to figure out what this new program does.

1.  Save the script to a new file named `murphy2.py`.
1.  Copy your previous submit file to a new name and change the `executable` to `murphy2.py`.
1.  If you like, submit the new file — but after a while be sure to remove the whole cluster to clear out the “hung” jobs.
1.  Now try to change the submit file to automatically remove any jobs that **run** for more than one minute. You can make this change with just a single line in your submit file

        :::file
        periodic_remove = (JobStatus == 2) && ( (CurrentTime - EnteredCurrentStatus) > 60 )

1.  Submit the new file. Do the long running jobs get removed? What does `condor_history` show for the cluster after all jobs are done? Which job status (i.e. idle, held, running) do you think `JobStatus == 2` corresponds to?

Bonus Exercise
--------------

If you have time, edit your submit file so that instead of removing long running jobs, have HTCondor automatically put the long-running job on hold, and then automatically release it.

