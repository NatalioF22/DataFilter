pytest -v
pytest_status=$?
pytest_pass=0
if [ $pytest_status -eq $pytest_pass ]
then
    echo "All your unit test have passed"
    git add .
    echo "Enter a commit message: "
    read commitMsg
    git commit -m "$commitMsg"
    echo "What branch should be pushed to: " 
    read branch
    git push origin "$branch"
else
    echo "At least one of your unit test have failed. Commit Not created."
fi

