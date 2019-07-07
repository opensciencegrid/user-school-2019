---
status: done
---

<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: \#008; } </style>

Monday Exercise 3.1: Explore condor_q
======================================

The goal of this exercise is try out some of the most common options to the `condor_q` command, so that you can view jobs effectively.

The main part of this exercise should take just a few minutes, but if you have more time later, come back and work on the extension ideas at the end to become a `condor_q` expert!

Selecting Jobs
--------------

The `condor_q` program has many options for selecting which jobs are listed. You have already seen that the default mode (as of version 8.5) is to show only your jobs in "batch" mode:

``` console
username@learn $ condor_q
```

You've seen that you can view all jobs (all users) in the submit node's queue by using the `-all` argument:

``` console
username@learn $ condor_q -all
```

And you've seen that you can view more details about queued jobs, with each separate job on a single line using the `-nobatch` option:

``` console
username@learn $ condor_q -nobatch
username@learn $ condor_q -all -nobatch
```

Did you know you can also name one or more user IDs on the command line, in which case jobs for all of the named users are listed at once?

``` console
username@learn $ condor_q %RED%<username1> <username2> <username3>%ENDCOLOR%
```

There are two other, simple selection criteria that you can use. To list just the jobs associated with a single cluster number:

``` console
username@learn $ condor_q %RED%<CLUSTER>%ENDCOLOR%
```

For example, if you want to see the jobs in cluster 5678 (i.e., `5678.0`, `5678.1`, etc.), you use `condor_q 5678`.

To list a specific job (i.e., cluster.process, as in 5678.0):

``` console
username@learn $ condor_q %RED%<JOB.ID>%ENDCOLOR%
```

For example, to see job ID 5678.1, you use `condor_q 5678.1`.

!!! note
    You can name more than one cluster, job ID, or combination thereof on the command line, in which case jobs for
    **all** of the named clusters and/or job IDs are listed.

Let’s get some practice using `condor_q` selections!

1.  Using a previous exercise, submit several `sleep` jobs.
1.  List all jobs in the queue — are there others besides your own?
1.  Practice using all forms of `condor_q` that you have learned:
    -   List just your jobs, with and without batching.
    -   List a specific cluster.
    -   List a specific job ID.
    -   Try listing several users at once.
    -   Try listing several clusters and job IDs at once.
1.  When there are a variety of jobs in the queue, try combining a username and a different user's cluster or job ID in the same command — what happens?

Viewing a Job ClassAd
---------------------

You may have wondered why it is useful to be able to list a single job ID using `condor_q`. By itself, it may not be that useful. But, in combination with another option, it is very useful!

If you add the `-long` option to `condor_q` (or its short form, `-l`), it will show the complete ClassAd for each selected job, instead of the one-line summary that you have seen so far. Because job ClassAds may have 80–90 attributes (or more), it probably makes the most sense to show the ClassAd for a single job at a time. And you know how to show just one job! Here is what the command looks like:

``` console
username@learn $ condor_q -long %RED%<JOB.ID>%ENDCOLOR%
```

The output from this command is long and complex. Most of the attributes that HTCondor adds to a job are arcane and uninteresting for us now. But here are some examples of common, interesting attributes taken directly from `condor_q` output (except with some line breaks added to the `Requirements` attribute):

``` file
MyType = "Job"
Err = "sleep.err"
UserLog = "/home/cat/1-monday-2.1-queue/sleep.log"
JobUniverse = 5
Requirements = ( IsOSGSchoolSlot =?= true ) &&
        ( TARGET.Arch == "X86_64" ) &&
        ( TARGET.OpSys == "LINUX" ) &&
        ( TARGET.Disk >= RequestDisk ) &&
        ( TARGET.Memory >= RequestMemory ) &&
        ( TARGET.HasFileTransfer )
ClusterId = 2420
WhenToTransferOutput = "ON_EXIT"
Owner = "cat"
CondorVersion = "$CondorVersion: 8.5.5 May 03 2016 BuildID: 366162 $"
Out = "sleep.out"
Cmd = "/bin/sleep"
Arguments = "120"
```

!!! note
    Attributes are listed in no particular order and may change from time to time.
    Do not assume anything about the order of attributes in `condor_q` output.

**See what you can find in a job ClassAd from your own job.**

1.  Using a previous exercise, submit a `sleep` job that sleeps for at least 3 minutes (180 seconds).
1.  Before the job executes, capture its ClassAd and save to a file:

        :::console
        condor_q -l %RED%<JOB.ID>%ENDCOLOR% > classad-1.txt

