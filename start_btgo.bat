@echo off
echo 🏦 Starting BT-GO Banking Platform...
echo.

cd /d "%~dp0"

if not exist "bt_go_env" (
    echo Creating virtual environment...
    python -m venv bt_go_env
)

echo Activating virtual environment...
call bt_go_env\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo 🚀 Starting BT-GO Services...
echo.

start "BT-GO Assistant API" cmd /k "python app.py"
timeout /t 3 /nobreak > nul

start "BT-GO Reports API" cmd /k "python RapoarteFinanciare.py"
timeout /t 3 /nobreak > nul

start "BT-GO Frontend" cmd /k "python -m http.server 3000"

echo.
echo ✅ BT-GO Platform Started Successfully!
echo.
echo 🌐 Frontend: http://localhost:3000
echo 🤖 Assistant API: http://localhost:5000
echo 📊 Reports API: http://localhost:5001
echo.
echo Waiting for services to start...
timeout /t 8 /nobreak > nul

echo Opening application in browser...
start "" "http://localhost:3000"

if errorlevel 1 (
    echo.
    echo ⚠️  Could not open browser automatically.
    echo Please open manually: http://localhost:3000
)

echo.
echo Application opened in browser!
echo Keep this window open to maintain services.
echo Press Ctrl+C in each service window to stop.
pause