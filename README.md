# Unity-Launcher

Unity-Launcher is a utility for performing simple, data parallel, high throughput computing (HTC) workflows on the Unity cluster.

## Installing Unity-Launcher
Launcher does not need to be compiled. Unpack the tarball or clone the repository in the desired directory. Then, set `LAUNCHER_DIR` to point to that location. 

* Set `LAUNCHER_JOB_FILE` to point to your job file. Example job files are provided in extras/examples.
* Be sure that `LAUNCHER_DIR` is set to the directory containing the launcher source files (user-installed ONLY. Not required if using system installed version of launcher).
* From the command-line or within your jobscript, run:`$LAUNCHER_DIR/paramrun`

## Available Environment Variables

You should set the following environment variables:

* `$LAUNCHER_JOB_FILE` is the file containing the jobs to run in your parametric submission.
* `$LAUNCHER_WORKDIR` is the directory where the launcher will execute. All relative paths will resolve to this directory.

The launcher defines the following environment variables for each job that is started:

* `$LAUNCHER_CORES_TOTAL` contains the number of processes running simultaneously in your parametric submission.
* `$LAUNCHER_NJOBS` contains the number of jobs in your job file.

Note: you can also use the launcher to run a sequence of serial jobs when you have more jobs to run than the requested number of processors.  

## Task Scheduling Behavior

Launcher on Unity relies entirely on the Unity SLURM install


## Referencing Launcher
If you are using Launcher, please remember to make a reference to it when publishing results. The file `paper/paper.bib` contains the BibTeX-formatted citation list. Please reference entry `Wilson:2014:LSF:2616498.2616533` (i.e., in LaTeX: `\cite{Wilson:2014:LSF:2616498.2616534}`).
