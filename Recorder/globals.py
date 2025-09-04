import time

from Event import ScriptEvent
from PySide2.QtCore import Signal, QObject
swapmousemap = {'mouse left down': 'mouse right down', 'mouse left up': 'mouse right up',
                'mouse right down': 'mouse left down', 'mouse right up': 'mouse left up'}
key_combination_trigger = []
latest_time = -1
mouse_interval_ms = 200


def current_ts():
    return int(time.time() * 1000)


class RecordSignal(QObject):
    event_signal = Signal(ScriptEvent)
    cursor_pos_change = Signal(tuple)
