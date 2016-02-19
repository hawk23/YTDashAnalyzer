#!/bin/python

import youtube_dl
import csv

ydl = youtube_dl.YoutubeDL({'outtmpl': u'%(id)s%(ext)s', 'ignoreerrors': True})

with ydl:
    result = ydl.extract_info(
            'https://www.youtube.com/playlist?list=PLirAqAtl_h2r5g8xGajEwdXd3x1sZh8hC',
            #'https://www.youtube.com/playlist?list=PLDC963AC0FD2A0FCB',
            #'https://www.youtube.com/watch?v=7zp1TbLFPp8',
            download=False # We just want to extract the info
    )

representationWriter = csv.writer(open('representation_stats.csv', 'wb'), dialect='excel')
representationWriter.writerow(['Youtube ID', 'Video Codec', 'Audio Codec', 'Width', 'Height', 'FPS', 'Extension', 'Format', 'Resolution', 'Bitrate'])

videoWriter = csv.writer(open('video_stats.csv', 'wb'), dialect='excel')
videoWriter.writerow(['Youtube ID', 'Representation Count'])


def analyze_video(video):
    repCount = 0

    if video is not None and 'formats' in video:
        for rep in video['formats']:
            if rep['vcodec'] != u'none':
                representationWriter.writerow([
                    video['id'],
                    rep.get('vcodec', '-').strip(),
                    rep.get('acodec', '-').strip(),
                    rep.get('width', 0),
                    rep.get('height', 0),
                    rep.get('fps', 0),
                    rep.get('ext', '-'),
                    rep.get('format'),
                    "{0}x{1}".format(rep.get('width', '?'), rep.get('height', '?')),
                    rep.get('tbr', 'none')
                ])

                repCount += 1

        videoWriter.writerow([video['id'], repCount])

if result is not None and 'entries' in result:
    # Can be a playlist or a list of videos
    for video in result['entries']:
        analyze_video(video)
