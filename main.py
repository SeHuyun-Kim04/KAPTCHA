# -*- coding: UTF-8 -*-

"""
KAPTCHA
: Korean Automated Public Turing test to tell Computers and Humans Apart

= Necessary package(pip install)
- hgtx
- six
"""

import mix_sentence as ms
import db_call as dc

if __name__ == '__main__':

    result_1 = ms.main(dc.main('subject'))
    # 주어 -은, -는, -이, -가

    result_2 = ms.main(dc.main('object'))
    # 목적어(물건) -을, -를, -는, -도, -만

    result_3 = ms.main(dc.main('verb'))
    # 서술어(행동, 상태) Ex) 웃다, 말하다

    original = result_1[0] + result_2[0] + result_3[0]
    questions = result_1[1] + result_2[1] + result_3[1]

    print(questions)
    print('Dev :', original)

    ip = input()

    if ip == original[:len(original) - 1]:
        print("Correct!")
    else:
        print("Wrong!")
