"""
Given a string and a list of stopwords, return the substring that appears before the first occurrence of any stopword.

Follow-up:
What if the input is a stream and cannot be fully loaded into memory?

"""
import random
from math import inf
def get_sentence(inp, stops):
    min_index = inf
    for stop in stops:
        if stop in inp:
            min_index = min(min_index, inp.index(stop))
    return inp[:min_index] if min_index != inf else inp

def partial_match_index(inp, stop):
    idx = len(inp) - len(stop)
    si = 0
    while idx < len(inp):
        if inp[idx] == stop[si]:
            idx += 1
            si += 1
        else:
            idx += 1
            si = 0
    return si

def stream_input(inp):

    i = 0
    max_len = len(inp)
    while i < len(inp):
        stream_size = random.randint(1, 7)
        yield inp[i: min(i + stream_size, max_len)]
        i += stream_size

def get_sentence2(inp, stop):
    from collections import deque
    words = deque()
    cur_len = 0
    for w in stream_input(inp):
        if cur_len < len(stop):
            cur_len += len(w)
            words.append(w)
            continue
        else:
            words.append(w)
        sentence = ''.join(words)
        print(words, sentence)
        if stop in sentence:
            yield sentence[:sentence.index(stop)]
            return None
        else:
            slen = len(sentence)
            while slen >= len(stop):
                word = words.popleft()
                slen -= len(word)
                cur_len -= len(word)
                yield word

    return None







def test():
    inp = 'Given a string and a list of stopwords, return the substring that appears before any stop word'
    stops = ['substring', 'ing and a list o', 'list']

    print(get_sentence(inp, stops))
    print(partial_match_index(inp, 'op word'))
    print(partial_match_index(inp, 'stop words are not'))

def test2():
    inp = 'Given a string and a list of stopwords, return the substring that appears before any stop word'
    words = []
    for e in stream_input(inp):
        words.append(e)
    print(words)

    sentence_words = []
    for e in get_sentence2(inp, 'opwords, return the subs'):
        sentence_words.append(e)
    print(sentence_words)


#test()
test2()