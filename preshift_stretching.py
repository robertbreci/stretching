import streamlit as st
st.set_page_config(
    page_title="Pre-Shift Stretching",
    layout="wide",
)
st.title("Stretching Videos")

# Add your new functionality for Page 2 here
# List of YouTube video IDs
video_ids = [
    "KFcnspwkyLA",
    "Pd5ggr1bEqg",
    "yJgLmCqmNCo",
    "9wmWEaydbzk",
    "Cng_VaXD-w0",
    "00Ur64JL2ps",
    "WhiL_aaEdr8",
    "uPO-zST-7EE",
    "a9WC_eLmP30",
    "T9wBznkjcFM",
    "-0k_URgPpLI",
    "wC8gn-eqrDU",
    "zfzcfwwFxEI",
    "N9Ss6zm-Mg0",
    "EbDoQG91kpI",
    "i-cVdyo7wWk",
    "5OnHd1ZMtik",
    "AxwGqbSfDhI",
    "37tBZS7-E9k",
    "yKw9Pz0pE0c",
    "ZLFOUQZEWwk",
    "s9IB7Slo9KY",
    "QPa_xD7Kb1A"
]

# Create a layout for videos: 3 videos per row
num_columns = 3
num_rows = (len(video_ids) + num_columns - 1) // num_columns  # Calculate rows needed

for row in range(num_rows):
    cols = st.columns(num_columns)  # Create columns for the row
    for col in range(num_columns):
        video_index = row * num_columns + col
        if video_index < len(video_ids):  # Check if the video index is within the list
            video_id = video_ids[video_index]
            video_url = f"https://www.youtube.com/embed/{video_id}"
            video_html = f"""
            <iframe width="750" height="369" 
                    src="{video_url}" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen>
            </iframe>
            """
            # Display the video title
            cols[col].markdown(f"### # {video_index + 1}")  # Numbering starts from 1
            cols[col].markdown(video_html, unsafe_allow_html=True)  # Display the video in the column