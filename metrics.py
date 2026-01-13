from radon.complexity import cc_visit

def complexity_score(code):
    result = cc_visit(code)
    return {item.name: item.complexity for item in result}
