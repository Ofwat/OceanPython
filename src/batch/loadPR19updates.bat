@echo off

echo .
echo loadPR19updates.bat
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
for %%f in (..\resources\updates\*.xlsx) do (
    echo running ... python.exe .\outcomesDataProc.py PR19update --user "ken.macdonald" --comment "Initial APR load" --input_file "%%f" 
    python.exe .\outcomesDataProc.py PR19update --user "ken.macdonald" --comment "Initial APR load" --input_file "%%f" 
    move /Y "%%f" ..\resources\updates\loaded\
)

echo running dbt 
cd %DBT_DIR%
dbt snapshot --select pc_updates_snapshot
dbt run --models F_PC_apr_table

echo Changing back to the batch dir
cd %~dp0
echo Changing to the main python dir.
cd ..\main\python

echo Switching back to the dbt dev settings
python.exe .\tools\replaceDBTTarget.py --from_target %DBT_TARGET% --to_target dev

echo Changing back to the batch dir
cd %~dp0
