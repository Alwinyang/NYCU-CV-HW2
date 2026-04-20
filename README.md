
NYCU Computer Vision HW2

Project Description

This project is part of the NYCU Computer Vision course homework.

The goal is to perform object detection on a given dataset and generate prediction results in the required JSON format.



We adopt \*\*YOLOv8\*\* as the main model for training and inference due to its strong performance and ease of use.



\## Method Overview



The workflow of this project includes:



1\. Data preprocessing (format conversion to YOLO format)

2\. Model training using YOLOv8

3\. Model inference on test dataset

4\. Output prediction results as `pred.json`



\## Project Structure



NYCU-CV-HW2/

├── train.py                # Training script

├── submission.py           # Inference script (generate pred.json)

├── convert.py              # Convert dataset to test format

├── pred.json               # Final submission file

├── README.md               # Project documentation



\## ⚙️ Environment Setup



\### Requirements



\* Python 3.8+

\* PyTorch

\* Ultralytics YOLOv8



\### Install dependencies



pip install ultralytics torch torchvision opencv-python numpy



\## 📊 Dataset



The dataset should be organized as follows:

data/

├── train/

├── valid/

└── test/

&#x20;   └── images/





※ Dataset is not included in this repository.



\## Training



Run the following command to train the model:

python train.py





\### Training Details



\* Model: YOLOv8

\* Image size: 640

\* Batch size: 16

\* Epochs: 50 (can be adjusted)



\---



\## Inference



To generate prediction results:

python submission.py

This will produce:

pred.json



\## Output Format



The output file `pred.json` follows the required format:



```json

\[

&#x20; {

&#x20;   "image\_id": "1.png",

&#x20;   "bbox": \[x, y, width, height],

&#x20;   "score": 0.95,

&#x20;   "category\_id": 3

&#x20; }

]

```



\---



\## Result



\* The model achieves a valid score on the evaluation platform.

\* Example score: \*\*0.24 (baseline)\*\*



\---



\## Experiment Notes



\* Lowering confidence threshold improves recall.

\* Adjusting IoU threshold helps reduce duplicate boxes.

\* Data augmentation can improve performance.



\---



\## Limitations



\* Model performance depends heavily on training data quality.

\* No hyperparameter tuning was extensively performed.

\* Training was conducted on Google Colab with limited runtime.



\---



\## Implementation Details



\* Framework: PyTorch + Ultralytics YOLOv8

\* Platform: Google Colab

\* OS: Windows (local environment)



\---



\## Notes



\* Model weights (`.pt`) are not included due to file size limitation.

\* Dataset is not uploaded due to course policy.

\* Only final prediction file is included.











