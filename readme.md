# quizApp

**quizApp**, a Python portfolio project, is a simple multiple choice question and answer program.

The program utilizes [Textualize/rich](https://github.com/Textualize/rich) for the User Interface and 
[coleifer/peewee](https://github.com/coleifer/peewee) for creating and interacting with an SQLite database.

**This program is a work in progress, so stay tuned!** 😀

## Usage
To get the game ready, install **rich** and **peewee**:
```bash
pip install rich
pip install peewee
```
Run **create_db.py** to initialize and seed the database. Note that only a few question / answer combinations
are included under **questions_answers.json**. Then run **main.py** to play!
```bash
python create_db.py
python quizapp.py
```