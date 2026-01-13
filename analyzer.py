import ast

def analyze_code(code):
    tree = ast.parse(code)

    functions = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    loops = [n for n in ast.walk(tree) if isinstance(n, (ast.For, ast.While))]
    variables = [n for n in ast.walk(tree) if isinstance(n, ast.Name)]

    return {
        "functions": len(functions),
        "loops": len(loops),
        "variables": len(variables)
    }
