# Fantasy Football Twitter Sentiment Analysis

This project uses the Twitter API and the [VADER](https://github.com/cjhutto/vaderSentiment) Sentiment Analysis tool. VADER is a natural language processing library primarily used to analyze social media sentiment.

This project generates a positive and negative sentiment score for the top 20 players at TE, WR, QB, RB. It does this by searching for non-truncated tweets from a list of Fantasy Football analysts listed in `config.py` in the `Config` class. Feel free to adjust this list of analysts.
The project then downloads this data to a csv file located in the `data` directory under the file name `sentiment.csv`

To use this project, you need to create a `.env` file with the following environment variables:
1. TWITTER_API_KEY
2. TWITTER_API_SECRET
3. TWITTER_ACCESS_TOKEN
4. TWITTER_ACCESS_SECRET

[These keys can be found after setting up a twitter app to interact with the Twitter API.](https://developer.twitter.com/en/apps/) `TWITTER_API_KEY` is your consumer API key, `TWITTER_SECRET_KEY` is your consumer API secret key, `TWITTER_ACCESS_TOKEN` is your twitter API access token, and `TWITTER_ACCESS_SECRET` is your twitter API access secret.

[This project also depends on having weekly Fantasy Data available from the Fantasy Football Data Pros website here.](https://www.fantasyfootballdatapros.com/csv_files)

The project is ran using `python main.py` after installing dependencies listed in the `requirements.txt`. It's also recommended that you run this code in a virtual environment and then install dependencies listed in `requirements.txt`. For example:

  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt

  python main.py
