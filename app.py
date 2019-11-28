from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from twitter_fizzbuzz.api import TwitterAPI
from twitter_fizzbuzz.auth import get_auth
from twitter_fizzbuzz.helpers import fizzbuzz


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    username = db.Column(db.String(80))

    def __repr__(self):
        return '<Twitter {}:{}>'.format(self.username, self.twitter_id)


class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    username = db.Column(db.String(80))
    in_reply_to = db.Column(db.Integer)


@app.route('/')
def index():
    auth = get_auth()
    twitter = TwitterAPI(auth=auth)

    mentions = twitter.get_mentions_timeline()

    # Checks if the tweet is in the database
    for mention in mentions:
         # If yes, just pass
        if Tweet.query.get(mention.get('id')):
            pass
        # If no, do FizzBuzz
        else:
            fb = fizzbuzz(mention.get('text'))
            
            if fb is None:
                print('Entrada invalida para ', mention.get('user').get('screen_name'))

            # Reply with the result
            else:
                fb = '@{} {}'.format(mention.get('user').get('screen_name'), fb)
                reply = twitter.reply_to(fb, mention.get('id'))

            # Save tweet in databse
            t = Tweet(
                id=mention.get('id'),
                text=mention.get('text'),
                username=mention.get('user').get('screen_name')
            )

            # Save reply in databse
            r = Reply(
                id=reply.get('id'),
                text=reply.get('text'),
                username=reply.get('user').get('screen_name'),
                in_reply_to=mention.get('id')
            )

            db.session.add(t)
            db.session.add(r)
            db.session.commit()

    return '<Twitter FizzBuzz> '
