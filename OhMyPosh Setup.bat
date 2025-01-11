@echo off

:: Check if the script is running as Administrator
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo This script requires administrator privileges. Please run as Administrator.
    pause
    exit /b
)

echo Installing Oh-Py-Posh and JetBrains Nerd Font
winget install JanDeDobbeleer.OhMyPosh DEVCOM.JetBrainsMonoNerdFont
echo Installation Complete

echo Installing PSReadLine for History Prediction
powershell -Command "Install-Module -Name PSReadLine -Force -SkipPublisherCheck"
powershell -Command "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned"
echo PSReadLine Installed Succesfully

mkdir %USERPROFILE%\OneDrive\Documents\WindowsPowerShell
cd %USERPROFILE%\OneDrive\Documents\WindowsPowerShell

echo oh-my-posh init pwsh --config 'C:\Users\shubh\AppData\Local\Programs\oh-my-posh\themes\tonybaloney.omp.json' ^| Invoke-Expression >> Microsoft.PowerShell_profile.ps1
echo Set-PSReadLineOption -PredictionSource History >> Microsoft.PowerShell_profile.ps1
echo Set-PSReadLineOption -PredictionViewStyle ListView >> Microsoft.PowerShell_profile.ps1
echo clear >> Microsoft.PowerShell_profile.ps1

echo $PROFILE setup complete

echo "                  +-+-+-+-+ +-+-+                         "
echo "                  |M|a|d|e| |B|y|                         "
echo "                  +-+-+-+-+ +-+-+                         "
echo "   ______        __   __     ____                     _   "
echo "  / __/ /  __ __/ /  / /    / __/__  __ _  ___ ____  (_)  "
echo " _\ \/ _ \/ // / _ \/ _ \  _\ \/ _ \/  ' \/ _ `/ _ \/ /   "
echo "/___/_//_/\_,_/_.__/_//_/ /___/\___/_/_/_/\_,_/_//_/_/    "
echo .
echo .
echo .

echo Remember to set up the JetBrains Nerd Font , In the PowerShell Apperiance tab under settings.

pause

