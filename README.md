# FedHarmo: Harmonizing Global Aggregation and Local Alignment in Cross-Domain Federated Medical Image Segmentation

This repo is the implementation of "FedHarmo: Harmonizing Global Aggregation and Local Alignment in Cross-Domain Federated Medical Image Segmentation".

## 💻 Requirements
Please review the following requirements and install the packages listed in the `requirements.txt` file.
```bash
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

## 📚 Data Preparation
Download the required datasets and unzip them to ``` ../Dataset/ ``` folder. Please reorganize the dataset according to the structure specified in the ``` tree.txt ``` file.  \
Download links(Repo: [FedEvi](https://github.com/JiayiChen815/FedEvi)): endoscopic polyp dataset, prostate MRI dataset.  \
Navigate to the ``` data/ ``` folder and run python ``` prepare_dataset.py ``` to transform the original dataset into *.npyformat.  \
Run ``` python data_split.py ``` to divide the data into training, validation, and test sets.  \

## 🚀 Usage
For endoscopic polyp segmentation, the command for execution is as follows:
```bash
CUDA_VISIBLE_DEVICES=0 python main_seg_al.py --dataset Polyp --fl_method FedHarmo --deterministic True --seed 2025 --max_round 200 --gamma 0.99 --annealing_step 10
```
For prostate segmentation, the command for execution is as follows:
```bash
CUDA_VISIBLE_DEVICES=0 python main_seg_al.py --dataset Prostate --fl_method FedHarmo --deterministic True --seed 2025 --max_round 200 --gamma 0.99 --annealing_step 10
```

## 🙏 Acknowledment
This repository is based on modifications of the following code repositories: 
* [FedEvi](https://github.com/JiayiChen815/FedEvi);
* [MMD](https://github.com/ZongxianLee/MMD_Loss.Pytorch);  \
We would like to express our sincere gratitude to the original authors for their outstanding contributions, which have laid a solid foundation for our work. Their dedication and expertise have been invaluable in shaping the development of this project.
