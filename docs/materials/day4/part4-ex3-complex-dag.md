---
status: done
---

<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: \#008; } </style>

Monday Exercise 4.3: A More Complex DAG
=======================================

The objective of this exercise is to run a real set of jobs with DAGMan.

Make Your Job Submission Files
------------------------------

We'll run our `goatbrot` example. If you didn't read about it yet, [please do so now](/materials/day1/part4-ex2-mandelbrot.md). We are going to make a DAG with four simultaneous jobs (`goatbrot`) and one final node to stitch them together (`montage`). This means we have five jobs. We're going to run `goatbrot` with more iterations (100,000) so each job will take longer to run.

You can create your five jobs. The goatbrot jobs are very similar to each other, but they have slightly different parameters and output files.

### goatbrot1.sub

``` file
executable              = /usr/local/bin/goatbrot
arguments               = -i 100000 -c -0.75,0.75 -w 1.5 -s 500,500 -o tile_0_0.ppm
log                     = goatbrot.log
output                  = goatbrot.out.0.0
error                   = goatbrot.err.0.0
request_memory          = 1GB
request_disk            = 1GB
request_cpus            = 1
queue
```

### goatbrot2.sub

``` file
executable              = /usr/local/bin/goatbrot
arguments               = -i 100000 -c 0.75,0.75 -w 1.5 -s 500,500 -o tile_0_1.ppm
log                     = goatbrot.log
output                  = goatbrot.out.0.1
error                   = goatbrot.err.0.1
request_memory          = 1GB
request_disk            = 1GB
request_cpus            = 1
queue
```

### goatbrot3.sub

``` file
executable              = /usr/local/bin/goatbrot
arguments               = -i 100000 -c -0.75,-0.75 -w 1.5 -s 500,500 -o tile_1_0.ppm
log                     = goatbrot.log
output                  = goatbrot.out.1.0
error                   = goatbrot.err.1.0
request_memory          = 1GB
request_disk            = 1GB
request_cpus            = 1
queue
```

### goatbrot4.sub

``` file
executable              = /usr/local/bin/goatbrot
arguments               = -i 100000 -c 0.75,-0.75 -w 1.5 -s 500,500 -o tile_1_1.ppm
log                     = goatbrot.log
output                  = goatbrot.out.1.1
error                   = goatbrot.err.1.1
request_memory          = 1GB
request_disk            = 1GB
request_cpus            = 1
queue
```

### montage.sub

You should notice that the `transfer_input_files` statement refers to the files created by the other jobs.

``` file
executable              = /usr/bin/montage
arguments               = tile_0_0.ppm tile_0_1.ppm tile_1_0.ppm tile_1_1.ppm -mode Concatenate -tile 2x2 mandel-from-dag.jpg
transfer_input_files    = tile_0_0.ppm,tile_0_1.ppm,tile_1_0.ppm,tile_1_1.ppm
output                  = montage.out
error                   = montage.err
log                     = montage.log
request_memory          = 1GB
request_disk            = 1GB
request_cpus            = 1
requirements            = OpSysMajorVer =?= 6
queue
```

Make your DAG
-------------

In a file called `goatbrot.dag`, you have your DAG specification:

``` file
JOB g1 goatbrot1.sub
JOB g2 goatbrot2.sub
JOB g3 goatbrot3.sub
JOB g4 goatbrot4.sub
JOB montage montage.sub
PARENT g1 g2 g3 g4 CHILD montage
```

Ask yourself: do you know how we ensure that all the `goatbrot` commands can run simultaneously and all of them will complete before we run the montage job?

Running the DAG
---------------

Submit your DAG:

``` console
username@learn $ condor_submit_dag goatbrot.dag
-----------------------------------------------------------------------
File for submitting this DAG to Condor           : goatbrot.dag.condor.sub
Log of DAGMan debugging messages                 : goatbrot.dag.dagman.out
Log of Condor library output                     : goatbrot.dag.lib.out
Log of Condor library error messages             : goatbrot.dag.lib.err
Log of the life of condor_dagman itself          : goatbrot.dag.dagman.log

Submitting job(s).
1 job(s) submitted to cluster 71.

-----------------------------------------------------------------------
```

