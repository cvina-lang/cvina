@echo off
REM ========================================
REM Cvina Command Launcher
REM ========================================

REM Change directory to the folder containing cvinac.py
SET CVINA_PATH=%~dp0source\cvina

REM Run Python with all arguments passed to this script
python "%CVINA_PATH%\cvinac.py" %*