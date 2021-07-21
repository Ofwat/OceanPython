@echo off

echo .
echo .
echo .
echo %date% %time% running loadOutcomesData.bat ...

@REM SET DBT_TARGET=dev
SET DBT_TARGET=power_bi
SET DBT_DIR=\dbt\demo_dbt
SET UPDATE_AUTHORISED_BY="ken.macdonald"

echo %date% %time% Ensuring we are in the batch directory.
if NOT %CD%\ == %~dp0 (
    echo  %date% %time% Changing to dir: %~dp0
    %~d0
    cd %~dp0
)

echo %date% %time% calling .\loadPR14base.bat with DBT_TARGET = %DBT_TARGET%
call .\loadPR14base.bat

echo %date% %time% calling .\loadPR14submeasures.bat with DBT_TARGET = %DBT_TARGET%
call .\loadPR14submeasures.bat

echo %date% %time% calling .\loadPR19base.bat with DBT_TARGET = %DBT_TARGET%
call .\loadPR19base.bat

copy C:\dev\projects\OceanPython\src\main\resources\updates\KMc\* C:\dev\projects\OceanPython\src\main\resources\updates
echo %date% %time% calling .\loadPR19updates.bat with DBT_TARGET = %DBT_TARGET%
call .\loadPR19updates.bat

SET UPDATE_AUTHORISED_BY="andy.duff"
copy C:\dev\projects\OceanPython\src\main\resources\updates\AD\* C:\dev\projects\OceanPython\src\main\resources\updates
echo %date% %time% calling .\loadPR19updates.bat with DBT_TARGET = %DBT_TARGET%
call .\loadPR19updates.bat

echo %date% %time% completed loadOutcomesData.bat ...
echo .
echo .
echo .
