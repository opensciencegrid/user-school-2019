---
status: done
---

<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: \#008; } </style>

Tuesday Exercise 3.2: Using a Pre-compiled Binary
===================================================

In this exercise, we will run a job using a downloaded, pre-compiled binary. This exercise should take 10-15 minutes.

Background
----------

In the previous exercise, we used a piece of software that was available as source code, and could be compiled to a static binary. However, software is available in many different forms. You may also encounter scientific software provided as a static binary. Here, the software provider has compiled the software for you (typically on several operating systems). Using a pre-compiled binary means you can avoid compiling the code yourself; accessing the software and getting it ready to run is as simple as downloading the binary.

Our Software Example
--------------------

The software we will be using for this example is a common tool for aligning genome and protein sequences against a
reference database, the BLAST program.

1.  Search the internet for the BLAST software.  Searches might include "blast executable or "download blast software".  Hopefully these searches will lead you to a BLAST website page that looks like this:

    ![BLAST landing page](/materials/day2/files/osgus19-day2-part3-ex2-blast-front-page.png)

1.  Click on the title that says "Download BLAST" and then look for the link that has the latest installation and source code.  You should end up on a page with a list of each version of BLAST that is available for different operating systems.

1.  We could download the source and compile it ourselves, but instead, we're going to use one of the pre-built binaries.  Before proceeding, look at the list of downloads and try to determine which one you want. 

1.  Based on our operating system, we want to use the Linux binary, which is labelled with the `x64-linux` suffix. 

	![BLAST downloads](/materials/day2/files/osgus19-day2-part3-ex2-blast-src-page.png)

	All the other links are either for source code or other operating systems. 
	
1. While logged into `training.osgconnect.net`, create a directory for this exercise. Then download the appropriate `tar.gz` file and un-tar it. You can download the file directly from the BLAST website using `wget` or download our local copy with the command below: 

        :::console
        user@training $ wget http://proxy.chtc.wisc.edu/SQUID/osgschool19/ncbi-blast-2.9.0+-x64-linux.tar.gz
        user@training $ tar -xzf ncbi-blast-2.9.0+-x64-linux.tar.gz

1.  We're going to be using the `blastx` binary in our job. Where is it in the directory you just downloaded?

Copy the Input Files
--------------------

To run BLAST, we need an input file and reference database. For this example, we'll use the "pdbaa" database, which contains sequences for the protein structure from the Protein Data Bank. For our input file, we'll use an abbreviated fasta file with mouse genome information.

1.  Download these files to your current directory: 

        :::console
        username@training $ wget http://proxy.chtc.wisc.edu/SQUID/osgschool19/pdbaa.tar.gz
        username@training $ wget http://proxy.chtc.wisc.edu/SQUID/osgschool19/mouse.fa

1.  Untar the `pdbaa` database: 

        :::console
        username@training $ tar -xzf pdbaa.tar.gz


Submitting the Job
------------------

We now have our program (the pre-compiled `blastx` binary) and our input files, so all that remains is to create the submit file. The form of a typical `blastx` command looks something like this:

```file
blastx -db <database_dir/prefix> -query <input_file> -out <output_file>
```

1.   Copy the submit file from the last exercise into your current directory. 

1. Think about which lines you will need to change or add to your submit file in order to submit the job successfully. In particular:    
	-   What is the executable?
	-   How can you indicate the entire command line sequence above?
	-   Which files need to be transferred in addition to the executable?
	-   Does this job require a certain type of operating system?

1. Try to answer these questions and modify your submit file appropriately.

1. Once you have done all you can, check your submit file against the lines below, which contain the exact compoenents to run this particular job.

    * The executable is `blastx`, which is located in the `bin` directory of our downloaded BLAST directory. We need to use the `arguments` line in the submit file to express the rest of the command. 
    
            :::file
            executable = ncbi-blast-2.9.0+/bin/blastx
            arguments = -db pdbaa/pdbaa -query mouse.fa -out results.txt

    * The BLAST program requires our input file and database, so they must be transferred with `transfer_input_files`. 
    
            :::file
            transfer_input_files = pdbaa, mouse.fa

    * Because we downloaded a Linux-specific binary, we need to request machines that are running Linux. 
    
            :::file
            requirements = (OSGVO_OS_STRING == "RHEL 7")

1. Submit the blast job using `condor_submit`. Once the job starts, it should run in just a few minutes and produce a file called `results.txt`.
