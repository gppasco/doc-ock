import feedparser
import random

# LAST HURDLE: GET THIS TO PUBLISH AUTOMATICALLY
# BONUS: TRY TO PULL THE OUTLET?

URL_TEXT = "https://crosswordfiend.com/feed/"
STU_PUNS = ["Tuesday? More like STU'S DAY! (note i'm sorry if today is not Tuesday):",
	"Let's Ock and roll:",
	"Go check out the latest from the STUdio:",
	"*carl weathers voice* Baby, you got a STU going!",
	"Solve the STU's, read the 'VIEWS! (short for reviews):",
	"Et STU, STU-te?",
	"Good news, good STUs!",
	"Call your family, it's STU day!",
	"Ock's got today on lock!", 
	"S-T-U for Y-O-U!",
	"It's a beautiful day for a STU puz!"]

# Get a few of the most recent Crossword Fiend posts
def get_feed():
	feed = feedparser.parse(URL_TEXT)
	return feed

# Returns "True" if Stu Ockman has constructed a puzzle in that day's blog entry
def stu_check(entry):

	# Build a list of all constructors for a particular day
	all_constructors = []
	for tag in entry.tags:
		all_constructors.append(tag.term)

	# Return true if Stu Ockman is in the constructors for a day
	return ("Stu Ockman" in all_constructors)

def get_text():
	feed = get_feed()

	# Right now this goes over all entries; refine this later
	for entry in feed.entries:
		if stu_check(entry):
			publish_time = entry.published.split(" ")
			new_time = " ".join(publish_time[:4])
			return "Stu was published on {}. {} {}".format(new_time, random.choice(STU_PUNS), entry.link)
	return False