# AI-Learning-Journey
A curated portfolio showcasing my journey in artificial intelligence and machine learning. This repository contains a collection of projects demonstrating my skills in areas like natural language processing, computer vision, and data analysis.

## Recent Activities (as of 2025-09-03)
- **Initiated the `006_Tuberculosis_Detection` project.**
- Built a complete, end-to-end image classification pipeline from scratch, including data preprocessing, augmentation, model building (CNN), training, and a comprehensive evaluation (Accuracy, Confusion Matrix, Classification Report, ROC/AUC).
- Established a baseline model performance (AUC: 0.52), which highlights the challenges of working with small datasets and provides a clear motivation for using Transfer Learning next.

## Projects

### [006_Tuberculosis_Detection: Computer Vision for Medical Imaging](./006_Tuberculosis_Detection/) (In Progress)

This project focuses on building a deep learning model to detect signs of tuberculosis in chest X-ray images. It serves as a practical application of computer vision for a real-world medical problem.

**Key Activities:**
- **Baseline Model:** A Convolutional Neural Network (CNN) was built from scratch to establish a performance baseline.
- **Data Preprocessing:** Implemented a robust data pipeline using `ImageDataGenerator` for normalization and data augmentation.
- **Comprehensive Evaluation:** Analyzed model performance not just with accuracy, but with professional diagnostic metrics like Sensitivity, Specificity, PPV, NPV, and the ROC/AUC score.

**Technologies Used:** Python, TensorFlow, Keras, NumPy, Matplotlib, Scikit-learn

### [000_Assignments: NLP Auto-Complete](./000_Assignments/)

This project involves building a prototype of an auto-complete system using N-gram language models. It's an assignment from Coursera's "Natural Language Processing with Probabilistic Models" course.

**Key Features:**
- Text preprocessing and tokenization.
- N-gram counting and probability estimation.
- Perplexity calculation for model evaluation.

**Technologies Used:** Python, NLTK, Pandas, NumPy

### [001_Data_Analysis: Roller Coaster, Netflix & FRED EDA](./001_Data_Analysis/)

An exploratory data analysis (EDA) of three datasets: roller coasters, Netflix movies, and FRED economic data. This project involves data cleaning, preparation, and visualization to uncover insights.

**Key Findings (FRED Economic Data):
- The S&P 500 index shows significant growth over time, with notable fluctuations during economic events.
- The national unemployment rate exhibits cyclical patterns, with sharp increases during recessions.
- State-level unemployment data reveals regional disparities in economic performance, particularly during the COVID-19 pandemic.

**Technologies Used:** Python, Pandas, Matplotlib, Seaborn, fredapi, Plotly

### [002_NLP: Natural Language Processing Projects](./002_NLP/) (In Progress)

This folder contains various Natural Language Processing (NLP) projects, including a voice assistant and a sentiment analysis model.

**Key Projects:**
- **IMDb Sentiment Analysis with TensorFlow:** A Jupyter Notebook demonstrating sentiment analysis on movie reviews, covering data preprocessing, model building, training, and evaluation.
- **Python Voice Assistant:** A simple voice-controlled assistant capable of recognizing voice commands and performing basic tasks.

**Technologies Used:** Python, TensorFlow, Keras, NumPy, Pandas, Matplotlib, Seaborn, SpeechRecognition, pyttsx3, PyAudio

## Getting Started

To run these projects, clone the repository and install the required dependencies for each project as listed in their respective README files.

```bash
git clone https://github.com/your-username/AI-Learning-Journey.git
cd AI-Learning-Journey
```

## Contact

For any questions or collaborations, please feel free to reach out.
