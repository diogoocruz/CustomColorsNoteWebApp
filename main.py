import streamlit as st
import json

st.set_page_config(
    page_title="CustomColorNotes Color Picker",
    page_icon="🎶"
)

st.title("🎶 CustomColorNotes Color Picker for MuseScore Studio 4")
st.text("Easily create a custom color file for the CustomColorNotes plugin for MuseScore Studio!")
st.text("Select a color for each note or start with a template, and download your customized color palette.")

colors_notes = {
    "C": "#00f900",
    "C#/Db": "#00f900",
    "D": "#00f900",
    "D#/Eb": "#00f900",
    "E": "#00f900",
    "F": "#00f900",
    "F#/Gb": "#00f900",
    "G": "#00f900",
    "G#/Ab": "#00f900",
    "A": "#00f900",
    "A#/Bb": "#00f900",
    "B": "#00f900"
}

with open("color_palettes.json") as f:
    color_palettes = json.load(f)

def apply_palette(palette):
    for key in colors_notes:
        colors_notes[key] = palette[key]

selected_palette = st.selectbox(
    "Select a color template to start with:",
    options=list(color_palettes.keys())
)

if selected_palette:
    apply_palette(color_palettes[selected_palette])

for key in colors_notes:
    colors_notes[key] = st.color_picker(f"Choose color for {key}", colors_notes[key])

formatted_text = "\n".join(f"{note}: {color}" for note, color in colors_notes.items())

st.download_button(
    label="Download Color File",
    data=formatted_text,
    file_name="colors.txt",
    mime="text/plain"
)

st.markdown("*Made by: [diogoocruz](https://github.com/diogoocruz)*")
