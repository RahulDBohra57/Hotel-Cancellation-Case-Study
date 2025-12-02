App Link: https://hotel-cancellation-case-study.streamlit.app/

Hotel Booking Cancellation Prediction

This project builds a machine learning–driven system to predict the likelihood of hotel booking cancellations using key factors such as arrival month, arrival day, booking type (online/offline), lead time, number of adults, and several other customer and reservation attributes.

🚀 Project Overview

The primary objective is to help hotels anticipate cancellations and optimize revenue and resource planning.
We performed end-to-end data exploration, model development, evaluation, and deployment.

🔍 Exploratory Data Analysis (EDA)

- Identified trends and patterns influencing cancellations
- Handled missing values, outliers, and data imbalance
- Visualized key insights to understand customer booking behavior

🤖 Machine Learning Models Used

Models evaluated:
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

After performance benchmarking, a Voting Classifier (combining XGBoost + Decision Tree) was selected as the final model due to its strong accuracy and stability.

🛠️ Tech Stack

- Python
- Visual Studio Code
- GitHub (Version Control)
- Streamlit (Model Deployment)

🌐 Deployment

The final model is deployed through a Streamlit web app, allowing users to input booking details and instantly view the predicted cancellation probability.

📁 Project Highlights

- End-to-end ML pipeline: EDA → preprocessing → model training → evaluation → deployment
- Multiple model comparison for optimal performance
- Clean and interactive UI for predictions
- Practical industry application for hotel revenue management
