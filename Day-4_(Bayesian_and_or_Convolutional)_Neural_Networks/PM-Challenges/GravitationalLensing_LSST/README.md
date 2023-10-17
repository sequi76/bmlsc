# Bayesian Machine Learning Summer Camp
## Deep Learning Solutions for Strong Lensing Problems

**Before You Begin**:

In this repository, you will find three Jupyter notebooks for different challenge tasks related to gravitational lens images. To access image data and notebooks directly, please visit the following link:

https://drive.google.com/drive/folders/1pcqw1edIOqrCuaQT1p1xA7owUngdWr4X?usp=sharing

Inside this shared Google Drive folder, you'll find the following structure:

- **Images with Background (LSST_with_background/)**
    - *CONFIGURATION_1_images.npy* - Gravitational lens images
    - *CONFIGURATION_1_metadata.csv* - Metadata for the corresponding images
    - *CONFIGURATION_1_simulation_parameters.npy* - Configuration settings for the simulations
    - *CONFIGURATION_1_truth_table.npy* - Truth tables for the simulations
    
- **Images without Background (LSST_without_background/)**
    - *CONFIGURATION_1_images.npy* - Gravitational lens images
    - *CONFIGURATION_1_metadata.csv* - Metadata for the corresponding images
    - *CONFIGURATION_1_simulation_parameters.npy* - Configuration settings for the simulations
    - *CONFIGURATION_1_truth_table.npy* - Truth tables for the simulations

- **Segmentation Maps (segmentation_maps/)**
    - *segmentations.npy* - Segmentation maps for the images

- **Classification Notebook (classification.ipynb)**
- **Regression Notebook (regression.ipynb)**
- **Segmentation Notebook (segmentation.ipynb)**

You **do not need to download the image data**. To access the applications, follow these steps:
1. Open the desired notebook by double-clicking the corresponding .ipynb file.
2. Google Drive will redirect you to Google Colab.
3. Once in Google Colab, click on *File* and select *Save a Copy in Drive*.
4. You're ready to run the notebook, and data will be automatically downloaded via wget during execution.