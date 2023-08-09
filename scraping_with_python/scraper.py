import requests
from bs4 import BeautifulSoup
import json


def sort_stores_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)


def create_custom_hn(links, subtext, hn):
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return hn


def get_n_hackernews(i):
    hn = []
    for num in range(1, i + 1):
        # Call hacker website and retreive its html document
        res = requests.get(f"https://news.ycombinator.com/?p={num}")

        # Pass that html document to BeautifulSoup to create a soup object
        soup = BeautifulSoup(res.text, "html.parser")

        links = soup.select(".titleline > a")
        subtext = soup.select(".subtext")

        hn.extend(create_custom_hn(links, subtext, hn))
    final_list = sort_stores_by_votes(hn)
    return final_list


def send_top_stories(hn):
    title = [hn[i]["title"] for i in range(3)]
    link = [hn[i]["link"] for i in range(3)]
    votes = [hn[i]["votes"] for i in range(3)]

    data = ""
    for i in range(3):
        data = data + f"{i + 1}: {title[i]} Votes : {votes[i]} \n"
    actions = [
        {
            "action": "view",
            "label": "Story 1",
            "url": link[0],
        },
        {
            "action": "view",
            "label": "Story 2",
            "url": link[1],
        },
        {
            "action": "view",
            "label": "Story 3",
            "url": link[2],
        },
    ]
    headers = {"Title": "Todays Top Stories", "Tags": "computer", "Actions": actions}

    res = requests.post(
        "https://ntfy.sh/",
        data=json.dumps(
            {
                "topic": "tophnstories",
                "message": data,
                "actions": actions,
            }
        ),
    )
    print(res)


if __name__ == "__main__":
    hn = get_n_hackernews(1)
    print(hn)
    send_top_stories(hn)
    print("done")
