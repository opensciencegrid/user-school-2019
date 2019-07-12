---
status: done
---

<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: #008; } </style>

Wednesday Exercise 1.4: Pre-packaging Code
==========================================

In this exercise, you will create an installation of a Bayesian inference package (OpenBUGS) and then create a wrapper script to unpack that installation to run jobs. It should take 30-35 minutes.

Background
----------

Some software cannot be compiled into a single executable, whether you compile it yourself (as in [Exercise 3.1](/materials/day2/part3-ex1-compiling)) or download it already compiled (as in [Exercise 3.2](/materials/day2/part3-ex2-precompiled)). In this case, it is necessary to download or create a portable copy of the software and then use a wrapper script (as in the [previous exercise](/materials/day2/part3-ex3-wrapper)) to "install" the software on a per job basis. This script can either install the software from the source code, or (as in this exercise), unpack a portable software package that you've pre-built yourself.

Our Software Example
--------------------

For this exercise, we will be using the Bayseian inference package OpenBUGS. OpenBUGS is a good example of software that is not compiled to a single executable; it has multiple executables as well as a helper library.

1.  Do an internet search to find the Open BUGS software downloads page.

1.  Create a directory for this exercise on the CHTC submit server `learn.chtc.wisc.edu` (**not** `training.osgconnect.net`), 

1. Because you can't download the OpenBUGS source tarball directly, download it from our "squid" webserver: 

		:::console
		username@learn $ wget http://proxy.chtc.wisc.edu/SQUID/osgschool19/OpenBUGS-3.2.3.tar.gz

Where to Prepare
----------------

Our goal is to pre-build an OpenBUGS installation, and then write a script that will unpack that installation and run a simulation.

1.  Where can we create this pre-built installation? Based on the end of the lecture, what are our options and which would be most appropriate? Make a guess before moving on.

1.  Because we're on the CHTC-based submit node (`learn.chtc.wisc.edu`), we have the option of using an interactive job to build the OpenBUGS installation. This is a good option because the submit server is already busy with lots of users and we don't know how long the OpenBUGS install will take. We'll also target specific build servers with extra tools by adding some special requirements to our interactive job. 

    1.  Copy the following lines into a file named `build.submit`

            :::file
			log = build.log

			should_transfer_files = YES
			when_to_transfer_output = ON_EXIT
			transfer_input_files = 
			
			+IsBuildJob = true
			requirements = (IsBuildSlot == true)

			request_cpus = 1
			request_disk = 2GB
			request_memory = 2GB

			queue

	1.  Note the lack of executable. Condor doesn't need an executable for this job because it will be interactive, meaning *you* are running the commands instead of Condor.
	1.  In order to create the installation, we will need the source code to come with us. The `transfer_input_files` line is blank - **fill it in with the name of our Open BUGS source tarball**.

	1.  To request an interactive job, we will add a `-i` flag to the `condor_submit` command. The whole command you enter should look like this: 

			:::console
			username@learn $ condor_submit -i build.submit

Read Through Installation Documentation
---------------------------------------

While you're waiting for the interactive job to start, you can start reading the Open BUGS installation documentation online.

1.  Find the installation instructions for Open BUGS.
1.  On the downloads page, there are short instructions for how to install Open BUGS. There are two options shown for installation -- which should we use?
1.  The first installation option given uses `sudo` -- which is an administrative permission that you won't have as a normal user. Luckily, as described in the instructions, you can use the `--prefix` option to set where Open BUGS will be installed, which will allow us to install it without administrative permissions.

Installation
------------

Your interactive job should have started by now and we've learned about installing our program. Let's test it out.

1.  Before we follow the installation instructions, we should create a directory to hold our installation. You can create this in the current directory. 

		:::console
		username@host $ mkdir openbugs

1.  Now run the commands to unpack the source code: 

        :::console
		username@host $ tar -zxf OpenBUGS-3.2.3.tar.gz
		username@host $ cd OpenBUGS-3.2.3

1.  Now we can follow the second set of installation instructions. For the prefix, we'll use the command `$(pwd)` to capture the name of our current working directory and then a relative path to the `openbugs` directory we created in step 1: 

		:::console
		username@host $ ./configure --prefix=$(pwd)/../openbugs
		username@host $ make
		username@host $ make install

1.  **Go back to the job's main working directory**: 

		:::console
		username@host $ cd ..

	and confirm that our installation procedure created `bin`,  `lib`, and `share` directories. 

		:::console
		username@host $ ls openbugs
		bin lib share

1.  Now we want to package up our installation, so we can use it in other jobs. We can do this by compressing any necessary directories into a single gzipped tarball. 

		:::console
		username@host $ tar -czf openbugs.tar.gz openbugs/

1.  Once everything is complete, type `exit` to leave the interactive job. Make sure that your tarball is in the main working directory - it will be transferred back to the submit server automatically. 

		:::console
		username@learn $ exit

Note that we now have two tarballs in our directory -- the *source* tarball (`OpenBUGS-3.2.3.tar.gz`), which we will no longer need and our newly built installation (`openbugs.tar.gz`) which is what we will actually be using to run jobs.

Wrapper Script
--------------

Now that we've created our portable installation, we need to write a script that opens and uses the installation, similar to the process we used in the  [previous exercise](part3-ex3-wrapper.md). These steps should be performed back on the submit server (`learn.chtc.wisc.edu`).

1.  Create a script called `run_openbugs.sh`. The script will first need to untar our installation, so the script should start out like this:  

		:::bash
		#!/bin/bash

		tar -xzf openbugs.tar.gz

1.  We're going to use the same `$(pwd)` trick from the installation in order to tell the computer how to find Open BUGS. We will do this by setting the `PATH` environment variable, to include the directory where Open BUGS is installed: 

		:::bash
		export PATH=$(pwd)/openbugs/bin:$PATH

1.  Finally, the wrapper script needs to not only setup Open BUGS, but actually run the program. Add the following lines to your `run_openbugs.sh` wrapper script. 

        :::bash
		OpenBUGS < input.txt > results.txt

1.  Make sure the wrapper script has executable permissions: 

		:::console
		username@learn $ chmod u+x run_openbugs.sh


Run a Open BUGS job
-------------------

We're almost ready! We need two more pieces to run a OpenBUGS job.

1.  Download the necessary input files to your directory on the submit server and then untar them. 

		:::console
		username@learn $ wget http://proxy.chtc.wisc.edu/SQUID/osgschool18/openbugs_files.tar.gz
		username@learn $ tar -xzf openbugs_files.tar.gz

1.  Our last step is to create a submit file for our Open BUGS job. Think about which lines this submit file will need. Make a copy of a previous submit file (you could use the blast submit file from the [previous exercise](/materials/day2/part3-ex3-wrapper) as a base) and modify it as you think necessary.

1.  The two most important lines to modify for this job are listed below; check them against your own submit file: 

        :::file
        executable = run_openbugs.sh
        transfer_input_files = openbugs.tar.gz, openbugs_files/

    A wrapper script will always be a job's `executable`.
    When using a wrapper script, you must also always remember to transfer the software/source code using
    `transfer_input_files`.

    !!! note
        The `/` in the `transfer_input_files` line indicates that we are transferring the *contents* of that directory (which in this case, is what we want), rather than the directory itself.

1.  We also need to add a requirement to ensure that the job will run on a Linux system. This can be done with the line:

        :::file
        requirements = (OpSys == "LINUX")

1.  Submit the job with `condor_submit`.

1.  Once the job completes, it should produce a `results.txt` file.


