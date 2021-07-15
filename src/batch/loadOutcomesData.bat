@echo off

echo .
echo .
echo .
echo %date% %time% running loadOutcomesData.bat ...

@REM SET DBT_TARGET=dev
SET DBT_TARGET=power_bi
SET UPDATE_AUTHORISED_BY="andy.duff"
@REM SET UPDATE_AUTHORISED_BY="ken.macdonald"
SET DBT_DIR=\dbt\demo_dbt

echo %date% %time% Ensuring we are in the batch directory.
if NOT %CD%\ == %~dp0 (
    echo  %date% %time% Changing to dir: %~dp0
    %~d0
    cd %~dp0
)

@REM echo %date% %time% calling .\loadPR14base.bat with DBT_TARGET = %DBT_TARGET%
@REM call .\loadPR14base.bat

@REM echo %date% %time% calling .\loadPR14submeasures.bat with DBT_TARGET = %DBT_TARGET%
@REM call .\loadPR14submeasures.bat

@REM echo %date% %time% calling .\loadPR19base.bat with DBT_TARGET = %DBT_TARGET%
@REM call .\loadPR19base.bat

echo %date% %time% calling .\loadPR19updates.bat with DBT_TARGET = %DBT_TARGET%
call .\loadPR19updates.bat

echo %date% %time% completed loadOutcomesData.bat ...
echo .
echo .
echo .