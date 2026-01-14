@echo off
echo ===============================
echo Git Daily Push Script
echo ===============================

git checkout main || goto :error
git pull --rebase origin main || goto :error

git add .

git diff --cached --quiet && (
    echo No changes to commit.
) || (
    git commit -m "Daily LeetCode update"
)

git push origin main || goto :error

echo ===============================
echo Push completed successfully!
echo ===============================
pause
exit /b 0

:error
echo.
echo ❌ Git operation failed.
echo Fix the error above and run again.
pause
exit /b 1