1.  After the job starts execution but before it finishes, capture its ClassAd again and save to a file

        :::console 
        condor_q -l %RED%<JOB.ID>%ENDCOLOR% > classad-2.txt

Now examine each saved ClassAd file. Here are a few things to look for:

-   Can you find attributes that came from your submit file? (E.g., JobUniverse, Cmd, Arguments, Out, Err, UserLog, and so forth)
-   Can you find attributes that could have come from your submit file, but that HTCondor added for you? (E.g., Requirements)
-   How many of the following attributes can you guess the meaning of?
    -   DiskUsage
    -   ImageSize
    -   BytesSent
    -   JobStatus

Why Is My Job Not Running?
--------------------------

Sometimes, you submit a job and it just sits in the queue in Idle state, never running. It can be difficult to figure out why a job never matches and runs. Fortunately, HTCondor can give you some help.

To ask HTCondor why your job is not running, add the `-better-analyze` option to `condor_q` for the specific job. For example, for job ID 2423.0, the command is:

``` console
username@learn $ condor_q -better-analyze 2423.0
```

Of course, replace the job ID with your own.

Let’s submit a job that will never run and see what happens. Here is the submit file to use:

``` file
executable = /bin/hostname
output = norun.out
error = norun.err
log = norun.log
should_transfer_files = YES
when_to_transfer_output = ON_EXIT
request_memory = 8TB
queue
```

(Do you see what I did?)

1.  Save and submit this file.
1.  Run `condor_q -analyze` on the job ID.

There is a lot of output, but a few items are worth highlighting. Here is a sample from my own job (with many lines left out):

``` file
-- Submitter: learn.chtc.wisc.edu : ....
...
---
2423.000:  Run analysis summary.  Of 12388 machines,
   12388 are rejected by your job's requirements 
...
WARNING:  Be advised:
   No resources matched request's constraints

The Requirements expression for your job is:
...

Suggestions:

    Condition                         Machines Matched    Suggestion
    ---------                         ----------------    ----------
1   ( TARGET.Memory >= 8388608 )      0                   MODIFY TO 1000064
2   ( ... )
                                      12145                
3   ( TARGET.Arch == "X86_64" )       12388                
4   ( TARGET.OpSys == "LINUX" )       12386                
5   ( TARGET.Disk >= 20 )             12387                
6   ( TARGET.HasFileTransfer )        12388                
```

Toward the top, `condor_q` said that it considered 12388 “machines” (really, slots) and **all** 12388 of them were rejected by **my job’s requirements**. In other words, I am asking for something that is not available. But what?

The real clue comes from the breakdown of the Requirements expression, at the end of the output. 
Note the highlighted line: My job asked for **8 terabytes** of memory (8,388,608 MB) and **no** machines matched that part of the expression. 
Well, of course! 8 TB is a lot of memory on today’s machines. 
And finally, note the suggestion: If I reduce my memory request to 1,000,064 MB (about 1 TB), there will be at least one slot in the pool that will match that expression.

The output from `condor_q -analyze` (and `condor_q -better-analyze`) may be helpful or it may not be, depending on your exact case. The example above was constructed so that it would be obvious what the problem was. But in many cases, this is a good place to start looking if you are having problems matching.

Bonus: Automatic Formatting Output
----------------------------------

**Do this exercise only if you have time, though it's pretty awesome!**

There is a way to select the specific job attributes you want `condor_q` to tell you about with the `-autoformat` or `-af` option. In this case, HTCondor decides for you how to format the data you ask for from job ClassAd(s). 
(To tell HTCondor how to specially format this information, yourself, you could use the `-format` option, which we're not covering.)

To use autoformatting, use the `-af` option followed by the attribute name, for each attribute that you want to output:

``` console
username@learn $ condor_q -af Owner ClusterId Cmd
moate 2418 /share/test.sh
cat 2421 /bin/sleep
cat 2422 /bin/sleep
```

**Bonus Question**: If you wanted to print out the `Requirements` expression of a job, how would you do that with `-af`? Is the output what you expected? (HINT: for ClassAd attributes like "Requirements" that are long expressions, instead of simple values, you can use `-af:r` to view the expressions, instead of what it's current evaluation.)

References
----------

As suggested above, if you want to learn more about `condor_q`, you can do some reading:

-   Read the `condor_q` man page or HTCondor Manual section (same text) to learn about more options
-   Read about ClassAd attributes in Appendix A of the HTCondor Manual


