# ð¤ Discord_bot

A discord bot written in Python

## âï¸ Installation

* Run `create_venv.bat` script in the terminal by typing: `.\create_venv.bat "nameYouWant"`
* Fill the `.env` file you just created with your *discord bot token*
* Activate the virtual environment by typing: `.\venv_yourVenv\Scripts\activate` in the terminal
* `py manage.py makemigrations`
* `py manage.py migrate`
* `py manage.py createsuperuser` and follow the instructions.
\
\
... et voilÃ 

## ð¨ Keep it updated

To ensure your library requirements are up to date with the rest of the people working on the project, it is recommended you run `reqs_install.bat` whenever you **pull**, and `pip freeze > requirements.txt` whenever you **push** (pushing can be done using the `pushgit.bat` script, read: **ð Push to Github**)

## ð Running the program

Now you can run the program by typing `py manage.py runserver` in the terminal.

## ð Push to Github

Push your updated code by typing `pushgit.bat "commit message here"`  in the terminal.
