---
status: done
---

<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: #008; } </style>

Tuesday Exercise 4.2: Python Installation
===========================================

In this exercise, you will write a wrapper script that installs Python and then use it to run jobs. This exercise should take about 10 minutes.

Background
----------

In the previous exercise, we used a method that pre-built Python and then used that pre-built package to run Python scripts. In this exercise, we will use an alternative method for running Python jobs, by writing a wrapper script that installs Python with every job. This exercise should be done in the same directory as the previous exercise - you will need the same Python source code and `fib.py` script.

Wrapper script
--------------

Our wrapper script will need to install Python from the source code and then run our `fib.py` script.

1.  Based on the previous exercise, what are the steps we need to install Python? What file can we use for reference?

1.  We put our installation steps from the previous exercise into a file called `python_install.txt`. Based on this, put the installation steps into a script called `run_py.sh` 

1. Check your script against the file below 

		:::bash
		#!/bin/bash

		export PATH

		mkdir python
		tar -xzf Python-3.7.0.tgz
		cd Python-3.7.0
		./configure --prefix=$(pwd)/../python
		make
		make install
		cd ..

1.  We also need to run our `fib.py` script. We can do so by adding our installation location to the `PATH`, or by referencing the installation directly: 

		:::bash
		export PATH=$(pwd)/python/bin:$PATH

		python3 fib.py 90

	or

		:::bash
		python/bin/python3 fib.py 90

	Choose whichever method you prefer, and add it to your `run_py.sh` script.

1.  Make your `run_py.sh` script executable.

Submit file
-----------

The submit file for this exercise can be very similar to the [last one from Exercise 4.1](/materials/day2/part4-ex1-python-built.md).

1.  Make a copy of the submit file from the last exercise. What lines need to change? Make changes as appropriate.
1.  You need to change the transferred tarball (the Python source, instead of our `prebuilt_python.tar.gz`) and the job's executable. Once you've made these changes, submit the job using `condor_submit`.
1.  Check for the results in the `.out` file.


