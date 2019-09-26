import re

def compute_word_freqs(s):
    words = re.findall(r'[A-Za-z\']+', s.lower())
    freqs = {}
    for w in words:
        freqs[w] = freqs.get(w, 0) + 1
    return sorted(freqs.items(), key=lambda x: -x[1])

# For writing the results:
# lines = ['%s,%d' % (w, c) for w, c in sortedfreqs]
# with open('word_frequencies.txt', 'w') as f:
#     f.write('\n'.join(lines))