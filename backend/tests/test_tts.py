import pytest
from app.services.text_to_speech import generate_speech, list_voices


def test_generate_speech():
    text = "Hello, this is a test."
    audio_content = generate_speech(text)

    assert isinstance(audio_content, bytes)
    assert len(audio_content) > 0


def test_generate_speech_with_language():
    text = "Bonjour, c'est un test."
    audio_content = generate_speech(
        text, language_code="fr-FR", voice_name="fr-FR-Standard-A"
    )

    assert isinstance(audio_content, bytes)
    assert len(audio_content) > 0


def test_generate_speech_invalid_input():
    with pytest.raises(Exception):
        generate_speech("")

    with pytest.raises(Exception):
        generate_speech("Hello", language_code="invalid-lang")


def test_list_voices():
    voices = list_voices()

    assert isinstance(voices, list)
    assert len(voices) > 0
    assert all(isinstance(voice, dict) for voice in voices)
    assert all("name" in voice and "language_codes" in voice for voice in voices)


def test_list_voices_with_language():
    language_code = "en-US"
    voices = list_voices(language_code)

    assert isinstance(voices, list)
    assert len(voices) > 0
    assert all(language_code in voice["language_codes"] for voice in voices)


@pytest.mark.parametrize(
    "text, language_code, voice_name",
    [
        ("Hello, world!", "en-US", "en-US-Standard-C"),
        ("Hola, mundo!", "es-ES", "es-ES-Standard-A"),
        ("Bonjour, le monde!", "fr-FR", "fr-FR-Standard-A"),
    ],
)
def test_various_languages(text, language_code, voice_name):
    audio_content = generate_speech(text, language_code, voice_name)

    assert isinstance(audio_content, bytes)
    assert len(audio_content) > 0
