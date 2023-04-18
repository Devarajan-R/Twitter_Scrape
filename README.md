# Twitter_Scrape
Allows user to scrape , download and store tweets.
This solution meet the requirements by allowing the user to search for a keyword or hashtag, select a date range, limit the tweet count, scrape the tweets, display them in the page, insert them into the MongoDB database, and download them in CSV and JSON formats.

# This Program deals with
python, Mongodb Atlas, snscrape, streamlit, vs code

# Installations
1. vscode
2. create account in Mogodb Atlas
3. pip install snscrape pandas pymongo streamlit ( Terminal command )


# Program Workflow
1. Import the required libraries
2. from pymongo import MongoClient
3. Define a function to scrape the twitter data based on the keyword or hashtag, date range, and tweet count
4. create a list to hold the scraped tweets
5. use snscrape to scrape the tweets based on the search criteria
6. create a pandas dataframe from the scraped tweets
7. connect to the MongoDB Atlas database
8. insert the tweets dataframe into the MongoDB collection
9. set the app title
10. define the search criteria inputs
11. scrape the tweets based on the search criteria
12. insert the scraped tweets into the MongoDB database
13. download the scraped tweets in CSV and JSON formats
14. Run the Streamlit app
 
