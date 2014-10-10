#
# Copyright (c) 2014 townhallpinball.org
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import locale
import traceback
import os
import pinlib
from pinlib import system

def main():
    # The score display uses the locale to determine if commas or
    # periods should be used as the number separator.
    locale.setlocale(locale.LC_ALL, "")

    system.init()
    pinlib.use("pingame.attract", {
        "start": ["request_attract"]
    })
    pinlib.use("pinlib.modes.coin", {
        "start": ["reset"]
    })
    pinlib.use("pinlib.modes.core", {
        "start": ["reset"]
    })
    #machine.use("pinlib.modes.oops", {
    #    "start": ["crashed"],
    #    "stop": "reset"
    #})
    pinlib.use("pinlib.modes.service", {
        "start": ["request_service"]
    })
    pinlib.use("pinlib.modes.splash", {
        "start": ["reset"],
        "stop": "request_attract"
    })

    system.run()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print traceback.format_exc()
        os._exit(1)
