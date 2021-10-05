- Conversion rate:
Mostly followed the provided template, improved the logistic regression. Decision tree, random forest and SVM left to explore

- Kayak
Methodology has been requesting API for the cities weather information, then picked a random from the top 5 and scapped the hotels.
The hotel to go to is the one with the best score.
Left API key for weather info and AWS information as place holders, the code has been tested and worked

- Speed Dating
Messy dataset, have done a small handfuls of visualizations to show the use of the different libraries
Other explorations that can be done are, for example, studying the answers by race, how carreers and hobbies affect the answer, etc

- Tolk
The final project, with NLP, we had to work on logs. Preprocessed them (including spell checking), used tf-idf for vectorization and a logistic regression as model with MCCF as performance metric.

- Tweets
Deep learning NLP Project. Dataset was made of tweets that had to be preprocessed, then tokenized and vectorized. 
The model used Adam as an optimizer, poor results on the validation scores as I used a random prediction as a starter.
Left to do is trying to predict directly on the unlabelled data.

- Uber
Picked the month of July for the dataset. It was sizeable so I took a sample of 50000 lines to reduce the computing times.
Methodology has been checking the DBScan clusters, and then adjusting the KMeans' numbers of clusters accordingly to be able to compare side by side. First on the whole dataset, then on each day of the week. 
Left to do is fixing the error on the last day.

- Walmart
Supervised machine learning. Following the guidelines of the project i chose to remove the date column, as i didn't recognize a pattern, just random fluctuations. Removed the outliers in the 4 columns that had some, and imputed 10 missing values.
Score is very poor (~15%). I think this is due to the preprocessing for the most part. What can be explored is keeping the date columns and working again on the outliers as they cut a significant (~30%) of the dataset.

- Wine
Model training and endpoint testing were provided. I set up the requirements and Procfile as well as the app to be deployed.
Wrote an index page explaining how the API works (http://wine-app-mcheraki.herokuapp.com). Deployed on Heroku.
Testing the API using the Test_Endpoint notebook worked both locally and with the app deployed on Heroku, however using cUrl yielded me an error that i could not figure out.
