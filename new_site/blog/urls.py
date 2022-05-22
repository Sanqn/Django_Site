# from django.urls import path, include
# from . import views
# from .views import MainHome, PostDetailView
#
#
# urlpatterns = [
#     path('', MainHome.as_view(), name='home'),
#     path('home/<slug>/', PostDetailView.as_view(), name='detail_page'),
# ]

from collections import Counter
from string import punctuation
import re

a = ['hit', 'it']
# paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
# paragraph = input()
# banned = input().split()
# pu = punctuation
# paragraph = paragraph.lower().split()
paragraph = re.sub(r'[^\w\s]',' ',input()).lower().split()
banned = input().split()
new_par = [paragraph[i] for i in range(len(paragraph)) if paragraph[i] not in a]
count_par = Counter(new_par)
print(sorted(count_par.items(), key=lambda x: x[1])[-1][0])

# banned = input().split()
# print(banned)

# words = ['Micke', 'Noriv', 'Colet', 'Micke', 'Colet']
# name = Counter(words)
# print(name) #Counter({'Micke': 2, 'Colet': 2, 'Noriv': 1})

# s = ['GGG', 'ggg', 'DDDDD', 'dd', 'mmmmmm', 'JJJ']
# print(sorted(s))
# print(sorted(s, key=str.lower))
