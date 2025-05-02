from django.utils.text import slugify

action_movies = [
    {"id": 1, "title": "Amaran", "tmdb_id": 927342},
    {"id": 2, "title": "Good Bad Ugly", "tmdb_id": 1259024},
    {"id": 3, "title": "Veera Dheera Sooran: Part 2", "tmdb_id": 1198208-2},
    {"id": 4, "title": "Arunachalam", "tmdb_id": 66245},
    {"id": 5, "title": "Vidaamuyarchi", "tmdb_id": 949716},
    {"id": 6, "title": "Sivaji: The Boss", "tmdb_id": 24049},
    {"id": 7, "title": "Master", "tmdb_id": 626392},
    {"id": 8, "title": "Retro", "tmdb_id": 1265827},
    {"id": 9, "title": "Kadaikutty Singam", "tmdb_id": 498821},
    {"id": 10, "title": "Vikram", "tmdb_id": 743563},
    {"id": 11, "title": "Kaththi", "tmdb_id": 263475},
    {"id": 12, "title": "Kanguva", "tmdb_id": 622792},
    {"id": 13, "title": "Sarkar", "tmdb_id": 504231},
    {"title": "Jilla", "tmdb_id": 246087},
    {"title": "Captain Miller", "tmdb_id": 962074},
    {"title": "Saravana", "tmdb_id": 69625},
    {"title": "Maharaja", "tmdb_id": 1118224},
    {"title": "Leo", "tmdb_id": 949229},
    {"title": "Mankatha", "tmdb_id": 76788},
    {"title": "The Greatest of All Time", "tmdb_id": 1129608},
]

# Generate slugs for each movie
for movie in action_movies:
    movie["slug"] = slugify(movie["title"])
