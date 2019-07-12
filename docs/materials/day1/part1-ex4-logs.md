---
status: done
---

<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: \#008; } </style>

Monday Exercise 1.4: Read and Interpret Log Files
=================================================

The goal of this exercise is quite simple: 
Learn to understand the contents of a job log file, which is where HTCondor describes the steps 
taken to run your job.
When things go wrong with your job, the log is the best place to look for first pointers (in addition to the .err file).

This exercise is short, but you'll want to at least read over it before moving on (and come back later, if you can't run through it now).

Reading a Log File
------------------

For this exercise, we can examine a log file for any previous job that you have run. The example output below is based on the `sleep 60` job.

A job log file is updated throughout the life of a job, usually at key events. Each event starts with a heading that indicates what happened and when. Here are **all** of the event headings from the `sleep` job log (detailed output in between headings has been omitted here):

``` file
000 (5739.000.000) 07/25 10:44:20 Job submitted from host: <128.104.100.43:9618?addrs=...>
001 (5739.000.000) 07/25 10:45:11 Job executing on host: <128.104.55.42:9618?addrs=...>
006 (5739.000.000) 07/25 10:45:20 Image size of job updated: 72
040 (5739.000.000) 07/25 10:45:20 Started transferring output files
040 (5739.000.000) 07/25 10:45:20 Finished transferring output files
006 (5739.000.000) 07/25 10:46:11 Image size of job updated: 4072
005 (5739.000.000) 07/25 10:46:11 Job terminated.
```

There is a lot of extra information in those lines, but you can see:

-   The job ID: cluster 5739, process 0 (written `000`)
-   The date and local time of each event
-   A brief description of the event: submission, execution, some information updates, and termination

Some events provide no information in addition to the heading. For example:

``` file
000 (5739.000.000) 07/25 10:44:20 Job submitted from host: <128.104.100.43:9618?addrs=...>
...
```

and

``` file
001 (5739.000.000) 07/25 10:45:11 Job executing on host: <128.104.55.42:9618?addrs=...>
...
```

!!! note
    Each event ends with a line that contains only 3 dots: `...`

But the periodic information update event contains some additional information:

``` file
006 (5739.000.000) 07/25 10:45:20 Image size of job updated: 72
    1  -  MemoryUsage of job (MB)
    72  -  ResidentSetSize of job (KB)
...
```

These updates record the amount of memory that the job is using on the execute machine. This can be helpful information, so that in future runs of the job, you can tell HTCondor how much memory you will need.

The job termination event includes a great deal of additional information:

``` file
005 (5739.000.000) 07/25 10:46:11 Job terminated.
    (1) Normal termination (return value 0)
        Usr 0 00:00:00, Sys 0 00:00:00  -  Run Remote Usage
        Usr 0 00:00:00, Sys 0 00:00:00  -  Run Local Usage
        Usr 0 00:00:00, Sys 0 00:00:00  -  Total Remote Usage
        Usr 0 00:00:00, Sys 0 00:00:00  -  Total Local Usage
    0  -  Run Bytes Sent By Job
    27848  -  Run Bytes Received By Job
    0  -  Total Bytes Sent By Job
    27848  -  Total Bytes Received By Job
    Partitionable Resources :    Usage  Request Allocated
       Cpus                 :                 1         1
       Disk (KB)            :       40       30   4203309
       Memory (MB)          :        1        1         1
...
```

Probably the most interesting information is:

-   The `return value` (`0` here, means the executable completed and didn't indicate any internal errors; non-zero usually means failure)
-   The total number of bytes transferred each way, which could be useful if your network is slow
-   The `Partitionable Resources` table, especially disk and memory usage, which will inform larger submissions.

There are many other kinds of events, but the ones above will occur in almost every job log.


Understanding When Job Log Events Are Written
---------------------------------------------

When are events written to the job log file? Let’s find out. Read through the entire procedure below before starting, because some parts of the process are time sensitive.

1.  Change the `sleep` job submit file, so that the job sleeps for 2 minutes (= 120 seconds)
1.  Submit the updated sleep job
1.  As soon as the `condor_submit` command finishes, hit the return key a few times, to create some blank lines
1.  Right away, run a command to show the log file and **keep showing** updates as they occur:

        :::console
        username@learn $ tail -f sleep.log

1.  Watch the output carefully. When do events appear in the log file?
1.  After the termination event appears, press Control-C to end the `tail` command and return to the shell prompt.


Understanding How HTCondor Writes Files
---------------------------------------

When HTCondor writes the output, error, and log files, does it erase the previous contents of the file or does it add new lines onto the end? Let’s find out!

For this exercise, we can use the `hostname` job from earlier.

1.  Edit the `hostname` submit file so that it uses new and unique filenames for output, error, and log files.  
Alternatively, delete any existing output, error, and log files from previous runs of the `hostname` job.
1.  Submit the job three separate times in a row (there are better ways to do this, which we will cover in the next lecture)
1.  Wait for all three jobs to finish
1.  Examine the output file: How many hostnames are there? Did HTCondor erase the previous contents for each job, or add new lines?
1.  Examine the log file… carefully: What happened there? Pay close attention to the times and job IDs of the events.

If you have questions about how HTCondor handles these files, you could try finding relevant sections of the manual (this is hard and not as useful as one would hope), discuss it with neighbors or instructors, or ask questions at the end of this session.

