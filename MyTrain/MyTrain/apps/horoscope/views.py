from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


zodiac_dict = {
    "Aries": ["Овен" ,"""
        Feel like you're tripping over your own tongue? 
        That's not surprising, considering the constant 
        flow of verbosity that's spilling forth from you right now. 
        Go ahead and enjoy your extreme eloquence -- everyone else is.
    """],

    "Taurus": ["Телец", """
        Stay in the now rather than trying to jump forward into the future. 
        You'll do best when you focus your attention on all the immediate 
        details that require your assistance. Remember that, no matter how 
        tempting it is to start booking yourself weeks in advance.
    """],

    "Gemini": ["Близнецы", """
        From you, a wink and a smile go beyond a thousand words -- 
        they're practically an entire romantic saga. Your flirty energy 
        livens things up wherever you go right now, so make sure that as 
        many people as possible can appreciate your fabulous self.
    """],

    "Cancer": ["Рак", """
        For the first time in a very long time, you're listening only 
        to one authority -- yourself. This is especially true regarding 
        a social matter. You've been worried far too long about doing the right thing. 
        Now it's time to do right by you.
    """],

    "Leo": ["Лев", """
        You may feel ready to move into a decisive new leadership role, 
        but the stars say to let things gestate for a little while longer 
        before you make your big move. Try talking things over with your 
        boon companions and hear what they have to say.
    """],

    "Virgo": ["Дева", """
        Don't try to do more than you can comfortably handle -- 
        and make sure you're very clear about your limits if others try 
        to ask you to take more on. When possible, lighten your load rather than add more to it.
    """],

    "Libra": ["Весы", """
        You love watching this new scenario unfold in your life, 
        but suddenly watching it isn't enough. You want -- no, 
        you need -- to take action, but you're not sure which way to turn. 
        Take a moment and look before you leap.
    """],

    "Scorpio": ["Скорпион", """
        Minor details could become major mistakes if they're left unchecked, 
        but fortunately, there's plenty of time to check everything. 
        Not only will this ensure your enterprise will go swimmingly, 
        but it'll give you some much-needed peace of mind.
    """],

    "Sagittarius": ["Стрелец", """
        Having this much activity going on around you can be somewhat unsettling, 
        but don't sulk. Just because something seems out of sync doesn't mean 
        it'll be that way permanently. Wait it out and you'll feel things start to jell.
    """],

    "Capricorn": ["Козерог", """
        Put the kibosh on anyone who's absolutely determined to make sure even 
        the smallest things go haywire. With a little extra care, you can defuse 
        this live wire before they make life any more difficult than it is.
    """],

    "Aquarius": ["Рыбы", """
        Taking other people's opinions into consideration is usually the 
        last item on your list of priorities, and that goes double when it 
        comes to a very new and very exciting person in your life.
    """],

    "Pisces": ["Водолей", """
        Learn to deal with ambiguity by letting it exist, 
        rather than trying to make it go away. If you act too rapidly, 
        you might just find that the solution becomes a much larger 
        problem than the original situation.
    """]
}

signs_of_zodiac = [
    'Aries', 'Taurus', 'Gemini', 
    'Cancer', 'Leo', 'Virgo', 
    'Libra', 'Scorpio', 'Sagittarius',
    'Capricorn', 'Aquarius', 'Pisces'
]

def index(request):

    return render(
        request,
        template_name="horoscope/index.html",
        context={"title": "Horoscope", "signs_of_zodiac": signs_of_zodiac}
    )


def zodiac_info(request, sign_of_zodiac):
    # zodiac_name = request.GET.get("zodiac", "")

    if sign_of_zodiac in signs_of_zodiac:
        info = zodiac_dict[sign_of_zodiac]
        return render(
            request,
            template_name="horoscope/zodiac.html",
            context={"title": sign_of_zodiac, "zodiac": info[0], "info": info[-1]}
        )
    else:
        return HttpResponseNotFound(f"Unknown sign of zodiac - {sign_of_zodiac}")


def secret(request):
    import requests as req

    page = req.get("https://pornhub.com")
    return HttpResponse(page)

"""
<iframe width="754" height="480" src="https://www.youtube.com/embed/oQtED7Ambz4" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
"""