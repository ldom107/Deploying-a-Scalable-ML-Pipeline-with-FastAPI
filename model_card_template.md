# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This machine learning project uses a Random Forest Classifier to predict whether an individual's annual income is <= $50K or > $50K, utilizing demographic and employment information from the Census Income dataset located in the UC Irvine Machine Learning Repository. The model was implemented using Python and the scikit-learn machine learning library. Random Forest Classifier is an ensemble machine learning algorithm that combines predictions from multiple decision trees to recognize patterns and classify which category the individual belongs to, <= $50K or >$50K. This model is part of a machine learning pipeline that includes data preprocessing, model training, inference, and performance evaluation.

## Intended Use

The intended use of this project is to demonstrate the application of supervised machine learning to a classification problem. It also demonstrates how a machine learning pipeline can process data, train a model, generate predictions, and evaluate performance using multiple evaluation metrics. The model is intended for educational and experimental purposes only, and it is not designed for real world financial and employment decisions. Its predictions should not be used as a defining representation of an individual's financial circumstance or earning potential.

## Training Data

The model was trained using the Census Income dataset provided by the UCI Machine Learning Repository. The original dataset contains 32,561 records and 15 columns. The dataset features include: age, workclass, education, marital status, occupation, relationship, race, sex, capital gain, capital loss, salary, and other demographic and employment information. The dataset was divided into training and testing subsets using an 80/20 split. The training dataset contained 26,048 records, and it was used to fit the machine learning model, while the remaining 20% was reserved for testing and evaluating model performance. Before training, categorical features were transformed into numerical representations using OneHotEncoder, and the salary feature was converted into a binary value using LabelBinarizer. These preprocessing steps allowed the categorical information to be processed by the classification algorithm.

## Evaluation Data

The testing subset contained 20% of the original dataset, totaling 6,513 records. These records were randomly selected and separated from the training data and were not used to fit the machine learning model. The testing data followed the same preprocessing transformations as the training data using OneHotEncoder and LabelBinarizer. This ensured consistency between the training and testing subsets, and it allows the model's performance to be evaluated on unseen data. The trained model's predictions were compared against the actual income in the testing dataset to measure performance. Additional evaluations were conducted across individual values within each categorical feature, providing insight into the model's performance across different data groups. The performance metrics results were saved in the slice_output.txt file.

## Metrics

The model was evaluated using precision, recall, and F1 score. These metrics were selected to assess different aspects of the model's classification performance, particularly its ability to correctly identify whether an individual's income is <=$50K or >$50K. The model achieved a precision score of 73.59%, a recall score of 63.84%, and an F1 score of 68.37%. The precision score measures the proportion of positive predictions that were correctly classified, the recall score measures the proportion of actual positive cases that the model correctly identified, and the F1 score combines both precision and recall using their harmonic mean to provide an overall measure of the model's ability to balance both metrics. 

## Ethical Considerations

The Census Income dataset contains demographic characteristics such as age, race, sex, and native country. These characteristics are important to consider because historical income data may reflect existing social and economic inequalities. Since the model is trained using this information, it may learn patterns that reflect biases and potentially reinforce them when making predictions. The use of demographic characteristics may also result in differences in prediction performance across different groups of people. Even though the model is designed to identify patterns in the dataset, its predictions should not be interpreted as an accurate representation of an individual's abilities, financial standing, or earning potential. Additional fairness evaluations are needed to determine whether certain demographic groups experience more prediction errors than others. For these reasons, the model should only be used for educational and experimental purposes.

## Caveats and Recommendations

The model has multiple limitations that should be considered when interpreting its predictions. First, the Census Income dataset represents historical information and may not accurately represent current economic conditions or income distributions. Second, the model achieved an F1 score of 68.37% on the testing dataset. This indicates that its predictions are not consistently accurate and improvement is needed. The approximate 10% difference between the precision and recall score also indicates that the model does not identify all individuals earning >$50K.

Another limitation is that the overall performance metrics does not represent performance across every demographic or categorical group. The slice-level results should be reviewed to identify groups that may have lower precision, recall, or F1 scores. 

Future improvements could include testing other classification algorithms, adjusting model parameters, and conducting additional fairness evaluations. These changes could improve prediction performance and provide a better understanding of how the model performs across different demographic groups. Overall, this model is best suited for educational and experimental purposes to demonstrate a machine learning pipeline, and it should not be used for real world decisions. 