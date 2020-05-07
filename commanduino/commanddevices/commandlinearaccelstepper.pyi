from typing import Optional
from . import CommandDevice
from ..lock import Lock
from ..commandhandler import GenericCommandHandler

class CommandLinearAccelStepper(CommandDevice):
    def __init__(self, speed: int, max_speed: int, acceleration: int, homing_speed: int,
                 enabled_acceleration: bool = True, reverted_direction: bool = False, reverted_switch: bool = False): ...
    def init(self) -> None: ...
    def set_all_params(self) -> None: ...
    cmdHdl: GenericCommandHandler
    def wait_until_idle(self) -> None: ...

    # Acceleration
    acceleration_lock: Lock
    def get_acceleration(self) -> float: ...
    def set_acceleration(self, steps_per_second_per_second: float) -> None: ...
    # Current position
    current_position_lock: Lock
    def get_current_position(self) -> float: ...
    def set_current_position(self, steps: float) -> None: ...
    # Distance to go
    distance_to_go_lock: Lock
    def get_distance_to_go(self) -> float: ...
    # Enabled acceleration
    enabled_acceleration: bool
    def enable_acceleration(self) -> None: ...
    def disable_acceleration(self) -> None: ...
    # Moving state
    moving_state_lock: Lock
    @property
    def is_moving(self) -> bool: ...
    def get_moving_state(self) -> bool: ...
    # Max speed
    max_speed_lock: Lock
    def get_max_speed(self) -> float: ...
    def set_max_speed(self, steps_per_second: float) -> None: ...
    # Speed
    # Ok so this might be confusing...
    # set_speed() sets the speed in the Arduino before actually moving the motor [e.g. in move(), move_to() or home()]
    # set_running_speed sets the value of the running_speed variable, used for set_speed before normal movements
    # set_homing_speed sets the value of the homing_speed variable, used for set_speed before homing movements in home()
    speed_lock: Lock
    def get_speed(self) -> float: ...
    def set_speed(self, steps_per_second: float) -> None: ...
    def set_running_speed(self, steps_per_second: int) -> None: ...
    def set_homing_speed(self, steps_per_second: int) -> None: ...

    def enable_revert_switch(self) -> None: ...
    def disable_revert_switch(self) -> None: ...
    def home(self, wait: bool = True) -> None: ...
    def move_to(self, steps: float, wait: bool = True) -> None: ...
    def move(self, steps: float, wait: bool = True): ...
    def stop(self, wait: bool = True) -> None: ...
# Dynamically generated
