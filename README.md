# Book API
This API let's the user search for books using open library's API and returning
a list of details for all the books related to this search. In addition, users
have the ability to add and remove books, as well as seeing the current list.

## Prerequisites and Installation
[Install Docker from this link.](https://docs.docker.com/v17.12/install/#supported-platforms) 

## Setup
After having installed Docker, follow the next steps to run the app locally.

1. To build the images and services from the docker-compose.yml file run:
    ```
    docker-compose build
    ```

1. To build the images and start the containers run:
    ```
    docker-compose up
    ```
   Note: If the images do not exist it will build them.

Note: If you encounter any DB problems run:
    ```
    docker-compose down
    ```
It will stops and remove the containers, networks, volumes, and images created 
by docker-compose up.

## Getting Started
### Using WishList API
1. To see the list of wish list books, make a GET request to:
    ```
    http://0.0.0.0:3000/wish-list/
    ```

1. To add a book to the wish list make a POST request to:
    ```
    http://0.0.0.0:3000/wish-list/
    ```
    The request must always include the following parameters in the body:
    ```
    "ol_id": "OL1532643M"
    ```
   
   Note: The API is setup, so when you provide the **ol_id** in the POST
   request, it will automatically make a request to Open Library that will go 
   and get the following fields: title, publish_date, number_of_pages, 
   physical_format, genres, isbn_13, isbn_10, description.
   
 1. To remove a book from the wish list, send a DELETE request to:
    ```
    http://0.0.0.0:3000/wish-list/<wish_list_id>/
    ```
    
### BookSearch API
1. To perform a search of books, you can simply add query parameters to the
**book-search** end point. For instance:
    ```
    http://0.0.0.0:3000/api/book-search/?q=the+lord+of+the+rings
    ```
   Note: This API supports adding multiple query parameters, so feel free to
   try adding more ;).
   
## Running tests
To run all tests in this project, from the command line run:
    ```
    docker-compose run app sh -c "python manage.py test"     
    ```

## Running flake8
To follow PEP8 style standards, flake8 was added. Flake8 is a tool that
will make sure we are following good PEP8 practices. Flake8 will be run when
committing new changes to the Github Repository, but it can be run with the
following command as well:
```
 docker-compose run app sh -c "flake8"   
```

##Architectural decisions
###App
1. PostgreSQL was the data store tool used as it is versatile and provides a lot
of support for Django queries.

1. Docker was used to make it easier to create, deploy, and run the app 
by using containers. As known, Containers allow a developer to package up an 
application with all of the parts it needs, such as libraries and other 
dependencies, and ship it all out as one package.

### Book Search API
1. For creating the book-search API client, I decided to use the Django
APIViews because it gives the most control over the application logic which 
is perfect for making external API calls. 

1. When making a search the API, it will return a compressed list of details 
for the books that match the search criteria.

1. TravisCI was used to integrate a have continuous integration workflow. 
TravisCI will run tests, and inform the developer if the build fails.

###Wish List app
1. In the models, I decided to add a list of what I think are the most 
important details of a book. It was a little tricky because the API doesn't 
have a way to make API requests to book end-point using the open library id.
Although, I found some documentation about it, it didn't work as expected.
However, I found that I have access to a book's API by adding the Open Library
book's ID to the following URI ending with .json. See example:

    ```
    http://openlibrary.org/work/<open_library_id>.json
    ```

1. For the views, I used the ModelViewSet because it comes with all the HTTP
protocol requests, and it makes it easier to write the API as I already have
a Model available.

##Thoughts and Improvements
1. Both wish_list and book_search_api apps could be under one app or folder, 
but for the future, if the app scales up, I thought it might be a better idea 
to have them be in 2 separate Django apps. Although, these 2 apps are returning
a list of books, their functions are different. One returns a simple list of
books containing book details, the other one store books in the wish-list.

1. I decided to create only 1 model for managing the wish list. However, it 
would be better to create a Book and WishList model where the WishList table 
contains Book id's. This will prevent books from completely being remove from
the database when sending a DELETE request the the wish-list API endpoint.

1. As the app scales, models for authors, ISBNs, etc might be added as adding
a ArrayField would not the most optimal for querying and storing book data.

1. To improve performance, I would look into adding a caching tool such as 
Redis to cache searches and then looking in the cache to see if a book exists
instead of making another request to the Open Library API when trying to add
a book to the Wish List.

1. To be able to find out more details about failures, I would use a logging
tool such as LogDNA to get a good idea when things fail and how.

1. Perhaps, I would improve the naming convention of the Django Apps.

### Core app
Although, this is not necessary, I created the **core app** to support admin 
users whom will be able to use the admin interface to make changes to the wish 
list.

## Authors
* **Anthony Torres**

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) 
file for details
