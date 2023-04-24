import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


class CreditScoreClassifier:
    def __init__(self, csv_file):
        self.df_train = pd.read_csv(csv_file)

    def select_samples(self):
        score1 = self.df_train[self.df_train["Credit_Score"] == 1].sample(n=100, random_state=42)
        score2 = self.df_train[self.df_train["Credit_Score"] == 2].sample(n=100, random_state=42)
        score3 = self.df_train[self.df_train["Credit_Score"] == 3].sample(n=100, random_state=42)
        self.data = pd.concat([score1, score2, score3], ignore_index=False)
        self.df_train = self.df_train.drop(self.data.index,axis=0).reset_index(drop=True)

    def train_model(self):
        X = self.df_train.drop('Credit_Score', axis=1)
        y = self.df_train['Credit_Score']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model = RandomForestClassifier(n_jobs=-1)
        self.model.fit(self.X_train, self.y_train)

    def predict(self,data):
        self.pred = self.model.predict(data)