Watch Your DAG
--------------

Let’s follow the progress of the whole DAG:

1.  Use the `watch` command to run `condor_q -nobatch` every 10 seconds:

        :::console
        username@learn $ watch -n 10 condor_q -nobatch

    %RED%**Here we see DAGMan running:**%ENDCOLOR% 

        :::console
         ID  OWNER  SUBMITTED   RUN_TIME ST PRI SIZE CMD 
        71.0 roy   6/22 17:39 0+00:00:03 R  0    0.3 condor_dagman

    %RED%**DAGMan has submitted the goatbrot jobs, but they haven't started running yet**%ENDCOLOR%
    
        :::console
         ID  OWNER SUBMITTED   RUN_TIME ST PRI SIZE CMD 
        71.0 roy  6/22 17:39 0+00:00:17 R  0    0.3 condor_dagman 
        72.0 roy  6/22 17:39 0+00:00:00 I  0    0.0 goatbrot -i 100000 
        73.0 roy  6/22 17:39 0+00:00:00 I  0    0.0 goatbrot -i 100000 
        74.0 roy  6/22 17:39 0+00:00:00 I  0    0.0 goatbrot -i 100000 
        75.0 roy  6/22 17:39 0+00:00:00 I  0    0.0 goatbrot -i 100000

    %RED%**They're running**%ENDCOLOR% 

        :::console
         ID  OWNER SUBMITTED   RUN_TIME ST PRI SIZE CMD
        71.0 roy  6/22 17:39 0+00:07:15 R  0    0.3 condor_dagman 
        72.0 roy  6/22 17:39 0+00:00:03 R  0    0.0 goatbrot -i 100000 
        73.0 roy  6/22 17:39 0+00:00:03 R  0    0.0 goatbrot -i 100000 
        74.0 roy  6/22 17:39 0+00:00:03 R  0    0.0 goatbrot -i 100000 
        75.0 roy  6/22 17:39 0+00:00:03 R  0    0.0 goatbrot -i 100000

    %RED%**They finished, but DAGMan hasn't noticed yet. It only checks periodically:**%ENDCOLOR%

        :::console
         ID  OWNER SUBMITTED   RUN_TIME ST PRI SIZE CMD 
        71.0 roy  6/22 17:39 0+00:08:46 R  0    0.3 condor_dagman
 

    Eventually, you'll see the montage job submitted, then running, then leave the queue, and then DAGMan will leave the queue.

1.  Examine your results. For some reason, goatbrot prints everything to stderr, not stdout.

        :::console
        username@learn $ cat goatbrot.err.0.0 
        Complex image: Center: -0.75 + 0.75i Width: 1.5 Height: 1.5 Upper Left: -1.5 + 1.5i Lower Right: 0 + 0i
         
        Output image: Filename: tile_0_0.ppm Width, Height: 500, 500 Theme: beej Antialiased: no
        
        Mandelbrot: Max Iterations: 100000 Continuous: no
         
        Goatbrot: Multithreading: not supported in this build

        Completed: 100.0%

1.  Examine your log files (`goatbrot.log` and `montage.log`) and DAGMan output file (`goatbrot.dag.dagman.out`). Do they look as you expect? Can you see the progress of the DAG in the DAGMan output file?
1.  As you did earlier, copy the resulting `mandel-from-dag.jpg` to your `public_html` directory, then access it from your web browser. Does the image look correct?
1.  Clean up your results by removing all of the `goatbrot.dag.*` files if you like. Be careful to not delete the `goatbrot.dag` file.

Bonus Challenge
---------------

-   Re-run your DAG. When jobs are running, try `condor_q -nobatch -dag`. What does it do differently?
-   Challenge, if you have time: Make a bigger DAG by making more tiles in the same area.
