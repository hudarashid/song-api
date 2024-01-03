from fastapi import FastAPI

app = FastAPI()

data = {
    "song": {
        "title": "Good Day",
        "artist": "IU",
        "release_date": "December 09, 2010",
        "genre": "K-pop",
        "album": "Real",
        "duration": "3:53",
        "language": "Korean",
    },
    "singer": {
        "name": "IU",
        "birth_date": "May 16, 1993",
        "birth_place": "Songjeong-dong, Seoul",
        "debut_year": 2008,
        "active_years": "2008-present",
        "genres": ["K-pop", "R&B", "soul"],
    },
}


@app.get("/songsinger")
def sample_data():
    return data
