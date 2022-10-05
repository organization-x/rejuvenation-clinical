# ![Rejuvenation Tech Logo](readme_static/rejuvenation_logo.png) Rejuvenation Tech (Natural Trials) Clinical Trials Platform
## Table of Contents
* [Introduction](#Introduction)
* [Tech Stack](#tech-stack)
* [Pages](#pages)
* [Usage](#usage)
* [License](#license)

## Introduction
[Rejuvenation Technologies](https://rejuvenationtech.com/) is developing a drug meant to [extend the human healthspan](https://www.notion.so/Rejuvenation-Tech-Tester-Onboarding-Platform-Product-Spec-562111ccc70d455da3ffbe5300f919ef), and is in need of people to test it. As such, they’ve tasked us with creating a custom clinical trial(s) platform (webapp) where they can send people to be walked through the entire testing process.

The hope with this platform is that we’re going to develop it with the broader aim of creating a place where labs / development agencies (at first, limited to those specifically developing nutraceuticals) can freely post their trials and receive feedback—a sort of job board for clinical trials, if you will.

For a full outline of each component in the platform, reference [Webapp User Pipeline](https://www.notion.so/Webapp-User-Pipeline-5a2a7e91d5fa41e681d1e7027ce65c1e).


## Tech Stack
### Backend
We use [Django](https://www.djangoproject.com/), a Python web framework, and a [PostgreSQL](https://www.postgresql.org/) database for the backend. We use [Docker](https://www.docker.com) to
containerize our project and make it deployable. We use the [Cryptography](https://cryptography.io/en/latest/fernet/) package to encrypt all plain-text information, and the [django-encrypted-files](https://pypi.org/project/django-encrypted-files/) to encrypt all medical documents (pdfs).

### Frontend
Our website was wireframed with [Figma](https://www.figma.com/), and our prototype can be seen [here](https://www.figma.com/file/XnedOZytyIexZ7UFxDkYKh/Clinical-Trials-Frontend-Page?node-id=0%3A1). It was then exported to vanilla html/css via the [Quest.ai](https://www.quest.ai/figma) Figma plugin. We (will) create visual graphs to display information about our collections using [Chart.js](https://www.chartjs.org/).

## Pages
- Sign-in page
  - Initial page for users who have scanned the QR code on the capsule bottle
- Registration
  - A HIPAA-compliant registration page for initially creating a trial-tester account
- All-Trials Dashboard
  - The dashboard where the user may browse and sign up for all active trials on the site
- Consent Form
  - Before joining each trial, the user will be prompted with a consent form given
  by the lab hosting the trial
- Single-Trial Dashboard
  - After successfully joining a trial, the user will be able to track their progress
  via a trial todo list, view all of their trial health stats, view any changes to the
  trial, and (as a future feature) be able to 'play' games that monitor certain aspects
  of their drug's effects on cognitive performance (e.x., a memory-test game)
- Cumulative User Profile
  - A cumulative user profile containing the user's registration information and trial
  stats across all trials

## Usage

### Server
We are considering [AWS](https://aws.amazon.com/) (Amazon Web Services) or [Railway](https://railway.app) for deployment; we are leaning towards Railway. Both work with our Docker-containerized project.

### When running on localhost

Note: If using a virtual environment, you will need to modify `settings.py`. See [this guide](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f) for help.
- Install all necessary packages with `pip3 install -r requirements.txt`
- Ensure [PostgreSQL](https://www.postgresql.org/download/) is installed
- In cmd/terminal navigate to the `rejuvenation` directory
- Ensure migrations are applied with: `python3 manage.py makemigrations` and then: `python3 manage.py migrate`
- Run with: `python manage.py runserver --noreload`

### Requirements/framework versions

Please check out requirements.txt

## License

The Rejuvenation Tech Clinical Trials Platform is released under the MIT License.
