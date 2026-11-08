# CloudTech Docker Help Desk API

A hands-on project packaging a Python HTTP API into a Docker image and running it on an Amazon Linux 2023 EC2 instance.

## Technologies
- AWS EC2, IAM and Systems Manager Session Manager
- Docker
- Python standard library
- Security group restricting port 8000 to my IP

## Application
- GET / returns a fixed welcome response.
- GET /health returns {"status": "healthy"}.
- Other paths return HTTP 404.
- This is a learning demo using Python's built-in HTTP server.
- It does not connect to Amazon Bedrock.

## Install Docker on Amazon Linux 2023
```bash
sudo dnf install -y docker
sudo systemctl enable --now docker
```

## Build and run
From the folder containing app.py and Dockerfile:
```bash
sudo docker build -t cloudtech-helpdesk:v1 .
sudo docker run -d --name cloudtech-helpdesk -p 8000:8000 cloudtech-helpdesk:v1
```

## Verify
```bash
sudo docker ps
curl http://localhost:8000/
curl http://localhost:8000/health
```

For browser access, allow inbound TCP port 8000 from your IP
and visit http://EC2-PUBLIC-IP:8000/.

## Logs and restart
```bash
sudo docker logs --tail 20 cloudtech-helpdesk
sudo docker restart cloudtech-helpdesk
curl http://localhost:8000/health
```

## Stop and remove the container
```bash
sudo docker stop cloudtech-helpdesk
sudo docker rm cloudtech-helpdesk
```

## Results
- Built the Docker image successfully.
- Verified the API from the EC2 terminal and a browser.
- Reviewed request logs.
- Restarted the container and verified API recovery.

## AWS cleanup
Save the project before terminating the instance.
Terminate the lab EC2 instance and verify its root EBS volume
is deleted. Remove the lab security group if no longer needed.
Stopping a Docker container does not stop EC2 charges.
