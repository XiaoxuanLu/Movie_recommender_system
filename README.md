# Movie Recommender System

## Demo website for the simple movie recommender
[Simple recommender System](https://tm22pro.herokuapp.com/)

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
- [x] Training the Recommender System
    - [x] Calculating the Weighted Rating (using the IMDB formula)
    - [x] Simple recommendation system   
         * offer generalized recommendations to every user, based on movie ratings
         * user can chose based on different features, e.g. genre, language, publication year, cast, runtime, popularity, director and cast.
    - [x] Content-based recommendation system    
         * Based on Movie Overviews and Taglines
         * Based on Movie Cast, Crew, Keywords and Genre 
         * Compared severl methods: Cosine similarity with TF-IDF and CountVectorizer & KL Divergence 
- [x] Testing and Validation
   * Compare content-based results to Netflix recommendations?
   * Compare the simple recommender to information on [IMDb website](https://www.imdb.com/chart/top/?ref_=nv_mv_250).
   * Compare the content-based recommender systems to other mainstreams such as Amazon prime videos
- [x] Saving the Trained Model for Deployment
- [x] Deploying the website on cloud if time allowed
- [ ] Writing the report

## Division of work
- Xiaoyu: simple recommender, evaluations
- Xiaoxuan: content-based recommender, website deployment
- Yiming: simple recommender, website deployment
- Violette: content-based recommender, evaluations

## Documentation
- README.md: an overview of the project
- General_recommendation_system.ipynb: build simple recommendation systems based on popularity and weighted rating we calculated. Additional features like genre, language, year, runtime, director etc are added to expand the recommender
- Content_based_recommendation_systems.ipynb: build two types of content-based recommendation systems, one is based on Overviews and Taglines and the other is based on Cast, Crew, Keywords and Genre
- Recommendation_system_watch_history.ipynb: build a content-based recommendation system based on user's watch history
- Evaluation.ipynb: evalute simple/generalized recommender and content-based recommender by comparing with mainstream movie websites
- Simple_app.py: create an app for simple recommendation system
- Content_based_app.py: create an app for content-based recommendation system
- presentation.pdf: presentation slides for the project
- ...

## How to run the project? 
- clone or download this repository to your local machine
- download the [datasets](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset/download), and save the datasets into **data** folder in the repository. 
- Install package and run app
```properties
pip install streamlit
streamlit run Content_based_app.py
streamlit run Simple_app.py
``` 

## References
Altszyler, E., Sigman, M., & Slezak, D.F. (2018). Corpus Specificity in LSA and Word2vec: The Role of Out-of-Domain Documents. Rep4NLP@ACL.

Gomez-Uribe, C. A., & Hunt, N. (2015). The Netflix Recommender System. ACM Transactions on Management Information Systems, 6(4), 1–19. https://doi.org/10.1145/2843948


Isinkaye, F. O., Folajimi, Y. O., & Ojokoh, B. A. (2015). Recommendation systems: Principles, methods and evaluation. Egyptian Informatics Journal, 16(3), 261–273. https://doi.org/10.1016/j.eij.2015.06.005

Jalali, M., Mustapha, N., Sulaiman, Md. N., & Mamat, A. (2010). WebPUM: A Web-based recommendation system to predict user future movements. Expert Systems with Applications, 37(9), 6201–6212. https://doi.org/10.1016/j.eswa.2010.02.105

Lops, P., de Gemmis, M., & Semeraro, G. (2010). Content-based Recommender Systems: State of the Art and Trends. Recommender Systems Handbook, 73–105. https://doi.org/10.1007/978-0-387-85820-3_3

Meel, P., Bano, F., Goswami, A., Gupta, S. (2021). Movie Recommendation Using Content-Based and Collaborative Filtering. In: Gupta, D., Khanna, A., Bhattacharyya, S., Hassanien, A.E., Anand, S., Jaiswal, A. (eds) International Conference on Innovative Computing and Communications. Advances in Intelligent Systems and Computing, vol 1165. Springer, Singapore. https://doi.org/10.1007/978-981-15-5113-0_22

Merve Acilar, A., & Arslan, A. (2009). A collaborative filtering method based on artificial immune network. Expert Systems with Applications, 36(4), 8324–8332. https://doi.org/10.1016/j.eswa.2008.10.029

Pal, A., Parhi, P., Aggarwal, M. (2017) An improved content based collaborative filtering algorithm for movie recommendations. 2017 Tenth International Conference on Contemporary Computing (IC3), 1-3, doi: 10.1109/IC3.2017.8284357.

‌Reddy, SRS & Nalluri, Sravani & Kunisetti, Subramanyam & Ashok, S. & Venkatesh, B. (2019). Content-Based Movie Recommendation System Using Genre Correlation: Proceedings of the Second International Conference on SCI 2018, Volume 2. 10.1007/978-981-13-1927-3_42. 

