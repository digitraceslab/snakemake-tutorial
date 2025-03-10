# snakemake-tutorial
Introduction to snakemake as a workflow management tool. 

Steps to run this tutorial on Triton Cluster.

1. Clone the project
2. Load the default environment: `module load scicomp-python-env`
3. Alternatively, use the environment specified in `env.yml` with the following steps:

   a. module load mamba
   b. mamba env create --file env.yml
   c. source activate snakemake-tutorial
