# WW Tweeter Application

## Build Status

Linting Status: ![Linting Status:](https://img.shields.io/github/workflow/status/timothyhull/ww_tweeter/Linting%20and%20Static%20Code%20Analysis "Linting Status")

`pytest` Status: ![`pytest` Status](https://img.shields.io/github/workflow/status/timothyhull/ww_tweeter/pytest%20Testing "pytest Status")

[Code Analysis:](https://bettercodehub.com/results/timothyhull/ww_tweeter "Better Code Hub") ![Better Code Hub Analysis](https://bettercodehub.com/edge/badge/timothyhull/ww_tweeter?branch=main "Better Code Hub Analysis")

## Application for #100DaysOfCode

This project is the result of a challenge from [days 59-60](https://github.com/talkpython/100daysofcode-with-python-course/tree/master/days/58-60-twitter-api#day-2-and-3-practice) in the [TalkPython #100DaysOfCode course](https://training.talkpython.fm/courses/explore_100days_in_python/100-days-of-code-in-python).

The lesson focuses on learning to use the Python `Tweepy` module to interact with the Twitter API and the course suggests a number of challenges to get practice with the lesson content, listed at the end of [this Jupyter Notebook](https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/58-60-twitter-api/twitter-api.ipynb).  I wanted to learn to build a full-fledged application, so I chose to follow the example in the [RealPython article: Building a web app with Bottle, SQLAlchemy, and the Twitter API](https://realpython.com/building-a-simple-web-app-with-bottle-sqlalchemy-twitter-api/).

Over [roughly two months](https://github.com/timothyhull/100daysofcode/tree/main/days/_59_60), my version of the application gave me extensive practice with topics like:

- Classes, including class inheritance.
- GitHub Actions
- `pytest`
- `Tweepy`
- `PostgreSQL`
- PGAdmin
- `SQLAlchemy`
- Containerized applications with Docker
- Docker Compose
- Clean code writing using Better Code Hub
- `bottle`
- Visual Studio Code development containers
- Docker Compose

I successfully built an application that:
    - Uses `Tweepy` to retrieve a set tweets for the [wwt_inc](https://twitter.com/wwt_inc) Twitter account.
    - Extract hashtags from the set of tweets.
    - Builds database tables in a PostgreSQL database for tweets and hashtags using `SQLAlchemy`.
    - Loads tweets and hashtags into the database.
    - Write `pytest` tests that mock several `Tweepy` and `SQLAlchemy` objects/classes.
    - Read tweets and hashtags from the database, optionally filtering data.
    - Display tweets and hashtags with a `bottle` hosted web application.

My application uses Docker Compose to build the following components:
    - 1 x PostgreSQL container.
    - 1 x Pgadmin container.
    - 1 x Application container for Python applications that interact with Twitter and PostgreSQL, plus serve a web application with `bottle`.
    - 1 x Docker network with auto-DNS.
    - 1 x Docker persistent volume for database storage.
    - Several local volume mounts for container code consumption and Pgadmin configuration storage.

To give the application a try for yourself, I recommend the following setup steps:

1. Clone this repository to an environment with Docker and Docker Compose runtime environments, plus an Internet connection.
2. Use your shell prompt to navigate to the cloned repository.
3. Create the following **.env** files and populate the variable values with the appropriate information:

    ```bash
    # ./app/.env
    APP_DB_USER=db_user
    APP_DB_PASS=
    APP_LOCATION=local
    POSTGRES_USER=root
    POSTGRES_PASSWORD=
    DB_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/ww_tweeter
    DB_TEST_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/ww_tweeter_test
    TWITTER_KEY=
    TWITTER_SECRET=
    TWITTER_ACCESS_TOKEN=
    TWITTER_ACCESS_SECRET=
    ```

    ```bash
    # ./dockerfiles/db/.env
    APP_DB_USER=db_user
    APP_DB_PASS=
    POSTGRES_USER=root
    POSTGRES_PASSWORD=
    ```

    ```bash
    # ./dockerfiles/db_admin/.env
    PGADMIN_DEFAULT_EMAIL=user@dbadmin.com
    PGADMIN_DEFAULT_PASSWORD=
    ```

4. Enter the following command in your shell:

    ```bash
    docker compose up -d
    ```

5. Wait a few minutes for the images to build and for the containers to start.
6. Attach to the application container with the following command:

    ```bash
    docker exec -it ww-tweeter-app-1 /bin/bash
    ```

7. Start the Python application with the following command:

    ```bash
    ./app/tweeter/ww_tweeter.py
    ```

8. Navigate to the [web application](http://localhost:8081) with a browser.

Take note that this application is built for learning, development, and testing, so the Python application does not automatically start (via the Dockerfile `CMD` or `ENTRYPOINT` instructions) and `SQLAlchemy` and `bottle` debugging are active.
