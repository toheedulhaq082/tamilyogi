from django.conf import settings

def genres_processor(request):
    # List of genres with corresponding TMDb IDs
    genre_data = [
        {'id': 28, 'name': 'action'},
        {'id': 53, 'name': 'thriller'},
        {'id': 80, 'name': 'crime'},
        {'id': 18, 'name': 'drama'},
        {'id': 10749, 'name': 'romance'},
        {'id': 35, 'name': 'comedy'},
        {'id': 12, 'name': 'adventure'},
        {'id': 16, 'name': 'animation'},
        {'id': 10751, 'name': 'family'},
        {'id': 14, 'name': 'fantasy'},
        {'id': 36, 'name': 'history'},
        {'id': 27, 'name': 'horror'},
        {'id': 10402, 'name': 'music'},
        {'id': 9648, 'name': 'mystery'},
        {'id': 878, 'name': 'science-fiction'},
        {'id': 10752, 'name': 'war'}
    ]
    return {'genres': genre_data}
