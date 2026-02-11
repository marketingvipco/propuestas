@echo off
chcp 65001 >nul 2>&1
echo.
echo  ============================================
echo   Marketing VIP - Deploy Propuestas (GitHub)
echo  ============================================
echo.
cd /d "%~dp0"
echo  Carpeta: %CD%
echo.

git add -A
git commit -m "Actualizar propuestas"
git push origin main

if %errorlevel% equ 0 (
    echo.
    echo  ============================================
    echo   Listo! Se publicara en ~1 minuto en:
    echo   https://adriancanom.github.io/propuestas-mvip/
    echo  ============================================
) else (
    echo.
    echo  [ERROR] El push fallo. Revisa los mensajes arriba.
)

echo.
pause
