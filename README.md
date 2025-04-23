# services.image-housekeeping

1. Create the lambda
2. Create the Cloudwatch rule for listening to ECR and calling the lambda

```bash
aws ecr describe-images --repository-name applications.paper-trail.financial-data-ingestion-service
```