test_scores=list(map(int,input().split()))
graded_curve=[score+10 if score<50 else score+5 if score<=95 else 100 for score in test_scores]
print(graded_curve)

