---
status: in progress
---

Thursday Exercise 3.1: Large Input Data
=======================================

In this exercise, we will do a similar version of the [previous exercise](/materials/day4/part2-ex3-stashcache-unique.md).
This exercise should take 10-15 minutes.

Background
----------

In the previous exercises, we used two "web-based" tools to stage and deliver our files to jobs:
[the squid web proxy](/materials/day4/part2-ex1-blast-proxy.md)  and [Stash](/materials/day4/part2-ex2-stashcache-shared.md).
Another alternative for handling large files (both input and output), especially if they are unique to each job, is a
local shared filesystem.
This is a filesystem that all (or most) of the execute servers can access, so data stored there can be copied to the job
from that system instead of as a transfer or download.

For this example, we'll be submitting the same jobs as the [previous exercise](/materials/day4/part2-ex3-stashcache-unique.md),
but we will stage our data in a shared filesystem local to CHTC.
The name of our shared filesystem is Gluster and user directories are found as sub-directories  of the path `/mnt/gluster`.
This is just one example of what it can look like to use a shared filesystem.
If you are running jobs at your own institution, the shared filesystem and how to access it may be different.

Accessing the Filesystem
------------------------

!!! note "Running on `learn.chtc.wisc.edu`"
    For these next 2 exercises, we will be using **`learn.chtc.wisc.edu`**.

Because our shared filesystem is **only** available on the local CHTC HTCondor pool, you'll need to log into our local
submit server, **`learn.chtc.wisc.edu`**.

Once you've logged in, navigate to your Gluster directory.
It should be at the location `/mnt/gluster/<USERNAME>`, where `<USERNAME>` is your username on `learn.chtc.wisc.edu`.

Previous Files
--------------

### Data

Like the previous example, we'll start by downloading our source movie files into the Gluster directory.
Run this command **in your Gluster directory**, `/mnt/gluster/<USERNAME>`.

``` console
user@learn $ wget http://proxy.chtc.wisc.edu/SQUID/osgschool19/videos.tar.gz
```

While the files are copying, feel free to open a second connection to `learn.chtc.wisc.edu` and follow the instructions below.
Once the files have finished downloading, untar them.

### Software, Executable, Submit File

Because these jobs will be similar to the previous exercise, we can copy the software (`ffmpeg`), our executable
(`run_ffmpeg.sh`) and submit file from `user-training.osgconnect.net` to `learn.chtc.wisc.edu`, or, feel free to
replicate these by following the instructions in the [previous exercise](/materials/day4/part2-ex3-stashcache-unique.md).
These files should go into a sub-directory of your **home** directory, **not your Gluster directory**.

Ch-ch-ch-changes
----------------

What changes will we need to make to our previous job submission in order to submit it in CHTC, using the Gluster
location?
Read on.

### Script

The major actions of our script will be the same: *copy* the movie file to the job's current working directory,
*run* the appropriate `ffmpeg` command, and then *remove* the original movie file.
The main difference is that the `mov` file will be copied from  your Gluster directory instead of being downloaded from
Stash.
Like before, your script should remove  that file before the job completes so that it doesn't get transferred back to
the submit server.

1. Remove the lines in the `run_ffmpeg.sh` that mention `module load`.

2. Remove the `stashcp` line

3. Change the first command of your `run_ffmpeg.sh` script to only copy one `.mov` file: 

        cp /mnt/gluster/<USERNAME>/test_open_terminal.mov ./

You should use your username on `learn.chtc.wisc.edu` in the path above.
If you have a version of the script that uses arguments instead of the filenames, that's okay.

### Submit File

1.  Remove any previous requirements and add a line to the file (before the final queue statement) that ensures your job
    will land on computers that have access to Gluster: 

        requirements = (Target.HasGluster == true)

Initial Job
-----------

As before, we should test our job submission with a single `mov` file before submitting jobs for all three.
Alter your submit file (if necessary) to  run a job that converts the `test_open_terminal.mov` file.

Once the job finishes, check to make sure everything ran as expected:

1.  Check the directory where you submitted the job. Did the output `.mp4` file return?
2.  Also in the directory where you submitted the job - did the original `.mov` file return here accidentally?
3.  Check file sizes. How big is the returned `.mp4` file? How does that compare to the original `.mov` input?

If your job successfully returned the converted `.mp4` file and **not** the `.mov` file to the submit server, and the
`.mp4` file was appropriately scaled down, then our script did what it should have.

Multiple jobs
-------------

Change your submit file as in the previous exercise in order to submit 3 jobs to convert all three files!


