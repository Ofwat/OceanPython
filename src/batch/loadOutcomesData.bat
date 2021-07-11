@echo off

SET DBT_TARGET=dev
SET DBT_DIR=\dbt\demo_dbt

echo Ensuring we are in the batch directory.
if NOT %CD%\ == %~dp0 (
    echo Changing to dir: %~dp0
    %~d0
    cd %~dp0
)


echo .\loadPR14base.bat
call .\loadPR14base.bat

echo .\loadPR14submeasures.bat
call .\loadPR14submeasures.bat

echo .\loadPR19base.bat
call .\loadPR19base.bat

echo .\loadPR19updates.bat
call .\loadPR19updates.bat

