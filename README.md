# Lyric Counter

## Overview
Lyrics counter is a django project that provides a rest api for getting information about music artists. The project is
divided into 3 apps lyricsovh_client and musicbrainzngs_client, clients for their respective online apis 
[lyricsovh](https://lyricsovh.docs.apiary.io/#reference) and 
[musicbrainzngs](https://musicbrainz.org/doc/MusicBrainz_API), 
and stats, that provides statistics, leveraging the client models. In future these clients should be modified to use 
the rest APIs provided by the respective services in order to provide a microservice architecture, where each app can 
be containerized.

## To Run
*   Install Python (3.9.2)
*   Install dependencies in **requirements.txt** using [pip](https://pypi.org/project/pip/)
*   In the command line, from the project directory **lyric_counter**, execute
    ```shell
    py manage.py runserver
    ```
*   To run tests, the following command can be used
    ```shell
    py manage.py test
    ```

## Hitting the api
*   Using your browser go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
*   The available endpoints are returned by the request, and are organised by app
