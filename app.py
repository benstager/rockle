import streamlit as st
import random
import pandas as pd

# Load your dataset (artist, location, release dates)
DATASET = pd.read_csv('band_unit_test.csv')

# Initialize game state
if "current_band" not in st.session_state:
    st.session_state.current_band = DATASET.head(1)
    st.session_state.attempts = []
    st.session_state.game_over = False

current_band = st.session_state.current_band
artist_name = current_band["name"]
artist_name = artist_name.values[0]
location = current_band["location"]
start_year = current_band['form_date']
release_date_1 = current_band["release_1"]
release_date_2 = current_band["release_2"]
release_date_3 = current_band["release_3"]
release_date_4 = current_band["release_4"]

# Game Title
st.title("Rockle! (Merry Christmas Dad.)")
st.write("Guess the rock band based on the hints provided.")
st.write("🔥 = you are within 3 years of that album, ✅ = album was released that year")

# Input for guesses
if not st.session_state.game_over:
    guess = st.selectbox(
        "Select your guess:",
        options=[""] + DATASET["name"].tolist(),  # Add an empty option for default
    )

    if st.button("Submit Guess"):
        if not guess:
            st.warning("Please enter a guess!")
        elif len(st.session_state.attempts) < 7:
            # Append guess to attempts
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

# Show previous guesses as a table
# Display rows as a table with all guesses, showing the correct/incorrect status
if st.session_state.attempts:
    st.subheader("Your Guesses")

    # Prepare rows to display
    rows = []
    for attempt in st.session_state.attempts:
        # Locate the guessed band in the DataFrame (case-insensitive)
        guessed_band = DATASET[DATASET["name"].str.lower() == attempt["guess"].lower()]
        if not guessed_band.empty:
            guessed_band = guessed_band.iloc[0]
            rows.append({
                "Artist": guessed_band["name"],
                "Location": guessed_band["location"],
                "Release Year 1": f"{guessed_band['release_1']} {'✅' if guessed_band['release_1'] == release_date_1.values[0] else '🔥' if abs(pd.Timestamp(guessed_band['release_1']).year - pd.Timestamp(release_date_1.values[0]).year) <= 3 else ''}",
                "Release Year 2": f"{guessed_band['release_2']} {'✅' if guessed_band['release_2'] == release_date_2.values[0] else '🔥' if abs(pd.Timestamp(guessed_band['release_2']).year - pd.Timestamp(release_date_2.values[0]).year) <= 3 else ''}",
                "Release Year 3": f"{guessed_band['release_3']} {'✅' if guessed_band['release_3'] == release_date_3.values[0] else '🔥' if abs(pd.Timestamp(guessed_band['release_3']).year - pd.Timestamp(release_date_3.values[0]).year) <= 3 else ''}",
                "Release Year 4": f"{guessed_band['release_4']} {'✅' if guessed_band['release_4'] == release_date_4.values[0] else '🔥' if abs(pd.Timestamp(guessed_band['release_4']).year - pd.Timestamp(release_date_4.values[0]).year) <= 3 else ''}",
                "Correct?": "✅" if attempt["correct"] else "❌"
            })
        else:
            # Add the guessed data even if the band is not in the DataFrame
            rows.append({
                "Artist": attempt["guess"],
                "Location": "Unknown",
                "Release Year 1": "Unknown",
                "Release Year 2": "Unknown",
                "Release Year 3": "Unknown",
                "Release Year 4": "Unknown",
                "Correct?": "❌",
            })

    # Display the table
    st.table(rows)
# Play again button
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.current_band = random.choice(DATASET)
        st.session_state.attempts = []
        st.session_state.game_over = False