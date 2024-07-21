"""
This module provides functionality for generating lectures and accompanying slides using OpenAI's language model.

It utilizes the LangChain library to create a chain that processes a prompt template
with input variables for the lecture topic and duration. The generated content includes
a full lecture and a set of slides summarizing the main points.

Functions:
    generate_lecture_and_slides: Generates a lecture and slides on a given topic.

Dependencies:
    - OpenAI API key (configured in app.config)
    - langchain library
"""

from app.config import OPENAI_API_KEY
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.7, api_key=OPENAI_API_KEY)

lecture_prompt = PromptTemplate(
    input_variables=["topic", "duration"],
    template="""Create a {duration}-minute lecture on {topic}. Include an introduction, main points, and a conclusion.
    For each main section, provide a brief summary suitable for a presentation slide.
    Format the output as follows:
    LECTURE:
    [Full lecture content here]
    SLIDES:
    1. [Title of slide 1]
    - [Bullet point 1]
    - [Bullet point 2]
    2. [Title of slide 2]
    - [Bullet point 1]
    - [Bullet point 2]
    [Continue for all main sections]""",
)

lecture_chain = LLMChain(llm=llm, prompt=lecture_prompt)


def generate_lecture_and_slides(topic: str, duration: int) -> dict:
    """
    Generate a lecture and accompanying slides on a given topic.

    Args:
        topic (str): The topic of the lecture.
        duration (int): The intended duration of the lecture in minutes.

    Returns:
        dict: A dictionary containing the lecture content and slides.
    """
    try:
        result = lecture_chain.run(topic=topic, duration=duration)
        lecture_content, slides_content = result.split("SLIDES:")

        lecture = lecture_content.strip()
        slides = [
            slide.strip().split("\n") for slide in slides_content.strip().split("\n\n")
        ]

        return {"lecture": lecture, "slides": slides}
    except Exception as e:
        # Log the error here
        raise Exception(f"Failed to generate lecture: {str(e)}")
