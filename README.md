# Learning a Little about Containerlab

Hello all. This is the respository based on this [blog post](https://juliopdx.com/2021/12/10/my-journey-and-experience-with-containerlab/).

## Getting Started

Feel free to use this example. You will need access to the same version of cEOS image I used. If you use another version, just make sure those changes are reflected in the `net.clab.yaml` file, as well as any configuration differences in the `/configs/post` directory.

## Installing requirements

```bash
# Downlad and install Containerlab
bash -c "$(curl -sL https://get-clab.srlinux.dev)"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Deploy topology

```bash
sudo containerlab deploy -t net.clab.yaml
```

## Run Deployment Script

```bash
python3 deploy.py
```
