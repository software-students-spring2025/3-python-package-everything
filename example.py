from facedbook.faces import replace_with_faces
from facedbook.stories import face_story
from facedbook.feelings import ask_user_feeling
from facedbook.encoder import face_encoder


def example():
    # Replace words with faces: replace_with_faces()
    sentence = "This project is so cool and fun to use!"
    print(replace_with_faces(sentence))

    # Generate a spooky story: face_story()
    print(face_story(3))

    # Get a face based on emotion: ask_user_feeling()
    print(ask_user_feeling("happy"))

    # Encode words into faces: face_encoder()
    print(face_encoder("happy", 3))


if __name__ == "__main__":
    example()
