from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os
import time
import sys

key = "6ac7a207cf378cdaaf67c6288783646c"
secret = "8680f0f094d6bf93"

wait_time = 1

keyword = sys.argv[1]
savedir = "./" + keyword
if not os.path.exists(savedir):
    os.mkdir(savedir)

flickr = FlickrAPI(key, secret, format="parsed-json")
result = flickr.photos.search(
    text=keyword,
    per_page=400,
    media="photo",
    sort="relevance",
    safe_search=1,
    extras="url_q, license"
)

photos = result["photos"]

for i, photo in enumerate(photos["photo"]):
    url_q = photo["url_q"]
    filepath = savedir + '/' + photo['id'] + ".jpg"
    if os.path.exists(filepath):
        continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
