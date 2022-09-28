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



### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘Gars-Steakhouse’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

<hr>

### Google Cloud Storage

To set up bucket and service account. Please see - [Medium Article](https://medium.com/@mohammedabuiriban/how-to-use-google-cloud-storage-with-django-application-ff698f5a740f). The service account credentials will be needed for deployment.

**Code** 

Packages needed for deployment:

* django-storages[google]
* Pillow

Create a .profile file with the following line inside:

```echo ${GOOGLE_CREDENTIALS} > /app/ga-creds.json```

This line is used to instruct heroku that the GOOGLE_CREDENTIALS var is called ga-creds.json

## Credits

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