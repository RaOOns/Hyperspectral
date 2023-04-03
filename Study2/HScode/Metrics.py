import statsmodels.api as sm
import numpy as np
    
def R2(true, pred, version = "ssr") :
    sse = ((np.array(true) - np.array(pred))**2).sum()
    ssr = ((np.array(pred) - np.mean(true))**2).sum()
    sst = ((np.array(true) - np.mean(true))**2).sum()
    
    r2 = ssr/sst if version == "ssr" else 1 - (sse/sst)

    return np.round(r2, 3)



def MAPE(true, pred, zero = 0.00000001) :
    mape = np.mean(np.abs((np.array(true) - np.array(pred)) / (np.array(true) + zero))) * 100
    return np.round(mape, 3)



def RMSE(true, pred) :
    mse = np.mean((np.array(true) - np.array(pred))**2)
    rmse = np.sqrt(mse)
    return np.round(rmse, 3)



def MAE(true, pred) :
    mae = np.mean(np.abs((np.array(true) - np.array(pred))))
    return np.round(mae, 3)




def R2_OLS(true, pred, const = "add") :
    const_pred = sm.add_constant(pred, has_constant = const)
    ols = sm.OLS(true, const_pred).fit()
    return np.round(ols.rsquared, 3)