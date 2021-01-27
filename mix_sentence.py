# -*- coding: UTF-8 -*-

"""
KAPTCHA
: Korean Automated Public Turing test to tell Computers and Humans Apart

= Necessary package(pip install)
- hgtx
- six
"""

import random
import hgtk

def main(word):
    stra = ""
    o_word=word

    for i in word:
        rand = word[random.randint(0, len(word) - 1)]
        stra += shift_letter(rand)
        word = word.replace(rand, "", 1)

    return o_word + ' ', stra + ' '


def shift_letter(letter):
    ld = list(hgtk.text.decompose(letter))
    ch_str=""

    for i in ld:
        if i == 'ㄱ':
            ch_str += 'ㄲ'

        elif i == 'ㄷ':
            ch_str += 'ㄸ'

        elif i == 'ㅅ':
            ch_str += 'ㅆ'

        elif i == 'ㅈ':
            ch_str += 'ㅉ'

        elif i == 'ㅂ':
            ch_str += 'ㅃ'

        else :
            ch_str+=i

    return hgtk.text.compose(ch_str)
