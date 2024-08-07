def cov1Para(Y,k = None):

    #Pre-Conditions: Y is a valid pd.dataframe and optional arg- k which can be
    #    None, np.nan or int
    #Post-Condition: Sigmahat dataframe is returned

    import numpy as np
    import pandas as pd
    import math

    # de-mean returns if required
    N,p = Y.shape                      # sample size and matrix dimension

    #default setting
    if k is None or math.isnan(k):

        mean = Y.mean(axis=0)
        Y = Y.sub(mean, axis=1)                               #demean
        k = 1

    #vars
    n = N-k                                    # adjust effective sample size

    #Cov df: sample covariance matrix
    sample = pd.DataFrame(np.matmul(Y.T.to_numpy(),Y.to_numpy()))/n

    # compute shrinkage target
    diag = np.diag(sample.to_numpy())
    meanvar= sum(diag)/len(diag)
    target=meanvar*np.eye(p)

    # estimate the parameter that we call pi in Ledoit and Wolf (2003, JEF)
    Y2 = pd.DataFrame(np.multiply(Y.to_numpy(),Y.to_numpy()))
    sample2= pd.DataFrame(np.matmul(Y2.T.to_numpy(),Y2.to_numpy()))/n     # sample covariance matrix of squared returns
    piMat=pd.DataFrame(sample2.to_numpy()-np.multiply(sample.to_numpy(),sample.to_numpy()))

    pihat = sum(piMat.sum())

    # estimate the parameter that we call gamma in Ledoit and Wolf (2003, JEF)
    gammahat = np.linalg.norm(sample.to_numpy()-target,ord = 'fro')**2

    # diagonal part of the parameter that we call rho
    rho_diag=0;

    # off-diagonal part of the parameter that we call rho
    rho_off=0;

    # compute shrinkage intensity
    rhohat=rho_diag+rho_off
    kappahat=(pihat-rhohat)/gammahat
    shrinkage=max(0,min(1,kappahat/n))

    # compute shrinkage estimator
    sigmahat=shrinkage*target+(1-shrinkage)*sample

    return sigmahat