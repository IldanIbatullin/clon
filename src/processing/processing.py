def filter_by_state(data, state='EXECUTED'):
    return [item for item in data if item.get('state') == state]
def sort_by_date(data, reverse=False):
    return sorted(data, key=lambda x: x['date'], reverse=reverse)