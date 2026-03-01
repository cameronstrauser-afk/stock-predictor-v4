import numpy as np
from scipy.optimize import minimize

def optimize(returns):

    mean = returns.mean()
    cov = returns.cov()

    def neg_sharpe(w):
        ret = np.dot(w, mean)
        vol = np.sqrt(np.dot(w.T, np.dot(cov, w)))
        return -(ret/vol)

    cons = {"type":"eq","fun":lambda w: np.sum(w)-1}
    bounds = [(0,1)]*len(mean)
    init = np.ones(len(mean))/len(mean)

    result = minimize(neg_sharpe, init, bounds=bounds, constraints=cons)
    return result.x
