# -*- coding: utf-8 -*-

from zope.interface import implementer
from zope.interface import Interface


class IBrowserLayer(Interface):
    """browser layer for the package"""


class ITriggerAutopublishingEvent(Interface):
    """Event to tirgger the Autobpublishing"""


@implementer(ITriggerAutopublishingEvent)
class TriggerAutopublishingEvent:
    """Event to tirgger the Autobpublishing"""

    def __init__(self, context):
        self.context = context
