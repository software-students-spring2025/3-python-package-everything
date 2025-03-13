# facedbook

![Build Status](https://github.com/software-students-spring2025/3-python-package-everything/actions/workflows/event-logger.yml/badge.svg)

## Project Description

facedBook is a fun Python package for transforming text with cute and eerie keyboard faces, generating scary stories, and displaying emotions with expressive faces.

Its features include:

- Replacing words in a sentence with expressive keyboard faces
- Generating creepy horror stories with random actions and spooky characters
- Displaying emotions with keyboard keys based on how a user is feeling

## Installation

You can install facedbook directly from PyPI using:

```
pip install facedbook
```

[Facedbook on PyPI](LINK)

## Usage and Examples

Once installed, you can easily use its functions in your Python code.

1. Replace words with faces

```
from facedbook.faces import replace_with_faces

sentence = "This project is so cool and fun to use!"
print(replace_with_faces(sentence))
```

Example output:

```
This (づ ᴗ _ᴗ)づ♡ project (๑♡⌓♡๑) is fun ( ´͈ ᗨ `͈ )!
```

2. Generate a spooky story

```
from facedbook.stories import face_story

print(face_story(3))  # Generates a 3-sentence scary story
```

Example output:

```
(ノωヽ) saw something move in the shadows behind (／。＼).
Σ(°△°|||)︴ was trapped in a haunted house with (つ﹏⊂).
(☉_☉’) was cursed by (ᗒᗣᗕ)՞.
```

3. Get a face based on emotion

```
from facedbook.feelings import ask_user_feeling

print(ask_user_feeling("happy"))  # Returns a happy face
```

Example output:

```
(⌒▽⌒)☆
```

## Developer Setup & Contribution

1. Clone the Repository

```
git clone https://github.com/software-students-spring2025/3-python-package-everything.git
cd 3-python-package-everything
```

2. Create a Virtual Environment

```
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install Dependencies

```
pip install -r requirements.txt
```

4. Run Tests

```
pytest
```

5. Build and Publish the Package

```
python -m build
python -m twine upload dist/*
```

## Contributors

[Claire Kim] (https://github.com/radishsoups)
[Jennifer Yu] (https://github.com/jenniferyuuu)
[Iva Park] (https://github.com/ivapark)
[Chrisim Kim] (https://github.com/ChrisimKim)

## Configuration & Running Instructions

This package is compatible with Python 3.6+ and works on Windows, macOS, and Linux.
Simply install with `pip install facedbook` and use the functions as demonstrated above!

For additional environment configurations, create a .env file:

```
# Example .env
DEBUG=True
LOG_LEVEL=INFO
```

Then load environment variables using:

```
from dotenv import load_dotenv
load_dotenv()
```
