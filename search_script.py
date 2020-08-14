#!/usr/bin/env python3
import webbrowser
import sys
import pyperclip
if len(sys.argv) > 1:
    if sys.argv[1] == 'yt' or sys.argv[1] == 'youtube':
        webbrowser.open(
            'https://youtube.com/results?search_query={}'.format(' '.join(sys.argv[2:])), new=2)
    elif sys.argv[1] == 'am' or sys.argv[1] == 'amazon':
        webbrowser.open(
            'https://www.amazon.com/s?k={}&ref=nb_sb_noss_2'.format(' '.join(sys.argv[2:])), new=2)
    else:
        webbrowser.open(
            'https://www.google.com/search?q={}'.format(' '.join(sys.argv[1:])), new=2)
else:
    webbrowser.open(
        'https://www.google.com/search?q={}'.format(pyperclip.paste()), new=2)
