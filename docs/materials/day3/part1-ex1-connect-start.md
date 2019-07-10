---
status: in progress
---

<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: \#008; } </style>

Thursday Exercise 1.1: Try an OSG Connect Software Module
=========================================================

In this exercise, we will submit a similar job to yesterday, but use OSG Connect's built-in Python software module to run our software. 

Setup
-----

Make sure you are logged into `training.osgconnect.net` (the OSG Connect submit server for this workshop). Create a scratch directory using your username in the `/local-scratch` folder if one doesn't already exist, and then `cd` to that folder. Copy the `fib.py` script from [yesterday](/materials/day2/part4-ex2-python-built) into this folder. 

Modules on OSG Connect
----------------------

1. The software installed in the OSG Connect software repository is able to viewed and used via a module system. To see the available software modules, you can type: 

		:::console
		username@training $ module avail

1. If you want to search for a specific module, you can use the `module spider` command. For this example, we want to use python, so let's look for it: 

		:::console
		username@training $ module spider python

	What is the name of the available Python modules? 

1. Finally, in order to use the available software, the software module has to be "loaded." First, let's check which version of Python is available by default: 

		:::console
		username@training $ python --version

1. Now, what happens after we load the `python/3.7.0` module?

		:::console
		username@training $ module load python/3.7.0
		username@training $ python --version

	Note that we won't be actually running Python on this server, but we'll use the same command inside the job to "activate" the Python installation. 

Using Modules in Jobs
---------------------

1. To use the modules we've just seen in jobs, we can load it via a script. Take a moment to consider which commands should go into this script, and then proceed. 

1. The job's executable script should look like this: 

		:::file
		#!/bin/bash
		
		module load python/3.7.0
		python3 fib.py 90

1. The submit file should like something like the submit files you used yesterday. Besides including requests for cpus, memory and disk, and transferring the python script, the submit file for this job should include a list of arguments that ensures the job will only run on servers where the OSG Connect software repository and modules are available:

		:::file
		requirements = (HAS_MODULES =?= true) && (OSGVO_OS_STRING == "RHEL 7") && (OpSys == "LINUX")

1. Submit this job. Does it produce the expected results? 