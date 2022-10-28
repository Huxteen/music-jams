- [Installation](#installation)

### Installation

#### Clone repo

``` bash
# clone the repo
$ git clone https://github.com/Huxteen/music-jams.git

# go into app's directory
$ cd music-jams

# Build docker-compose
$ docker-compose build

## Run test and Flake8
$ docker-compose run app sh -c "python manage.py test && flake8"

# start project
$ docker-compose up

# API Documentation Endpoint
 {{base_url}}/swagger/schema/


# Deployment Instructions for AWS
# Step to Deploy a Docker Container on EC2
    1. SSH onto the EC2 Instance.
    2. Generate a public SSH key for Github SSH permissions.
    3. Copy the EC2 user’s public key.
    4. Add the EC2 public key to the Github account with ownership access to the repository.
    5. Set up the repo on the server.
    6. Start the Docker container.

