import streamlit as st
import random
import pandas as pd
import numpy as np
import datetime
import sys
import ast

def highlight_closeness(guess_year, release_year):
    if guess_year is None:
        return ""
    
    release_year = pd.Timestamp(release_year).year
    guess_year = pd.Timestamp(guess_year).year
    
    arrow = "⬆️" if release_year > guess_year else "⬇️"
    
    if release_year == guess_year:
        return f"✅" 
    elif abs(release_year - guess_year) <= 3:
        return f"🔥 {arrow}" 
    else:
        return arrow

def display_globe(guessed_location, location):
    if guessed_location is None:
        return ""
    
    if full_country_dict[guessed_location] == full_country_dict[location]:
        return f"🌎"
    
    else:
        return ""
    
def highlight_first_letter(guessed_band, band):
    if guessed_band is None:
        return ""
    
    if str(guessed_band)[0].lower() == str(band)[0].lower():
        return f"🔠"
    
    else:
        return ""
    
def has_played_today():
    return None

DATASET = pd.read_csv('backend/BANDS.csv')
rng_df = pd.read_csv('backend/DAY_RESET.csv')
rng_dict = {str(i):j for i,j in zip(rng_df['date'].tolist(), rng_df['idx'].tolist())}
album_df = pd.read_csv('backend/ALBUMS.csv')
album_name_dict = {i:j for i,j in zip(album_df['artist'].tolist(), album_df['albums'].tolist())}
country_df = pd.read_csv('backend/COUNTRIES.csv')
full_country_dict = {i:j for i,j in zip(country_df['country'].tolist(), country_df['continents'].tolist())}

if "current_band" not in st.session_state:
    curr_date = str(pd.Timestamp.now().date())
    st.session_state.current_band = DATASET.iloc[rng_dict[curr_date]]
    st.session_state.attempts = []
    st.session_state.game_over = False

current_band = st.session_state.current_band
artist_name = current_band["name"]
artist_name = artist_name
location = current_band["location"]
start_year = current_band['form_date']
release_date_1 = current_band["release_1"]
release_date_2 = current_band["release_2"]
release_date_3 = current_band["release_3"]
release_date_4 = current_band["release_4"]

st.title("🎸 Rock Riddle 🎶")
st.write("Guess the rock band based on the form date, and album release dates provided. You have a total of 7 guesses. The 4 albums are the first studio albums they released.")
st.write("")
st.write("🔥 : you are within 3 years of that album release year, or band formed year")
st.write("✅ : album was released that year, or band was formed that year")
st.write("⬆️ : your guess is lower than that release year, or band formed year")
st.write("⬇️ : your guess is higher than that release year, or band formed year")
st.write("🌎 : your guess is in the correct continent")
st.write("🔠: your guess starts with the same letter as the correct band")
st.write("")

if st.button("Click to view one of this band's albums. Clicking several times reveals more albums."):
    albums = ast.literal_eval(album_name_dict[artist_name])
    random_album = random.choice(albums)
    st.write(f"Hint: {random_album}")

if not st.session_state.game_over:
    guess = st.selectbox(
        "Select your guess:",
        options=[""] + DATASET["name"].tolist(), 
    )

    if st.button("Submit Guess"):
        if not guess:
            st.warning("Please enter a guess!")
        elif len(st.session_state.attempts) < 7:
            st.session_state.attempts.append({
                "guess": guess,
                "correct": guess.lower() == artist_name.lower(),
            })
            
            if guess.lower() == artist_name.lower():
                st.success(f"🎉 Correct! The band is {artist_name}!")
                st.session_state.game_over = True
            elif len(st.session_state.attempts) == 7:
                st.error(f"Game Over! The correct band was {artist_name}.")
                st.session_state.game_over = True
        else:
            st.error(f"Game Over! The correct band was {artist_name}.")
            st.session_state.game_over = True

if st.session_state.attempts:
    st.subheader("Your Guesses")
    rows = []
    for attempt in st.session_state.attempts:

        guessed_band = DATASET[DATASET["name"].str.lower() == attempt["guess"].lower()]
        if not guessed_band.empty:
            guessed_band = guessed_band.iloc[0]
            rows.append({
                "Artist": f"{guessed_band['name']} {highlight_first_letter(guessed_band['name'], artist_name)}",
                "Location": guessed_band["location"].replace("\n", " "),
                "Location": f"{guessed_band['location']} {display_globe(guessed_band['location'], location)}",
                "Date Formed": f"{guessed_band['form_date']} {highlight_closeness(guessed_band['form_date'], start_year)}",
                "Album 1": f"{guessed_band['release_1']} {highlight_closeness(guessed_band['release_1'], release_date_1)}",
                "Album 2": f"{guessed_band['release_2']} {highlight_closeness(guessed_band['release_2'], release_date_2)}",
                "Album 3": f"{guessed_band['release_3']} {highlight_closeness(guessed_band['release_3'], release_date_3)}",
                "Album 4": f"{guessed_band['release_4']} {highlight_closeness(guessed_band['release_4'], release_date_4)}",
        
        "Correct?": "✅" if attempt["correct"] else "❌",
                "Correct?": "✅" if attempt["correct"] else "❌"
            })
        else:

            rows.append({
                "Artist": attempt["guess"],
                "Location": "Unknown",
                "Release Year 1": "Unknown",
                "Release Year 2": "Unknown",
                "Release Year 3": "Unknown",
                "Release Year 4": "Unknown",
                "Correct?": "❌",
            })

    st.table(rows)

if st.session_state.game_over:
    if st.button("Play Again"):
        curr_date = str(pd.Timestamp.now().date())
        st.session_state.current_band = DATASET.iloc[rng_dict[curr_date]]
        st.session_state.attempts = []
        st.session_state.game_over = False

st.markdown("---") 
st.markdown("For my Dad, Christmas 2024")
st.markdown("Created by Ben Stager, 2024 (https://github.com/benstager)")