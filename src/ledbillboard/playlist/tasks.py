# -*- coding: utf-8 -*-
import threading

from ledbillboard.utils import get_video_metadata


class SaveMediaMetadata(threading.Thread):
    def __init__(self, media, **kwargs):
        self.media = media
        super(SaveMediaMetadata, self).__init__(**kwargs)

    def run(self):
        metadata = get_video_metadata(self.media.file.path)
        duration = metadata.get('streams', [{}, ])[0].get('duration', 0)
        self.media.duration = float(duration)
        self.media.save()
