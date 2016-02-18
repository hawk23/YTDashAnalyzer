#!/bin/python

import youtube_dl
import csv

ydl = youtube_dl.YoutubeDL({'outtmpl': u'%(id)s%(ext)s'})

with ydl:
    result = ydl.extract_info(
            # 'https://www.youtube.com/playlist?list=PLirAqAtl_h2r5g8xGajEwdXd3x1sZh8hC',
            'https://www.youtube.com/playlist?list=PLDC963AC0FD2A0FCB',
            download=False # We just want to extract the info
    )

csvwriter = csv.writer(open('stats.csv', 'wb'), dialect='excel')

csvwriter.writerow(['Youtube ID', 'Video Codec', 'Audio Codec', 'Width', 'Height', 'FPS', 'Extension', 'Format'])

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

    for rep in video['formats']:
        if rep['vcodec'] != u'none':
            csvwriter.writerow([
                video['id'],
                rep.get('vcodec', '-'),
                rep.get('acodec', '-'),
                rep.get('width'),
                rep.get('height'),
                rep.get('fps', 0),
                rep.get('ext', '-'),
                rep.get('format')
            ])

if 'entries' in result:
    # Can be a playlist or a list of videos
    for video in result['entries']:
        analyze_video(video)
