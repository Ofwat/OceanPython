@echo off

echo .
echo  %date% %time% running loadPR19updates.bat ...
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
for %%f in (..\resources\updates\*.xlsx) do (
    echo  %date% %time% running ... python.exe .\outcomesDataProc.py PR19actualupdate --user %UPDATE_AUTHORISED_BY% --comment "Initial APR load" --input_file "%%f"
    python.exe .\outcomesDataProc.py PR19actualupdate --user %UPDATE_AUTHORISED_BY% --comment "Initial APR load" --input_file "%%f"
    move /Y "%%f" ..\resources\updates\loaded\
)

echo  %date% %time% running dbt 
cd %DBT_DIR%
dbt test --models source:generated_sources.pc_actuals_updates
dbt run --models stg_pc_updates_with_key
dbt snapshot --select pc_updates_snapshot
dbt run --models stg_F_pc_apr_updated F_PC_apr_table F_PC_apr


echo  %date% %time% Changing back to the batch dir
cd %~dp0
echo  %date% %time% Changing to the main python dir.
cd ..\main\python

echo  %date% %time% Switching back to the dbt dev settings
python.exe .\tools\replaceDBTTarget.py --from_target %DBT_TARGET% --to_target dev

echo  %date% %time% Changing back to the batch dir
cd %~dp0

echo  %date% %time% completed loadPR19updates.bat
