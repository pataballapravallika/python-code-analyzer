def give_suggestions(metrics):
    tips = []
    for func, score in metrics.items():
        if score > 10:
            tips.append(f"Refactor '{func}' to reduce complexity.")
    return tips
