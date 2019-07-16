<style type="text/css"> pre em { font-style: normal; background-color: yellow; } pre strong { font-style: normal; font-weight: bold; color: \#008; } </style>

Wednesday Bonus Exercise 2.2: Use Singularity to Run Tensorflow
============================================================

In this tutorial, we see how to submit a [tensorflow](<https://www.tensorflow.org/>) job on the OSG through [Singularity containers](<https://support.opensciencegrid.org/solution/articles/12000024676-singularity-containers>). We currently offer CPU and GPU containers for tensorflow (both based on Ubuntu). Here, we focus on a CPU container.

Setup
-----

You should still be logged into `training.osgconnect.net` (the OSG Connect submit server for this workshop).

Get the example files and understand the job requirements.
----------------------------------------------------------

In order to run this example quickly, you can download all the files into a new folder using the `tutorial` command: 

``` console
username@training $ tutorial tensorflow-matmul
```

This creates a directory `tutorial-tensorflow-matmul`. Go inside the directory and see what is inside.

``` console
username@training $ cd tutorial-tensorflow-matmul
username@training $ ls -F
```

You will see the following files

``` file
tf_matmul.py            (Python program to multiply two matrices using tensorflow package)
tf_matmul.submit        (HTCondor Job description file)
tf_matmul_wrapper.sh    (Job wrapper shell script that executes the python program)
tf_matmul_gpu.submit    (HTCondor Job description file targeting gpus)
```

NOTE: The file `tf_matmul_gpu.submit` is for gpus, but we will not focus on gpus in this exercise. You are welcome to take a look.

The python script \`tf\_matmul.py\` uses tensorflow to perform the matrix multiplication of a \`2x2\` matrix. 

The submit file will have similar requirements and options as our previous job, including: 

``` file
Requirements = HAS_SINGULARITY == True
```

In addition, we also provide the full path of the image via the keyword `+SingularityImage`.

``` file
+SingularityImage = "/cvmfs/singularity.opensciencegrid.org/opensciencegrid/tensorflow:latest"
```

Submit the tensorflow example job
---------------------------------

Now submit the job to the OSG.

``` console
username@training $ condor_submit tf_matmul.submit 
```

The job will look for a machine on the OSG that has singularity installed. On a matched machine, the job creates the singularity container from the image `/cvmfs/singularity.opensciencegrid.org/opensciencegrid/tensorflow:latest`. Inside this container, the program `tf_matmul.py` begins to execute. 

After your job completed, you will see an output file `tf_matmul.output`. 

``` console
username@training $ cat tf_matmul.output 
result of matrix multiplication
===============================
[[ 1.0000000e+00  0.0000000e+00]
 [-4.7683716e-07  1.0000002e+00]]
===============================

```
The result printed in the output file should be a `2x2` identity matrix.


