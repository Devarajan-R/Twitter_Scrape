import snscrape.modules.twitter as sntwitter
import pandas as pd
import pymongo
import streamlit as st
import base64



def scrape_tweets(keyword, start_date, end_date, tweet_count):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' since:' + str(start_date) + ' until:' + str(end_date) + ' lang:en').get_items()):
        if i >= tweet_count:
            break
        tweets.append((tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.sourceLabel, tweet.likeCount))
    df = pd.DataFrame(tweets, columns=['date', 'id', 'url', 'content', 'user', 'reply_count', 'retweet_count', 'language', 'source', 'like_count'])
    return df

def download_csv(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="twitter_data.csv">Download CSV</a>'
    return href

def download_json(df):
    json = df.to_json(orient='records')
    b64 = base64.b64encode(json.encode()).decode()
    href = f'<a href="data:file/json;base64,{b64}" download="twitter_data.json">Download JSON</a>'
    return href

def store_tweets(df):
    client = pymongo.MongoClient("mongodb+srv://devarajan:samsungm31@cluster0.yzngdkz.mongodb.net/?retryWrites=true&w=majority")
    db = client["twitter"]
    collection = db["tweets"]
    tweets = df.to_dict('records')
    st.write(tweets)
    collection.insert_many(tweets)
    st.success('Your data is stored successfully!')

st.title('Twitter Scrape')

keyword = st.text_input('Hashtag / Keyword to be searched')
start_date = st.date_input('Start date')
end_date = st.date_input('End date')
tweet_count = st.number_input('Enter tweet counting ', min_value=1)
search=st.button('Search Tweets')
#st.write(search)
if keyword and search:
    
    df = scrape_tweets(keyword, start_date, end_date, tweet_count)
    st.table(df)
    st.markdown(download_csv(df), unsafe_allow_html=True)
    st.markdown(download_json(df), unsafe_allow_html=True)
    if st.button('Store Tweets to MongoDB'):
        store_tweets(df)


