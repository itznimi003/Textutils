#I have created this file-"nimi"
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'/Textutils/templates/index.html')

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    #Check checkbox values
    removepunc = request.GET.get('removepunc', 'off') 
    fullcaps = request.GET.get('fullcaps', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    newlineremover = request.GET.get('newlineremover', 'off') 
    charactercounter = request.GET.get('charactercounter', 'off') 
    #check which checkbox is on
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations','analyzed_text': analyzed }
        
        return render(request, 'analyze.html', params)
    # return HttpResponse("<a href='https://www.google.com/'>Google</a>")
    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed  = analyzed + char.upper()
            params = {'purpose': 'changed to uppercase','analyzed_text': analyzed }
        return render(request, '/Textutils/templates/analyze.html', params)
    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n":
                analyzed  = analyzed + char
        params = {'purpose': 'remove new lines','analyzed_text': analyzed }
        return render(request, '/Textutils/templates/analyze.html', params)
    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed  = analyzed + char
        params = {'purpose': 'extraspaceremover','analyzed_text': analyzed }
        return render(request, '/Textutils/templates/analyze.html', params)
    elif(charactercounter=="on"):
        analyzed = ""
        for char in djtext:
            analyzed  = char + char.count(char)
            params = {'purpose': 'count the characters','analyzed_text': analyzed }
        return render(request, '/Textutils/templates/analyze.html', params)    
    else:
        return HttpResponse("Error")
