""""""
import wikipedia

wiki_search = input("Enter your wiki search: ")
while not wiki_search == "":
    try:
        wiki_page = wikipedia.page(wiki_search)
        print(wiki_page.title)
        print(wikipedia.summary(wiki_search))
        print(wiki_page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    wiki_search = input("Enter your wiki search: ")
