# notebook_gh-actions
Project with a github action that:
1. runs all python notebooks in a directory. (by transforming it into .py files with a .sh script)
2. exports output data to a gh-pages branch
3. imports conda in a github action workflow .yml

To set up a similiar project:
- Generate the `environment.yml` from your conda environment with command: `conda env export > environment.yml`
- Create a branch *gh-pages*
- In the repo settings : *Actions > General > Workflow permission* grant read and write permissions in order to write output into gh-pages branch.