def highFive(items):
    scores = {}
    for sid, score in items:
        if sid not in scores:
            scores[sid] = []
        scores[sid].append(score)
    res = []
    for sid in sorted(scores.keys()):
        top5 = sorted(scores[sid], reverse=True)[:5]
        res.append([sid, sum(top5)//5])
    return res
