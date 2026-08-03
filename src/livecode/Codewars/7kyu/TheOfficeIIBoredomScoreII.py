def boredom(staff):
    scores = {
        'accounts': 1,
        'finance': 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25
    }

    total = 0
    for person, department in staff.items():
        total += scores.get(department, 0)

    if total <= 80:
        return 'kill me now'
    elif total < 100:
        return 'i can handle this'
    else:  
        return 'party time!!'
