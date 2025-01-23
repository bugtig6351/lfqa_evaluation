import numpy as np
from scipy.stats import spearmanr, kendalltau

def calculate_correlation(x, y, corr='r'):
    if corr == 'r':
        corr, _ = spearmanr(x, y)
    else:
        corr, _ = kendalltau(x, y)

    return corr*100

def generate_relation_sequence(seq):
    # 生成序列的偏序关系列表
    n = len(seq)
    relation_seq = []
    for i in range(n):
        for j in range(i + 1, n):
            if seq[i] > seq[j]:
                relation_seq.append(1)
            elif seq[i] == seq[j]:
                relation_seq.append(0)
            else:
                relation_seq.append(-1)
    return np.array(relation_seq)

def calculate_agreement(x, y, with_tie=True):
    #计算两个序列中每两个元素偏序关系的一致性
    assert len(x) == len(y)
    assert len(x) > 0
    X = generate_relation_sequence(x)
    Y = generate_relation_sequence(y)
    if not with_tie:
        # 不包括平局的情况
        idx = np.where(X != 0)
        X = X[idx]
        Y = Y[idx]
    
    consistency_count = sum(1 for a, b in zip(X, Y) if a == b)/len(X)
    
    return consistency_count

def cal_winrates(matrix, with_tie=True):
    # 计算矩阵中每两列(model i 与model j)之间的胜率和model i的平均胜率
    # matrix.shape = (m,n) # queries*models
    n = matrix.shape[1]
    winrates = np.zeros((n,n))
    for i in range(n):
        for j in range(i+1, n):
            if with_tie:
                # m个问题中，每个model_i>model_j的得1分+平局得0.5分    
                winrates[i,j] = (sum(matrix[:,i] > matrix[:, j])+sum(matrix[:,i] == matrix[:, j])/2) / (matrix.shape[0]) 
                # print(i,j,sum(matrix[:,i] > matrix[:, j]), sum(matrix[:,i] == matrix[:, j])/2, winrates[i,j])
            else:    
                winrates[i,j] = sum(matrix[:,i] > matrix[:, j]) / (matrix.shape[0])
            winrates[j,i] = 1 - winrates[i,j]
    return winrates, np.sum(winrates,axis=1)/(winrates.shape[0]-1)