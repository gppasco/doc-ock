import tweepy
import DocOck as doc
import tokens

# THIS TWEETS
if __name__ == "__main__":
	auth = tweepy.OAuthHandler(tokens.API_KEY, tokens.API_SECRET_KEY)
	auth.set_access_token(tokens.ACCESS_TOKEN, tokens.ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

	timeline = api.user_timeline()

	# Avoid duplicating tweets
	past_tweets = []
	for item in timeline:
		past_tweets.append(item.text.split(".")[0])

	if doc.get_text():
		if doc.get_text().split(".")[0] not in past_tweets:
			api.update_status(doc.get_text())

			# DM me so I know it's working
			api.send_direct_message(tokens.PERSONAL_ID, "good news good stus")
		else:
			api.send_direct_message(tokens.PERSONAL_ID, "there's a stu waiting for u")
	else:

		# Again, DM me so I know it's working
		api.send_direct_message(tokens.PERSONAL_ID, "no Stu for now :(")