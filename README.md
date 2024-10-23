# Craigslist Used Vehicle Price Prediction

This project aims to predict the price of used cars listed on Craigslist using machine learning. 

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Project Overview

This project uses machine learning models to estimate the prices of used cars listed on Craigslist. The project is implemented using Python and popular machine learning libraries such as scikit-learn and XGBoost.

## Dataset

The dataset used is the "Craigslist Carstrucks Data" available on Kaggle. You can download it from: [Add link to the dataset here]

**Dataset Features:**
- **price:** The price of the car.
- **year:** The year the car was manufactured.
- **manufacturer:** The manufacturer of the car.
- **model:** The model of the car.
- **condition:** The condition of the car.
- **cylinders:** The number of cylinders in the car's engine.
- **fuel:** The type of fuel the car uses.
- **odometer:** The mileage of the car.
- **title_status:** The title status of the car.
- **transmission:** The transmission type of the car.
- **drive:** The drive type of the car.
- **size:** The size of the car.
- **type:** The type of car.
- **paint_color:** The paint color of the car.
- **state:** The state where the car is listed.


## Data Preprocessing

The following preprocessing steps are performed:

1. **Handling Missing Values:**
   - Columns with more than 25% missing values are dropped.
   - Rows with any remaining missing values are dropped.

2. **Outlier Removal:**
   - Outliers in the 'price' column are removed. We considered prices above $100,000 and below $100 to be outliers, so we removed those entries.


3. **Feature Encoding:**
   - Categorical features are converted to numerical using Label Encoding. We performed label encoding for columns that contained string values, such as the region, model, and type of car.


## Model Training

The following models are trained and evaluated:

1. **XGBRegressor:** A gradient boosting model known for its performance and efficiency.
2. **RandomForestRegressor:** A robust ensemble learning method that creates multiple decision trees and combines their predictions.
3. **GradientBoostingRegressor:** Another type of gradient boosting model with different hyperparameters.

## Evaluation

The models are evaluated using the R-squared score on the test set. The R-squared score measures the proportion of variance in the target variable (price) explained by the model. A higher R-squared score indicates a better fit.

- **XGBRegressor:** Achieved an R-squared score of [0.72].
- **RandomForestRegressor:** Achieved an R-squared score of [0.92].
- **GradientBoostingRegressor:** Achieved an R-squared score of [.68].

Permutation Feature Importance is also calculated to determine the relative importance of each feature in the model's predictions. 

## Usage

To use this project, follow these steps:

1. **Clone the repository:** `git clone [https://github.com/SriRamK345/Used-Vehicle-resale-price-prediction.git]`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Download the dataset:** Download the "Craigslist Carstrucks Data" from Kaggle and place it in the `data` directory.
4. **Run the notebook:** Open and run the Jupyter notebook `Used Vehicle price prediction.ipynb` to train and evaluate the models.
