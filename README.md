# django-unstuck
Suggestions for overcoming common challenges in Django projects

There are some challenges that come up in every Django project. Some of them right at the start: How do I organize my
apps?  Where do I put the base template, and all the other templates? Should I do internationalization right away?  
Other problems only crop up a little later: how do I manage production settings? How do I make sure permissions are
checked correctly? How do I make menus appear correctly?  
Some may appear at any point in time: how do I add content pages? What code goes into models/controllers/views?

In this repository, we try to find ways to get unstuck from these challenges. Some people may call the things we do here
“best practices” or “patterns” or “recipes” or “ideas” or “opinions”.  These are just things we’ve found to work in
these situations many times. Some of our solutions are more directly applicable, others are more guideline-style.

You can also join us on [Discord](https://discord.gg/bUsu9B6Ek6) or on [Telegram](https://t.me/djangoRhein).

Here are the things we have ideas for:

[comment]: <> ( * [Splitting settings: local, dev, testing and production]&#40;docs/settings.md&#41;)

 * [App management and placement and settings (and urlpatterns)](docs/app-management.md)
 * [Username vs email address](docs/username.md) (WIP)
 * [Registration in general](docs/registration.md) (WIP)
 * [Background tasks and long-running processes and Caching](docs/background-tasks.md) (WIP)
 * [Templates: Placement, folders, blocks and inheritance and namespaces](docs/templates.md) (WIP)
 * [Should you do i18n and l10n right away?](docs/i18n.md)
 * [When and how to start caching (memcached, redis etc.)](docs/caching.md) (WIP=)
 * [Where does your code go: models, views or managers or somewhere else?](docs/where-does-the-code-go.md) (WIP)
 * [When to use Middlewares and context processors and what are they?](docs/middleware.md) (WIP)
 * [How to secure access: security middlewares or login_required (white vs black list)](docs/secure-access.md) (WIP)
 * [How to create files and store them in file models](docs/files.md) (WIP)
 * [What to do about image scaling and thumbnailing (and hosting)?](docs/images.md) (WIP)
 * [How to serve content: coded pages, flatpages or Wagtail?](docs/flatpages.md) (WIP)
