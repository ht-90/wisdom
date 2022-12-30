# wisdom

Wisdom is a django based web application for an audio platform.

Users can register account and upload audio files on Wisdom, and also play audio files uploaded by others.

## Setup

1. Install Docker
2. Set environmental variables
3. Create .env directory and file

### Install Docker

Docker needs to be installed to build a development environment and run application.

### Set environmental variables

Set `SYSTEM_ENV` environmental variable on terminal.

Example:

`>>> export SYSTEM_ENV=development`

### Create .env directory and file

Create `.env` directory at root, and a file which is the same name as the value of SYSTEM_ENV environmental variable.

This file will be parsed to map other environmental variables and app configurations.

Example:

`.env/development`

```development file
# Django
SECRET_KEY=nRLgP9y?fen_sl7
DEBUG=True

# Database
export POSTGRES_DB=postgres
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=password

# Mailgun
export SYSTEM_ENV=test
export MAILGUN_API_DEV=test
export MAILGUN_DOMAIN_DEV=test
export DEFAULT_FROM_EMAIL_DEV=test
export SERVER_EMAIL_DEV=test
```

## Usage

1. Start App
2. Sign Up and Log In
3. Upload a Video

### Start App

1. Set environmental variable `SYSTEM_ENV` (i.e. `>>> export SYSTEM_ENV=development`)
2. Build and start a docker container (`>>> docker-compose up`)
3. Access `localhost:8000` on a browser to open an app

### Sign Up and Log In

1. Sign up an account
2. Confirm an email with a verification email sent from Mailgun
3. Log in with the account detail

### Upload a Video

## CI/CD

* Lint and test are automated by tox (`>>> txox`)
* CI/CD is set up for Github Actions (.github/workflows)
