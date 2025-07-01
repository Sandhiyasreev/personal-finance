import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import plotly.graph_objects as go

# 1. 📊 Pie Chart: Savings vs Debts
def savings_vs_debt_pie(savings, debts):
    fig, ax = plt.subplots()
    ax.pie([savings, debts], labels=["Savings", "Debts"], autopct='%1.1f%%')
    ax.set_title("Savings vs Debts")
    return fig

# 2. 📈 Line Chart: Projected Savings using Linear Regression
def savings_projection_chart(income, expenses, savings):
    # Simulate past 6 months of savings
    past_savings = []
    for i in range(6, 0, -1):
        est = savings - i * (expenses - income) * 0.3
        past_savings.append(max(est, 0))

    months = ['-5m', '-4m', '-3m', '-2m', '-1m', 'Now']
    df = pd.DataFrame({'Month': months, 'Savings': past_savings})
    df['MonthIndex'] = range(6)

    # Train Linear Regression
    X = df[['MonthIndex']]
    y = df['Savings']
    model = LinearRegression()
    model.fit(X, y)

    # Predict next 6 months
    future_indices = np.array(range(6, 12)).reshape(-1, 1)
    predicted = model.predict(future_indices)

    # Plot
    plt.figure(figsize=(8, 4))
    plt.plot(df['MonthIndex'], y, marker='o', label='Past Savings')
    plt.plot(future_indices, predicted, marker='x', linestyle='--', label='Projected Savings')
    plt.xticks(list(range(12)), ['-5m', '-4m', '-3m', '-2m', '-1m', 'Now', '+1m', '+2m', '+3m', '+4m', '+5m', '+6m'])
    plt.title("📈 Projected Savings for Next 6 Months")
    plt.xlabel("Month")
    plt.ylabel("Amount Saved")
    plt.legend()
    plt.tight_layout()

    return plt.gcf()

# 3. 🧠 Gauge Chart: Financial Health Score
def financial_health_score_chart(score):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': "🧠 Financial Health Score"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "green" if score >= 70 else "orange" if score >= 40 else "red"},
            'steps': [
                {'range': [0, 40], 'color': "lightcoral"},
                {'range': [40, 70], 'color': "khaki"},
                {'range': [70, 100], 'color': "lightgreen"}
            ]
        }
    ))
    fig.update_layout(height=300)
    return fig
