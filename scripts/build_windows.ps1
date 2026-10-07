$ErrorActionPreference = "Stop"
if ($env:OS -ne "Windows_NT") { throw "Bouw de Windows-versie op Windows." }
Push-Location (Join-Path $PSScriptRoot "..")
try {
    python -m PyInstaller --noconfirm --clean --onedir --windowed --name ReasoningAssistent --collect-data reasoning_assistent main.py
    if ($LASTEXITCODE -ne 0) { throw "PyInstaller-build mislukt." }
} finally { Pop-Location }
