$ErrorActionPreference = "Stop"
if ($env:OS -ne "Windows_NT") { throw "Bouw de Windows-versie op Windows." }
Push-Location (Join-Path $PSScriptRoot "..")
try {
    python -m PyInstaller --noconfirm --clean --onedir --windowed --name ReasoningAssistent --collect-data reasoning_assistent --collect-all sounddevice --collect-all _sounddevice_data --collect-all faster_whisper --collect-all ctranslate2 --collect-all onnxruntime --collect-all av --collect-all tokenizers main.py
    if ($LASTEXITCODE -ne 0) { throw "PyInstaller-build mislukt." }
} finally { Pop-Location }
