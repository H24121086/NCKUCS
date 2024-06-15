import csv

# Load and inspect the data
file_path = '/mnt/data/IMDB-Movie-Data.csv'

def load_data(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data

data = load_data(file_path)

# Display the first few rows to understand the structure
data[:5]


def top_3_movies_2016(data):
    movies_2016 = [movie for movie in data if movie['Year'] == '2016']
    top_3 = sorted(movies_2016, key=lambda x: float(x['Rating']), reverse=True)[:3]
    for i, movie in enumerate(top_3, 1):
        print(f"Top {i} movie in 2016: {movie['Title']} with a rating of {movie['Rating']}")

top_3_movies_2016(data)


def most_involved_director(data):
    director_count = {}
    for movie in data:
        director = movie['Director']
        if director in director_count:
            director_count[director] += 1
        else:
            director_count[director] = 1
    top_director = max(director_count, key=director_count.get)
    print(f"The director involved in the most movies: {top_director} with {director_count[top_director]} movies")

most_involved_director(data)


def highest_revenue_actor(data):
    actor_revenue = {}
    for movie in data:
        if movie['Revenue (Millions)']:
            revenue = float(movie['Revenue (Millions)'])
            actors = movie['Actors'].split('|')
            for actor in actors:
                actor = actor.strip()
                if actor in actor_revenue:
                    actor_revenue[actor] += revenue
                else:
                    actor_revenue[actor] = revenue
    top_actor = max(actor_revenue, key=actor_revenue.get)
    print(f"The actor generating the highest total revenue: {top_actor} with ${actor_revenue[top_actor]:.2f} million")

highest_revenue_actor(data)

def average_rating_emma_watson(data):
    total_rating = 0
    count = 0
    for movie in data:
        if 'Emma Watson' in movie['Actors']:
            total_rating += float(movie['Rating'])
            count += 1
    average_rating = total_rating / count if count > 0 else 0
    print(f"The average rating of Emma Watson's movies: {average_rating:.2f}")

average_rating_emma_watson(data)

def top_4_actors(data, top_n=4):
    actor_count = {}
    for movie in data:
        actors = movie['Actors'].split('|')
        for actor in actors:
            actor = actor.strip()
            if actor in actor_count:
                actor_count[actor] += 1
            else:
                actor_count[actor] = 1
    top_actors = sorted(actor_count.items(), key=lambda x: x[1], reverse=True)[:top_n]
    for i, (actor, count) in enumerate(top_actors, 1):
        print(f"Top {i} actor: {actor} with {count} movies")

top_4_actors(data)

def top_7_collaborations(data, top_n=7):
    collaborations = {}
    for movie in data:
        director = movie['Director']
        actors = movie['Actors'].split('|')
        for actor in actors:
            actor = actor.strip()
            pair = (director, actor)
            if pair in collaborations:
                collaborations[pair] += 1
            else:
                collaborations[pair] = 1
    top_collaborations = sorted(collaborations.items(), key=lambda x: x[1], reverse=True)[:top_n]
    for i, ((director, actor), count) in enumerate(top_collaborations, 1):
        print(f"Top {i} collaboration: Director {director} & Actor {actor} with {count} collaborations")

top_7_collaborations(data)

def top_3_directors_with_most_actors(data, top_n=3):
    director_actors = {}
    for movie in data:
        director = movie['Director']
        actors = movie['Actors'].split('|')
        if director not in director_actors:
            director_actors[director] = set()
        for actor in actors:
            actor = actor.strip()
            director_actors[director].add(actor)
    director_actors_count = {director: len(actors) for director, actors in director_actors.items()}
    top_directors = sorted(director_actors_count.items(), key=lambda x: x[1], reverse=True)[:top_n]
    for i, (director, count) in enumerate(top_directors, 1):
        print(f"Top {i} director: {director} collaborating with {count} actors")

top_3_directors_with_most_actors(data)

def top_6_actors_in_genres(data, top_n=6):
    actor_genres = {}
    for movie in data:
        genres = movie['Genre'].split('|')
        actors = movie['Actors'].split('|')
        for actor in actors:
            actor = actor.strip()
            if actor not in actor_genres:
                actor_genres[actor] = set()
            for genre in genres:
                genre = genre.strip()
                actor_genres[actor].add(genre)
    actor_genre_count = {actor: len(genres) for actor, genres in actor_genres.items()}
    top_actors = sorted(actor_genre_count.items(), key=lambda x: x[1], reverse=True)[:top_n]
    for i, (actor, count) in enumerate(top_actors, 1):
        print(f"Top {i} actor: {actor} playing in {count} genres")

top_6_actors_in_genres(data)

def top_3_actors_max_year_gap(data, top_n=3):
    actor_years = {}
    for movie in data:
        year = int(movie['Year'])
        actors = movie['Actors'].split('|')
        for actor in actors:
            actor = actor.strip()
            if actor not in actor_years:
                actor_years[actor] = []
            actor_years[actor].append(year)
    actor_max_gaps = {}
    for actor, years in actor_years.items():
        if len(years) > 1:
            max_gap = max(years) - min(years)
            actor_max_gaps[actor] = max_gap
    top_actors = sorted(actor_max_gaps.items(), key=lambda x: x[1], reverse=True)[:top_n]
    for i, (actor, gap) in enumerate(top_actors, 1):
        print(f"Top {i} actor: {actor} with a maximum year gap of {gap}")

top_3_actors_max_year_gap(data)

