# Streamer-Interactivity-Analyzer
This GitHub repository contains a machine learning project focused on analyzing short clips from YouTube videos of streamers to measure the level of interactivity. The project utilizes techniques to extract insights from both the number of comments and the audio data of the stream clips.

## Project Overview
The objective of this project is to understand the level of interactivity in YouTube streamer videos by examining two key factors: the number of comments received during specific time intervals, text analysis of those comments, and the characteristics of the audio in those clips. By combining these two aspects, the project aims to provide insights into the level of engagement and interactivity within the videos.

## Project Workflow
- Data Collection: Collect YouTube streamer videos that are relevant to the analysis. These videos should have comment data available and cover a diverse range of streamers and topics

- Clip Extraction: Extract short clips from the collected videos to focus on specific segments of interest. These clips should capture different levels of interactivity and engagement

- Comment Analysis: Analyze the number of comments received during each clip and aggregate them into meaningful time intervals. This step helps identify periods of high and low interactivity

- Audio Processing: Process the audio data of each clip to extract relevant features such as speech intensity, sentiment, or acoustic characteristics. These features provide additional insights into the level of interactivity

- Feature Integration: Combine the extracted features from both the comment analysis and audio processing stages to create a comprehensive dataset for further analysis

- Model Training: Utilize machine learning algorithms, such as regression or classification models, to train a model on the integrated dataset. The model should learn to predict or classify the level of interactivity based on the combined features

- Model Evaluation: Evaluate the trained model's performance using appropriate metrics, such as accuracy or mean squared error, to assess its effectiveness in predicting interactivity levels

- Interpretation and Insights: Analyze the results of the model to gain insights into the relationship between the number of comments, audio characteristics, and the level of interactivity. Extract meaningful conclusions and observations from the analysis
