import pandas as pd
import numpy as np

import requests
import json

from config import *


def get_channel_stats():
    url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}'

    request = requests.get(url)
    json_stats = json.loads(request.text)

    stats = json_stats['items'][0]['statistics']
    
    print(stats)


get_channel_stats()
