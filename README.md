# catalog
Python3.6, Django2.1.2, Djangorestframework, PostGIS, Openlayers, jQuery, Docker-compose

The task is to create a simple Django application that satisfies the following requirements. 
 
1. Create a personnel model. It should consist of: 
 - First name; 
 - Last name; 
 - Position title. 
 
2. Create a branch model which should consist of: 
 - Branch name; 
 - Facade image (uploading to S3 is a preferred option); 
 - Latitude and Longitude (coordinates of the branch office). A user should be able to fill 
them in two ways: by typing values in the text boxes or by pointing a location on a 
map (e.g. Google Maps, but every provider would suffice) with subsequent 
autocompletion of the latitude and longitude fields. 

On the same page users should be able to add personnel to a branch (e.g. inline models can 
be used for that purpose). 
 
On the personnel list admin page, there should be a filter by first name and last name of a 
person. 

Requirements 
1. The code should be provided as a link to a Git repository (e.g. at Github or 
BitBucket). 
2. The web application should be developed using Python 3.x and Django 2.x. It should 
support production deployment with PostgreSQL. 
3. Implement a REST API that provides access to branches and personnel. 

Would be a plus 
1. Create roles for users and assign permissions to hide map coordinates editing if a 
particular user doesn’t have required permissions. 
2. Provide a Docker distribution of the application (e.g. create a Docker compose file) to 
deploy the app with all dependencies.