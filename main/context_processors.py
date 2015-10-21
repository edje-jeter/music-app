from forms import MusicSearchForm


def search_form(request):
    return {
         'search_form': MusicSearchForm()
    }
