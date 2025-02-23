import pandas as pd
import datetime 
import musicbrainzngs as music
import numpy as np
import sys

sys.path.append("/Users/benstager/Desktop/rock riddle/data")

music.set_useragent("Rock-Riddle", "1.0", "bstager@tulane.edu")

additional_bands = [
    "38 Special", "A Flock of Seagulls", "Accept", "Adrian Belew", "Aldo Nova", "Alphaville", "Ambrosia", 
    "Angel", "April Wine", "Argent", "Atomic Rooster", "Babyshambles", "Bananarama", "Barclay James Harvest", 
    "Big Audio Dynamite", "Black Oak Arkansas", "Blodwyn Pig", "Bloodrock", "Bonzo Dog Doo-Dah Band", 
    "Booker T. & the M.G.'s", "Brownsville Station", "Budgie", "Captain Beefheart", "Canned Heat", 
    "Chicory Tip", "City Boy", "Climax Blues Band", "Conway Twitty", "Country Joe and the Fish", 
    "Crack the Sky", "Crazy Horse", "Cursive", "David Crosby", "Dennis DeYoung", "Devil Doll", 
    "Diesel", "Dr. Feelgood", "Electric Prunes", "Elvis Costello and the Attractions", "Eric Burdon", 
    "Family", "Fanny", "Focus", "Foghat", "Franz Ferdinand", "Giant Sand", "Golden Earring", 
    "Graham Parker", "Green On Red", "Gypsy", "Haircut One Hundred", "Hawkwind", "Head East", 
    "Heaven 17", "Herman's Hermits", "Ian Dury", "It Bites", "Jefferson Starship", "Jo Jo Gunne", 
    "Johnny Hates Jazz", "Johnny Winter", "Kayak", "Klaatu", "Krokus", "Lighthouse", "Little River Band", 
    "Long John Baldry", "Love Sculpture", "Magazine", "Mahogany Rush", "Man", "Manic Street Preachers", 
    "Marble Arch", "Max Webster", "MC5", "Moby Grape", "Morcheeba", "Mother Love Bone", 
    "Murray Head", "Nantucket", "Nash the Slash", "Nazareth", "Nektar", "Nils Lofgren", 
    "Norman Greenbaum", "Outlaws", "Ozzy Osbourne", "Pale Saints", "Paul Revere & the Raiders", 
    "Pentangle", "Peter Green", "Pigbag", "Player", "Point Blank", "Poco", "Porcupine Tree", 
    "Portishead", "Pretty Things", "Quicksilver Messenger Service", "Renaissance", "Riot", 
    "Riverside", "Ritchie Blackmore's Rainbow", "Robin Trower", "Roger Hodgson", "Rory Gallagher", 
    "Screaming Jets", "Sensational Alex Harvey Band", "Severed Heads", "Shooting Star", "Shriekback", 
    "Siren", "Soft Machine", "Southside Johnny & the Asbury Jukes", "Spiral Starecase", "Spirit", 
    "Spooky Tooth", "Stackridge", "Stan Ridgway", "Starcastle", "Starsailor", "Steeleye Span", 
    "Strawbs", "Streetheart", "Strife", "Suede", "Super Furry Animals", "Swervedriver", 
    "Sweet", "Tangerine Dream", "Tavares", "Taxxi", "Ten Years After", "The Alarm", "The Amboy Dukes", 
    "The Band", "The Big Dish", "The Cramps", "The Cryan' Shames", "The Dictators", 
    "The Fugs", "The Hollies", "The Incredible String Band", "The Jayhawks", "The Knack", 
    "The La's", "The Mars Volta", "The Nice", "The Psychedelic Furs", "The Saints", 
    "The Shadows", "The Spencer Davis Group", "The Stooges", "The Tea Party", "The The", 
    "The Turtles", "The Vapors", "The Yardbirds", "Thin White Rope", "Thunderclap Newman", 
    "Tommy Tutone", "Tony Joe White", "Traffic", "Triumph", "Trooper", "U.K.", "Ultimate Spinach", 
    "Vanilla Fudge", "Wall of Voodoo", "Wanda Jackson", "Wang Chung", "Wet Willie", "Wishbone Ash", 
    "Wolfmother", "X-Ray Spex", "Y&T", "Yellow Magic Orchestra", "Zebra", "Zero 7", 
    "Ziggy Marley", "Zounds", "Zwan", "Autograph", "Baltimora", "Barenaked Ladies", 
    "Be Bop Deluxe", "Bill Bruford", "Billy Thorpe", "Blitzen Trapper", "Blue Cheer", 
    "Blue Mink", "Boomtown Rats", "Brendan Benson", "Bruce Hornsby", "Calexico", "Chris Isaak", 
    "Clannad", "Commander Cody and His Lost Planet Airmen", "Coven", "Crack the Sky", 
    "Crosby & Nash", "Damnation of Adam Blessing", "Dan Hicks", "Danny Kirwan", "David Lindley", 
    "David Sylvian", "Delaney & Bonnie", "Dixie Dregs", "Donovan", "Doug Sahm", "Dr. Hook", 
    "Earth Opera", "Emitt Rhodes", "England Dan & John Ford Coley", "Fairport Convention", 
    "Flying Burrito Brothers", "Fotheringay", "Gabriel Bondage", "Gentle Giant", 
    "Gerry Rafferty", "Godley & Creme", "Gordon Lightfoot", "Grand Funk Railroad", 
    "Hedgehoppers Anonymous", "Horace Silver", "Ian Hunter", "Iggy Pop", "Jellyfish", 
    "John Cale", "John Mayall's Bluesbreakers", "Johnny Thunder", "Jon and Vangelis", 
    "Junior's Eyes", "Keef Hartley Band", "Kevin Ayers", "Laurie Anderson", "Leo Kottke", 
    "Leslie West", "Lindisfarne", "Loggins and Messina", "Marc Bolan", "Matching Mole", 
    "Michael Nesmith", "Mike Oldfield", "Minutemen", "Moby Grape", "Neil Innes", 
    "Nico", "Nick Drake", "NRBQ", "Os Mutantes", "Pavlov's Dog", "Pentangle", 
    "Peter Gabriel", "Peter, Paul and Mary", "Procol Harum", "Quintessence", 
    "Robin Williamson", "Roger Waters", "Sandy Denny", "Savoy Brown", "Seatrain", 
    "Shane MacGowan", "Sky", "Soft Boys", "Sons of Champlin", "Spirit", "Stackridge", 
    "Steeleye Span", "Steve Hackett", "Steve Hillage", "String Driven Thing", "T. Rex", 
    "Television", "The Band", "The Chambers Brothers", "The Dead Boys", "The Electric Flag"
]

