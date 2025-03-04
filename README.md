# GSEApy vs fGSEA comparison

![R](https://img.shields.io/badge/r-%23276DC3.svg?style=for-the-badge&logo=r&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

Dual Python and R script that compares ouput for two methods of Gene Set Enrichment Analysis (GSEA) of GSEApy and fGSEA. GSEApy is the Python/Rust implementation of GSEA and contains the prerank version and traditional version of GSEA whilst fGSEA is the R package for Fast GSEA. This notebook allows users to explore the differences in GSEA results when employing different settings(e.g: ranking metric, gene sets, permutation type, threads, minimum and maximum size of genes).

## Usage
1. Install Python and R
2. Install Rpy2 by running the following command in Bash:
```
pip install rpy2
```
3. Download the Jupyter Notebook from the gh-pages branch (.ipynb)
4. Open the Jupyternotebook in Jupyterlab or Jupyternotebook.
5. Run the cells of the notebook document step-by-step (one cell a time) by pressing shift + enter or run the whole notebook in a single step by clicking on the menu Cell -> Run All.
6. Adapt the notebook with your own dataset or parameters of interest.


