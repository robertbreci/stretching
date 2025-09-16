import streamlit as st
st.set_page_config(
    page_title="Pre-Shift Stretching",
    layout="wide",
)
st.title("Stretching Videos")

# Add your new functionality for Page 2 here
# List of YouTube video IDs
video_ids = [
    "KFcnspwkyLA",  # Video 1
    "Pd5ggr1bEqg",  # Video 2
    "yJgLmCqmNCo",  # Video 3
    "9wmWEaydbzk",  # Video 4
    "Cng_VaXD-w0",  # Video 5
    "00Ur64JL2ps",  # Video 6
    "WhiL_aaEdr8",  # Video 7
    "uPO-zST-7EE",  # Video 8
    "a9WC_eLmP30",  # Video 9
    "T9wBznkjcFM",  # Video 10
    "-0k_URgPpLI",  # Video 11
    "wC8gn-eqrDU",  # Video 12
    "zfzcfwwFxEI",  # Video 13
    "N9Ss6zm-Mg0",  # Video 14
    "EbDoQG91kpI"   # Video 15
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