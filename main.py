#!/usr/bin/python3

import colorama

from mathboss.mathboss import *
from mathboss.settings import Settings

def main():
    colorama.init()

    settings = Settings()

    run_main_loop(settings)


if __name__ == '__main__': main()