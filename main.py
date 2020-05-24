from sentiment import generate_sentiment_scores
from pprint import pprint
import pandas as pd
from nltk_install import nltk_install

#install nltk dependencies
nltk_install()

positions = ['RB', 'WR', 'TE', 'QB']

df = pd.DataFrame()

for p in positions:
    data = generate_sentiment_scores(p)
    pos_df = pd.DataFrame(data)
    pos_df = pos_df.transpose()
    pos_df['Pos'] = p

    df = pd.concat([df, pos_df])

df.to_csv('data/sentiment.csv')
