import logging as log

from abc import ABC, abstractmethod
from profile import TwitterProfile


class State(ABC):
    """
    class to define a state object.
    """

    def __init__(self):
        print('Processing current state:', str(self))

    @abstractmethod
    def on_event(self, event):
        """
        Handle events that are delegated to this State.
        """
        pass

    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__


class BullishState(State):
    """
    Indicates Bitcoin is Bullish
    """

    def __init__(self):
        super().__init__()
        profile = TwitterProfile()
        profile.setBullishProfileStatus()
        log.debug('Bullish State Initialized')

    def on_event(self, asset_percent_change):
        if asset_percent_change <= 0:
            log.debug('BullishState Event Triggered')
            return BearishState()

        return self


class BearishState(State):
    """
    Indicates Bitcoin is Bearish
    """

    def __init__(self):
        super().__init__()
        profile = TwitterProfile()
        profile.setBearishProfileStatus()
        log.debug('Bearish State Initialized')

    def on_event(self, bitcoin_percent_change):
        if bitcoin_percent_change > 0:
            log.debug('BearishState Event Triggered')
            return BullishState()
        return self


class ProfileStateSwap:

    def __init__(self, bitcoin_percent_change):
        if bitcoin_percent_change > 0:
            self.state = BullishState()
        else:
            self.state = BearishState()

    def on_event(self, event):
        self.state = self.state.on_event(event)
