#
# Copyright (c) 2014 - 2015 townhallpinball.org
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

from pinlib import p, mode, util

def init():
    p.load_mode(BackgroundMode, { "start": ["reset"] })
    p.load_mode(GameMode,       {
        "start": ["game_reset"],
        "stop":  ["game_over"]
    })

class BackgroundMode(mode.Base):

    def __init__(self, options):
        options["id"] = options.get("id", "background")
        super(BackgroundMode, self).__init__(options, priority=100)

    def start(self):
        p.machine.lamps("gi", lambda lamp: lamp.enable())


class GameMode(mode.Base):

    dropTarget = "up"

    def __init__(self, options):
        options["id"] = options.get("id", "game")
        super(GameMode, self).__init__(options, priority=110)

    def start(self):
        p.sounds.play_music("credits", start_time=2.4)
        p.events.on("next_player", self.next_player)
        self.machine.flippers().enable()

    def stop(self):
        p.events.off("next_player", self.next_player)
        self.machine.flippers().disable()

    def next_player(self):
        p.machine.coil("trough").pulse()
        self.lowerDropTarget(40)

    def raiseDropTarget(self):
        if self.dropTarget == "down":
            p.machine.coil("dropTargetUp").pulse()

    def lowerDropTarget(self, delay=0):
        if self.dropTarget == "up":
            p.machine.coil("dropTargetDown").pulse(delay=delay)

    def sw_trough1_active_for_2s(self, sw=None):
        p.game.next_player()

    def sw_spinner_active(self, sw=None):
        p.game.player.award(10)

    def sw_popperRight1_active_for_2s(self, sw=None):
        p.machine.coil("popperRight").pulse()

    def sw_eject_active_for_2s(self, sw=None):
        p.game.player.award(250)
        p.machine.coil("eject").pulse()

    def sw_magnetLeft_active(self, sw=None):
        p.machine.coil("magnetLeft").pulse(30)

    """
    def sw_magnetCenter_active_for(self, sw=None):
        p.machine.coil("magnetCenter").pulse(30)
    """

    def sw_magnetRight_active(self, sw=None):
        p.machine.coil("magnetRight").pulse(30)

    def sw_kickback_active(self, sw=None):
        p.machine.coil("kickback").pulse()

    def sw_dropTarget_active(self, sw=None):
        p.game.player.award(500)
        self.lowerDropTarget()

    def sw_troughEnterLeft_active(self, sw=None):
        p.game.player.award(1000)
        self.raiseDropTarget()
