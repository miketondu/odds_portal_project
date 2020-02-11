# odds_portal_project
Machine Learning project focused on utilizing historical betting odds and match results for smaller gambling markets such as the Professional Bolivian Football League. The result of this project has an average of **66% accuracy** predicting home team wins, resulting in a positive ROI of up to 50% on simulated seasons.

The data was scraped from oddsportal.com using webscraper.io and python's selenium package

The project consists of 3 notebooks:

#### 1. Cleaning data and creating basic features from the scraped strings in the raw dataset

#### 2. Feature engineering and visualization

#### 3. Supervised learning modelling and retroactively simulating bets on historical matches using the predicted results obtained

The model was then deployed using a Docker image and an AWS instance:

#### ec2-13-59-94-10.us-east-2.compute.amazonaws.com

The final prediction compares discrepancies between the given house odds, the model's odds and ouputs a suggested percentage of the total bank roll that should be placed as a wager.


