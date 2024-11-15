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


### Catching up aperta-api with Moments' drf-api

I rapidly coded the aspects of my API which are similar to the functionality already provided in Moments. The specifics will have been recorded within my commit history, but some occurrences worthy of explicit mention here are:

- In my ERDs, I had given each model a more descriptive first attribute than simply 'owner'. However, I realised that this would significantly impact the efficiency of code in my permissions file. Therefore, I changed all such attributes back to 'owner' and re-migrated the models.

- I refactored the views files of my posts and profiles apps to use generics. If I was a little more experienced than at present, I likely would have thought to code it that way right from the start. Code Institute's Moments walkthrough had us code the equivalent apps the longhand way and then refactor them and, because I was treating my drf-api GitHub repository as notes on how to correctly code a Django REST Framework API, I accidentally first mirrored the inefficient version that we were shown initially.

- I added 'post_text' to search_fields in the PostList view. Either the Moments walkthrough did not include an equivalent or I had missed it out, but for Aperta, it will be useful functionality to be able to search for any posts that contain certain words, essentially allowing thematic searching.

![recent git commit history](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1730566914/rapid-fire-commits_dvfpjr.png)

### Mentor Meeting and Agile Methodology

I had a mid-project meeting with my Code Institute mentor, Gareth McGirr. He clarified the importance of grouping my user stories into milestones. Informally, I had done so naturally, since I find that my user stories for each milestone/category are next to each other in my kanban board. However, I have now made it official, with one of four milestone-titling keywords being present like a label on each user story.

![milestones](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1730476903/milestones_si7l6w.png)
![milestone grouping of user stories](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1730476902/milestone-signposts_m4ys5o.png)

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

### Remove related_name from liked_post in Like model

I tried to run server and received exceptions indicating that the lack of an 's' after 'like' in my querysets, in my PostList and PostDetail views, was problematic. I noticed that there was a `related_name='likes'` in my Like model. I considered whether that needed to be there and, since there are no direct equivalents in my other models (the Follow model is different, because it links to two User instances), I decided that the simplest solution was to remove it, and that appears to have silenced the exceptions.

### Add DEFAULT_AUTO_FIELD in settings.py

When trying to run server and also when trying to dry-run making migrations, I received warnings suggesting that DEFAULT_AUTO_FIELD needed to be configured, and I have done so in settings, silencing the warnings. I then made migrations and migrated.

### Prepare settings for deployment

