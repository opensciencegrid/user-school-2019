---
status: in progress
---

# OSG User School 2019 Materials

## Monday

### Monday Morning: Introduction to HTC and HTCondor

- Lecture: Introduction to HTC ([PDF](/materials/day1/files/osgus19-day1-part1-intro-to-htc.pdf);[PPT](/materials/day1/files/osgus19-day1-part1-intro-to-htc.pptx))
- [Exercise 1.1: Log in to the local submit machine and look around](/materials/day1/part1-ex1-login.md)
- [Exercise 1.2: Experiment with basic HTCondor commands](/materials/day1/part1-ex2-commands.md)
- [Exercise 1.3: Run jobs!](/materials/day1/part1-ex3-jobs.md)
- [Exercise 1.4: Read and interpret log files](/materials/day1/part1-ex4-logs.md)
- [Exercise 1.5: Determining Resource Needs](/materials/day1/part1-ex5-request.md)
- [Exercise 1.6: Remove jobs from the queue](/materials/day1/part1-ex6-remove.md)
- [Bonus Exercise 1.7: Compile and run some C code](/materials/day1/part1-ex7-compile.md)

### Monday Morning: Running Many HTC Jobs

- Lecture: More HTCondor ([PDF](/materials/day1/files/osgus19-day1-part2-many-HTCondor-jobs.pdf);[PPT](/materials/day1/files/osgus19-day1-part2-many-HTCondor-jobs.pptx))
- [Exercise 2.1: Work with input and output files](/materials/day1/part2-ex1-files.md)
- [Exercise 2.2: Use `queue N`, `$(Cluster)`, and `$(Process)`](/materials/day1/part2-ex2-queue-n.md)
- [Exercise 2.3: Use `queue matching` with a custom variable](/materials/day1/part2-ex3-queue-matching.md)
- [Exercise 2.4: Use `queue from` with custom variables](/materials/day1/part2-ex4-queue-from.md)

### Monday Afternoon: Job Attributes and Handling

- Lecture: Intermediate HTCondor: Workflows ([PDF](/materials/day1/files/osgus19-day1-part3-matching-handling.pdf);[PPT](/materials/day1/files/osgus19-day1-part3-matching-handling.pptx))
- [Exercise 3.1: Explore `condor_q`](/materials/day1/part3-ex1-queue.md)
- [Exercise 3.2: Explore `condor_status`](/materials/day1/part3-ex2-status.md)
- [Exercise 3.3: A job that needs retries](/materials/day1/part3-ex3-job-retry.md)

### Monday Afternoon: Introduction to Distributed HTC

- Lecture: Introduction to DHTC ([PDF](/materials/day1/files/osgus19-day1-part4-intro-to-dhtc.pdf);
  [PPT](/materials/day1/files/osgus19-day1-part4-intro-to-dhtc.pptx))
- [Exercise 4.1: Refresher - Submitting multiple jobs](/materials/day1/part4-ex1-submit-refresher.md)
- [Exercise 4.2: Log in to the OSG submit machine](/materials/day1/part4-ex2-login-scp.md)
- [Exercise 4.3: Running jobs in the OSG](/materials/day1/part4-ex3-submit-osg.md)
- [Exercise 4.4: Hardware differences in the OSG](/materials/day1/part4-ex4-hardware-diffs.md)
- [Exercise 4.5: Software differences in the OSG](/materials/day1/part4-ex5-software-diffs.md)

<!--  All below here needs to be updated!

### Monday Afternoon: Automating Workflows with HTCondor's DAGMan

