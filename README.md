# book-api
Book api.


## Core app
Although, this is not necessary, I created the **core app** to support admin users whom will be able to use the /admin interface 
to make changes to the wish list.

##Flake8
I added Flake8 to have Travis ci tool build tests upon commits pushes.

For creating the api client which sends a request to "website". I decided to use APIViews because it gives me the most 
control for the application logic and this is perfect for calling other APIs/services. 
