
# DevSecOps Setup & Bash Commands

This document lists all Bash commands used to build, secure, scan, and automate the DevSecOps demo project.

---

## 1. System Preparation (Ubuntu Server)

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-venv git docker.io curl

## 2. Docker Setup

sudo systemctl enable --now docker
sudo usermod -aG docker $USER
sudo reboot

##3. Project Setup

mkdir devsecops-demo
cd devsecops-demo

##4. Flask Application Test

python3 app.py
curl http://localhost:8080

##5.Docker Build && Run

docker build -t secure-app .
docker run -p 8080:8080 secure-app

##6. Python Dependency Security Scan (pip-audit)

python3 -m venv venv
source venv/bin/activate
pip install pip-audit
pip-audit

##7. Container Image Security Scan (Trivy)
trivy image secure-app

##8. Git Version Control
git init
git add .
git commit -m "Initial DevSecOps project"
git branch -M main
git push -u origin main

##9. CI/CD Pipeline Trigger
git commit -m "Trigger CI pipeline"
git pull
git push

##10.
=======

