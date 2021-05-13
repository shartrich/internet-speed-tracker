# Internet Speed Tracker

## Description
Want to know the best time of day to download heavy content? 
Feel like your ISP throughput is inconsistent throughout the day? 
Use Python to track your wifi speed throughout the day!

Host with a Raspberry Pi or any other Unix based device


## Setup

### Clone this project
clone this project to your device

```
git clone https://github.com/shartrich/internet-speed-tracker.git
```

### Install dependencies
cd into new directory:

```
cd internet-speed-tracker
```

Use pip to install the necessary dependencies

```
pip install -r requirements.txt
```

### Environment Variables
Create a new .env file:

```
nano .env
```

Configure environment variables:

| Variable | Type | Description |
| - | - | - |
| DEBUG_MODE | boolean | Specify `True` if you want to print your data to a local CSV instead of uploading to a remote database |
| DB_HOST | string | domain of remote database to push your data to |
| DB_PORT | string | which port to access database via `'3306'` |
| DB_USERNAME | string | username to access provided database |
| DB_PASSWORD | string | password to access provided database |

## Running service
You can manually invoke the service or host it on a Cronjob

### Manual Invocation
Navigate to your project directory

Set the DEBUG_MODE .env file to `True`

Run main.py:

```
python3 main.py
```

Find your results inside ./data/results.csv

### Host via Crontab

Use a tool like [crontab guru](https://crontab.guru/) to come up with an expression matching your desired run frequency

open your crontab:
```
crontab -e
```

Add a cron expression mapping to your python installation and main.py in your project directory. 

Example 1 - Run every 15 minutes:

```
0,15,30,45,35 * * * * /usr/bin/python3 /home/pi/Documents/GitHub/internet-speed-tracker/main.py
```