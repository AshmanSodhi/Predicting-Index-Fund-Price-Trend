# Predicting-Index-Fund-Price-Trend
This machine learning project focuses on predicting price trends for index funds. The project leverages historical financial data and advanced predictive models to forecast future price movements, aiming to provide insights for investors and financial analysts.

## API Used
  - `twelvedata`
  -  You can use this API to access world financial markets including stocks, forex, ETFs, indices, and cryptocurrencies. Most of the data is available in real-time.

## ML Model Used
  - The project uses a neural network model - Long Short-Term Memory (LSTM) architecture, which is a type of Recurrent Neural Network (RNN) commonly used for time series prediction and sequence modeling.
  - Long Short-Term Memory networks are designed to handle the vanishing gradient problem and maintain long-term dependencies in sequences. They are effective for tasks where context from previous time steps is crucial for prediction.

## Dataset
The dataset used in this project consists of historical financial data for index funds, which includes the following columns:
  - `datetime`: The timestamp indicating the date and time of the recorded data.
  - `open` : The opening price of the index fund at the beginning of the trading period.
  - `high` : The highest price reached by the index fund during the trading period.
  - `low` : The lowest price reached by the index fund during the trading period.
  - `close` : The closing price of the index fund at the end of the trading period.
  - `volume` : The number of shares or contracts traded during the trading period.

## Dependencies
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `scikit-learn`
  - `plotly`

## Results

Candlestick Graph - Predicting Trend
![image](https://github.com/AshmanSodhi/Predicting-Index-Fund-Price-Trend/assets/132582176/d4090120-4732-4006-9fbb-16d24f9020d8)
![image](https://github.com/AshmanSodhi/Predicting-Index-Fund-Price-Trend/assets/132582176/2d87fa98-ecc2-4883-bbe8-d44f797c114f)


## WebApp

## Team
+ Dhairya Parikh
+ Ashman Sodhi
+ Aditya
+ Veydant
+ Rashel Garg

## Acknowledgements
We would like to extend our heartfelt gratitude to VITMAS for giving us the opportunity to work on this exciting machine learning project.
We would also like to thank Kunal and <name> for their invaluable help and guidance throughout this project. Their expertise and support have been crucial for our projects, and we deeply appreciate their contributions. 
