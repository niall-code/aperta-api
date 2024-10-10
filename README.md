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
