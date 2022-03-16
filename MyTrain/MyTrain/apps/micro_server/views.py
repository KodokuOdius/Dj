import threading
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import MSG

# Create your views here.


def msg(request):
    from .bots import send_msg as msg
    import asyncio

    if request.method == 'POST':
        form = MSG(request.POST)
        if form.is_valid():

            data = form.cleaned_data

            print(data)

            def worker(ws, loop):
                asyncio.set_event_loop(loop)
                loop.run_until_complete(ws(data))

            ws = msg.send_msg
            loop = asyncio.new_event_loop()
            p = threading.Thread(target=worker, args=(ws, loop,))
            p.start()

            # loop = asyncio.get_event_loop()
            # loop.run_until_complete(msg(data))

            return redirect(".")
    else:
        form = MSG()


    return render(
        request=request,
        template_name="micro_server/send_msg.html",
        context={"form": form}
    )