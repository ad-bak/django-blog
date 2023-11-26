from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Everest_North_Face_toward_Base_Camp_Tibet_Luca_Galuzzi_2006.jpg",
        "author": "Some dude",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened halfway through.",
        "content": "The name of the first black samurai was Yasuke. He lived during the 1500s, and he was a slave. He was brought to Japan by an Italian Jesuit named Alessandro Valignano. He was given to the Japanese warlord Oda Nobunaga. Nobunaga was so impressed with Yasuke's strength that he made him a samurai.",
    },
    {
        "slug": "programming-is-fun",
        "image": "https://cdn.sanity.io/images/tlr8oxjg/production/9f15109746df254c5a030a7ba9239f8a4bb5dadb-1456x816.png?w=3840&q=100&fit=clip&auto=format",
        "author": "Some dude",
        "date": date(2021, 7, 22),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": "They literally made me stop eating foods that were shaped like dicks. No hotdogs, no popsicles. You know how many foods are shaped like dicks? The best kinds.",
    },
    {
        "slug": "into-the-woods",
        "image": "https://www.treehugger.com/thmb/nSp8ESJ1N6zq_bsTVL_MoSrKAqA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1273584292-cbcd5f85f4c646d58f7a7fa158dcaaeb.jpg",
        "author": "Some dude",
        "date": date(2021, 7, 23),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": "You know what they call a quarter pounder with cheese in Paris? They call it a royale with cheese. That's right. What do they call a Big Mac? I dunno, I didn't go into Burger King. ",
    },
]


def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    post = next(post for post in all_posts if post["slug"] == slug)
    return render(
        request,
        "blog/post-detail.html",
        {"post": post},
    )
