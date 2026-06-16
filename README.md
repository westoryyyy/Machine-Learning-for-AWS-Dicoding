# Machine Learning for AWS Dicoding

This repository contains the final submission for the Dicoding AWS Machine Learning project by Rotua Paulina.

## Project Overview

The project consists of two main notebooks:

- `[Clustering]_Submission_Akhir_BMLP_Rotua_Paulina.ipynb`
  - Performs data loading, preprocessing, exploration, encoding, outlier handling, scaling, and clustering using K-Means.
  - Includes model evaluation with silhouette score and PCA visualization.
  - Saves clustering results to `data_clustering.csv` and `data_clustering_inverse.csv`.

- `[Klasifikasi]_Submission_Akhir_BMLP_Rotua_Paulina.ipynb`
  - Uses the clustering output as a labeled dataset.
  - Builds classification models including Decision Tree and Random Forest.
  - Performs model evaluation with accuracy, precision, recall, and F1-score.
  - Includes hyperparameter tuning and saves model artifacts.

## Included Files

- `model_clustering.h5` — trained KMeans clustering model
- `PCA_model_clustering.h5` — optional PCA-based clustering model
- `decision_tree_model.h5` — trained Decision Tree classification model
- `explore_random_forest_classification.h5` — optional Random Forest model
- `tuning_classification.h5` — tuned classification model
- `data_clustering.csv` — clustering dataset ready for classification
- `data_clustering_inverse.csv` — inverse-transformed clustering dataset
- `dashboard.py` — Streamlit dashboard for exploring clustering results

## Notes

- All submitted notebooks have been executed and include output results.
- The notebooks use Python and standard machine learning libraries such as pandas, scikit-learn, seaborn, matplotlib, and yellowbrick.
- The repository is ready for review and further development.

## Run Dashboard

To run the dashboard locally:

```bash
python3 -m streamlit run dashboard.py
```

Open the local URL displayed by Streamlit in your browser.
