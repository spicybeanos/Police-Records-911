# 911 Emergency Call Analysis

## Overview
This project analyzes a real-world dataset of 911 emergency calls from Montgomery County, Pennsylvania, USA. The goal is to extract actionable insights from call patterns to improve emergency response planning and resource allocation.  

The dataset contains approximately 260,000 records, including details such as call type, location (latitude/longitude), zip code, township, time of call, and description.

## Objective
- Identify the **top zip codes** and **townships** with the highest volume of 911 calls.  
- Determine **most common reasons** for calls and their distribution across days of the week and months.  
- Visualize call patterns to support **data-driven decision-making** for emergency services.  

## Dataset
The dataset `data\911.csv` contains the following columns:
- `lat`: Latitude of the call  
- `lng`: Longitude of the call  
- `desc`: Description of the emergency  
- `zip`: Zip code of the call  
- `title`: Emergency type  
- `timeStamp`: Date and time of the call (YYYY-MM-DD HH:MM:SS)  
- `twp`: Township  
- `addr`: Address  
- `e`: Dummy variable (always 1)  

## Tools & Technologies
- **Python**: Core programming  
- **Pandas & NumPy**: Data cleaning, transformation, and feature engineering  
- **Matplotlib & Seaborn**: Data visualization and plotting  

## Key Analyses
1. Identify the **top 10 zip codes** for 911 calls and check for specific zip codes.  
2. Find the **top 4 townships** with the most calls and highlight missing ones.  
3. Determine the **most common reasons** for 911 calls.  
4. Visualize calls by reason using **horizontal bar charts**.  
5. Analyze **day-wise and month-wise call trends** for EMS, Fire, and Traffic calls.  
6. Create **countplots** showing calls per day of the week and per month, categorized by reason.

## Insights & Outcomes
- Pinpointed high-density areas and peak times for emergency calls.  
- Provided visualizations to help emergency services **allocate resources efficiently**.  
- Demonstrated the use of Python and data analytics techniques on a **large-scale real-world dataset**.  

## How to Run
1. Clone the repository:  
   ```bash
   git clone <repo-url>
