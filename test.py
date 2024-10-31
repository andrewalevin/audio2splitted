import pprint

from src.audio2splitted.audio2splitted import get_audio_segments_by_timecodes


print('🦄 Segments: ')
tests = [
    [999, [4, 8, 16, 32,  100, 200, 300, 484, 488, 492, 496, 500, 502, 504, 508, 512, 516, 600, 700, 800, 984, 988, 992, 998, 1000, 1027, 1034], 1],
]


for test in tests:
    print('🦄 Segments:  for: ', test)
    segments = get_audio_segments_by_timecodes(total_audio_duration=test[0], timecodes=test[1], padding_duration=test[2])
    pprint.pprint(segments)
    print()


