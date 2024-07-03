# bit.mortgage
Purchasing a home is a daunting task and perhaps the most important financial decision of our lives. bit.mortgage help ease the process by providing research and financial guidelines for users.

### Note
This repository only includes the code for the Python Web Server. The full Devpost submission can be viewed here: https://devpost.com/software/bit-mortgage

## Inspiration
We were inspired by the 28/36 rule in finance. Which states that you should not spend more than 28% of your income on total housing expenses and no more than 36% on housing plus other debt. So we sought to make an app that does mortgage planning based on this rule.

## What it does
The app takes in a few basic parameters like income, credit score range, and zip code to provide personalized guidelines and statistics for prospective home owners. We provide users up to date information on current mortgage interest rates based on credit score, and how that affects their budget in adherence to the 28/36 rule. In addition, we have a database of typical home value data for each zip code in the US, allowing us to compare the user’s budget to typical houses in the area they live in.

## How we built it
The majority of the app is built using swift. The UI is all in SwiftUI for a native iOS experience. We utilized some python scripts to clean up the Zillow dataset of typical home value based on zip code and convert it to an html file. Our app acquires this data by using a web scraper to search for the data we need for a certain zip code.

## Challenges we ran into
The main challenge we ran into was time. For a more efficient and versatile solution, we could’ve set up a server backend that returns the necessary home value data when we called to it. However, we went with a web scraping solution as it was faster to implement.

Finding proper data was also a great challenge for us. For example, interest rates are quite complex and varied greatly due to factors like loan size, credit score, and location. We were eventually able to find the data of national averages, but it is not as personalized as we would like.

## Accomplishments that we're proud of
We are proud of the overall product we made. The UI design and experience was aesthetically pleasing and also easy to use. The experience is also very quick to use and streamlined. We are also proud of the various formulas we researched and implemented to provide recommended budgets and guidelines.

## What we learned
We have learned a great deal from this experience. We have certainly learned to become better UI designers and became more familiar with Swift. We also learned for the first time how to web scrape using Swift. We also learned a little more about python’s pandas library while cleaning up and extracting the data we needed from Zillow’s dataset.

## What's next for bit.mortgage
We plan on implementing more features to the project like accounting for property tax in our expenses and perhaps even insurance. We also plan eventually ditching web scraping and utilizing a server for our mobile app.