I examined my commits from my [drf-api GitHub repo](https://github.com/niall-code/drf-api/commits/main/), from the Moments walkthrough project, and looked carefully at all the changing and rechanging I tried before, making sure that I imitated only the final version of my settings.py file, which had appeared to be working correctly. I made some notes in relation to it. Guided by a combination of those notes and my heavily-annotated printout of Code Institute's "DRF Cheat Sheet - Deployment", I began to add to and adjust my settings and env files appropriately.

I altered SECRET_KEY, DEBUG, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS, INSTALLED_APPS, DATABASES, and MIDDLEWARE, and added JWT_AUTH_SAMESITE, CORS_ALLOWED_ORIGINS, and CORS_ALLOW_CREDENTIALS.

I generated a new secret key by temporarily creating a `key_generator.py` file, at the same level as `manage.py`, giving it the following code (as read in this article: https://www.makeuseof.com/django-secret-key-generate-new/),

> from django.core.management.utils import get_random_secret_key
> 
> secret_key = get_random_secret_key()
> 
> print(secret_key)

running `python key_generator.py`, and copying the printed string to my git-ignored `env.py` file.

In drf-api, "comment out sqlite database setting" had been done at the suggestion of a Code Institute tutor, to ensure that I was migrating to the PostgreSQL database. Therefore, at this point in my project, I have similarly replaced DATABASES value, rather than making it conditional.

I then ran `python manage.py migrate` to migrate to the newly-connected PostgreSQL database.

Finally, I ran `python manage.py createsuperuser`, to create a new superuser for that database.

### Deploy to Heroku

From my Heroku dashboard, I clicked _New_, then _Create new app_, and then gave it an app name, **aperta-api**, selected _Europe_ for region, and clicked _Create app_. Then, I clicked _GitHub_, searched for my repo (also 'aperta-api'), and clicked _Connect_, then _Enable Automatic Deploys_.

I navigated to the "Settings" tab, clicked _Reveal Config Vars_, and added key-value pairs mirroring my env file, including DATABASE_URL, SECRET_KEY, and CLOUDINARY_URL, but with DISABLE_COLLECTSTATIC instead of DEV, plus ALLOWED_HOST (assigned the value of this new app's URL, gained by clicking _Open app_, minus the `https://` on the front) and CLIENT_ORIGIN_DEV (assigned the development URL of my front-end React app). Once the React app has also been deployed to Heroku, I can also add CLIENT_ORIGIN, with the production URL.

My environment variables configured, I clicked _Hide Config Vars_, navigated back to the "Deploy" tab, and clicked _Deploy Branch_.

### Add is_staff field to CurrentUserSerializer

I added Django's `is_staff` property as a field of my `CurrentUserSerializer`. This meant that in my React app, I could add a `currentUser?.is_staff` condition to a link in the navbar.

### Amend Heroku config vars of deployed API

In my React app, I was unable to sign up. Error messages in the console indicated that it was a CORS-related issue.

![access permission error messages](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1731415530/cors-policy-issue_jegruw.png)

Here in my API, my settings file includes:

>     if 'CLIENT_ORIGIN' in os.environ:
>         CORS_ALLOWED_ORIGINS = [
>             os.environ.get('CLIENT_ORIGIN'),
>             os.environ.get('CLIENT_ORIGIN_DEV'),
>         ]

I checked the config vars of my deployed API and realised that the absence of a CLIENT_ORIGIN key meant that the present CLIENT_ORIGIN_DEV key also could not be read. I therefore added one, provisionally also with the React app's development server's URL as the value, but shall alter it once there is a production URL available.

In my React app, I saw that this cleared away the critical error, allowing my signup to complete and redirect me to the login page.

![access errors resolved](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1731415530/cors-policy-resolved_divm4t.png)

I have written that in _this_ readme because the change was in the Heroku app I had deployed from here.

### Create and migrate Block and Report models

I wrote Block and Report models and migrated them to my database.

In my previous milestone project, The Barn Owl Inn, the repo for which is also public on my GitHub, I had included a multiple choice in a Django model using IntegerField.

>     course = models.IntegerField(
>         choices=[(1, "Starters"), (2, "Main Course"), (3, "Desserts")],
>         blank=False
>     )

Therefore, for my Report model's "reason" field, I will try following that pattern - using IntegerField, rather than CharField like my ERD initially suggested.

>     reason = models.IntegerField(
>         choices=[
>             (1, "Graphic violence"),
>             (2, "Explicit sexual content"),
>             (3, "Sexualization of minors"),
>             (3, "Inciting hatred"),
>             (4, "Encouraging suicide or self-harm"),
>             (5, "Attempting to defraud"),
>             (6, "Advertising illegal products"),
>             (7, "Blatant copyright infringement"),
>             (8, "Other serious reason (please describe in 'explanation')")
>         ],
>         blank=False
>     )

### Add a related_name to liked_post in the Like model

In my React app, I was having issues with its 'Liked' page. As part of my efforts to solve it, I here added `related_name='likes'` into the `liked_post` field of my Like model, connectedly added two letter 's' within `likes/views.py`, and re-migrated.

### Addressing issues regarding front end's 'Liked' and 'Followed' pages

With the commit "add filterset_fields to views files", I enabled my React app's 'Liked' page to display posts that the logged-in user had liked, as mentioned also in the other readme.

In consultation with Code Institute tutor Holly, while trying to fix my front end's 'Followed' page, I made three trial-and-error commits also relating to `filterset_fields`, also on 14 Nov. '24. In combination with a small adjustment to the React app's `App.js` file, the 'Followed' page was indeed eventually fixed.

### Re-migrate Report model

![making a migration](https://res.cloudinary.com/dlqwhxbeh/image/upload/v1731677613/re-migrate_report_qmmcuc.png)

## Credit

- My project has been significantly based on my previous codealong work from Code Institute's Moments walkthrough project, but with additional functionality, including two new models, and other miscellaneous alterations.

- My Code Institute mentor, Gareth McGirr, suggested the convenient inclusion of the 'reported' attribute in my Post model, and provided general support with clarifying my ideas and priorities for the project.

- A Code Institute tutor, Sarah, helped while writing my Follow model by clarifying a confusion over apparently ambiguous terms.

- Another Code Institute tutor, Thomas, provided some guidance regarding what dependency version numbers would be compatible.