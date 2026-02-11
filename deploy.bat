@echo off
chcp 65001 >nul 2>&1
echo.
echo  ============================================
echo   Marketing VIP - Deploy Propuesta a Vercel
echo  ============================================
echo.
cd /d "%~dp0"
echo  Carpeta: %CD%
echo.

:: Verificar que Node existe
where node >nul 2>&1
if %errorlevel% neq 0 (
    echo  [ERROR] Node.js no encontrado. Instalalo desde https://nodejs.org
    echo.
    pause
    exit /b 1
)

:: Verificar login
npx vercel whoami >nul 2>&1
if %errorlevel% neq 0 (
    echo  No estas logueado. Iniciando login...
    echo.
    npx vercel login
    if %errorlevel% neq 0 (
        echo.
        echo  [ERROR] Login fallido.
        pause
        exit /b 1
    )
)

echo  Desplegando...
echo.
npx vercel --prod --yes

if %errorlevel% equ 0 (
    echo.
    echo  ============================================
    echo   Listo! Copia la URL de arriba para el cliente
    echo  ============================================
) else (
    echo.
    echo  [ERROR] El deploy fallo. Revisa los mensajes arriba.
)

echo.
pause
