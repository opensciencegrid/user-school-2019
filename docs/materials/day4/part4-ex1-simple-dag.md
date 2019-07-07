---
status: done
---

<style type="text/css">
  pre em { font-style: normal; background-color: yellow; }
  pre strong { font-style: normal; font-weight: bold; color: \#008; }
</style>

# Monday Exercise 4.1: Coordinating a Set of Jobs With a Simple DAG

The objective of this exercise is to learn the very basics of running a set of jobs, where our set is just one job.

## What is DAGMan?

In short, DAGMan lets you submit complex sequences of jobs as long as they can be expressed as a directed acylic graph.
For example, you may wish to run a large parameter sweep but before the sweep run you need to prepare your data.  After
the sweep runs, you need to collate the results.  This might look like this, assuming you want to sweep over five
parameters:

![simple Dag](/materials/day1/files/osgus18-day1-part4-ex1-simple-dag.gif)

DAGMan has many abilities, such as throttling jobs, recovery from failures, and more.  More information about DAGMan can
be found at [in the HTCondor manual](http://research.cs.wisc.edu/htcondor/manual/v8.7/DAGManApplications.html).

## Submitting a Simple DAG

For our job, we will return briefly to the `sleep` program.

``` file
executable              = /bin/sleep
arguments               = 4
log                     = simple.log
output                  = simple.out
error                   = simple.error
request_memory = 1GB
request_disk = 1GB
request_cpus = 1
queue
```

We are going to get a bit more sophisticated in submitting our jobs now.  Let's have three windows open.  In one window,
you'll submit the job.  In another you will watch the queue, and in the third you will watch what DAGMan does.

First we will create the most minimal DAG that can be created: a DAG with just one node.  Put this into a file named
`simple.dag`.

``` file
Job Simple simple.sub
```

In your first window, submit the DAG:

``` console
username@learn $ condor_submit_dag simple.dag
-----------------------------------------------------------------------
File for submitting this DAG to Condor           : simple.dag.condor.sub
Log of DAGMan debugging messages                 : simple.dag.dagman.out
Log of Condor library output                     : simple.dag.lib.out
Log of Condor library error messages             : simple.dag.lib.err
Log of the life of condor_dagman itself          : simple.dag.dagman.log

Submitting job(s).
1 job(s) submitted to cluster 61.
-----------------------------------------------------------------------
```

In the second window, watch the queue:

``` console
username@learn $ watch -n 10 condor_q -nobatch

-- Submitter: learn.chtc.wisc.edu : <128.104.100.55:9618?sock=28867_10e4_2> : learn.chtc.wisc.edu
 ID      OWNER            SUBMITTED     RUN_TIME ST PRI SIZE CMD               
  61.0   roy             6/21 22:51   0+00:00:01 R  0   0.3  condor_dagman     

1 jobs; 0 completed, 0 removed, 0 idle, 1 running, 0 held, 0 suspended

-- Submitter: learn.chtc.wisc.edu : <128.104.100.55:9618?sock=28867_10e4_2> : learn.chtc.wisc.edu
 ID      OWNER            SUBMITTED     RUN_TIME ST PRI SIZE CMD               
  61.0   roy             6/21 22:51   0+00:01:25 R  0   0.3  condor_dagman     
  62.0   roy             6/21 22:51   0+00:00:00 I  0   0.7  simple 4 10      

2 jobs; 0 completed, 0 removed, 1 idle, 1 running, 0 held, 0 suspended

-- Submitter: learn.chtc.wisc.edu : <128.104.100.55:9618?sock=28867_10e4_2> : learn.chtc.wisc.edu
 ID      OWNER            SUBMITTED     RUN_TIME ST PRI SIZE CMD               
  61.0   roy             6/21 22:51   0+00:03:47 R  0   0.3  condor_dagman     
  62.0   roy             6/21 22:51   0+00:00:03 R  0   0.7  simple 4 10      

2 jobs; 0 completed, 0 removed, 0 idle, 2 running, 0 held, 0 suspended

-- Submitter: learn.chtc.wisc.edu : <128.104.100.55:9618?sock=28867_10e4_2> : learn.chtc.wisc.edu
 ID      OWNER            SUBMITTED     RUN_TIME ST PRI SIZE CMD               

0 jobs; 0 completed, 0 removed, 0 idle, 0 running, 0 held, 0 suspended
#%RED%<Ctrl-C>%ENDCOLOR%
```

In the third window, watch what DAGMan does:

``` console
username@learn $ tail -f --lines=500 simple.dag.dagman.out
6/21/12 22:51:13 Setting maximum accepts per cycle 8.
06/21/12 22:51:13 ******************************************************
06/21/12 22:51:13 ** condor_scheduniv_exec.61.0 (CONDOR_DAGMAN) STARTING UP
06/21/12 22:51:13 ** /usr/bin/condor_dagman
06/21/12 22:51:13 ** SubsystemInfo: name=DAGMAN type=DAGMAN(10) class=DAEMON(1)
06/21/12 22:51:13 ** Configuration: subsystem:DAGMAN local:<NONE> class:DAEMON
06/21/12 22:51:13 ** $CondorVersion: 7.7.6 Apr 16 2012 BuildID: 34175 PRE-RELEASE-UWCS $
06/21/12 22:51:13 ** $CondorPlatform: x86_64_rhap_5.7 $
06/21/12 22:51:13 ** PID = 5812
06/21/12 22:51:13 ** Log last touched 6/21 22:51:00
06/21/12 22:51:13 ******************************************************
06/21/12 22:51:13 Using config source: /etc/condor/condor_config
06/21/12 22:51:13 Using local config sources: 
06/21/12 22:51:13    /etc/condor/config.d/00-chtc-global.conf
06/21/12 22:51:13    /etc/condor/config.d/01-chtc-submit.conf
06/21/12 22:51:13    /etc/condor/config.d/02-chtc-flocking.conf
06/21/12 22:51:13    /etc/condor/config.d/03-chtc-jobrouter.conf
06/21/12 22:51:13    /etc/condor/config.d/04-chtc-blacklist.conf
06/21/12 22:51:13    /etc/condor/config.d/99-osg-ss-group.conf
06/21/12 22:51:13    /etc/condor/config.d/99-roy-extras.conf
06/21/12 22:51:13    /etc/condor/condor_config.local
06/21/12 22:51:13 DaemonCore: command socket at <128.104.100.55:60417>
06/21/12 22:51:13 DaemonCore: private command socket at <128.104.100.55:60417>
06/21/12 22:51:13 Setting maximum accepts per cycle 8.
06/21/12 22:51:13 DAGMAN_USE_STRICT setting: 0
06/21/12 22:51:13 DAGMAN_VERBOSITY setting: 3
06/21/12 22:51:13 DAGMAN_DEBUG_CACHE_SIZE setting: 5242880
06/21/12 22:51:13 DAGMAN_DEBUG_CACHE_ENABLE setting: False
06/21/12 22:51:13 DAGMAN_SUBMIT_DELAY setting: 0
06/21/12 22:51:13 DAGMAN_MAX_SUBMIT_ATTEMPTS setting: 6
06/21/12 22:51:13 DAGMAN_STARTUP_CYCLE_DETECT setting: False
06/21/12 22:51:13 DAGMAN_MAX_SUBMITS_PER_INTERVAL setting: 5
06/21/12 22:51:13 DAGMAN_USER_LOG_SCAN_INTERVAL setting: 5
06/21/12 22:51:13 allow_events (DAGMAN_IGNORE_DUPLICATE_JOB_EXECUTION, DAGMAN_ALLOW_EVENTS) setting: 114
06/21/12 22:51:13 DAGMAN_RETRY_SUBMIT_FIRST setting: True
06/21/12 22:51:13 DAGMAN_RETRY_NODE_FIRST setting: False
06/21/12 22:51:13 DAGMAN_MAX_JOBS_IDLE setting: 0
06/21/12 22:51:13 DAGMAN_MAX_JOBS_SUBMITTED setting: 0
06/21/12 22:51:15 DAGMAN_MAX_PRE_SCRIPTS setting: 0
06/21/12 22:51:15 DAGMAN_MAX_POST_SCRIPTS setting: 0
06/21/12 22:51:15 DAGMAN_ALLOW_LOG_ERROR setting: False
06/21/12 22:51:15 DAGMAN_MUNGE_NODE_NAMES setting: True
06/21/12 22:51:15 DAGMAN_PROHIBIT_MULTI_JOBS setting: False
06/21/12 22:51:15 DAGMAN_SUBMIT_DEPTH_FIRST setting: False
06/21/12 22:51:15 DAGMAN_ALWAYS_RUN_POST setting: True
06/21/12 22:51:15 DAGMAN_ABORT_DUPLICATES setting: True
06/21/12 22:51:15 DAGMAN_ABORT_ON_SCARY_SUBMIT setting: True
06/21/12 22:51:15 DAGMAN_PENDING_REPORT_INTERVAL setting: 600
06/21/12 22:51:15 DAGMAN_AUTO_RESCUE setting: True
06/21/12 22:51:15 DAGMAN_MAX_RESCUE_NUM setting: 100
06/21/12 22:51:15 DAGMAN_WRITE_PARTIAL_RESCUE setting: True
06/21/12 22:51:15 DAGMAN_DEFAULT_NODE_LOG setting: null
06/21/12 22:51:15 DAGMAN_GENERATE_SUBDAG_SUBMITS setting: True
06/21/12 22:51:15 ALL_DEBUG setting: 
06/21/12 22:51:15 DAGMAN_DEBUG setting: 
06/21/12 22:51:15 argv[0] == "condor_scheduniv_exec.61.0"
06/21/12 22:51:15 argv[1] == "-Lockfile"
06/21/12 22:51:15 argv[2] == "simple.dag.lock"
06/21/12 22:51:15 argv[3] == "-AutoRescue"
06/21/12 22:51:15 argv[4] == "1"
06/21/12 22:51:15 argv[5] == "-DoRescueFrom"
06/21/12 22:51:15 argv[6] == "0"
06/21/12 22:51:15 argv[7] == "-Dag"
06/21/12 22:51:15 argv[8] == "simple.dag"
06/21/12 22:51:15 argv[9] == "-CsdVersion"
06/21/12 22:51:15 argv[10] == "$CondorVersion: 7.7.6 Apr 16 2012 BuildID: 34175 PRE-RELEASE-UWCS $"
06/21/12 22:51:15 argv[11] == "-Force"
06/21/12 22:51:15 argv[12] == "-Dagman"
06/21/12 22:51:15 argv[13] == "/usr/bin/condor_dagman"
06/21/12 22:51:15 Default node log file is: </home/roy/condor/simple.dag.nodes.log>
06/21/12 22:51:15 DAG Lockfile will be written to simple.dag.lock
06/21/12 22:51:15 DAG Input file is simple.dag
06/21/12 22:51:15 Parsing 1 dagfiles
06/21/12 22:51:15 Parsing simple.dag ...
06/21/12 22:51:15 Dag contains 1 total jobs
06/21/12 22:51:15 Sleeping for 12 seconds to ensure ProcessId uniqueness
06/21/12 22:51:27 Bootstrapping...
06/21/12 22:51:27 Number of pre-completed nodes: 0
06/21/12 22:51:27 Registering condor_event_timer...
06/21/12 22:51:28 Sleeping for one second for log file consistency
06/21/12 22:51:29 MultiLogFiles: truncating log file /home/roy/condor/simple.log
06/21/12 22:51:29 Submitting Condor Node Simple job(s)...
```

%RED%**Here's where the job is submitted**%ENDCOLOR%

```file
06/21/12 22:51:29 submitting: condor_submit 
                              -a dag_node_name' '=' 'Simple 
                              -a +DAGManJobId' '=' '61 
                              -a DAGManJobId' '=' '61 
                              -a submit_event_notes' '=' 'DAG' 'Node:' 'Simple 
                              -a DAG_STATUS' '=' '0 
                              -a FAILED_COUNT' '=' '0 
                              -a +DAGParentNodeNames' '=' '"" submit
06/21/12 22:51:30 From submit: Submitting job(s).
06/21/12 22:51:30 From submit: 1 job(s) submitted to cluster 62.
06/21/12 22:51:30   assigned Condor ID (62.0.0)
06/21/12 22:51:30 Just submitted 1 job this cycle...
06/21/12 22:51:30 Currently monitoring 1 Condor log file(s)
06/21/12 22:51:30 Event: ULOG_SUBMIT for Condor Node Simple (62.0.0)
06/21/12 22:51:30 Number of idle job procs: 1
06/21/12 22:51:30 Of 1 nodes total:
06/21/12 22:51:30  Done     Pre   Queued    Post   Ready   Un-Ready   Failed
06/21/12 22:51:30   ===     ===      ===     ===     ===        ===      ===
06/21/12 22:51:30     0       0        1       0       0          0        0
06/21/12 22:51:30 0 job proc(s) currently held
06/21/12 22:55:05 Currently monitoring 1 Condor log file(s)
```

%RED%**Here's where DAGMan noticed that the job is running**%ENDCOLOR%

```file
06/21/12 22:55:05 Event: ULOG_EXECUTE for Condor Node Simple (62.0.0)
06/21/12 22:55:05 Number of idle job procs: 0
06/21/12 22:55:10 Currently monitoring 1 Condor log file(s)
06/21/12 22:55:10 Event: ULOG_IMAGE_SIZE for Condor Node Simple (62.0.0)
06/21/12 22:56:05 Currently monitoring 1 Condor log file(s)
06/21/12 22:56:05 Event: ULOG_IMAGE_SIZE for Condor Node Simple (62.0.0)
```

%RED%**Here's where DAGMan noticed that the job finished.**%ENDCOLOR%

```file
06/21/12 22:56:05 Event: ULOG_JOB_TERMINATED for Condor Node Simple (62.0.0)
06/21/12 22:56:05 Node Simple job proc (62.0.0) completed successfully.
06/21/12 22:56:05 Node Simple job completed
06/21/12 22:56:05 Number of idle job procs: 0
06/21/12 22:56:05 Of 1 nodes total:
06/21/12 22:56:05  Done     Pre   Queued    Post   Ready   Un-Ready   Failed
06/21/12 22:56:05   ===     ===      ===     ===     ===        ===      ===
06/21/12 22:56:05     1       0        0       0       0          0        0
06/21/12 22:56:05 0 job proc(s) currently held
```

%RED%**Here's where DAGMan noticed that all the work is done.**%ENDCOLOR%

```file
06/21/12 22:56:05 All jobs Completed!
06/21/12 22:56:05 Note: 0 total job deferrals because of -MaxJobs limit (0)
06/21/12 22:56:05 Note: 0 total job deferrals because of -MaxIdle limit (0)
06/21/12 22:56:05 Note: 0 total job deferrals because of node category throttles
06/21/12 22:56:05 Note: 0 total PRE script deferrals because of -MaxPre limit (0)
06/21/12 22:56:05 Note: 0 total POST script deferrals because of -MaxPost limit (0)
06/21/12 22:56:05 **** condor_scheduniv_exec.61.0 (condor_DAGMAN) pid 5812 EXITING WITH STATUS 0
```

Now verify your results:

``` console
username@learn $ cat simple.log
000 (062.000.000) 06/21 22:51:30 Job submitted from host: <128.104.100.55:9618?sock=28867_10e4_2>
    DAG Node: Simple
...
001 (062.000.000) 06/21 22:55:00 Job executing on host: <128.104.58.36:46761>
...
006 (062.000.000) 06/21 22:55:09 Image size of job updated: 750
    3  -  MemoryUsage of job (MB)
    2324  -  ResidentSetSize of job (KB)
...
006 (062.000.000) 06/21 22:56:00 Image size of job updated: 780
    3  -  MemoryUsage of job (MB)
    2324  -  ResidentSetSize of job (KB)
...
005 (062.000.000) 06/21 22:56:00 Job terminated.
    (1) Normal termination (return value 0)
        Usr 0 00:00:00, Sys 0 00:00:00  -  Run Remote Usage
        Usr 0 00:00:00, Sys 0 00:00:00  -  Run Local Usage
        Usr 0 00:00:00, Sys 0 00:00:00  -  Total Remote Usage
        Usr 0 00:00:00, Sys 0 00:00:00  -  Total Local Usage
    57  -  Run Bytes Sent By Job
    608490  -  Run Bytes Received By Job
    57  -  Total Bytes Sent By Job
    608490  -  Total Bytes Received By Job
    Partitionable Resources :    Usage  Request          
       Cpus                 :                 1          
       Disk (KB)            :      750      750          
       Memory (MB)          :        3        3          
...
```

Looking at DAGMan's various files, we see that DAGMan itself ran as a Condor job (specifically, a scheduler universe job).

``` console
username@learn $ ls simple.dag.*
simple.dag.condor.sub  simple.dag.dagman.log  simple.dag.dagman.out  simple.dag.lib.err  simple.dag.lib.out 

username@learn $ cat simple.dag.condor.sub
# Filename: simple.dag.condor.sub
# Generated by condor_submit_dag simple.dag 
universe    = scheduler
executable  = /usr/bin/condor_dagman
getenv      = True
output      = simple.dag.lib.out
error       = simple.dag.lib.err
log     = simple.dag.dagman.log
remove_kill_sig = SIGUSR1
+OtherJobRemoveRequirements = "DAGManJobId == $(cluster)"
# Note: default on_exit_remove expression:
# ( ExitSignal =?= 11 || (ExitCode =!= UNDEFINED && ExitCode >=0 && ExitCode <= 2))
# attempts to ensure that DAGMan is automatically
# requeued by the schedd if it exits abnormally or
# is killed (e.g., during a reboot).
on_exit_remove  = ( ExitSignal =?= 11 || (ExitCode =!= UNDEFINED && ExitCode >=0 && ExitCode <= 2))
copy_to_spool   = False
arguments   = "-f -l . -Lockfile simple.dag.lock -AutoRescue 1 -DoRescueFrom 0 -Dag simple.dag 
                              -CsdVersion $CondorVersion:' '7.7.6' 'Apr' '16' '2012' 'BuildID:' '34175' 'PRE-RELEASE-UWCS' '$ -Force -Dagman /usr/bin/condor_dagman"
environment = _CONDOR_DAGMAN_LOG=simple.dag.dagman.out;_CONDOR_MAX_DAGMAN_LOG=0
queue
```

IF you want to clean up some of these files (you may not want to, at least not yet):

``` console
username@learn $ rm simple.dag.*
```

## Challenge

- What is the scheduler universe? Why does DAGMan use it?
