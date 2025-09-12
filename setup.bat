@echo off
echo =========================================
echo   TELEGRAM TO FACEBOOK BOT
echo   Quick Setup for Windows
echo =========================================
echo.

echo Step 1: Installing required packages...
pip install -r requirements.txt

echo.
echo Step 2: Testing your setup...
python test_setup.py

echo.
echo =========================================
echo Setup complete!
echo.
echo Next steps:
echo 1. Edit simple_telegram_to_facebook.py
echo 2. Add your API credentials 
echo 3. Run: run_bot.bat
echo =========================================
pause
