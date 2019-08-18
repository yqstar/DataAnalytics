feature_dict={i:label for i,label in zip(
range(4),
('sepal length [cm]',
'sepal width [cm]',
'petal length [cm]',
'petal width [cm]'))}

import pandas as pd

df = pd.io.parsers.read_csv(
    filepath_or_buffer = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
    header=None,
    sep=',')

df.columns = [l for i,l in sorted(feature_dict.items())]+['class label']

df.dropna(how="all",inplace=True)

df.tail()

from sklearn.preprocessing import LabelEncoder

X = df[['sepal length [cm]','sepal width [cm]','petal length [cm]','petal width [cm]']].values

y=df['class label'].values

enc = LabelEncoder()

label_encoder = enc.fit(y)

y = label_encoder.transform(y)+1

import numpy as np

np.set_printoptions(precision=4)

mean_vectors = []

for cl in range(1,4):
    mean_vectors.append(np.mean(X[y==cl],axis=0))
    print('Mean Vector class %s:%s\n' %(cl,mean_vectors[cl-1]))


S_W=np.zeros((4,4))
for cl,mv in zip(range(1,4),mean_vectors):
    class_sc_mat = np.zeros((4,4))
    for row in X[y==cl]:
        row,mv = row.reshape(4,1),mv.reshape(4,1)
        class_sc_mat += (row-mv).dot((row-mv).T)
    S_W += class_sc_mat
print('within-class Scatter Matrix:\n',S_W)

# 引入全局均值
overall_mean = np.mean(X,axis=0)

S_B=np.zeros((4,4))
for i,mean_vec in enumerate(mean_vectors):
    n = X[y==i+1,:].shape[0]
    mean_vec = mean_vec.reshape(4,1) # make column vector
    overall_mean = overall_mean.reshape(4,1) # make column vector
    S_B += n*(mean_vec-overall_mean).dot((mean_vec-overall_mean).T)
print("between-class Scatter Matrix:\n",S_B)

eig_vals,eig_vecs = np.linalg.eig(np.linalg.inv(S_W).dot(S_B))

for i in range(len(eig_vals)):
    eigvec_sc = eig_vecs[:,i].reshape(4,1)
    print("\nEigenvector {}:\n {}".format(i+1,eigvec_sc.real))
    print("\nEigenvalue {:}:\n {:.2e}".format(i + 1, eig_vals[i].real))

# 特征值和特征向量
# 特征向量：表示映射方向
# 特征值： 特征向量的重要程度

# Make a list of (eigenvalue,eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# sort the (eigenvalue,eigenvector) tuples from high to low
eig_pairs = sorted(eig_pairs,key=lambda k:k[0],reverse=True)

# Visually confirm that the list is correctly sorted by decreasing eigenvalues
print("Eigenvalues in decreasing orders:\n")
for i in eig_pairs:
    print(i[0])

print("Variance explained:\n")
eigv_sum=sum(eig_vals)
for i,j in enumerate(eig_pairs):
    print("eigenvalue {0:}:{1:.2%}".format(i+1,(j[0]/eigv_sum).real))

W = np.hstack((eig_pairs[0][1].reshape(4,1),eig_pairs[1][1].reshape(4,1)))
print("Matrix W:\n",W.real)

X_lda = X.dot(W)

assert X_lda.shape == (150,2),"The Matrix is not 150x2 dimensional."

from matplotlib import pyplot as plt
def plot_step_lda():
    plt.figure()
    ax = plt.subplot(111)
    for label,marker,color in zip(
        range(1,4),('*','s','o'),('blue','red','green')):

        plt.scatter(x=X_lda[:,0].real[y==label],
                    y=X_lda[:,1].real[y==label],
                    marker = marker,
                    color=color,
                    alpha=0.5,
                    label=feature_dict[label])

        plt.xlabel("LD1")
        plt.xlabel("LD2")

        leg = plt.legend(loc='upper right',fancybox=True)
        leg.get_frame().set_alpha(0.5)
        plt.title('LDA:Iris projection onto the first 2 linear discriminants')

        # hide axix ticks
        plt.tick_params(
            axis="both",which="both",bottom="off",top="off",
            labelbottom="on",left="off",right="off",labelleft="on"
        )

        # remove axis spines
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["left"].set_visible(False)

        plt.grid()
        plt.tight_layout()
        plt.show()

plot_step_lda()


from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
# LDA
sklearn_lda=LDA(n_components=2)
X_lda_sklearn = sklearn_lda.fit_transform(X,y)

def plot_scikit_lda(X,title):
    plt.figure()
    ax = plt.subplot(111)
    for label,marker,color in zip(
        range(1,4),('*','s','o'),('blue','red','green')):

        plt.scatter(x=X[:,0][y==label],
                    y=X[:,1][y==label] * -1,
                    marker = marker,
                    color=color,
                    alpha=0.5,
                    label=feature_dict[label])

        plt.xlabel("LD1")
        plt.xlabel("LD2")

        leg = plt.legend(loc='upper right',fancybox=True)
        leg.get_frame().set_alpha(0.5)
        plt.title('LDA:Iris projection onto the first 2 linear discriminants')

        # hide axix ticks
        plt.tick_params(
            axis="both",which="both",bottom="off",top="off",
            labelbottom="on",left="off",right="off",labelleft="on"
        )

        # remove axis spines
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["left"].set_visible(False)

        plt.grid()
        plt.tight_layout()
        plt.show()

plot_step_lda()
plot_scikit_lda()