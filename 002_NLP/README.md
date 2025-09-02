# NLP Projects

This directory contains various Natural Language Processing (NLP) projects.

## File Descriptions

- `Chatbot.py`: A Python script for a simple rule-based chatbot.
- `voice_assistant.py`: A Python script for a voice-controlled assistant.
- `improvement_suggestions.txt`: A text file containing ideas for improving the voice assistant and chatbot.
- `requirements.txt`: A text file listing the Python dependencies for the voice assistant and chatbot.
- `Sentiment_Analysis_IMDb/sentiment_analysis_IMDb.ipynb`: A Jupyter Notebook that demonstrates sentiment analysis on the IMDb movie review dataset using TensorFlow and Keras. It covers data loading, preprocessing, model building (embedding, pooling, dense layers), training, evaluation, and prediction.

## NLP Projects Table

| Title | Dataset Name | Notes |
|---|---|---|
| [IMDb Sentiment Analysis with TensorFlow](./Sentiment_Analysis_IMDb/sentiment_analysis_IMDb.ipynb) | IMDb Movie Reviews | Building and training a deep learning model to classify movie reviews as positive or negative. |

## Dependencies

The projects in this folder may require the following Python libraries:

- tensorflow
- numpy
- pandas
- matplotlib
- seaborn

You can install these dependencies using pip:

```bash
pip install tensorflow numpy pandas matplotlib seaborn
```

## Key Findings

### IMDb Sentiment Analysis
- The sentiment analysis model achieved an accuracy of approximately 85.3% on the test dataset.
- The notebook demonstrates effective text preprocessing techniques, including HTML tag removal and punctuation stripping.
- It showcases the application of TensorFlow's `TextVectorization` layer for preparing text data for neural networks.
- A simple sequential deep learning model with embedding, global average pooling, and dense layers is effective for binary sentiment classification.