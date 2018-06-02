import datetime
from dateutil.relativedelta import relativedelta
from google_images_download import google_images_download
import random
from secrets import *
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

response = google_images_download.googleimagesdownload()

keyword = "bolivia paisaje"

today = datetime.date.today()
timemax = today.strftime('%m/%d/%Y')
timemin = (today + relativedelta(years=-1)).strftime('%m/%d/%Y')

arguments = {"keywords":keyword,"limit":50,"print_urls":True, "output_directory": "/tmp/", "language": "Spanish", "usage_rights": "labeled-for-reuse", "size": "large", "time_range": '{"time_min": "'+timemin+'","time_max": "'+timemax+'"}'}
paths = response.download(arguments)

api.update_with_media(random.choice(paths[keyword]), "")

# Delete files
for f in paths[keyword]:
    os.remove(f)
