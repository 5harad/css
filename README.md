# Introduction to Computational Social Science

Course website: https://5harad.com/mse231

Please follow the instructions below to ensure that your computing setup is sufficient for the course.

## Computing environment setup

A Unix-like setup is required (e.g., Linux, OS X, or [Cygwin](https://www.cygwin.com/)). We primarily use [R](http://www.r-project.org/) ([RStudio](https://www.rstudio.com/) is recommended) and Python 3.7 ([Anaconda Python](https://www.anaconda.com/distribution/#download-section) is recommended). We use the [Tidyverse](https://www.tidyverse.org/) suite of packages in R for data manipulation and visualization. We also use [Vowpal Wabbit](https://vowpalwabbit.org/) (a fast online learning algorithm), and [Amazon Elastic MapReduce](https://aws.amazon.com/elasticmapreduce/) (a web service for distributed computing).

## JupyterLab installation

[JupyterLab](https://jupyter.org/install.html), which runs in the browser, can be a convenient way to run Python (and R), and allows interleaving of explanatory text with executable code. We recommend you install JupyterLab with both Python 3 and R kernels.

**Note:** You must already have Python 3 installed in order to proceed.

Follow the [installation instructions](https://jupyter.org/install.html) (linked above as well) to install JupyterLab, using `conda` or `pip` as appropriate. (`conda` will do if you have Anaconda Python installed.)

Now in your terminal run the following command by typing it and pressing return:
```
jupyter lab
```
This will start running a web server that serves the JupyterLab application. This command should automatically open your default web browser to the JupyterLab page.

If you do not see JupyterLab open, read the output of the command you ran in the terminal. If Jupyter started correctly, it should have printed to the screen the URL you can use to access Jupyter.

### Installing the R kernel

By default, JupyterLab does not have the ability to execute R code. In order to use R with JupyterLab, you need to install the `IRkernel` package.

In an `R` shell started from the terminal,
```
install.packages('IRkernel')
```
to install the package, followed by
```
IRkernel::installspec()
```
to tell Jupyter where to find the kernel spec. (For more detail on these two steps, see [here](https://irkernel.github.io/installation/).)

Now, when you run `jupyter lab`, you should see the option to create a notebook with the `R` kernel.

### Python 3

The Python 3 kernel should be available by default when you open JupyterLab.

In rare cases, usually with Anaconda, you may have Python 3 installed but only be able to create notebooks with a Python 2 kernel. If this describes your situation, [here](https://stackoverflow.com/questions/28831854/how-do-i-add-python3-kernel-to-jupyter-ipython) is a potentially useful StackOverflow post about the issue.
