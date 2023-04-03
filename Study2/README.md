# Study2: Predicting Chlorophyll-a after 15-minute

We generated a pyhton code to predict chl-a after 15 minutes with real-time data.


- We needed to reconstruct the data because the time zones of the three datasets did not exactly match(hyperspectral/meteorological/water quality data).

- We reconstructed the data in the form of lag data.

- We used PLS method to reduce the number of variables and time taken.
<p align="center"><img src="https://user-images.githubusercontent.com/79679194/229430973-af03f2af-323e-42c0-9b1e-b2dadc24719c.PNG" height="300px" width="400px"></p>

- We created a basic model using a dataset from March and predicted chlorophyll-a in April .
<p align="center"><img src="https://user-images.githubusercontent.com/79679194/229431031-af6a57b2-64e0-42c5-916c-0da3c4525fbb.PNG" height="300px" width="800px"></p>

- We used the five prediction method.
  - Random Forest
  - Extremely Randomized Tree
  - LightGBM
  - 1D-CNN
  - Ensemble
