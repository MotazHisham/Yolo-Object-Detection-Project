# 🚀 YOLO Object Detection with Python

High-performance Object Detection system built using YOLOv8 and Python.\
This project demonstrates training, validation, and inference on custom
datasets using Ultralytics YOLO locally.

------------------------------------------------------------------------

## 🎯 Project Overview

This project implements a complete object detection pipeline:

-   Dataset preparation\
-   Model training\
-   Model validation\
-   Inference on images / videos\
-   Saving prediction results

Built and tested locally using Python.

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python 3.10+
-   PyTorch
-   Ultralytics YOLOv8
-   OpenCV
-   Matplotlib

------------------------------------------------------------------------

## 📂 Project Structure

yolo-object-detection/ │ ├── data/ │ ├── train/ │ ├── valid/ │ └──
data.yaml │ ├── runs/ │ ├── train.py ├── predict.py ├── requirements.txt
└── README.md

------------------------------------------------------------------------

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/yolo-object-detection.git\
cd yolo-object-detection

### 2️⃣ Create Virtual Environment (Recommended)

python -m venv venv\
venv`\Scripts`{=tex}`\activate`{=tex}

### 3️⃣ Install Dependencies

pip install -r requirements.txt

Or manually:

pip install ultralytics opencv-python matplotlib torch

------------------------------------------------------------------------

## 🏋️ Training the Model

``` python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="data/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16
)
```

Training results will be saved inside:

runs/detect/train/

------------------------------------------------------------------------

## 📊 Validation

``` python
metrics = model.val()
print(metrics)
```

------------------------------------------------------------------------

## 🔍 Inference (Prediction)

### On Image

``` python
results = model("image.jpg")
results[0].show()
```

### Save Predictions

``` python
results = model("image.jpg", save=True)
```

Output will be saved in:

runs/detect/predict/

------------------------------------------------------------------------

## 📈 Evaluation Metrics

-   mAP@0.5
-   Precision
-   Recall
-   F1-score

Example:

mAP@0.5 = 0.87\
Precision = 0.91\
Recall = 0.88

------------------------------------------------------------------------

## 🧠 How YOLO Works

YOLO (You Only Look Once) is a single-stage object detection model that:

1.  Divides the image into grid cells\
2.  Predicts bounding boxes and class probabilities\
3.  Applies Non-Max Suppression (NMS)\
4.  Outputs final detections

This project uses YOLOv8, the latest version from Ultralytics.

------------------------------------------------------------------------

## 📌 Future Improvements

-   Add real-time webcam detection\
-   Deploy using Flask API\
-   Add model comparison (YOLOv8n vs YOLOv8s)\
-   Hyperparameter tuning

------------------------------------------------------------------------

## 👨‍💻 Author

Motaz Saleh\
Aspiring AI Engineer \| Deep Learning Enthusiast
