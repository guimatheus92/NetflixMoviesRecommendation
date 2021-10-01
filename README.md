# NetflixMoviesRecommendation
This is a movie recommendation system project that I developed to put into practice some Machine Learning techniques, so the goal is for the user to choose a movie that have already been watched and receive the recommendation of new movies related to the chosen one.

## Project structure
    .
    └── NetflixMoviesRecommendation
        ├── app.py                       # setup our app
        ├── models.py                    # our user personalized ML model
        └── model                        # store necessary files in order to run sucessfully
        └── templates
            ├── index.html               # show the home page
            └── games.html    	         # show the movies page
        └── static
            ├── img                      # store images for this application
            ├── css                      # store css scripts for this application
            ├── js                       # store js scripts for this application
            ├── sass                     # store scss scripts for this application
            ├── webfonts                 # store fonts scripts for this application

## Tutorial

The tutorial of this application can be found on [GitHub Wiki](https://github.com/guimatheus92/Game-Recommendation-System/wiki/Tutorial-on-how-to-get-a-recommendation "GitHub Wiki") page.

## Changelog

- **30/09/2021**: Deployed the full project.

## Observationns

- I had to create the variable `movie_sparse_matrix` during the process, because the `.npz` file was greater than 2gb, so that's why we are not loading as the sparse file as for example `train_sparse_matrix`.

## Conclusion

1. Want my code? [Grab it here](https://github.com/guimatheus92/NetflixMoviesRecommendation "Grab it here") 📎
2. Want the tutorial of how to use it? [Go to Wiki](https://github.com/guimatheus92/Game-Recommendation-System/wiki/Tutorial-on-how-to-get-a-recommendation "Go to here") ✔️
3. Check the article on [Medium](https://guimatheus92.medium.com/get-new-netflix-movies-by-a-recommendation-system-afbb5d4c0e31 "Medium") about this development 📌
4. 3. Check the article on [Medium](https://guimatheus92.medium.com/deploy-python-application-on-amazon-web-services-aws-6d8bd385b5b "Medium") about this deploy 📌
5. New ideas for this app? Help me to improve it ❤️
6. Want something else added to this tutorial? Add an issue to the repo ⚠️
