import re


# x, y, z, w, i, j, k, l are allowed in variable names or indices
REGEX_SINGLE_VAR = re.compile(r'([A-H]|[M-V]|[a-h]|[m-v])')
REGEX_DOUBLE_VAR = re.compile(r'([A-Z]|[a-z]){2}')

# Regex for camelCase to snake_case.
REGEX_CAMEL_TO_SNAKE1 = re.compile(r'([A-Z]+)([A-Z][a-z])')
REGEX_CAMEL_TO_SNAKE2 = re.compile(r'([a-z\d])([A-Z])')
