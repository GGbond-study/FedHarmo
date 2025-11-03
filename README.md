# FedHarmo: Harmonizing Global Aggregation and Local Alignment in Cross-Domain Federated Medical Image Segmentation

This repo is the implementation of "FedHarmo: Harmonizing Global Aggregation and Local Alignment in Cross-Domain Federated Medical Image Segmentation".

## 💻 Requirements
Please review the following requirements and install the packages listed in the `requirements.txt` file.
```bash
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

## 📚 Data Preparation
Download the required datasets and unzip them to ../Dataset/ folder. Please reorganize the dataset according to the structure specified in the tree.txt file.  \
Download links: endoscopic polyp dataset, prostate MRI dataset(IN [FedEvi](https://github.com/JiayiChen815/FedEvi)).  \
Navigate to the data/ folder and run python prepare_dataset.py to transform the original dataset into *.npyformat.  \
Run python data_split.py to divide the data into training, validation, and test sets.  \

## 🚀 Usage
For endoscopic polyp segmentation, the command for execution is as follows:
```bash
$ bash run_polyp.sh
```

## 🙏 Acknowledment
This repository is based on modifications of the following code repositories: 
* [FedEvi](https://github.com/JiayiChen815/FedEvi);
* [MMD](https://github.com/ZongxianLee/MMD_Loss.Pytorch);  \
We would like to express our sincere gratitude to the original authors for their outstanding contributions, which have laid a solid foundation for our work. Their dedication and expertise have been invaluable in shaping the development of this project.
