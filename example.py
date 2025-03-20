from facedbook.faces import replace_with_faces
from facedbook.stories import face_story
from facedbook.feelings import ask_user_feeling
from facedbook.encoder import face_encoder


def example():
    # Replace words with faces: replace_with_faces()
    sentence = "This project is so cool and fun to use!"
    print("\n Testing replace_with_faces:\n")
    print(replace_with_faces(sentence))

    # Generate a spooky story: face_story()
    print("\n Testing face_story (3 sentences):\n")
    print(face_story(3))

    # Get a face based on emotion: ask_user_feeling()
    print("\n Feeling Check!\n")
    print ("How are you feeling today? (happy, sad, mad, soso, excited, tired, nervous, love, surprised, confused, scared, bored): \n")
    print(ask_user_feeling("happy"))
    
    # Encode words into faces: face_encoder()
    print("\n Testing face_encoder (3 happy faces):\n")
    print(face_encoder("happy", 3))


if __name__ == "__main__":
    example()
