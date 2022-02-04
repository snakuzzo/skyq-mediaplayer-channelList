import time
import requests
import sys
from importlib import reload
if "/config/pyscript_modules" not in sys.path:
    sys.path.append("/config/pyscript_modules")

import write_file

write_file = reload(write_file)

# configuration
filename = '/config/integrations/media_player_skyq.yaml'
name = pyscript.app_config["name"]     
host = pyscript.app_config["host"]
country = pyscript.app_config["country"]
volume_entity_id = pyscript.app_config["volume_entity"]
live_tv = pyscript.app_config["live_tv"]

@time_trigger("shutdown")
@service
def build_skyq_channel_list():

  sources = {}

  url = 'http://{0}:9006/as/services'.format(host)
  r = task.executor(requests.get, url, headers={'content-type': 'application/json'})
  array = r.json()
  for channel in array['services']:
    chName = channel['t'].replace(" ", "") + "_"+channel['c']
    chNumber = ",".join([channel['c'][i:i+1] for i in range(0, len(channel['c']), 1)])
    sources[chName] = chNumber

  entity = {'media_player':[
              {'platform': 'skyq',
                'name': name,
                'host': host,
                'live_tv': live_tv,
                'country': country,
                'volume_entity': volume_entity_id,
                'sources': sources
              }
            ]}

  task.executor(write_file.write_yaml, filename=filename, content=entity)
    
