from ml_model import CreditScoreClassifier

csc = CreditScoreClassifier('clean_data.csv')
df=csc.df_train
csc.select_samples()
csc.train_model()
data=csc.data[:100].sample(n=10)
data = data.drop('Credit_Score', axis=1)
csc.predict(data)
predict=csc.pred
print(predict)

print(data)
