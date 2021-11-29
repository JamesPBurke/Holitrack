import tweepy
import twauth

class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        status_text = "Yes, I can hear you @" + status.user.screen_name
        print(status.user.screen_name)
        print(status.text)
        screen_name = status.user.screen_name
        statid = status.id
        self.api.update_status(status_text, in_reply_to_status_id = statid)

auth = tweepy.OAuthHandler(twauth.API_KEY, twauth.API_SECRET)
auth.set_access_token(twauth.ACCESS_TOKEN, twauth.ACCESS_SECRET)

printer = IDPrinter(
    twauth.API_KEY, twauth.API_SECRET,
    twauth.ACCESS_TOKEN, twauth.ACCESS_SECRET
)

IDPrinter.api = tweepy.API(auth)

printer.filter(track=["#elfgoat"])


