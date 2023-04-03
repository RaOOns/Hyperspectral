# Hyperspectral
- The goal of this study is to prevent the increase of chlorophyll-a(chl-a) using hyperspectral sunlight reflected in water.

- Hyperspectral data is collected by the sensor at 15-minute intervals.

- We generated a pyhton code to predict chl-a after 15 minutes with real-time data.

- We used variable extraction such as PLS, PCA because it is real-time data and has a lot of variables.

### The data information is as follows:
- Response variable: Chl-a
- Explanatory variables:
  - Hyperspectral data: 350nm~900nm
  - meteorological/water quality data(Only study2)


### The study consists of two parts.
- **In the study1** , we predicted chl-a at the same time using only hyperspectral data at Paldang Dam in Korea(https://doi.org/10.3390/w14244080).

- **In the study2** , we predicted chl-a after 15 minutes using hyperspectral data and meteorological/water quality data at Yangpyeong Dam in Korea.
