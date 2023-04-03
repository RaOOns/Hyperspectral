# Study1: Predicting chlorophyll-a at the same time

We compared several pipelines to select an optimal pipeline.


### Data preprocessing
- None
- Standard Scaler
- Min-Max Scaler
- Principal Components Analysis(PCA)
- Partial Least Sqaure(PLS)

### Models
- Ordinary Least Squares
- Random Forest
- Extremely Randomized Tree
- Gradient Boosting
- AdaBoost
- K-Nearest Neighbor
- Support Vector Regression
- XGBoost

### Evaluation measures
- **R-square:** This is an applied evaluation metric for fit regression models that is used mainly in hydrological studies. However, there is a disadvantage that R-square increases unconditionally when the number of variables increases.
- **Nash-Sutcliffe efficiency(NSE):** This metric reflects the desirable and undesirable features of a model of interest, and it increases as the quality of the model increases. However, it is sensitive to extreme values because it uses squared differences, and it cannot identify model bias.
- **d:** This consists of MSE and potential error (PE). It offers the advantage that errors and differences are given an appropriate weightage that is not inflated by squared values. However, it is sensitive to extreme values because it uses squared differences.
- **Root mean square error(RMSE):** This metric is obtained by applying the root to the mean of the total squared error (the sum of the individual squared errors). Therefore, it increases when the variance associated with the frequency distribution of error magnitudes increase.
- **RSR(RMSE-observations standard deviation ratio):** This metric standardizes RMSE using the standard deviation of the observations. Therefore, a lower RSR means better model performance and a lower RMSE.
- **Percent bias(PBIAS):** This measures the average tendency of the simulated data to be larger or smaller than their observed counterparts. That is, positive values indicate a model underestimation bias, and negative values indicate a model overestimation bias. It is useful for continuous long-term simulations and can help identify the average model simulation bias.

<p align="center"><img src="https://user-images.githubusercontent.com/79679194/229425474-5738f956-c53a-4c89-be7c-d4d83349b434.PNG" height="400px" width="600px"></p>
