# Body Doodles API

Body Doodles API is the backend service used by the [Body Doodles Application](https://github.com/Gareth-McGirr/body-doodles).

## Development Goals

The goal of this API is provide a backend service to allow the Body Doodles front end application to perform, Create, Read, Update and Delete operations via the user interface.

## Agile Planning

This project was developed using agile methodologies by delivering small features in incremental sprints. There were 3 sprints in total, spaced out evenly over three weeks.

All stories were assigned to epics, prioritized under the labels, Must have, should have, could have and assigned to sprints. "Must have" stories were completed first, "should haves" and then finally "could haves". It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be capacity.

The Kanban board was created using github projects and can be located [here](https://github.com/users/Gareth-McGirr/projects/1/views/1) and can be viewed to see more information on the project cards. All stories except the documentation tasks have a full set of acceptance criteria in order to define the functionality that marks that story as complete.

IMAGE HERE


### Epics

**Set Up**

This Epic covers all the initial setup of the Django application and Django REST Framework in order to begin coding the features.

**Posts**

This Epic covers all API endpoint creation and database connections relating to the CRUD functionality of user posts. This includes like activity.

**Comments**

This Epic covers all API endpoint creation and database connections relating to the CRUD functionality of user comments in relation to posts.

**Profiles**

This Epic covers all API endpoint creation and database connections relating to the CRUD functionality of user created profiles. This includes following functionality.

**Artists**

This Epic covers all API endpoint creation and database connections relating to the CRUD functionality of users who register as Artists.

**Reviews**

This Epic covers all API endpoint creation and database connections relating to the CRUD functionality of Artist reviews and average rating as displayed on user profile.
<hr>

## Technologies

* Django
    * Main framework used for application creation
* Django REST Framework
    * Framework used for creating API
* Google Cloud Platform
    * Used for static image hosting
* Heroku
    * Used for hosting the application
* Git
    * Used for version control
* Github
    * Repository for storing code base and docs
<hr>

## Python Packages
<details open>
<summary> Details of packages </summary>

* dj-database-url==1.0.0
    * Used to parse the DATABASE_URL connection settings
* dj-rest-auth==2.2.5
    * Used with auth system
* Django==4.1.1
    * Main framework used to start the project
* django-allauth==0.50.0
    * Used for authentication
* django-cors-headers==3.13.0
    * Used for Cross-Origin Resource Sharing (CORS) headers to responses
* django-filter==22.1
    * Used to filter API results in serializers
* django-storages==1.13.1
    * Used to help connect with the google cloud storage bucket
* djangorestframework==3.13.1
    * Framework used to build the API endpoints
* djangorestframework-simplejwt==5.2.0
    * Used with djange rest framework to create access tokens for authentication
* gunicorn==20.1.0
    * Used for deployment of WSGI applications
* Pillow==9.2.0
    * Imaging Libray - used for image uploading
* psycopg2==2.9.3
    * PostgreSQL database adapter to allow deployed application to perform crud on the postgresql db
* PyJWT==2.5.0
    * For creating the Python Json Web Tokens for authentication

Installed as package dependcies with above installations:
* asgiref==3.5.2
* autopep8==1.7.0
* cachetools==5.2.0
* certifi==2022.6.15.1
* cffi==1.15.1
* charset-normalizer==2.1.1
* cryptography==38.0.1
* defusedxml==0.7.1
* idna==3.3
* oauthlib==3.2.1
* protobuf==4.21.5
* pyasn1==0.4.8
* pyasn1-modules==0.2.8
* pycodestyle==2.9.1
* pycparser==2.21
* python3-openid==3.2.0
* pytz==2022.2.1
* requests==2.28.1
* requests-oauthlib==1.3.1
* rsa==4.9
* six==1.16.0
* sqlparse==0.4.2
* toml==0.10.2
* types-cryptography==3.3.23
* tzdata==2022.2
* urllib3==1.26.12

Auto installed as package dependencies with django-storages[GOOGLE] to aid connection to google cloud buckets for static image hosting:
* google-api-core==2.10.0
* google-auth==2.11.0
* google-cloud-core==2.3.2
* google-cloud-storage==2.5.0
* google-crc32c==1.5.0
* google-resumable-media==2.3.3
* googleapis-common-protos==1.56.4
</details>
<hr>

## **Version Control** 

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘Gars-Steakhouse’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

<hr>

## **Google Cloud Storage**

To set up bucket and service account. Please see - [Medium Article](https://medium.com/@mohammedabuiriban/how-to-use-google-cloud-storage-with-django-application-ff698f5a740f). The service account credentials will be needed for deployment.

**Code** 

Packages needed for deployment:

* django-storages[google]
* Pillow

Create a .profile file with the following line inside:

```echo ${GOOGLE_CREDENTIALS} > /app/ga-creds.json```

This line is used to instruct heroku that the GOOGLE_CREDENTIALS var is called ga-creds.json
<hr>

## **Credits**

### Content:
<br>

This article was followed in order to implement google cloud storage for static image hosting.
* [how-to-use-google-cloud-storage-with-django-application](https://medium.com/@mohammedabuiriban/how-to-use-google-cloud-storage-with-django-application-ff698f5a740f)
<br>
<br>

This  article was followed in order to implement google cloud storage for static image hosting:   
* [django-imagefield-rename-file-on-upload](https://www.dangtrinh.com/2015/11/django-imagefield-rename-file-on-upload.html)
<br>
<br>

This  article was followed in order to implement average rating calculations in the correct way
* [How to calculate average of some field in Dango models and send it to rest API?](https://django.fun/en/qa/16172/)