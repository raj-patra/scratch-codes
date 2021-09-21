import wikipedia, argparse

def search_wiki(gist_query, page_query, lang='en'):
    response = {}
    try:
        wikipedia.set_lang(lang)
    except Exception as e:
        print({"message": "TypeError: Unsupported language preference passed. Setting default language preference as 'en'", "error": str(e)})

    try:
        if gist_query:
            gist = wikipedia.summary(gist_query)
            response["summary"] = {"query": gist_query, "gist": gist}

        print(response)
    except Exception as e:
        print({"message": "ValueError: Could not extract information from wikipedia", "error": str(e)})


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument("--search", action="store", type=str, required=False, help="Gets similar topic for any given query")
    my_parser.add_argument("--gist", action="store", type=str, required=False, help="Gets summary for a particular topic")
    my_parser.add_argument("--page", action="store", type=str, required=False, help="Gets wiki page for a particular topic")
    my_parser.add_argument("--lang", action="store", type=str, required=False, help="Set language preference for a search instance")

    args = my_parser.parse_args()
    
    gist = args.gist
    page = args.page
    lang = args.lang
    
    if lang:
        search_wiki(gist, page, lang)
    else:
        search_wiki(gist, page)
