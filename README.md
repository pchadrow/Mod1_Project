# Microsoft Movie Studio Exploration
## Preliminary Case Study

[Presentation](./Microsoft_Movie_Studio.pdf)
[Presentation Video]()
[Relevant Blog](https://medium.com/@pchadrow/a-data-science-beginners-first-foray-into-film-analysis-80f4694b4ee2)




## Purpose
To investigate the popularity and performance of specific genres along with the optimal production crew size in terms of how many directors and writers should be hired to produce a new film.

## Data Description
<details><summary>List of Files</summary>
* bom.movie_gross.csv.gz
* imdb.title.basics.csv.gz
* imdb.title.crew.csv.gz
* imdb.title.ratings.csv.gz
* tmdb.movies.csv.gz
* tn.movie_budgets.csv.gz
</details>
## Question 1 

### Which Genres Are the Most Popular?
*This question was explored by team member Leighanna and in the event that I failed to capture working elements of her code, her original work can be found in her [repository](https://github.com/leighannajo/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320).* <details><summary>Relevent Files</summary>
* [TMDB Genres v Popularity Cleaning](./TMDB_Genres_v_Popularity_Cleaning-L.ipynb)
* [Question 1](./Question_1-l.ipynb) </details>
### EDA

Using The Movie Database API we were able to decode their genre IDs to properly identify their genres and compare them against their developed popularity rating to find which genres seemed to be the most popular. 
![genretable](/images/genrebefore.png) ![genreid](/images/genreids.png)

After being able to separate out and identify each films unique genres we were then able to plot the data
![plot1](/images/lplot1.png)
From here we could further narrow our view to the top 9 genres.
![plot2](/images/lplot2.png)
### Conclusion
Ultimately we were able to determine that in terms of popularity, Action films ranked the highest. Followed by Animation and Drama. In our next question we'll compare these to our top grossing films to see if there's any correlation.

## Question 2
### What Are The Top Performing Genres Financially?
*This question was explored by team member Kaila and in the event that I failed to capture working elements of her code, her original work can be found in her [repository](https://github.com/kailakay/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320).* <details><summary>Relevant Files</summary> 
* [Plotting Genre Finance Info](./Plotting_Genre_Finance_Info-k.ipynb)
* [Question 2](./Question_2-k.ipynb)
</details>

### EDA 
After cleaning and priming the data we could look at the top grossing genres followed by the most expensive genres to produce.
![topgenre](/images/q2-top-7-genres.png)
![mostexpensive](/images/q2-genre-budget.png)
From here we could see a trend that showed the highest grossing genres also seemed to have high production budgets. We also noted that both Action and Animation were both very popular as well as high grossing. Next we would graph the return on investment of the top 6 genres to see how these compared. 
![violin](/images/q2-roi-violin.png)
### Conclusion
Comparing the results with our previous question, we can recommend the Action genre as a primary focuse due to both its high popularity, gross, and average ROI of 116%. Other genres worth looking into would be Adventure and Animation for fairly consistent results. 

## Question 3
### What Is The Optimal Crew Size and Their Affect on Film Financials
*This question was explored by myself*<details><summary>Relevant Files</summary>
* [Data Overview](./Data_Overview.ipynb)
* [Cleaning](./Cleaning.ipynb)
* [Question 3](./Question_3.ipynb)
</details>

### EDA
Here we would break down each film to determine how many writers and directors they had.
![table](/images/table.png)
This gave us quite a few unique combinations of varying numbers of both directors and writers on films. I decided to look a little deeper at how  our data was dispersed to help find a focus point.
![counts](/images/counts.png)
From here we could easily see that there just wasn't enough data to find accurate trends for films with more than three directors. Looking into writer trends we also noticed fewer and fewer pieces of data for films as the number of writers increased, so we narrowed our field of view even more.
![comparison](/images/plot3.png)
Here we see that both, the number of writers and number of directors, follow the same trend with gross and production budget. 
Having found the majority of films in our data to have one director and a range of 1 to 4 writers, we would see how this trend looked when compared specifically to the top genres we identifed previously. 
![last](/images/finalplot.png)

## Final Conclusion
Having priortized our top genres, it does appear to have some variance among crew sizes depending on genre. Our main recommendation of Action films would best be suited with a single director and 1 - 3 writers, while Animation and Adventure both could benefit from 2 - 4 writers. 

Given more time, we would like expound upon these findings to find deeper trends from a larger data set. We would also like to explore the affects of release date and runtime on popularity and profitability. I also believe a comparion of studios would be beneficial to identify competition, saturation, as well as niche markets. 