from django.conf import settings

def genres_processor(request):
    # List of genres with corresponding TMDb IDs
    genre_data = [
        {'id': 28, 'name': 'Action'},
        {'id': 53, 'name': 'Thriller'},
        {'id': 80, 'name': 'Crime'},
        {'id': 18, 'name': 'Drama'},
        {'id': 10749, 'name': 'Romance'},
        {'id': 35, 'name': 'Comedy'},
        {'id': 12, 'name': 'Adventure'},
        {'id': 16, 'name': 'Animation'},
        {'id': 10751, 'name': 'Family'},
        {'id': 14, 'name': 'Fantasy'},
        {'id': 36, 'name': 'History'},
        {'id': 27, 'name': 'Horror'},
        {'id': 10402, 'name': 'Music'},
        {'id': 9648, 'name': 'Mystery'},
        {'id': 878, 'name': 'Science-Fiction'},
        {'id': 10752, 'name': 'War'}
    ]
    return {'genres': genre_data}
