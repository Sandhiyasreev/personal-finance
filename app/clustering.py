import pandas as pd
from sklearn.cluster import KMeans

def get_cluster(income, expenses, savings):
    X = pd.DataFrame([[income, expenses, savings]], columns=['income', 'expenses', 'savings'])
    model = KMeans(n_clusters=3, random_state=42)
    mock_data = pd.read_csv("app/sample_data.csv")[['income', 'expenses', 'savings']]
    model.fit(mock_data)
    cluster = model.predict(X)[0]

    profiles = {0: "💰 Saver", 1: "💸 Spender", 2: "📈 Investor"}
    return profiles.get(cluster, "Unknown")
