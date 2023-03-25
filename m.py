import warnings

warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("error", ImportWarning)

warnings.warn("Warnings, no code here", SyntaxWarning)

try:
    warnings.warn("Warning, module not import", ImportWarning)

except:
    print("Warnings processed")