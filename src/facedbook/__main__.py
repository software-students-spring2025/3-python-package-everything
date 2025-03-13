# import packageName.faces as faces
from faces import replace_with_faces
from stories import face_story
from feelings import ask_user_feeling


def main():
    # line = faces.replace_with_faces()
    print(
        replace_with_faces(
            'All team members must have visibly contributed to the code using their own git & GitHub accounts in order to claim that they contributed to the project.'
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
    
if __name__ == "__main__":
    # run the main function
    main()
