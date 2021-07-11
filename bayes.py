import numpy as np 
import seaborn as sns 
import pandas as pd 
import statsmodels.api as sm 
import matplotlib.pyplot as plt 
from scipy import stats 
# 给定beta2后beta1的条件分布 
def p_beta1_given_beta2(beta2, mus, sigmas): 
    mu = mus[0] + sigmas[1, 0] / sigmas[1, 1] * (beta2 - mus[1]) 
    sigma = sigmas[0, 0] - sigmas[1, 0] / sigmas[1, 1] * sigmas[1, 0] 
    return np.random.normal(mu, sigma) 
# 给定beta1后beta2的条件分布 
def p_beta2_given_beta1(beta1, mus, sigmas): 
    mu = mus[1] + sigmas[0, 1] / sigmas[0, 0] * (beta1 - mus[0]) 
    sigma = sigmas[1, 1] - sigmas[0, 1] / sigmas[0, 0] * sigmas[0, 1] 
    return np.random.normal(mu, sigma) 
# 定义抽样 
def gibbs_sampling(mus, sigmas, iter=5000): 
    samples = np.zeros((iter, 2)) 
    # 产生beta2的初值 
    np.random.seed(20210628) 
    beta2 = np.random.rand() * 10 
    
    for i in range(iter): 
        beta1 = p_beta1_given_beta2(beta2, mus, sigmas) 
        beta2 = p_beta2_given_beta1(beta1, mus, sigmas) 
        samples[i, :] = [beta1, beta2] 
    return samples
if __name__ == '__main__': 
    mus = np.array([3544800 , 2.779]) 
    st1, st2 = 1815000, 0.07841
    p = -0.861
    sigmas = np.array([[st1**2, p*st1*st2], [p*st1*st2, st2**2]]) 
# 绘制高斯混合分布的密度函数图 
    x,y = np.random.multivariate_normal(mus, sigmas, 5000).T 
    sns.jointplot(x,y,kind="kde") 
# 绘制Gibbs样本的结果 
    samples = gibbs_sampling(mus, sigmas) 
    sns.jointplot(samples[:, 0], samples[:, 1])  
