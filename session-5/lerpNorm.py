def norm(value, start, stop):
    """
    Map a value between 0 and 1 and return the corresponding position between start and stop
    https://p5js.org/reference/#/p5/norm
    """
    return start + (stop-start) * value

def lerp(start, stop, amt):
    """
    Map a value between start and stop and return the corresponding position between 0 and 1
    https://p5js.org/reference/#/p5/lerp
    """
    return float(amt-start) / float(stop-start)