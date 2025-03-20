# import packageName.faces as faces
import facedbook.faces as faces
import facedbook.stories as stories
import facedbook.feelings as feelings
import facedbook.encoder as encoder


def main():
    # testing replace_with_faces
    print("\nReplacing with faces!")
    print(faces.replace_with_faces("This project is so cool and fun to use!"))

    # testing face_story
    print("\nSpooky story... \n")
    print(stories.face_story(3))
    print("\nLOOK BEHIND YOU...\n")
    print("BOO!\n")

    # Ask the user how they feel and show a related face emoji
    print("\nFeeling Check! \n")
    print("How are you feeling today? (happy, sad, mad, soso, excited, tired, nervous, love, surprised, confused, scared, bored): \n")
    print(feelings.ask_user_feeling("happy"))

    # testing face_encoder
    print("\nPrinting happy faces...")
    print(encoder.face_encoder("happy", 8))


if __name__ == "__main__":
    # run the main function
    main()
