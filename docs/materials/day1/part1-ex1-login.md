---
status: done
---

<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: \#008; } </style>

Monday Exercise 1.1: Log In and Look Around
===========================================

The goal of this first exercise is simply to log in to the local submit server and look around a little bit, which will take only a few minutes. 

**If you have trouble getting SSH access to the submit server, ask the instructors right away! Gaining access is critical for all remaining exercises.**

Logging In
----------

Today, you will use a submit server named `learn.chtc.wisc.edu`, which will allow you to submit jobs to our local HTCondor pool in CHTC.

To log in, use a [Secure Shell](http://en.wikipedia.org/wiki/Secure_Shell) (SSH) client.

-   From a Mac or Linux computer, run the Terminal app and use the `ssh` command, like so:

``` console
username@learn $ ssh %RED%<USERNAME>%ENDCOLOR%@learn.chtc.wisc.edu
```

-   On Windows, we recommend a free client called [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/), but any SSH client should be fine.

**If you need help finding or using an SSH client, ask the instructors for help right away**!

### About Your Password
-   Your username and initial password are located on the Accounts sheet of paper that you received this morning
-   While the `passwd` command will work (and will change your password temporarily), your initial password will be automatically reset for you on an hourly basis. (So you probably don't want to change your password, in the first place, and definitely want to keep your sheet of paper or memorize the password).

Running Commands
----------------

In the exercises, we will show commands that you are supposed to type or copy into the command line, like this:

``` console
username@learn $ hostname
learn.chtc.wisc.edu
```

!!! note
    In the first line of the example above, the `username@learn $` part is meant to show the Linux command-line prompt.
    You do not type this part! Further, your actual prompt probably is a bit different, and that is expected.
    So in the example above, the command that you type at your own prompt is just the eight characters `hostname`.
    The second line of the example, without the prompt, shows the output of the command; you do not type this part,
    either.

Here are a few other commands that you can try (the examples below do not show the output from each command):

``` console
username@learn $ whoami
username@learn $ date
username@learn $ uname -a
```

A suggestion for the day: Try typing into the command line as many of the commands as you can. Copy-and-paste is fine, of course, but **you WILL learn more if you take the time to type each command, yourself.**

Organizing Your Workspace
-------------------------

You will be doing many different exercises over the next few days, many of them on this submit server. Each exercise may use many files, once finished. To avoid confusion, it may be useful to create a separate directory for each exercise.

For instance, for the rest of this exercise, you may wish to create and use a directory named `monday-1.1-login`, or something like that.

``` console
username@learn $ mkdir Mon
username@learn $ mkdir Mon/1.1
username@learn $ cd Mon/1.1
```

Showing the Version of HTCondor
-------------------------------

HTCondor is installed on this server. But what version? You can ask HTCondor itself:

``` console
username@learn $ condor_version
$CondorVersion: 8.9.2 May 13 2019 BuildID: 469000 PackageID: 8.9.2-0.469000 $
$CondorPlatform: x86_64_RedHat7 $
```

As you can see from the output, we are using HTCondor 8.9.2.

### Background information about HTCondor version numbers

HTCondor always has two types of releases at one time: stable and development. HTCondor 8.6.x and 8.8.x are considered stable releases, indicated by even-numbered second digits (e.g., 6 or 8 in these cases). Within one stable series, all versions have the same features (for example 8.6.0 and 8.6.8 have the same set of features) and differ only in bug and security fixes.

HTCondor 8.9.2 is the latest development release series of HTCondor. You know that these are a development release because the second digit (i.e., 9) is an odd number.

Reference Materials
-------------------

Here are a few links to reference materials that might be interesting after the school (or perhaps during).

-   [HTCondor home page](http://research.cs.wisc.edu/htcondor/)
-   [HTCondor manuals](https://htcondor.readthedocs.io/en/v8_9_2/); it is probably best to read the manual corresponding to the version of HTCondor that you use (8.9.2 for today)
-   [Center for High Throughput Computing](http://chtc.cs.wisc.edu/), our campus research computing center, and home to HTCondor and other development of distributed computing tools
