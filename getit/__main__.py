import os

from getit.get_website_title import get_title_from_website


def get_website_from_environment_var():
    env_vars = dict(os.environ)
    return env_vars['WEBSITE']


if __name__ == '__main__':
    website = get_website_from_environment_var()
    print(f'Getting the title from website:${website}')
    (status, title) = get_title_from_website(website)
    print(f'Title: {title} [{status}]')
