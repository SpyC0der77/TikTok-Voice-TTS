from clackpy import text, select
from tiktok_voice import tts, Voice


# Prompt for text input
input_text = text("What should I say?")
if not input_text:
    print("No text entered.")
    exit()

# Prompt for voice selection with hints
voice_key = select(
    "Select a voice:",
    options=[
        {"value": "US_FEMALE_1", "label": "US_FEMALE_1", "hint": "Default female voice"},
        {"value": "US_FEMALE_2", "label": "US_FEMALE_2", "hint": "Alternative female voice"},
        {"value": "US_MALE_1", "label": "US_MALE_1", "hint": "Clear male voice"},
        {"value": "US_MALE_2", "label": "US_MALE_2", "hint": "Warm male voice"},
        {"value": "US_MALE_3", "label": "US_MALE_3", "hint": "Energetic male voice"},
        {"value": "US_MALE_4", "label": "US_MALE_4", "hint": "Deep male voice"},
    ],
    initial_value="US_FEMALE_1"
)

# Convert to Voice enum
voice = getattr(Voice, voice_key)

# Generate and play audio
tts(input_text, voice, "output.mp3", play_sound=True)
