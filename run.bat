echo Please pass BROWSER_PATH, CHROME_DRIVER, maskmodelPath, prototxtPath, weightsPath,
echo OPENCAGE_ACCESS_KEY, U_PASSWORD, U_EMAIL(for email sending), ME(Your name), OVERRIDE_S3_ENDPOINT,
echo SOURCE_BUCKET, JSON_KEY, access, secret, region, MODEL, BASE_URL

echo ************STARK-api************
start python app-api.py %*

echo ************STARK************
start python main.py %*