from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html',  {'hithere' : 'This is me'})

def about(request):
    return render(request, 'about.html',  {'hithere' : 'This is me'})

def eggs(request):
    return HttpResponse('Eggs are great!')

def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #Inc Count
            worddictionary[word] += 1
        else:
            #Add to the worddictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedwords)
    return render(request, 'count.html', {'fulltext':fulltext,
    'count':len(wordlist),
    'sortedwords':sortedwords
    })
