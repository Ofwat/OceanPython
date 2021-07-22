@echo off

echo .
echo  %date% %time% calling loadPR19base.bat ...
echo  %date% %time% Ensuring we are in the batch directory.
if NOT %CD%\ == %~dp0 (
    echo  %date% %time% Changing to dir: %~dp0
    %~d0
    cd %~dp0
)

echo  %date% %time% Changing to the main python dir.
cd ..\main\python

echo  %date% %time% Using the dbt power bi settings.
python.exe .\tools\replaceDBTTarget.py --from_target dev --to_target %DBT_TARGET%

echo  %date% %time% Loading data from Excel to DB.
echo  %date% %time% running ... python.exe .\outcomesDataProc.py PR19base --user %UPDATE_AUTHORISED_BY%  --comment "Initial load" --input_file "..\resources\Pauls_latest_PR19.xlsx"
python.exe .\outcomesDataProc.py PR19base --user %UPDATE_AUTHORISED_BY%  --comment "Initial load" --input_file "..\resources\Pauls_latest_PR19.xlsx"

echo  %date% %time% run dbt
cd %DBT_DIR%
dbt run

echo  %date% %time% Changing back to the batch dir
cd %~dp0
echo  %date% %time% Changing to the main python dir.
cd ..\main\python

echo  %date% %time% Switching back to the dbt dev settings
python.exe .\tools\replaceDBTTarget.py --from_target %DBT_TARGET% --to_target dev

echo  %date% %time% Changing back to the batch dir
cd %~dp0

echo  %date% %time% completed loadPR19base.bat
