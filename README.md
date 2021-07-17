# Twitter-Sentiment-Analysis

## Understanding Problem Statement

In this project we want to classfiy a tweet as Racist/Sexist or neutral
<br>
We have two classes : 

 - 1 Racist/Sexist
 - 0 Neutral

_You can access the problem statement and the data over [here](https://datahack.analyticsvidhya.com/contest/practice-problem-twitter-sentiment-analysis/)_

## Convertin Words into features

 - Bag of Words
 - TF-IDF
 - Word2Vec
 
 ## Model Building
 
<div>
        <table>
            <caption>F1 Score of different models</caption>
            <thead>
                <tr>
                    <th>Model</th>
                    <th>Bag of Words</th>
                    <th>TF-IDF</th>
                    <th>Word2Vec</th>
                </tr>
                <tr>
                    <td>Logistic Regression</td>
                    <td>52.1</td>
                    <td>58.7</td>
                    <td>59.4</td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>SVM</td>
                    <td>52.6</td>
                    <td>56.7</td>
                    <td>62.1</td>
                </tr>
                <tr>
                    <td>Random Forest</td>
                    <td>63.2</td>
                    <td>61.4</td>
                    <td>58.3</td>
                </tr>
                <tr>
                    <td>XGBoost</td>
                    <td>56.2</td>
                    <td>55.2</td>
                    <td>69.7</td>
                </tr>
            </tbody>
        </table>
    </div>
    
    We got the best score with XGBoost on Word2Vec so we will be using that as our final model.
