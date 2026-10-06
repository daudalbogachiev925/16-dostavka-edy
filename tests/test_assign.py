from algorithms.assign_courier import assign

def test_assign_nearest():
    order = {'lat': 0, 'lon': 0}
    couriers = [
        {'id': 1, 'lat': 5, 'lon': 5, 'available': True},
        {'id': 2, 'lat': 1, 'lon': 1, 'available': True},
        {'id': 3, 'lat': 0.5, 'lon': 0.5, 'available': False},
    ]
    assert assign(order, couriers)['id'] == 2
