# -*- coding: utf-8 -*-
import subprocess
import shlex
import json
from subprocess import SubprocessError


def get_video_metadata(filename):
    cmd = 'ffprobe -v quiet -print_format json -show_streams'
    args = shlex.split(cmd)
    args.append(filename)
    # run the ffprobe process, decode stdout into utf-8 & convert to JSON
    try:
        output = subprocess.check_output(args).decode('utf-8')
        return json.loads(output)
    except (SubprocessError, ValueError):
        return {}
