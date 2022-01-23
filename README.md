# skyq-mediaplayer-channelList

This Python script creates the `/ config / packages / skyq_mediaplayer.yaml` package with the media player entity as [SkyQ Media Player custom component](https://github.com/RogerSelwyn/Home_Assistant_SkyQ_MediaPlayer) expects

If you need to automatically create switches for control with voice assistants, be careful ... creating switches for all channels takes a lot of resources on the server and could crash the system.

If you need to view the new list on Home Assistant you need to restart Core, because at the moment it's not possible reload of media player entites.
Pleas vote this issue to make this possibile -> https://community.home-assistant.io/t/add-reload-media-player-entities/376614
