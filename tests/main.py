import instaloader


def post_download(loader, url):
    post = instaloader.Post.from_shortcode(
        loader.context,
        url
    )

    try:
        loader.download_post(post, target='posts')

    except Exception as e:
        print(e)


class Main:
    def __init__(self):
        self.loader = instaloader.Instaloader()

        self.dispatch()

    def dispatch(self):
            entry = input(" > ")

            if entry:
                post_download(self.loader, entry)
        


if __name__ == '__main__':
    Main()

