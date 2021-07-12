@echo off

echo .
echo loadPR14submeasures.bat
echo Ensuring we are in the batch directory.
if NOT %CD%\ == %~dp0 (
    echo Changing to dir: %~dp0
    %~d0
    cd %~dp0
)

echo Changing to the main python dir.
cd ..\main\python

echo Using the dbt power bi settings.
python.exe .\tools\replaceDBTTarget.py --from_target dev --to_target %DBT_TARGET%

echo Loading data from Excel to DB.
echo running ... python.exe .\outcomesDataProc.py PR14submeasures --user "ken.macdonald" --comment "Initial load" --input_file "..\resources\AnnesPR14.xlsx" 
python.exe .\outcomesDataProc.py PR14submeasures --user "ken.macdonald" --comment "Initial load" --input_file "..\resources\AnnesPR14.xlsx" 

echo run dbt 
cd %DBT_DIR%
dbt run

echo Changing back to the batch dir
cd %~dp0
echo Changing to the main python dir.
cd ..\main\python

echo Switching back to the dbt dev settings
python.exe .\tools\replaceDBTTarget.py --from_target %DBT_TARGET% --to_target dev

echo Changing back to the batch dir
cd %~dp0
