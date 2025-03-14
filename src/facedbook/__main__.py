# import packageName.faces as faces
from faces import replace_with_faces
from stories import face_story
from feelings import ask_user_feeling
from encoder import face_encoder

def main():
    print(
        replace_with_faces(
            'I want to go to bed.'
        ))

    # testing for face_story
    print("\nspooky story... \n")
    print(face_story(3))
    print("\nLOOK BEHIND YOU...\n")
    print("BOO!\n")

    # Ask the user how they feel and show a related face emoji
    print("\n Feeling Check! \n")
    print("\n How are you feeling today? (happy, sad, mad, soso): \n")
    print(ask_user_feeling("happy")) 

    # testing face_encoder
    print("\nPrinting happy faces...")
    print(face_encoder("happy", 8))
    
if __name__ == "__main__":
    # run the main function
    main()
