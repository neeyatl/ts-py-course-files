text = "what have the greek ever done for us"

caps = [c.upper() for c in text]    # () instead of [] doesn't produce a tuple, but a generator exp.
caps = tuple(caps)      # Use tuple constructor instead.
print("".join(caps))
