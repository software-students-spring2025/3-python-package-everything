from src.facedbook.faces import replace_with_faces
from src.facedbook.stories import face_story
from src.facedbook.feelings import ask_user_feeling
from src.facedbook.encoder import face_encoder


# Tests for replace_with_faces()
def test_replace_with_faces_basic():
    sentence = "This project is fun and cool!"
    result = replace_with_faces(sentence)
    assert isinstance(result, str)  # Ensure it returns a string
    assert result != sentence  # Ensure some modification happened

def test_replace_with_faces_empty():
    sentence = ""
    result = replace_with_faces(sentence)
    assert result == ""  # Ensure empty input returns empty output

def test_replace_with_faces_no_replacement():
    sentence = "Just a test sentence with no keywords."
    result = replace_with_faces(sentence)
    assert isinstance(result, str)
    assert result != ""  # Ensure it does not return empty
    assert result != sentence  # Ensure transformation happens



# Tests for face_story() 
def test_face_story_basic():
    story = face_story(3)
    assert isinstance(story, str)  # Ensure it returns a string
    assert len(story.split("\n")) == 3  # Ensure exactly 3 lines

def test_face_story_single_sentence():
    story = face_story(1)
    assert isinstance(story, str)
    assert len(story.split("\n")) == 1  # Ensure exactly 1 line

def test_face_story_large_input():
    story = face_story(10)
    assert isinstance(story, str)
    assert len(story.split("\n")) == 10  # Ensure exactly 10 lines



# Tests for ask_user_feeling()
def test_ask_user_feeling_happy():
    happy_face = ask_user_feeling("happy")
    assert isinstance(happy_face, str)  # Ensure it returns a string
    assert len(happy_face) > 0  # Ensure it's not empty

def test_ask_user_feeling_invalid():
    face = ask_user_feeling("unknown_emotion")
    assert isinstance(face, str)
    assert len(face) > 0  # Ensure it returns some default face

def test_ask_user_feeling_empty():
    face = ask_user_feeling("")
    assert isinstance(face, str)
    assert len(face) > 0  # Ensure it still returns a valid face



# Tests for face_encoder() 
def test_face_encoder_basic():
    encoded_faces = face_encoder("happy", 5)
    assert isinstance(encoded_faces, str)  # Ensure it returns a string
    assert len(encoded_faces.split("\n")) == 5  # Ensure it returns 5 faces

def test_face_encoder_invalid_word():
    encoded_faces = face_encoder("nonexistentword", 3)
    assert isinstance(encoded_faces, str)
    assert "error" in encoded_faces.lower()  # Ensure it handles unknown words gracefully

def test_face_encoder_large_number():
    encoded_faces = face_encoder("happy", 10)
    assert isinstance(encoded_faces, str)
    assert len(encoded_faces.split("\n")) == 10  # Ensure it returns exactly 10 faces

def test_face_encoder_zero_faces():
    encoded_faces = face_encoder("happy", 0)
    assert encoded_faces == ""  # Should return empty string

def test_face_encoder_negative():
    encoded_faces = face_encoder("happy", -5)
    assert "error" in encoded_faces.lower()  # Should return an error message
