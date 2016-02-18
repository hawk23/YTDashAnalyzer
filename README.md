# YTDashAnalyzer

# Prerequisits
* install youtube-dl package: ``pip install youtube-dl``
* run the script: ``python youtube-stats.py``

# Download MPD
* ``curl $(youtube-dl https://www.youtube.com/watch?v=iVAgTiBrrDA --youtube-include-dash-manifest --dump-intermediate-pages -s | grep manifest.google | cut -d ' ' -f 5) > test-manifest.mpd``