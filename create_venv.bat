@echo off
:: This batch file is for generating the Python virtual working environment for the given project
set application_name=%1

if "%1" == "" goto :byebye

:: (Re)create the virtual environment
echo (Re)creating virtual environment for project: %1

:: Remove existing virtual environment
@RD /S /Q  venv_%application_name%

:: Create it
py -m venv venv_%application_name%

:: Open virtual environment and install python dependencies
:: Upgrade pip
.\venv_%application_name%\Scripts\python.exe -m pip install --upgrade pip

:: Install required libs
echo Installing required Python libraries
.\venv_%application_name%\Scripts\pip.exe install -r .\requirements.txt

echo Creating .env file
py .\createEnv.py

:ready
echo Virtual environment for project '%application_name%' ready for use
goto :EOF

:byebye
echo. 
echo ==========================================
echo Please provide the following arguments:
echo - venv name, e.g. discord_bot
echo.
echo Example:
echo $ .\create_venv.bat "discord_bot"
echo ==========================================
echo.