def create_cleaned_artist(artist_name):
    try:
        artist_high_level = music.get_artist_by_id(music.search_artists(artist= artist_name)['artist-list'][0]['id'])['artist']
        first_albums = music.browse_release_groups(music.search_artists(artist=artist_name)['artist-list'][0]['id'], release_type=["album"])['release-group-list']
        try:
            start_band_date = music.search_artists(artist=artist_name)['artist-list'][0]['life-span']['begin']
        except:
            return None

        name = artist_name
        begin_date = pd.Timestamp(start_band_date).date()
        area = artist_high_level['area']['name']
        albums = []

        album_name = []
        release_date = []

        for album in first_albums:
            if len(album['first-release-date']) > 0:
                album_name.append(album['title'])
                release_date.append(album['first-release-date'])
            
        
        date_name_frame = pd.DataFrame({'albums':album_name, 'date':release_date}).sort_values('date')
        first_four_years = date_name_frame['date'].apply(lambda x: pd.Timestamp(x).date()).values[:4]

        final_dict = {
            'name':artist_name,
            'form_date':begin_date,
            'location':area,
            'release_1':first_four_years[0],
            'release_2':first_four_years[1],
            'release_3':first_four_years[2],
            'release_4':first_four_years[3]
        }

        return pd.DataFrame(final_dict,index=[0])
    
    except:
        print(f'FAILED: {artist_name}')
        return None

def create_album_dict(artist_name):
    try:
        artist_high_level = music.get_artist_by_id(music.search_artists(artist= artist_name)['artist-list'][0]['id'])['artist']
        first_albums = music.browse_release_groups(music.search_artists(artist=artist_name)['artist-list'][0]['id'], release_type=["album"])['release-group-list']
        start_band_date = music.search_artists(artist=artist_name)['artist-list'][0]['life-span']['begin']

        name = artist_name
        begin_date = pd.Timestamp(start_band_date).date()
        area = artist_high_level['area']['name']

        album_name = []
        release_date = []

        for album in first_albums:
            album_name.append(album['title'])
            release_date.append(album['first-release-date'])

        album_name = [i for i in album_name if artist_name not in i]
        albums = {artist_name:album_name}

        return albums
    
    except:
        print(f'FAILED: {artist_name}')
        return None

def update_backend(n_updates=5):
    try:
        # 1. update bands
        data = pd.read_csv('band_unit_test.csv')
        current_bands = data['name'].unique()
        bands_to_update = np.setdiff1d(additional_bands, current_bands)[:n_updates]

        bands_cleaned = [create_cleaned_artist(artist_name=artist) for artist in bands_to_update]
        bands_cleaned = pd.concat([i for i in bands_cleaned if i is not None])
        cleaned_artists = bands_cleaned['name'].unique()

        update = pd.concat([data, bands_cleaned])
        update.to_csv('~/Desktop/rock riddle/BANDS.csv', index=False)
        
        # 2. update albums
        albums_existing = pd.read_csv('~/Desktop/rock riddle/backend/ALBUMS.csv')
        album_frames = []
        for artist in cleaned_artists:
            try:
                album_data = create_album_dict(artist_name=artist)
                album_frame = pd.DataFrame({
                    'artist': list(album_data.keys())[0],
                    'albums': list(album_data.values())
                })
            except:
                album_frame = None
            
            album_frames.append(album_frame)
        
        album_frames = pd.concat([frame for frame in album_frames if frame is not None])

        albums_final = pd.concat([albums_existing, album_frames])
        albums_final.to_csv('~/Desktop/rock riddle/backend/ALBUMS.csv', index=False)

        # 3. update day indices 
        existing_days = pd.read_csv('~/Desktop/rock riddle/backend/DAY_RESET.csv')
        final_day = existing_days['date'].values[-1]
        range_dates = pd.date_range(
            start=(pd.Timestamp(final_day).date() + pd.DateOffset(days=1)), end=(pd.Timestamp(final_day).date() + pd.DateOffset(days=album_frames.shape[0])).date(), freq='D')
        
        arr = np.array(range(existing_days.shape[0] + 1, existing_days.shape[0] + album_frames.shape[0] + 1))

        np.random.shuffle(arr)

        new_days = pd.DataFrame({
            'date': [str(date.date()) for date in range_dates],
            'idx': arr
        })

        final_days = pd.concat([existing_days, new_days])

        final_days.to_csv('~/Desktop/rock riddle/backend/DAY_RESET.csv', index=False)

        return final_days.sort_values('date')

    except Exception as e:
        print(f"BACKEND UPDATE FAILED: {e}")
        raise

if __name__ == "__main__":
    
    updates = 5
    try: 
        update_backend(n_updates=updates)
    except Exception as error:
        print(f"UPDATE FAILED: {error}")