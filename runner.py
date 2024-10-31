import pathlib

import asyncio

from audio2splitted.audio2splitted import split_audio_second

print('🎃 Start')

audio = pathlib.Path('data/kofe.m4a')

result = asyncio.run(split_audio_second(audio, pathlib.Path('ouptup')))

print('result')