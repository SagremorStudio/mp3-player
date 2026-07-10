@echo off
cls
echo ========================================
echo    Player Szerver
echo ========================================
echo.
echo [1/3] Python szerver inditasa...
start /B python server.py

echo [2/3] Varakozas (2 masodperc)...
timeout /t 2 /nobreak >nul

echo [3/3] Bongeszo megnyitasa...
start http://localhost:8000/

echo.
echo ========================================
echo    KESZ! A szerver fut!
echo    URL: http://localhost:8000/
echo    Leallitas: CTRL+C
echo ========================================
echo.
pause