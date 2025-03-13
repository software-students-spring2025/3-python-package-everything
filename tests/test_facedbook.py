from src.facedbook.faces import replace_with_faces
from src.facedbook.stories import face_story
from src.facedbook.feelings import ask_user_feeling
from src.facedbook.encoder import face_encoder


# tests for replace_with_faces()



# tests for face_story() 
def test_face_story_basic(): # ensure it returns a string of 3 lines
    story = face_story(3)
    assert isinstance(story, str)
    assert len(story.split("\n")) == 3 

def test_face_story_single_sentence(): # ensure it returns a string of 1 line
    story = face_story(1)
    assert isinstance(story, str)
    assert len(story.split("\n")) == 1 

def test_face_story_large_input(): # ensure it returns a string of 10 lines
    story = face_story(10)
    assert isinstance(story, str)
    assert len(story.split("\n")) == 10 



# tests for ask_user_feeling()




# tests for face_encoder() 
