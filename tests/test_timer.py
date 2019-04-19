import time
from toolkit.managers import Timer


def test_timer():
    with Timer() as timer:
        time.sleep(1)

    assert timer.cost > 1
