# ![KrispyTools Logo](/krispiest_logo.png)

# I'm just using this as a template README for now

#### Rejuvenation Tech

#### Krispy Tools - A Non-Fungible Token analytics tool for _beginners_

## Overview

### Goal

We are a team of high schoolers who wanted to create an NFT analytics tool that would be beginner-friendly and help introduce beginners to the world of crypto. Our website is entirely designed for this purpose. Users will be able to straightforwardly navigate our top-notch NFT analytics too, all while journeying through the complex world of crypto and NFTs. Our platform will provide both a space for the absolute beginner, all the way to even the most experienced crypto-enthusiasts. Our goal is to create a simple but versatile platform that can ultimately teach those just starting to immerse themselves in NFTs, and provide a hand for those relying on up-to-date NFT information.

### Code

##### Backend

We get our data from the [OpenSea API](https://docs.opensea.io/reference/api-overview) and the [CoinGecko API](https://www.coingecko.com/en/api/documentation). We use [Django](https://www.djangoproject.com/), a Python framework, [Pythonanywhere](https://www.pythonanywhere.com/) for our javascript async function request, and a [PostgreSQL](https://www.postgresql.org/) database for the backend. Data retrieval is automated with [APScheduler](https://apscheduler.readthedocs.io/en/3.x/) and we store new data in our database every 1 minute. We use various packages including requests, django, apscheduler, datetime, pandas, and more!

##### Frontend

Our website was wireframed with [Figma](https://www.figma.com/), and our prototype can be seen [here](https://www.figma.com/proto/aKZdkErsEDpuVxpJnd0r0K/Krispy-Cohort-%3A?node-id=225%3A5&scaling=min-zoom&page-id=225%3A4&starting-point-node-id=225%3A5&show-proto-sidebar=1). It was then exported to a [Bootstrap](https://getbootstrap.com/) framework. We created visual graphs to display information about our collections using [Chart.js](https://www.chartjs.org/).

### Pages

- Home
  - Initial landing page for users
- Stats
  - Displays top 50 collections and relevant data
    - Can be sorted by volume, price, or sales
  - Has search bar for getting info on a specific collection
    - Requires the asset contract address and the token id
- Collections
  - Displays 50 (or 50 * offset depending on user) NFTs (assets) in the user specified collection along with relevant data
  - Displays graphs about the user specified collection regarding number of total sales over a period of time
- Learn
  - Has resources and explanations for beginners to help them understand terminology and other relevant concepts
- About
  - Contact information about the team as well as a general overview of our tool

## Usage

### Server?
We used the [AWS](https://aws.amazon.com/) (Amazon Web Services) as our web host

### When running on localhost

Note: If using a virtual environment, you will need to modify `settings.py`. See [this guide](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f) for help.
- Ensure necessary packages are installed with `pip install packagename`. The main packages we use are django, apscheduler, django-apscheduler, datetime, requests, psycopg2, datetime, and pandas.
- Ensure [PostgreSQL](https://www.postgresql.org/download/) is installed
- In cmd/terminal navigate to the krispy_merged directory
- Ensure migrations are applied with: `python manage.py makemigrations` and then: `python manage.py migrate`
- Run with: `python manage.py runserver --noreload`

## Requirements/framework versions

Please check out requirements.txt

## License

Krispy Tools is released under the MIT License.
