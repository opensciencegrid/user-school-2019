---
status: in progress
---

Monday Exercise 4.2: Log in to the OSG Submit Machine
=====================================================

The goal of this exercise is to log in to a different submit host so that you can start submitting jobs into the OSG
instead of the local cluster here at UW-Madison.
Additionally, you will learn about the `tar` and `scp` commands, which will allow you to efficiently copy files between
the two submit nodes.

If you have trouble getting `ssh` access to the submit machine, ask the instructors right away! Gaining access is
critical for all remaining exercises.

Log in to the OSG submit machine
--------------------------------

For some of the remaining exercises today, you will be using a machine named `training.osgconnect.net`.
The username and password are listed on your 'Accounts' paper that you received yesterday.
If you no longer have it, please ask the instructors for help.

Once you have your account details, `ssh` in to the machine and take a look around.

!!! note "IMPORTANT"
    For performance reasons, you will be doing all of your work on `training.osgconnect.net` out of
    your local scratch directory, `/local-scratch/<USERNAME>/` replacing `<USERNAME>` with your own username.

    Do **NOT** use your home directory for job submission.

Preparing files for transfer
----------------------------

When transferring files between computers, it's best to limit the number of files as well as their size.
Smaller files transfer more quickly and if your network connection drops, restarting the transfer is less painful than
it would be if you were transferring large files.

Archiving tools (WinZip, 7zip, Archive Utility, etc.) can compress the size of your files and place them into a single,
smaller archive file.
The `tar` command is a one-stop shop for creating, extracting, and viewing the contents of `tar` archives (called
tarballs) whose usage is as follows:

-   To **create** a tarball named `<archive filename>` containing `<archive contents>`, use the following command:

        :::console
        user@training $ tar -czvf <archive filename> <archive contents>

    Where `<archive filename>` should end in `.tar.gz` and `<archive contents>` can be a list of any number of files
    and/or folders, separated by spaces.

-   To **extract** the files from a tarball into the current directory:

        :::console
        user@training $ tar -xzvf <archive filename>

-   To **list** the files within a tarball:

        :::console
        user@training $ tar -tzvf <archive filename>

Using the above knowledge, log into `learn.chtc.wisc.edu`, create a tarball that contains today's exercise 4.1
directory, and verify that it contains all the proper files.

### Comparing compressed sizes

You can adjust the level of compression of `tar` by prepending your command with `GZIP=--<COMPRESSION>`, where
`<COMPRESSION>` can be either `fast` for the least compression, or `best` for the most compression (the default
compression is between `best` and `fast`).

1.  Use `wget` to download the following files from our web server:
    1.  Text file: <http://proxy.chtc.wisc.edu/SQUID/osgschool19/random_text>
    1.  Archive: <http://proxy.chtc.wisc.edu/SQUID/osgschool19/pdbaa.tar.gz>
    1.  Image: <http://proxy.chtc.wisc.edu/SQUID/osgschool19/obligatory_cat.jpg>
1.  Use `tar` on each file and use `ls -l` to compare the sizes of the original file and the compressed version.

Which files were compressed the least? Why?

Transferring files
------------------

### Using secure copy

[Secure copy](https://en.wikipedia.org/wiki/Secure_copy) (`scp`) is a command based on `SSH` that lets you securely copy
files between two different hosts.
It takes similar arguments to the `cp` command that you are familiar with but also takes additional host information:

```console
user@learn $ scp <source 1> <source 2>...<source N> <remote host>:<remote path>
```

For example, if I were logged in to `learn.chtc.wisc.edu` and wanted to copy the file `foo` from my current directory to
my local scratch directory on `training.osgconnect.net`, the command would look like this:

```console
user@learn $ scp foo training.osgconnect.net:/local-scratch/<USERNAME>/
```

Additionally, I could also pull files from `training.osgconnect.net` to `learn.chtc.wisc.edu`.
The following command copies `bar` from my local scratch directory on `training.osgconnect.net` to my current directory
on `learn.chtc.wisc.edu`:

``` console
user@learn $ scp training.osgconnect.net:/local-scratch/<USERNAME>/bar .
```

You can also copy folders between hosts using the `-r` option.
If I kept all my files from Monday's exercise 1.3 in a folder named `monday-1.3` on `learn.chtc.wisc.edu`, I could use
the following command to copy them to my local scratch directory on `training.osgconnect.net`:

``` console
user@learn $ scp -r monday-1.3 training.osgconnect.net:/local-scratch/<USERNAME>/
```

Try copying the tarball you created earlier in this exercise on `learn.chtc.wisc.edu` to `training.osgconnect.net`.

### Secure copy from your laptop

During your research, you may need to retrieve output files from your submit host to inspect them on your personal
machine, which can also be done with `scp`! To use `scp` on your laptop, follow the instructions relevant to your
machine's operating system:

#### Mac and Linux users

`scp` should be included by default and available via the terminal on both Mac and Linux operating systems.
Open a terminal window on your laptop and try copying the tarball containing today's exercise 4.1 from
`training.osgconnect.net` to your laptop.

#### Windows users

WinSCP is an `scp` client for Windows operating systems.

1.  Install WinSCP from <https://winscp.net/eng/index.php>
1.  Start WinSCP and enter your SSH credentials for `training.osgconnect.net`
1.  Copy the tarball containing today's exercise 4.1 to your laptop

### Extra challenge: Using rsync

`scp` is a great, ubiquitous tool for one-time transfers but there are better tools if you find yourself transferring
the same set of files to the same location repeatedly.
Another common tool available on many Linux machines is `rsync`, which is like a beefed-up version of `scp`.
The invocation is similar to `scp`: you can transfer files and/or folders, but the options are different and when
transferring folders, make sure they don't have a trailing slash (`/`, this means to copy all the files within the
folder instead of the folder itself):

``` console
user@learn $ rsync -Pavz <source 1> <source 2>...<source N> <remote host>:<remote path>
```

`rsync` has many benefits over `scp` but two of its biggest features are built-in compression (so you don't have to
create a tarball) and the ability to only transfer files that have changed.
Both of these feature are helpful when you're having connectivity issues so that you don't have to restart the transfer
from scratch every time your connection fails.

1.  Use `rsync` to transfer the folder containing today's exercise 1.1 to `training.osgconnect.net`
1.  Create a new file in your exercise 1.1 folder on `learn.chtc.wisc.edu` with the `touch` command:

        :::console
        user@learn $ touch <filename>

1. Use the same `rsync` command to transfer the folder with the new file you just created.
   How many files were transferred the first time? How many files were transferred if you run the same rsync command
   again?

Next exercise
-------------

Once completed, move onto the next exercise: [Running jobs in the OSG](/materials/day1/part4-ex3-submit-osg.md)

