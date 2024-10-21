# Aperta API

This Django REST Framework API (Application Programming Interface) is designed to serve as the back end of my full-stack portfolio project, Aperta.

The repository for the front end can be found here: https://github.com/niall-code/aperta

## Design, Development, and Deployment Process

### Initial Setup

I created a GitHub repository from Code Institute's project template, then created a Gitpod workspace from that.

![create repository](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1728569430/create-aperta-api-repo_udtnd7.png)

I installed Django and Django REST Framework, as well as dependencies regarding cloud-hosted images. I then started a Django project.

> `pip install django==3 djangorestframework django-cloudinary-storage Pillow`
>
> `pip freeze > requirements.txt`
>
> `django-admin startproject aperta_api .`

In `aperta_api/settings.py`, in `INSTALLLED_APPS`, I added 'cloudinary' and 'rest_framework' at the bottom, and 'cloudinary_storage' above the existing 'django.contrib.staticfiles'.

### Entity Relationship Diagrams (ERDs)

I looked at my repository from the Moments walkthrough project's API, to see how my Django models were constructed there. I used those as a starting point, removed a couple of attributes from Profile that currently seem unnecessary, altered the names of various attributes to increase their clarity to me, added some important new attributes, particularly 'green_listed' in my Post model, and planned two additional models, namely Block and Report.

I consulted a Code Institute tutor, Sarah, while writing my Follow model. She solidified my understanding of the similar Follower model in Moments by clearing up a confusion over its seemingly ambiguous use of the words "following" and "followed" as 'related terms'. In my own model, I have replaced those with "follows" and "followers", respectively. Therefore, when I want to know who I have followed, I should be able to query something like `me.follows.all()`, and if I wanted to know who is following me, I should be able to query something like `me.followers.all()`.

![entity relationship diagrams](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1729017520/aperta-erds_qkenrp.png)

### Cloudinary Setup

I created an env.py file, which will be git-ignored. In it, I set my Cloudinary URL as an environment variable. I then added code to my settings file to retrieve that from the environment and make Cloudinary my default image storage location, as taught during the Moments walkthrough.

### Starting Apps

I ran `python manage.py startapp <app_name>` seven times, with the app names being profiles, posts, likes, comments, follows, blocks, and reports. I then added those to my installed apps in my settings file.

### Mentor Meeting and ERDs

I had a Project Inception meeting with my Code Institute mentor, Gareth McGirr. He suggested that a 'reported' attribute in my Post model could be helpful and reminded me of my forgotten intention to have 'reason' and 'explanation' attributes in my Report model. Here are my updated ERDs:

![updated entity relationship diagrams](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1729280770/aperta-erds-2_p1bx7m.png)


### Create Profile model

I added the appropriated code to `profiles/models.py` and `admin.py`, taking example from Moments but adjusting it for the differences I planned in my ERD. I have included a stylistically different default profile picture, an outline-based avatar rather than shading-based. I then created a superuser, running:

> `python manage.py makemigrations`
>
> `python manage.py migrate`
>
> `python manage.py createsuperuser`

To check that the profile creation functionality was working, I ran `python manage.py runserver`, received an error message screen as expected, added the development workspace URL to ALLOWED_HOSTS like it advises, and was rewarded with the screen shown below.

![host allowed](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1729349063/dev-host-allowed_ygfpml.png)

I then appended `/admin` to the address, logged in with my new superuser account, and saw that a profile had indeed been created and the Cloudinary path for the default profile picture was being successfully interpreted when hovered, as seen below.

![profile creation success](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1729349063/create-profile-success_uaz3bf.png)

### Add ProfileSerializer and ProfileList view

I edited the `profiles/views.py` and `aperta_api/urls.py` files and created the `profiles/serializers.py` and `urls.py` files, so that appending `/profiles/` to the root address of the back-end application will display a JSON-formatted list of user profiles. Although the upcoming React UI will reduce the usefulness of that, if the stack had to be temporarily decoupled, this could be helpful to the developers.

![profile list](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1729434070/profile-list_wsbars.png)

### Add ProfileDetail view

I then further edited the `profiles` app's `views.py` and `urls.py` files, adding an extra class containing methods for handling GET and PUT requests, so that an individual profile will be possible to view or edit. Additionally appending a Profile instance's ID number onto the address, e.g. `/profiles/1/`, now will display a single profile's JSON-formatted details together with a simple form for the uploading of a replacement profile picture.

![profile detail](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1729447518/profile-detail_zk84cw.png)

### Add login button

I will move the Registration & Authentication user story to my kanban board's In Progress column. Its acceptance criteria are shown here.

![Registration and Authentication user story](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1729516945/signup-login-ustory_k7on9x.png)

I created a second superuser. As taught in the walkthrough, in `aperta_api`, I then created a `permissions.py` file and added a URL pattern in the `urls.py` file, and in `profiles`, edited the `views.py` and `serializers.py` files. The result is that I can now log in to the API without accessing the Django admin area. Having done so, my username is present indicating authenticated status and an attribute indicating which listed profile is and isn't owned by me is effectively added onto the profiles' data by the serializer, as shown below. Also, the Profile Detail for the second profile, not owned by the current user, appropriately now did not display the form for profile picture alteration.

![API user authentication](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1729516945/api-login_sijfie.png)

As I understand it, this authentication functionality on the back end will later be utilised by the React front end, rather than my React app starting from scratch and duplicating these efforts. Additionally and in either case, if the front and back end had to temporarily be decoupled, some direct useability would still remain.
