# 🦷 Oral Disease Detection System using Deep Learning

## 📌 Project Overview

This project presents a Deep Learning-based Oral Disease Detection System capable of classifying oral cavity images into six different disease categories.

The system was developed to assist in the early detection of common oral diseases using computer vision and transfer learning techniques. Multiple deep learning architectures were trained and compared, and the best-performing model was deployed through a Streamlit web application.

---

## 🎯 Objectives

* Build an automated oral disease classification system.
* Compare the performance of multiple deep learning architectures.
* Deploy the best-performing model in a user-friendly web application.
* Provide secure login and signup functionality for users.

---

## 📂 Dataset

The dataset contains oral cavity images belonging to six classes:

1. Calculus
2. Dental Caries
3. Gingivitis
4. Mouth Ulcer
5. Tooth Discoloration
6. Hypodontia

### Data Preparation

The original dataset contained nested folders and duplicated structures.

Data preprocessing included:

* Recursive image extraction
* Removal of unwanted folders
* Dataset cleaning
* Duplicate handling
* Train/Test split generation
* Image resizing to 225 × 225 pixels

Dataset split:

* Training Set: 80%
* Testing Set: 20%

Additionally, 20% of the training set was used as a validation set.

---

## 🛠 Technologies Used

### Programming Language

* Python

### Deep Learning Frameworks

* TensorFlow
* Keras

### Data Processing

* NumPy
* Pandas

### Visualization

* Matplotlib
* Seaborn

### Deployment

* Streamlit

### Security

* bcrypt password hashing

---

## 🧠 Models Implemented

Four different deep learning architectures were trained and evaluated.

### 1. Custom CNN

A custom convolutional neural network inspired by AlexNet architecture.

Architecture includes:

* Convolution Layers
* Max Pooling Layers
* Fully Connected Layers
* Dropout Regularization

---

### 2. DenseNet121

Transfer Learning using DenseNet121 pretrained on ImageNet.

Features:

* Frozen convolutional backbone
* Global Average Pooling
* Batch Normalization
* Dropout
* Softmax Output Layer

---

### 3. ResNet50

Transfer Learning using ResNet50 pretrained on ImageNet.

Features:

* Residual learning blocks
* Transfer learning
* Fine classification head

---

### 4. EfficientNetB0

Transfer Learning using EfficientNetB0 pretrained on ImageNet.

Features:

* Compound scaling
* Lightweight architecture
* High classification accuracy
* Efficient deployment performance

---

## ⚙ Training Configuration

| Parameter         | Value                           |
| ----------------- | ------------------------------- |
| Image Size        | 225 × 225                       |
| Batch Size        | 32                              |
| Epochs            | 100                             |
| Number of Classes | 6                               |
| Optimizer         | Adam                            |
| Learning Rate     | 0.001                           |
| Loss Function     | Sparse Categorical Crossentropy |

---

## 📊 Model Performance

### Final Evaluation Results

| Model          | Accuracy | Precision | Recall | F1 Score |
| -------------- | -------- | --------- | ------ | -------- |
| EfficientNetB0 | 89.59%   | 89.61%    | 89.59% | 89.44%   |
| ResNet50       | 87.88%   | 87.83%    | 87.88% | 87.82%   |
| Custom CNN     | 83.39%   | 83.50%    | 83.39% | 83.41%   |
| DenseNet121    | 71.35%   | 71.25%    | 71.35% | 70.56%   |

---

## 🏆 Best Model

EfficientNetB0 achieved the highest performance among all tested architectures.

### Best Model Metrics

* Accuracy: 89.59%
* Precision: 89.61%
* Recall: 89.59%
* F1 Score: 89.44%

Therefore, EfficientNetB0 was selected for deployment.

---

## 🚀 Streamlit Deployment

The final model was integrated into a Streamlit web application.

### Features

* User Signup
* User Login
* Secure Password Hashing using bcrypt
* Oral Image Upload
* Disease Prediction
* Confidence Score Display
* Probability Distribution for all Classes
* Modern Dental-Themed User Interface

---

## 🔐 Authentication System

User authentication was implemented using:

* bcrypt password hashing
* Local credential storage
* Session management through Streamlit

This ensures passwords are never stored in plain text.

---

## 📁 Project Structure

```text
Oral_Disease_Detection/
│
├── Final_Deployment.py
├── best_model.h5
├── credentials.txt
├── Dental.jpg
├── requirements.txt
├── README.md
│
├── notebooks/
│   └── Oral_Disease_Classification.ipynb
│
└── screenshots/
```

---

## ▶ How to Run

### Clone Repository

```bash
git clone https://github.com/yourusername/oral-disease-detection.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run Final_Deployment.py
```

---



## Author

Menna Lasheen

Project: Oral Disease Detection using Deep Learning

This project compares multiple CNN and Transfer Learning architectures and deploys the best-performing model using Streamlit for real-world usage.
