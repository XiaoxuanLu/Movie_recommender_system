# Movie Recommender System

## Abstract
For this project, we are interested in investigating how recommendation algorithms work on media platforms like Netflix. We want to build our own recommendation systems and (hopefully) make a cool movie recommerdation website in the end. We plan to build several movie recommendation systems based on different methods (popularity-based, content-based) and compare them in our evaluation. Later we plan to implement our recommender in a website format. <br/>
We will use the metadata and the rating data from the Kaggle [Movie Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset). The metadata contains cast, crew, plot keywords, budget, revenue, posters, release dates, languages, production companies, countries, TMDB vote counts and vote averages for 45,000 movies. The rating dataset contains 26 million ratings from 270,000 users for all 45,000 movies. Ratings are on a scale of 1-5 and have been obtained from the official GroupLens website.

## Research questions
What are the approaches of building a movie recommender?

## Dataset
For this project, we used [The Movie Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) on Kaggle. The dataset includes Metadata on over 45,000 movies and 26 million ratings from over 270,000 users.

## A tentative list of milestones for the project

- [x] Getting the dataset
- [x] Data Cleaning and Processing
    * Keywords, missing values, number of films per year, genres
        * plot some fancy graphs pf genres, years, keywords....
- [x] Training the Recommender System
    - [x] Calculating the Weighted Rating (using the IMDB formula)
    - [x] Simple recommendation system
        * offer generalized recommendations to every user, based on movie ratings
        * user can chose based on different features, e.g. genre, language, publication year, cast
    - [x] Content-based recommendation system (based on similarity of genres and keywords)
        * maybe cosine similarity or other similarity ways to find most related n movies
- [ ] Testing and Validation
    * Compare our results to Netflix recommendations?
- [ ] Saving the Trained Model for Deployment
- [ ] Writing the report
- [ ] Creating a Website and deploying the model if time allowed
- [ ] Deploying the website on cloud if time allowed

## Division of work (for now)
- Xiaoyu: simple recommender
- Xiaoxuan: data preprocessing and work on the content-based recommender
- Yiming: feature addition of the simple recommender, later join on the content-based recommender
- Violette: content-based recommender

## Documentation
- README.md: an overview of the project
- Simple_recommender.ipynb: build a simple recommender based on ranking, langauge, runttime, and year
- Content_based_recommendation.ipynb: build a content based recommender based on the text features such as tagline, overview, and actor. Compare and combine several similarity methods to build the recommender.
- Visualizing_data.ipynb: Visualize the original dataset, and plot some fancy graphs to see if any feature is interesting to use.