- Lecture: HTCondor: More on Workflows ([PDF](/materials/day1/files/osgus19-day1-part4-dagman.pdf);[PPT](/materials/day1/files/osgus19-day1-part4-dagman.pptx))
- [Exercise 4.1: Coordinating set of jobs: A simple DAG](/materials/day1/part4-ex1-simple-dag.md)
- [Exercise 4.2: A brief detour through the Mandelbrot set](/materials/day1/part4-ex2-mandelbrot.md)
- [Exercise 4.3: A more complex DAG](/materials/day1/part4-ex3-complex-dag.md)
- [Exercise 4.4: Handling jobs that fail with DAGMan](/materials/day1/part4-ex4-failed-dag.md)
- [Bonus Exercise 4.5: HTCondor challenges](/materials/day1/part4-ex5-challenges.md) (If and only if you have time)

## Tuesday

### Tuesday Afternoon: Security in OSG

- Lecture: Security in OSG ([PDF](/materials/day2/files/osgus19-day2-part3-security.pdf);
  [PPT](/materials/day2/files/osgus19-day2-part3-security.pptx))

### Tuesday Afternoon: Troubleshooting jobs

- Lecture: Troubleshooting jobs ([PDF](/materials/day2/files/osgus19-day2-part4-troubleshooting.pdf);
  [PPT](/materials/day2/files/osgus19-day2-part4-troubleshooting.pptx))
- [Exercise 3.1: Troubleshooting a DAG](/materials/day2/part3-ex1-troubleshooting.md)

### Tuesday Afternoon: Connecting to OSG

- Lecture: Ways to Connect to OSG ([PDF](/materials/day2/files/osgus19-day2-part5-ways-to-connect.pdf))

## Wednesday

### Wednesday Morning: Software Portability

- Lecture: Software Portability for DHTC ([PDF](/materials/day3/files/osgus19-day3-part1-software-portability.pdf); [PPT](/materials/day3/files/osgus19-day3-part1-software-portability.pptx))
- [Exercise 1.1: Compiling programs for portability](/materials/day3/part1-ex1-compiling.md)
- [Exercise 1.2: Using a pre-compiled binary](/materials/day3/part1-ex2-precompiled.md)
- [Exercise 1.3: Using a wrapper script](/materials/day3/part1-ex3-wrapper.md)
- [Exercise 1.4: Pre-packaging code](/materials/day3/part1-ex4-prepackaged.md)
- [Bonus Exercise 1.5: Passing Arguments Through the Wrapper Script](/materials/day3/part1-ex5-arguments.md)

### Wednesday Morning: Software Limitations

- Lecture: Considerations for licensing and programming packages
  ([PDF](/materials/day3/files/osgus19-day3-part2-software-license-interpret.pdf); [PPT](/materials/day3/files/osgus19-day3-part2-software-license-interpret.pptx))
- [Exercise 2.1: Compile and run Matlab code](/materials/day3/part2-ex1-matlab.md)
- [Exercise 2.2: Pre-packaging Python](/materials/day3/part2-ex2-python-built.md)
- [Exercise 2.3: In-job installation of Python](/materials/day3/part2-ex3-python-install.md)
- [Bonus Exercise 2.4: Using containers](/materials/day3/part2-ex4-containers.md)

### Wednesday Afternoon: On Your Own

- [Ideas for activities](/logistics/wednesday-activities.md)

## Thursday

### Thursday Morning: Data Handling

- Lecture: Overall data considerations ([PDF](/materials/day4/files/osgus19-day4-part2-overall-data.pdf))
- [Exercise 2.1: Understanding your data requirements](/materials/day4/part2-ex1-data-needs.md)
- [Exercise 2.2: HTCondor file transfer and compression](/materials/day4/part2-ex2-file-transfer.md)
- [Exercise 2.3: Splitting large input data](/materials/day4/part2-ex3-blast-split.md)

### Thursday Morning: Data Handling (continued)

- Lecture: Solutions for large input data ([PDF](/materials/day4/files/osgus19-day4-part3-large-input.pdf))
- [Exercise 3.1: Using a web proxy for large, shared input](/materials/day4/part3-ex1-blast-proxy.md)
- [Exercise 3.2: Using StashCache for large, shared input](/materials/day4/part3-ex2-stashcache-shared.md)
- [Exercise 3.3: Using StashCache for large, unique input](/materials/day4/part3-ex3-stashcache-unique.md)

