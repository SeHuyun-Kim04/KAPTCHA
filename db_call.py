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


def main(svo):
    if svo == 'subject':
        f = open("Noun.txt", 'r', encoding='utf-8')
        rdr = f.readlines()  # Read Db Result
        result = hgtk.josa.attach(
            rdr[
                random.randint(0, len(rdr) - 1)
            ],
            hgtk.josa.I_GA
        )
        f.close()

    elif svo == 'object':
        f = open("Noun.txt", 'r', encoding='utf-8')
        rdr = f.readlines()  # Read Db Result
        rand = random.randint(0, 2)
        if rand == 0:
            result = hgtk.josa.attach(
                rdr[
                    random.randint(0, len(rdr) - 1)
                ],
                hgtk.josa.EUL_REUL
            )
        elif rand == 1:
            result = hgtk.josa.attach(
                rdr[
                    random.randint(0, len(rdr) - 1)
                ],
                hgtk.josa.GWA_WA
            )
        elif rand == 2:
            result = hgtk.josa.attach(
                rdr[
                    random.randint(0, len(rdr) - 1)
                ],
                hgtk.josa.EURO_RO
            )
        f.close()

    elif svo == 'verb':
        f = open("Ver.txt", 'r', encoding='utf-8')
        rdr = f.readlines()  # Read Db Result
        result = rdr[
            random.randint(0, len(rdr) - 1)
        ]
        f.close()

    else:
        print("Err!")

    return result.replace('\n', '')
