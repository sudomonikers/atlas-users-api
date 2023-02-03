mkdir dist
pipenv requirements > dist/requirements.txt
cd dist
cp -R ../src ./
cp ../lambda_function.py ./
pip3 install --target ./  -r requirements.txt
zip -r ../deployment-package .
cd ../
aws lambda update-function-code --function-name users-api-dev --zip-file fileb://deployment-package.zip