# Tuberculosis Detection in X-Rays

This project aims to build a deep learning model to detect tuberculosis in chest X-ray images.

## Session 1 (2025-09-03): Building a Baseline CNN Model

In this session, we built our first image classification model from scratch to establish a baseline performance.

### Key Steps Completed:
1.  **Project Setup:** Created a structured project directory with separate folders for data, notebooks, and source code.
2.  **Data Loading & Preprocessing:** Used `ImageDataGenerator` to create a data pipeline that:
    *   Resized all images to a uniform 150x150 pixels.
    *   Normalized pixel values from a [0, 255] range to [0, 1].
    *   Applied data augmentation (random rotations, shifts, zooms) to the training set to prevent overfitting.
3.  **Model Architecture:** Built a sequential Convolutional Neural Network (CNN) from scratch.
4.  **Training:** Trained the model for 30 epochs on the dataset.
5.  **Comprehensive Evaluation:** Performed a detailed evaluation of the model's performance on the validation set, going beyond simple accuracy.

### Baseline Model Performance:
The model trained successfully and established a performance baseline.
*   **Accuracy:** Achieved a validation accuracy of approximately 62%.
*   **AUC (Area Under the ROC Curve):** The model scored an AUC of **0.52**, indicating its ability to distinguish between TB and Healthy cases was very close to random chance.

This baseline result strongly indicates that a more powerful approach is needed, setting the stage for using Transfer Learning in the next session.

## Session 2 (2025-09-04): Comparative Analysis and Advanced Techniques

In this session, we systematically tested more advanced models and consolidated our findings.

### Key Steps Completed:
1.  **Experimented with Transfer Learning:** Tested two popular pre-trained architectures, `MobileNetV2` and `ResNet50`, to leverage their existing knowledge of image features.
2.  **Attempted Fine-Tuning:** Implemented a fine-tuning strategy on the `MobileNetV2` model by unfreezing some of its top layers to adapt them to the X-ray dataset.
3.  **Consolidated Experiments:** Created a single, comprehensive Jupyter Notebook (`06_combined_tuberculosis_detection_models.ipynb`) to centralize all four modeling approaches (Scratch CNN, MobileNetV2, ResNet50, Fine-Tuning) for clear comparison.
4.  **Planned Next Steps:** Analyzed the consistently poor performance across all models and documented a clear plan for the next session, focusing on more advanced models (`EfficientNet`) and smarter training techniques (callbacks).

### Performance Analysis:
*   The transfer learning and fine-tuning approaches **did not yield significant improvements**.
*   The `ResNet50` model failed completely, predicting only one class.
*   All models performed close to random guessing (AUC ~0.5), confirming that the dataset is challenging and requires more sophisticated methods.