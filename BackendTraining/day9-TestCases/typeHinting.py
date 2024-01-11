def shreyFunc(x: str) -> str:
    """This is a test function for docstring."""
    return(f"This is good {x}")

print(shreyFunc("Shrey"))
print(shreyFunc.__doc__)
shreyFunc.__doc__ = "This is new docstring"
print(shreyFunc.__doc__)
print(dir(shreyFunc))