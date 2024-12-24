import streamlit as st
import random
import pandas as pd
import numpy as np
import datetime
from reset_day import rng_dict

DATASET = pd.read_csv('band_unit_test.csv')

if "current_band" not in st.session_state:
    curr_date = pd.Timestamp.now().date()
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

st.title("Rock Riddle! (Merry Christmas Dad.)")
st.write("Guess the rock band based on the hints provided.")
st.write("You have a total of 7 guesses.")
st.write("🔥 : you are within 3 years of that album release year, or band form date")
st.write("✅ : album was released that year, or band was formed that year")
st.write("A game made by Ben Stager (Christmas 2024)")

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
        # Locate the guessed band in the DataFrame (case-insensitive)
        guessed_band = DATASET[DATASET["name"].str.lower() == attempt["guess"].lower()]
        if not guessed_band.empty:
            guessed_band = guessed_band.iloc[0]
            rows.append({
                "Artist": guessed_band["name"],
                "Location": guessed_band["location"],
                "Date Formed": f"{guessed_band['form_date']} {'✅' if pd.Timestamp(guessed_band['form_date']).year == pd.Timestamp(start_year).year else '🔥' if abs(pd.Timestamp(guessed_band['form_date']).year - pd.Timestamp(start_year).year) <= 3 else ''}",
                "Release Year 1": f"{guessed_band['release_1']} {'✅' if pd.Timestamp(guessed_band['release_1']).year == pd.Timestamp(release_date_1).year else '🔥' if abs(pd.Timestamp(guessed_band['release_1']).year - pd.Timestamp(release_date_1).year) <= 3 else ''}",
                "Release Year 2": f"{guessed_band['release_2']} {'✅' if pd.Timestamp(guessed_band['release_2']).year == pd.Timestamp(release_date_2).year else '🔥' if abs(pd.Timestamp(guessed_band['release_2']).year - pd.Timestamp(release_date_2).year) <= 3 else ''}",
                "Release Year 3": f"{guessed_band['release_3']} {'✅' if pd.Timestamp(guessed_band['release_3']).year == pd.Timestamp(release_date_3).year else '🔥' if abs(pd.Timestamp(guessed_band['release_3']).year - pd.Timestamp(release_date_3).year) <= 3 else ''}",
                "Release Year 4": f"{guessed_band['release_4']} {'✅' if pd.Timestamp(guessed_band['release_4']).year == pd.Timestamp(release_date_4).year else '🔥' if abs(pd.Timestamp(guessed_band['release_4']).year - pd.Timestamp(release_date_4).year) <= 3 else ''}",
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
        st.session_state.current_band = DATASET.iloc[rng_dict[curr_date]]
        st.session_state.attempts = []
        st.session_state.game_over = False