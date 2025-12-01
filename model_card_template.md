# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This current model uses random forest classifier from the sklearn package for the classification tasks. 
## Intended Use
The intended use of this program is predict whether a person makes over 50k or not based on the census data provided by the class. 
## Training Data
The training data is census data from 1996 that was collected by Ron Kohavi.
The data within the rows respent individuals and their demograhpic along with their income information. 
The training data was 80% of the total dataset. 

## Evaluation Data
The evaluation data is the last 20% of the data that was split. processed the same way as the training data. 
## Metrics
_Please include the metrics used and your model's performance on those metrics._
Precision: 0.74
Recall: 0.64
Fbeta: 0.69
## Ethical Considerations
This dataset could be bias since it has information on demographic information like race and sex. Also this data can't be used for any real decision making in the real world. 
## Caveats and Recommendations
I would recommend that the data is updated as the data is very old and can't be used in any real world decision making.