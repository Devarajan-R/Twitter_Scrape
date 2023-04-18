# Twitter_Scrape
Allows user to scrape , download and store tweets.

# used models
python, Mongodb Atlas, snscrape, streamlit

# installations
1. vscode
2. create account in mogodb
3. pip install snscrape pandas pymongo streamlit ( Terminal command )


# program workflow
1. Import the required libraries
2. from pymongo import MongoClient
3. Define a function to scrape the twitter data based on the keyword or hashtag, date range, and tweet count
4. create a list to hold the scraped tweets
5. use snscrape to scrape the tweets based on the search criteria
6. create a pandas dataframe from the scraped tweets
7. connect to the MongoDB database
8. insert the tweets dataframe into the MongoDB collection
9. set the app title
10. define the search criteria inputs
11. scrape the tweets based on the search criteria
12. insert the scraped tweets into the MongoDB database
13. download the scraped tweets in CSV and JSON formats
14. Run the Streamlit app:


This solution meet the requirements by allowing the user to search for a keyword or hashtag, select a date range, limit the tweet count, scrape the tweets, display them in the page, insert them into the MongoDB database, and download them in CSV and JSON formats. The code is also modular, with each functional block serving a specific purpose.
