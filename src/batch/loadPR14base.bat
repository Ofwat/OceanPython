@echo off

echo Ensure we are in the batch directory
if NOT %CD%\ == %~dp0 (
    echo Changing to dir: %~dp0
    %~d0
    cd %~dp0
)

echo we need to be in the main python dir
cd ..\main\python

echo use the dbt power bi settings
python.exe ./tools/replaceDBTTarget.py --from_target dev --to_target power_bi


echo Load data from Excel to DB
python.exe ./outcomesDataProc.py PR19update --user adam.edgar --comment abc --input_file "C:\dev\python\PR19IPD01_ODI-performance-model-May-2021_v1.4 with dummy ANH data_23_Jun_21.xlsx" --test

echo run dbt here 
@REM cd \dbt\demo_dbt
@REM dbt debug
@REM dbt seed
@REM dbt dbt snapshot --select pc_updates_snapshot
@REM dbt run


echo switch back to the dbt dev settings
python.exe .\tools\replaceDBTTarget.py --from_target power_bi --to_target dev

echo change back to the batch dir
cd %~dp0
