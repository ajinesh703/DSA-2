def group_anagrams(strs):
    groups = {}
    for word in strs:
        key = tuple(sorted(word))  # Sorted tuple as key (e.g., 'eat' -> ('a','e','t'))
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    return list(groups.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
