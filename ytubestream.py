import requests
import json
import sys
from requests.utils import unquote

def get_video_info(url):
    id = url.split("v=")[1]
    info_url = f"https://www.youtube.com/youtubei/v1/player?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"
    post_data = "{\"context\":{\"client\":{\"clientName\":\"WEB\",\"clientVersion\":\"2.20210518.07.00\"}},\"videoId\":\""+id+"\"}"
    r = requests.post(info_url, post_data)
    info = json.loads(r.content)
    streaming_data = info["streamingData"]
    all_formats = []
    if "formats" in streaming_data:
        all_formats += streaming_data["formats"]
    if "adaptiveFormats" in streaming_data:
        all_formats += streaming_data["adaptiveFormats"]
    expire_time = streaming_data["expiresInSeconds"]
    video_info = {
        "formats": all_formats,
        "expiresInSeconds": expire_time
    }
    video_json = json.dumps(video_info, indent=4)
    print(video_json)
    with open('data.txt', 'w') as outfile:
        json.dump(video_json, outfile)
    

url=sys.argv[1]
get_video_info(url)