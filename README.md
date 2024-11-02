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

### Enable User Registration and Authentication for the Front End

I pip-installed `dj-rest-auth==2.1.9` and added `'rest_framework.authtoken', 'dj_rest_auth',` to INSTALLED_APPS,<br>
added `path('dj-rest-auth/', include('dj_rest_auth.urls')),` to `urlpatterns` in `aperta_api/urls.py`,<br>
then ran `python manage.py migrate`.

I next pip-installed `django-allauth==0.52.0` and added `'django.contrib.sites', 'allauth', 'allauth.account', 'dj_rest_auth.registration',` to INSTALLED_APPS and `SITE_ID = 1` underneath,<br>
and added `path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),` to `urlpatterns`.

I also pip-installed `djangorestframework-simplejwt==4.7.2`, put the session authentication value in `env.py`, added necessary code to `aperta_api/settings.py` to enable use of JSON Web Tokens in production, and created the `aperta_api/serializers.py` file, before again migrating.

### Workflow Transformation

So far, I have been aiming to fluidly move back and forth between making a back-end feature then its front-end user interface. This might be viable when I have more experience, but we were taught Django/React stack by coding the entirety of the back end first and then moving on to the front end, and unravelling what is and isn't necessary on the back end to have in place from square one is challenging. Therefore, to minimise the delaying effect of unnecessary extra problem-solving, I am thinking of now changing approach and as quickly as I can making all aspects of the back end that will be similar to Moments, then returning to where I was. This might result in multiple user stories being active at the same time. Ideally, I would have liked to avoid that, but it may need to be accepted given the tight timeframe of the project and my currently limited experience.

I have booked my next mentor session for about a week from now and hopefully by then can be getting to the point where most of my re-creation of a Moments-like app is in place and I can start giving my attention to those aspects of my project that will set it apart from that, particularly the blocking and reporting features. In theory, if I copy-pasted all of the Moments project, I could begin that almost immediately, but I want to show that I am able to code it again for myself, and also introduce some differences where I can.


### Fix Dependency Version Incompatibilities

I investigatively ran `python manage.py makemigrations --dry-run`.

The terminal told me:

> ModuleNotFoundError: No module named 'dj_database_url'

I pip-installed dependencies:

`pip install dj_database_url==0.5.0 psycopg2 gunicorn django-cors-headers`

The terminal showed me Django getting upgraded automatically:

> Downloading Django-5.1.2-py3-none-any.whl (8.3 MB)
> 
> ━━━━━━━━━━━━━━━━━━━━ 8.3/8.3 MB 98.9 MB/s eta 0:00:00

During the Moments walkthrough, I experienced strange difficulties that were largely resolved when, on the advice of a Code Institute tutor, Thomas, I downgraded Django to version 3. Therefore, I did not want this upgrade.

I ran `pip uninstall django`, then `pip install django==3`.

The terminal told me:

> django-cors-headers 4.6.0 requires django>=4.2, but you have django 3.0 which is incompatible.

I ran `pip uninstall django-cors-headers`, then `pip install django-cors-headers==4.3.1`.

Django was again automatically, unwantedly upgraded. I looked at what other dependency alterations had been made before, during that past tutoring session.

I ran `pip uninstall django django-cors-headers djangorestframework`, then

`pip install django==3.2.23 django-cors-headers==4.3.1 djangorestframework==3.14.0`,

and finally, since the dependency incompatibility warnings seemed silenced, `pip freeze > requirements.txt`.

### Fix Absent Underscore in settings.py

In a line of my settings file, `'rest_framework.renderers.JSONRenderer'`, I introduced the underscore. During my Moments walkthrough, I had experienced a ream of error messages that turned out to be caused by the same lack of underscore. The underscore is missing in the 'Adding Pagination' section of Code Institute's "DRF Cheat Sheet - Deployment" Google Doc and, due to currently being relatively inexperienced, during Moments and now Aperta, I failed to recognise it as a typo and trusted that its absence was correct. I have added an extra annotation to my heavily-annotated hard copy, which will hopefully prevent a third occurrence of this.

![annotated notes](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1730564580/annotated-printout_kbvkua.jpg)

## Credit

- My project has been significantly based on my previous codealong work from Code Institute's Moments walkthrough project, but with additional functionality, including two new models, and other miscellaneous alterations.

- My Code Institute mentor, Gareth McGirr, suggested the convenient inclusion of the 'reported' attribute in my Post model, and provided general support with clarifying my ideas and priorities for the project.

- A Code Institute tutor, Sarah, helped while writing my Follow model by clarifying a confusion over apparently ambiguous terms.

- Another Code Institute tutor, Thomas, provided some guidance regarding what dependency version numbers would be compatible.