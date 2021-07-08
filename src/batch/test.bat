@echo off

echo %~d0

if NOT %CD%\ == %~dp0 (
    echo Changing to dir: %~dp0
    %~d0
    cd %~dp0
)


