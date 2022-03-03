from django.shortcuts import render
from django.http import HttpResponse



def index(request):

    signs_of_zodiac = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Aquarius', 'Pisces']

    return render(
        request,
        template_name='horoscope/index.html',
        context={"title": "horoscope", "signs_of_zodiac": signs_of_zodiac}
    )
    # return HttpResponse("Hello, World!")
