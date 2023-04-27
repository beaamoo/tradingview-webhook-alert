# TradingView Webhook Alerts with AWS Lambda and Alpaca API

This repository contains the code to create an AWS Lambda function in Python that executes simple orders using the Alpaca API when receiving webhook alerts from TradingView.

## Prerequisites

- A TradingView account to create webhook alerts for the desired asset(s)
- An Alpaca account to execute bracket orders
- An AWS account to create an AWS Lambda function
- Python 3.8 or later installed on your local machine
- Chalice framework installed on your local machine

## Getting started

### Clone the repository to your local machine:

`$ git clone https://github.com/<your_github_username>/tradingview-webhook-alert.git

### Create a new virtual environment and activate it:


`$ python3 -m venv venv`
`$ source venv/bin/activate`

### Install the required packages using pip:


`$ pip install -r requirements.txt`

Update the config.json file with your Alpaca API key ID and secret key.

### Run the application locally:

`$ chalice local`

### Open a new terminal window and test the application using cURL:

`$ curl -X POST -H "Content-Type: application/json" -d '{"ticker": "AAPL", "type": "buy", "limit_price": 130, "take_profit": 135, "stop_loss": 125}' http://127.0.0.1:8000/`

The above command will simulate a TradingView webhook alert by sending a POST request to the local endpoint. The payload contains the ticker, type of order (buy or sell), limit price, take profit, and stop loss values.

### Deploy the application to AWS:

`$ chalice deploy`

This command will deploy the application to AWS Lambda and create an API Gateway.

### Create a webhook alert in TradingView:

In TradingView, navigate to the chart of the desired asset and open the Alerts dialog. Create a new alert and set the following values:

- Condition: The condition to execute trade
- Message: json format with the required place holders. 
- Send email: Test it by sending the alert with email to see the json messsage information.
- Webhook URL: The URL of the AWS API Gateway endpoint created in the previous step.

Save the alert and you're done! The webhook alert will trigger the AWS Lambda function, which will execute the trade using the Alpaca API.

## Tips
Use Insomnia or a similar tool to test your webhook alerts before deploying to TradingView. This will help you debug any issues and ensure that the payload is being sent correctly.

## Resources
[Chalice initialisation](https://aws.github.io/chalice/quickstart.html)

[Alpaca API documentation](https://alpaca.markets/docs/api-references/)

[TradingView webhook documentation](https://www.tradingview.com/support/solutions/43000529348-webhooks/)
