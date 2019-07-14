---
status: in progress
---

Tuesday Exercise 1.1: Troubleshooting Jobs
==========================================

The goal of this exercise is to troubleshoot some common problems that you may encounter when submitting jobs using HTCondor.
This exercise will likely take you longer than the allotted time;
don't fret, an answer key is available and office hours the rest of the week, so work at your own pace.

Acquiring the Materials
-----------------------

The materials for this exercise are located on our web server.

1.  Log into `learn.chtc.wisc.edu`
2.  Use `wget` to retrieve the materials from the web server:

        :::console
        user@learn $ wget http://proxy.chtc.wisc.edu/SQUID/osgschool19/tues-part1-ex1.tar.gz

3.  Extract the tarball using the commands that you learned yesterday
4.  Change into the directory extracted from the tarball and explore its contents

Solving a Project Euler Problem
-------------------------------

The contents of the tarball that you've extracted contain a series of submit files, Python scripts, and an input file 
that are designed to solve [Project Euler problem 98](https://projecteuler.net/problem=98):

> By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 =
> 36^2. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square
> number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes
> are not permitted, neither may a different letter have the same digital value as another letter.
>
> Using p098_words.txt, a 16K text file containing nearly two-thousand common English words, find all the square
> anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).
>
> What is the largest square number formed by any member of such a pair?
>
> **NOTE:** All anagrams formed must be contained in the given text file.

Unfortunately, there are many issues with the submit files that you will have to work through before you can you can
obtain the solution to the problem!
The code in the Python scripts themselves should be bug-free.

### Finding anagrams ###

The first step in our workflow takes an input file with a list of words (`p098_words.txt`) and extracts all of the
anagrams using the `find_anagrams.py` script.
Naturally, we want to run this as an HTCondor job, so 

1. Submit the accompanying `find-anagrams.sub` file from the tarball.
   Try to do this step without looking at materials from yesterday.
   But if you are stuck, see [yesterday’s exercise 1.3](/materials/day1/part1-ex3-jobs.md).
1. Resolve any issues that you encounter until the job returns pairs of anagrams as its output.

Once you have satisfactory output, move onto the next section.

!!! note "Please be polite"
    Submit hosts are shared resources, so you should clean up after yourself.
    After you're done troubleshooting held jobs, remove them with the following command:

        :::console
        user@learn $ condor_rm -const 'JobStatus =?= 5' <JOB FILTER>

    | Where replacing `<JOB FILTER>` with...                 | Will remove...                              |
    |--------------------------------------------------------|---------------------------------------------|
    | Your username (e.g. `blin`)                            | All of your held jobs                       |
    | A cluster ID (e.g. `74078`)                            | All held jobs matching the given cluster ID |
    | A job ID (e.g. `97932.30`)                             | That specific held job                      |

### Finding the largest square ###

The next step of the workflow uses the `max_square.py` script to find the largest square number, if any, for a given
anagram word pair.
Let's submit jobs that runs `max_square.py` for all of the anagram word pairs (i.e. one job per word pair) that you
found in the previous section:

1. Submit the accompanying `squares.sub` file from the tarball
1. Resolve any issues that you encounter until you receive output for each job.
   Note that some jobs may have empty output since not all anagram word pairs are *square* anagram word pairs.

Next, you can find the largest square among your output by directly using the command line.
For example, if all of your job output has been placed in the `squares` directory and are named `square-1.out`,
`square-2.out`, etc. then you could run the following command to find the largest square:

``` console
user@learn $ cat squares/square-*.out | sort -n | tail - 1
```

You can check if you have the right answer with any of the OSG staff or by submitting the answer to Project Euler
(requires an account).

Answer Key
----------

There is also a working solution on our web server that can be retrieved with

``` console
user@learn $ wget http://proxy.chtc.wisc.edu/SQUID/osgschool19/tues-part1-ex1-key.tar.gz
```

It contains comments labeled `SOLUTION` that you can consult in case you get stuck.
Like any answer key, it's mainly useful as a verification tool, so try to only use it as a last resort or for detailed
explanations to improve your understanding.
