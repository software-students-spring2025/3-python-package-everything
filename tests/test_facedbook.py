import pytest
from src.facedbook import faces
from src.facedbook import stories
from src.facedbook import feelings
from src.facedbook import encoder

# tests for replace_with_faces()



# tests for face_story() 
def test_face_story_basic(): # ensure it returns a string of 3 lines
    story = stories.face_story(3)
    assert isinstance(story, str)
    assert len(story.split("\n")) == 3 
    
def test_face_story_empty(): # ensure it returns empty string
    story = stories.face_story(0)
    assert story == ""

def test_face_story_large_input(): # ensure it returns a string of 10 lines
    story = stories.face_story(10)
    assert isinstance(story, str)
    assert len(story.split("\n")) == 10 

def test_face_story_negative(): # ensure it handles negative numbers
    story = stories.face_story(-5)
    assert story == "" 

def test_face_story_type_error(): # ensure it sends an error for non-int values
    with pytest.raises(TypeError):
        stories.face_story("five")




# tests for ask_user_feeling()




# tests for face_encoder() 
def test_face_encoder_output():
    """
    Checks that face_encoder() returns a string of the correct number of faces.
    """
    for num in range(1, 11):
        faces = encoder.face_encoder("happy", num)
        count = len(faces.split("\n"))
        assert isinstance(faces, str), f"Expected face_encoder() to return a string. However, it returned {faces}."
        assert count == num, f"Expected face_encoder() to return the correct number of faces. However, it returned {count} faces."

def test_face_encoder_no_faces():
    """
    Checks that face_encoder() returns an empty string when asked for 0 faces.
    """
    faces = encoder.face_encoder("happy", 0)
    assert isinstance(faces, str), f"Expected face_encoder() to return a string. However, it returned {faces}."
    assert faces == "", f"Expected face_encoder() to return an empty string. However, it returned {faces}."

def test_face_encoder_max_number():
    """
    Checks that face_encoder() returns an error message for the number of faces limit, which is a string.
    """
    faces = encoder.face_encoder("happy", 11)
    assert isinstance(faces, str), f"Expected face_encoder() to return an error message as a string. However, it returned {faces}."
    assert faces == "error: the maximum number of faces is 10", f"Expected face_encoder() to output an error message. However, it outputted {faces}."

def test_face_encoder_invalid_word():
    """
    Checks that face_encoder() returns an error message for a word not found, which is a string.
    """
    faces = encoder.face_encoder("hello", 1)
    assert isinstance(faces, str), f"Expected face_encoder() to return an error message as a string. However, it returned {faces}."
    assert faces == "error: face cannot be found for this word", f"Expected face_encoder() to output an error message. However, it outputted {faces}."
    