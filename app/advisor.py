def rule_based_advice(user):
    advice = []

    # Rule-based financial logic
    if user['savings'] < 0.2 * user['income']:
        advice.append("🔸 Try to save at least 20% of your monthly income.")
    if user['debts'] > 0.3 * user['income']:
        advice.append("🔸 Consider reducing debts – it’s over 30% of your income.")
    if user['age'] < 30 and "retirement" in user['goal'].lower():
        advice.append("🔸 Great that you're planning for retirement early. Invest in long-term funds.")

    # Keyword-based goal matching
    goal = user['goal'].lower()

    if any(word in goal for word in ["house", "home", "property", "real estate"]):
        advice.append("🏠 Saving for a house? Start a dedicated real estate fund and explore low-risk SIPs.")
    elif any(word in goal for word in ["wedding", "marriage", "education", "college", "study"]):
        advice.append("🎓 Plan for 2–3 years. Use short-term debt funds or RDs to safely grow your savings.")
    elif any(word in goal for word in ["travel", "vacation", "trip", "holiday"]):
        advice.append("✈️ For travel goals, try high-interest savings accounts or flexi-FDs.")
    elif any(word in goal for word in ["emergency", "medical", "health", "insurance"]):
        advice.append("🚑 Emergency fund? Keep at least 6x monthly expenses in liquid accounts.")
    elif any(word in goal for word in ["business", "startup", "venture"]):
        advice.append("💼 Business goal? Build capital safely and review small business loans or mutual funds.")

    # Default advice if goal is too vague
    if len(advice) <= 2:
        advice.append("💡 Try setting a clear, specific goal. It helps shape better financial decisions!")

    return advice