### Thursday Afternoon: Data Handling (continued)

- Lecture: Large output and shared file systems; Data summary
  ([PDF](/materials/day4/files/osgus19-day4-part4-output-shared-fs.pdf))
- [Exercise 4.1: Using a local shared filesystem for large input files](/materials/day4/part4-ex1-input.md)
- [Exercise 4.2: Using a local shared filesystem for large output files](/materials/day4/part4-ex2-output.md)

### Thursday Afternoon: Automating Workflows with HTCondor's DAGMan

- Lecture: HTCondor: More on Workflows ([PDF](/materials/day4/files/osgus19-day4-part4-dagman.pdf);[PPT](/materials/day4/files/osgus19-day4-part4-dagman.pptx))
- [Exercise 4.1: Coordinating set of jobs: A simple DAG](/materials/day4/part4-ex1-simple-dag.md)
- [Exercise 4.2: A brief detour through the Mandelbrot set](/materials/day4/part4-ex2-mandelbrot.md)
- [Exercise 4.3: A more complex DAG](/materials/day4/part4-ex3-complex-dag.md)
- [Exercise 4.4: Handling jobs that fail with DAGMan](/materials/day4/part4-ex4-failed-dag.md)
- [Bonus Exercise 4.5: HTCondor challenges](/materials/day4/part4-ex5-challenges.md) (If and only if you have time)

## Friday

### Friday Morning: From Science to Production Workflows

- Lecture: From Science to Real Workflow ([PDF](/materials/day5/files/osgus19-day5-part1-real-workflows.pdf), [PPT](/materials/day5/files/osgus19-day5-part1-real-workflows.pptx))
- [Exercise 1.1: Learn about Joe’s Desired Computing Work](/materials/day5/part1-ex1-science-intro.md)
- [Exercise 1.2: Plan Overall Workflow](/materials/day5/part1-ex2-plan-workflow.md)

### Friday Morning: From Science to Production Workflows

- Lecture: From Workflow to Automated Production
  ([PDF](/materials/day5/files/osgus19-day5-part2-production-workflows.pdf),[PPT](/materials/day5/files/osgus19-day5-part2-production-workflows.pptx))
- [Exercise 1.3: Execute Joe’s Workflow](/materials/day5/part2-ex1-execute-workflow.md)
- [Bonus Exercise 1.4: Further Optimization and Scaling](/materials/day5/part2-ex2-workflow-tuning.md)

### Friday Afternoon: HTC Showcase

- Talk: [Spencer Ericksen](https://cancer.wisc.edu/research/resources/ddc/smsf/), Small Molecule Facility (Carbone Cancer Center):
  *Exploring Virtual Screening Approaches with HTC* ([PDF](/materials/day5/files/osgus19-day5-part3-showcase1-ericksen.pdf))
- Talk: [Josh Karpel](https://www.physics.wisc.edu/people/joshkarpel), Physics:
  *High-Throughput Computing in Atomic Physics* ([PPT](/materials/day5/files/osgus19-day5-part3-showcase2-karpel.pptx))
- Talk: [Ross Kleiman](https://wid.wisc.edu/people/ross-kleiman/), Computer Sciences:
  *High-Throughput Machine Learning from Electronic Health Records*
  ([PPTX](/materials/day5/files/osgus19-day5-part3-showcase2-kleiman.pptx))
- Talk: [Dave O'Connor](https://www.pathology.wisc.edu/profile/david-oconnor), Pathology:
  *When Low Throughput Biologists Meet High Throughput Computing*

### Friday Afternoon: Foundations of HTC

- Lecture: The Principles of HTC ([PDF](/materials/day5/files/osgus19-day5-part4-htc-principles.pdf))

### Friday Afternoon: Wrap Up

- Lecture: Where to Go and What to Do Next ([PDF](/materials/day5/files/osgus19-day5-part5-whats-next.pdf))

All above here needs to be updated! -->
