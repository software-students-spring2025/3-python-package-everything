# import packageName.faces as faces
from faces import replace_with_faces


def main():
    # line = faces.replace_with_faces()
    print(
        replace_with_faces(
            'All team members must have visibly contributed to the code using their own git & GitHub accounts in order to claim that they contributed to the project.'
        ))


if __name__ == "__main__":
    # run the main function
    main()
