# encoding: utf-8
# module ctre._ctre
# from C:\Users\Nolan\Documents\Robotics\python-frc-robot-architecture\venv\lib\site-packages\ctre\_ctre.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


class PigeonIMU_StickyFaults(__pybind11_builtins.pybind11_object):
    """ Sticky faults available to Pigeon """

    def hasAnyFault(self):  # real signature unknown; restored from __doc__
        """
        hasAnyFault(self: ctre._ctre.PigeonIMU_StickyFaults) -> bool
        
        
        
        :returns: true if any faults are tripped
        """
        return False

    def toBitfield(self):  # real signature unknown; restored from __doc__
        """
        toBitfield(self: ctre._ctre.PigeonIMU_StickyFaults) -> int
        
        
        
        :returns: Current fault list as a bit field
        """
        return 0

    def __init__(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        __init__(*args, **kwargs)
        Overloaded function.
        
        1. __init__(self: ctre._ctre.PigeonIMU_StickyFaults, bits: int) -> None
        
        Creates fault list with specified bit field of faults
        
        :param bits: bit field of faults to update with
        
        2. __init__(self: ctre._ctre.PigeonIMU_StickyFaults) -> None
        """
        pass
