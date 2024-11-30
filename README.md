# Decode MEG Brainwave: A Comparative Analysis of ML Model Performance

This is the source code of 2024 NTHU CS Senior Project. It provides a way of processing MEG brainwave data and performing some binary classification tasks in some language features. 

## Installing requirements

`pip install -r requirements.txt`


## Dataset
- The dataset used is *MEG-MASC* Dataset, available at https://www.nature.com/articles/s41597-023-02752-5
- dataset is expected to be saved at absolute path`/home/dataset/Data/gw_data/download`, which is amendable in `./app/config/demo_config.json` at `raw_data_path` field under `house_keeping` field.

## How to run
- cd to root dir 

- `python main.py`

- `./app/config/demo_config.json` is able to control training task to perform and model to use.
