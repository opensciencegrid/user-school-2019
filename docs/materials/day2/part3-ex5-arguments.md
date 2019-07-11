---
status: done
---

<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: #008; } </style>

Bonus: Passing Arguments Through the Wrapper Script
===================================================

In this exercise, you will change the wrapper script and submit file from the previous exercise to use arguments.

Background
----------

So far, our wrapper scripts have had all files and options written out explicitly. However, imagine if you wanted to run the same job multiple times, or even just try out one or two different options or inputs. Instead of writing new wrapper scripts for each job, you can modify the script so that some of the values are set by *arguments*. Using script arguments will allow you to use the same script for multiple jobs, by providing different inputs or parameters. These arguments are normally passed on the command line:

But in our world of job submission, the arguments will be listed in the submit file, in the arguments line.

Identifying Potential Arguments
-------------------------------

1.  Find the directory you used to submit Open BUGS jobs and open your `run_openbugs.sh` wrapper script.
1.  What values might we want to input to the script via arguments? Hint: anything that we might want to change if we were to run the script many times.

In this example, some values we might want to change are the name of the input and output file. These will be the arguments for our script.

Modifying Files
---------------

1.  Note the name of the input and output files and open the submit file. Add an arguments line if it doesn't already exist, and fill it with our two chosen arguments: the name of the input file and the name of the output file: 

        :::file
		arguments = input.txt results.txt

1.  Now go back to the wrapper script. Each scripting language (bash, perl, python, R, etc.) will have its own particular syntax for capturing command line arguments. For bash (the language of our current wrapper script), the variables `$1` and `$2` represent  the first and second arguments, respectively. (If our script needed three arguments, we would use `$3` for the third one). Thus, in  the main command of the script, replace the file names with these variables: 

		:::file
		OpenBUGS < $1 > $2

1.  Once these changes are made, submit your jobs with `condor_submit`. Use `condor_q -nobatch` to see what the job command looks like to HTCondor.
