# MLOps Project - l232610

This project demonstrates a basic machine learning workflow using Git and MLOps practices. It includes dataset handling, model training, evaluation, and generation of a trained model artifact.

## Project Structure

```text
mlops-project-l232610/
├── data/
│   └── dataset.csv
├── src/
│   └── train_l232610.py
├── model/
│   └── model.pkl
├── .gitignore
├── requirements.txt
└── README.md
```

* `data/` - Contains the raw dataset. This directory is excluded from Git.
* `src/` - Contains the student-specific training script.
* `model/` - Contains the generated trained model. This directory is excluded from Git.
* `requirements.txt` - Contains the required Python packages.
* `.gitignore` - Prevents raw data, model artifacts, virtual environments, and Python cache files from being committed.

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Training the Model

Run the training script from the project root:

```bash
python src/train_l232610.py
```

The script loads the dataset from `data/dataset.csv`, trains a Random Forest regression model, evaluates it using Mean Squared Error, and saves the trained model to:

```text
model/model.pkl
```

Example output:

```text
Loading dataset for student l232610...
Mean Squared Error: 338929166.67
Model trained successfully.
Model saved to model/model.pkl
```

## Git and MLOps Workflow

This project demonstrates:

* Git repository initialization
* Branching and merging
* Merge conflict resolution
* Soft and hard resets
* Git status and history inspection
* `.gitignore` configuration
* Separation of source code, data, and model artifacts

Raw datasets and trained model artifacts are intentionally excluded from version control.

## Student ID **23L-2610**
