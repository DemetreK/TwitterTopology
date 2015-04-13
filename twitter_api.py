import io
import json
import twitter

# XXX: Go to http://twitter.com/apps/new to create an app and get values
# for these credentials that you'll need to provide in place of these
# empty string values that are defined as placeholders.
#
# See https://vimeo.com/79220146 for a short video that steps you
# through this process
#
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

CONSUMER_KEY = 'LADlDij0uzjl0NIZjtCxYDfwL'
CONSUMER_SECRET = 'pdS8XvGOHLGYRVLxCk5TIOixqVAnQ2kQA3KTUhKIl2UjsWiMnS'
OAUTH_TOKEN = '2250220794-3wFFftWYgISyqG0RI1wur0aH3rvSCYxPMBAeBj2'
OAUTH_TOKEN_SECRET = 'cWSPf3oi4vsojiUs87BFddrIk6rPp1J8Bb1U9aPWAzHzx'

# The keyword query

QUERY = 'je suis charlie'
#QUERY = 'q=%23jesuischarlie%20since%3A2015-01-07%20until%3A2015-01-14&src=typd&lang=en'

# The file to write output as newline-delimited JSON documents
OUT_FILE = QUERY + ".json"


# Authenticate to Twitter with OAuth

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                                   CONSUMER_KEY, CONSUMER_SECRET)

# Create a connection to the Streaming API

twitter_stream = twitter.TwitterStream(auth=auth)


print('Filtering the public timeline for "{0}"'.format(QUERY))

# See https://dev.twitter.com/docs/streaming-apis on keyword parameters

stream = twitter_stream.statuses.filter(track=QUERY)

# Write one tweet per line as a JSON document. 

with io.open(OUT_FILE, 'w', encoding='utf-8', buffering=1) as f:
        for tweet in stream:
                    f.write(str(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))
                            print(tweet['text'])
