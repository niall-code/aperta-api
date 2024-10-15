# Aperta API

This Django REST Framework API (Application Programming Interface) is designed to serve as the back end of my full-stack portfolio project, Aperta.

The repository for the front end can be found here: https://github.com/niall-code/aperta

## Design, Development, and Deployment Process

### Initial Setup

I created a GitHub repository from Code Institute's project template, then created a Gitpod workspace from that.

![create repository](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1728569430/create-aperta-api-repo_udtnd7.png)

![create workspace](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1728569430/create-aperta-api-workspace_sjr02o.png)

I installed Django and Django REST Framework, as well as dependencies regarding cloud-hosted images. I then started a Django project.

> `pip install django==3 djangorestframework django-cloudinary-storage Pillow`
>
> `pip freeze > requirements.txt`
>
> `django-admin startproject aperta_api .`

In `aperta_api/settings.py`, in `INSTALLLED_APPS`, I added 'cloudinary' and 'rest_framework' at the bottom, and 'cloudinary_storage' above the existing 'django.contrib.staticfiles'.

### Entity Relationship Diagrams (ERDs)

I looked at my repository from the Moments walkthrough project's API, to see how my Django models were constructed there. I used those as a starting point, removed a couple of attributes from Profile that currently seem unnecessary, altered the names of various attributes to increase their clarity to me, added some important new attributes, particularly 'category' and 'green_listed' in my Post model, and planned two additional models, namely Block and Report.

I consulted a Code Institute tutor, Sarah, while writing my Follow model. She solidified my understanding of the similar Follower model in Moments by clearing up a confusion over its seemingly ambiguous use of the words "following" and "followed" as 'related terms'. In my own model, I have replaced those with "follows" and "followers", respectively. Therefore, when I want to know who I have followed, I should be able to query something like `me.follows.all()`, and if I wanted to know who is following me, I should be able to query something like `me.followers.all()`.

![entity relationship diagrams](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1729017520/aperta-erds_qkenrp.png)
