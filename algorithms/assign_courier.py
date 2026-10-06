import math

def distance(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def assign(order, couriers):
    """Выбирает ближайшего свободного курьера."""
    best = None
    best_d = float('inf')
    for c in couriers:
        if not c['available']:
            continue
        d = distance((order['lat'], order['lon']), (c['lat'], c['lon']))
        if d < best_d:
            best_d, best = d, c
    return best
