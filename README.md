# skyq-mediaplayer-channelList

This Python script creates a package with the media player entity as [SkyQ Media Player custom component](https://github.com/RogerSelwyn/Home_Assistant_SkyQ_MediaPlayer) expects

If you need to automatically create switches for control with voice assistants, be careful ... creating switches for all channels takes a lot of resources on the server and could crash the system.

If you need to view the new list on Home Assistant you need to restart Core, because at the moment it's not possible reload of media player entites.
Pleas vote this issue to make this possibile -> https://community.home-assistant.io/t/add-reload-media-player-entities/376614


# pyscript service
to use the script as [pyscript](https://github.com/custom-components/pyscript) script follow the path used in this repo (or adjust the path accordingly in the py source file).
While installing pyscript, use the following configuration (adjust the skyq platform config according to your needs):
```
pyscript:
  allow_all_imports: true
  hass_is_global: true
  apps:
    skyq_update:
      name: SkyQ Living Room
      host: 192.168.0.10
      country: ITA
      live_tv: true
      volume_entity: media_player.tv
'''
