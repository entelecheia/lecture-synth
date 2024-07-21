import pytest
from app.services.lecture_generator import generate_lecture_and_slides


def test_generate_lecture_and_slides():
    topic = "Artificial Intelligence"
    duration = 10

    result = generate_lecture_and_slides(topic, duration)

    assert isinstance(result, dict)
    assert "lecture" in result
    assert "slides" in result
    assert isinstance(result["lecture"], str)
    assert isinstance(result["slides"], list)
    assert len(result["slides"]) > 0
    assert all(isinstance(slide, list) for slide in result["slides"])


def test_generate_lecture_content():
    topic = "Climate Change"
    duration = 15

    result = generate_lecture_and_slides(topic, duration)

    assert topic.lower() in result["lecture"].lower()
    assert (
        len(result["lecture"].split()) >= duration * 100
    )  # Assuming ~100 words per minute


def test_generate_slides_content():
    topic = "Quantum Computing"
    duration = 20

    result = generate_lecture_and_slides(topic, duration)

    assert len(result["slides"]) >= 3  # At least introduction, body, and conclusion
    assert all(
        len(slide) >= 2 for slide in result["slides"]
    )  # Each slide should have a title and at least one point


def test_invalid_input():
    with pytest.raises(Exception):
        generate_lecture_and_slides("", 0)

    with pytest.raises(Exception):
        generate_lecture_and_slides("Topic", -5)


@pytest.mark.parametrize(
    "topic, duration",
    [("Machine Learning", 5), ("Renewable Energy", 30), ("Space Exploration", 45)],
)
def test_various_topics_and_durations(topic, duration):
    result = generate_lecture_and_slides(topic, duration)

    assert isinstance(result, dict)
    assert "lecture" in result
    assert "slides" in result
    assert len(result["lecture"]) > 0
    assert len(result["slides"]) > 0
