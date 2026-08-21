# AWS CI/CD Pipeline with ECS

## Project Overview

This project demonstrates an end-to-end CI/CD pipeline using AWS.

The pipeline automatically takes application code from GitHub, builds a Docker image, pushes it to Amazon ECR, and deploys the application to Amazon ECS.

## Architecture

```text
GitHub
   ↓
AWS CodePipeline
   ↓
AWS CodeBuild
   ↓
Docker Image
   ↓
Amazon ECR
   ↓
Amazon ECS (Fargate)
   ↓
Application Load Balancer
   ↓
Application
```

## AWS Services Used

* GitHub
* AWS CodePipeline
* AWS CodeBuild
* Amazon ECR
* Amazon ECS
* AWS Fargate
* Application Load Balancer
* IAM

## Project Files

* `app.py` – Python application
* `Dockerfile` – Docker image configuration
* `buildspec.yml` – CodeBuild instructions
* `imagedefinitions.json` – Used by CodePipeline to deploy the new Docker image

## CI/CD Workflow

1. Developer pushes code to GitHub.
2. CodePipeline detects the change.
3. CodeBuild starts the build.
4. CodeBuild builds the Docker image.
5. Docker image is tagged with the commit SHA and `latest`.
6. Image is pushed to Amazon ECR.
7. CodePipeline sends the image information to the ECS Deploy stage.
8. ECS deploys the new container.
9. Application Load Balancer sends traffic to the ECS task.
10. Updated application is available through the ALB.

## Troubleshooting

During this project, I worked with and fixed several AWS issues:

* YAML buildspec formatting error
* `iam:PassRole` permission error
* ECR permission issues
* ECS task execution role issue
* ALB target health issues
* Availability Zone configuration issue
* Security Group and port 80 connectivity issue

## What I Learned

Through this project, I learned how different AWS services work together to create an automated CI/CD pipeline.

I also learned about:

* Docker image building
* Amazon ECR
* ECS Fargate
* IAM roles and permissions
* Application Load Balancer
* Target groups and health checks
* CodePipeline deployment
* CI/CD troubleshooting

## Final Result

The final workflow successfully automates application deployment:

**GitHub → CodePipeline → CodeBuild → ECR → ECS → ALB → Application**

A change pushed to GitHub can automatically go through the CI/CD pipeline and update the running application.
