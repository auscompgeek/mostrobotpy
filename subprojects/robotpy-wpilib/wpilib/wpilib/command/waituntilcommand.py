#----------------------------------------------------------------------------
# Copyright (c) FIRST 2008-2012. All Rights Reserved.
# Open Source Software - may be modified and shared by FRC teams. The code
# must be accompanied by the FIRST BSD license file in the root directory of
# the project.
#----------------------------------------------------------------------------

from .command import Command

from ..timer import Timer

class WaitUntilCommand(Command):
    """WaitUntilCommand - waits until an absolute game time.
    This will wait until the game clock reaches some value, then continue to
    the next command.
    """

    def __init__(self, time):
        super().__init__("WaitUntil(%s)" % time)
        self.time = time

    def isFinished(self):
        # Check if we've reached the actual finish time.
        return Timer.getMatchTime() >= self.time
