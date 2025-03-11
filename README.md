# snakemake-tutorial
Introduction to snakemake as a workflow management tool. 

Steps to run this tutorial on Triton Cluster.

1. Clone the project
2. Load the default environment: `module load scicomp-python-env`
3. Alternatively, use the environment specified in `env.yml` with the following steps:
   - module load mamba
   - mamba env create --file env.yml
   - source activate snakemake-tutorial
