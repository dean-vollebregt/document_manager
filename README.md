***To view the site please visit***

- https://www.flatdna.com.au

***To run locally***

- cd lambda

- npm install

***To sync public assets to production***

- cd public
   
- aws s3 sync . s3://www.flatdna.com.au/

***To update the cloudformation stack***

- aws s3 sync . s3://flatdna-backend --acl private --exclude "*" --include "cloudformation.yml"

- aws cloudformation update-stack --stack-name flatDNA --template-url 'https://flatdna-backend.s3-ap-southeast-2.amazonaws.com/cloudformation.yml'