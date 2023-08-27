import time


def make_readable(seconds=0):
    hour = seconds // 3600
    minute = (seconds % 3600) // 60
    second = seconds % 60
    return "%02d:%02d:%02d" % (hour, minute, second)


assert (make_readable() == "00:00:00")
assert (make_readable(5) == "00:00:05")
assert (make_readable(60) == "00:01:00")
assert (make_readable(86399) == "23:59:59")
assert (make_readable(359999) == "99:59:59")

print("Processed successfully")
