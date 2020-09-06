colors = {"red", "blue", "green", "yellow", "purple", "orange"}
subset = {"purple", "green"}
print(subset.issubset(colors))
print(colors.issuperset(subset))
print({"green", "red", "black"}.issubset(colors))

primary = {"red", "blue", "green"}
art_primary = {"magenta", "cyan", "yellow"}
print(primary.isdisjoint(art_primary))
