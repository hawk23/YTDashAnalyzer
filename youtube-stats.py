#!/bin/python

import youtube_dl
import json

ydl = youtube_dl.YoutubeDL({'outtmpl': u'%(id)s%(ext)s'})

with ydl:
    result = ydl.extract_info(
            # 'https://www.youtube.com/playlist?list=PLirAqAtl_h2r5g8xGajEwdXd3x1sZh8hC',
            'https://www.youtube.com/playlist?list=PLDC963AC0FD2A0FCB',
            download=False # We just want to extract the info
    )

stats = {
    'video_rep': {},
    'vcodec': {},
    'acodec': {},
    'format': {}
}

def increment(stat, key):
    if key in stats[stat]:
        stats[stat][key] += 1
    else:
        stats[stat][key] = 1

def analyze_video(video):
    rep_count = 0

    for rep in video['formats']:
        if rep['vcodec'] != u'none' and rep['ext'] != u'webm':
            rep_count += 1

            if 'fps' in rep:
                index = "{0} - {1}x{2}@{3}".format(video['id'], rep['height'], rep['width'], rep['fps'])
            else:
                index = "{0} - {1}x{2}".format(video['id'], rep['height'], rep['width'])
            increment('format', index)

            increment('vcodec', rep['vcodec'])

            print index + " - " + rep['ext']


    increment('video_rep', rep_count)


# if 'entries' in result:
    # Can be a playlist or a list of videos
#    for video in result['entries']:
#        analyze_video(video)

print json.dumps(result['entries'])