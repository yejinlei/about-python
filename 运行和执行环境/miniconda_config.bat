CALL conda config --remove-key channels &
CALL conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ &
CALL conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/ &
CALL conda config --set show_channel_urls yes &
CALL conda config --remove channels defaults &
CALL conda config --set ssl_verify true &

@echo off
c:
cd %USERPROFILE%
if not exist %USERPROFILE%\pip (
    md %USERPROFILE%\pip
)
set file=%USERPROFILE%\pip\pip.ini
if not exist %file% (
    echo [global]>%file%
    echo timeout=300>>%file%
    echo index-url=http://mirrors.aliyun.com/pypi/simple/>>%file%
    echo [install]>>%file%
    echo trusted-host=mirrors.aliyun.com>>%file%
    echo %file%+"创建成功"
) else ( echo %file%+"已经存在" )
pause

CALL conda config --set ssl_verify false
CALL conda update requests
CALL conda config --set ssl_verify true
CALL conda update conda