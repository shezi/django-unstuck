# App management and placement and settings (and urlpatterns)

When you start a new project, using the standard django template, you're given a project structure that is good for
starter projects. But it has shortcomings, too: there are duplicate names, some of the names are unclear, configuration
and code (and other things) are mixed.

We will try to separate these parts and make them more identifiable and easier to navigate.

# The challenge

Organize your project such that:

* everything has its place 
* what belongs together, stays together
* code/URLs are easily found
* settings are flexible


# Solutions

We're going to change the project structure in three steps: configuration, apps and URLs

## <a id="configuration"></a> Step 1: configuration

We want to separate the configuration into a directory that contains all of the configuration and is properly named. The
final layout will look like this:

```
project_root/
  config/
    asgi.py
    wsgi.py
    urls.py
    settings/
      base.py
      development.py
      production.py
      test.py
      local.py
```

This way, all configuration stays together. Also, this directory contains all configuration which is necessary and
specific to _this project_.

So, create a config directory. Below that, a settings directory. Put the configuration in config directory. Move your
project settings to `config/settings/base.py`. 

Create files for `development.py`, `production.py` and `test.py` and add this content to each:

```python
from .base import *

# add your configuration here

try:
    from .local import *
except ImportError:
    # you can add a message here if you want
    pass
```

A small adjustment is needed in `base.py`. We have changed the path of the settings relative to the project root, so we
have to fix that. Adjust your `base.py` like this:

```python
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
```

Just add one more `.parent` there and adjust the paths.

Now we need to use these settings in the contexts we want them to. Usually, in `manage.py` we refer to
`config.settings.development`, while in `asgi.py/wsgi.py` we refer to `config.settings.production`. These are sane
defaults for each entry point, but can be overriden by environment variables if necessary.

What have we achieved? We have one common settings file `base.py` and three environment-specific files. You can now add
the configuration that is specific for a certain environment into the respective file.  
Finally, you can create a `local.py` that will override any of these settings. If you add `config/settings/local.py` to
your `.gitignore`, you can safely put _machine-specific_ and sensitive configuration in there, without fear of
accidentally committing it.

Side-note/Example: One thing I like to add to my development settings is
```python
AUTH_PASSWORD_VALIDATORS = []
```
This makes it easier in development to have simple passwords.

## <a id="apps"></a> Step 2: apps

We're going to put all the apps in a directory. This makes it easier to find them, they will not be mixed in with other
things (like static files, documentation, tools/scripts, etc).

Our structure will look like this:
```
project_root/
  apps/
    your_app/
    ...
  config/
    ...
  static/
    ...
  templates/
    ...
```

As you can see, the project root directory now contains clear folders with specific, different contents. All the apps
stay together, and name clashes are minimized.

So create the `apps/` directory. To make apps findable without a prefix, we need to add the `apps/` directory to the
python search path. A good place to do this is right at the beginning of our settings. That way, we can make sure that
whenever Django starts, the path is set correctly.

Add this to `config/settings/base.py`:

```python
import sys
sys.path.append(str(BASE_DIR / "apps"))
```

Finally, move all your apps into the `apps/` directory. No further changes are necessary inside the apps.

You can now name your main app the same as your project.


## <a id="urlpatterns"></a> Step 3: urlpatterns

Each app gets urlpatterns and gets added to the project URLs right away. That way, you can make sure you easily add new
URLs to each app, and each app has its own URLs.

Simply put a file called `urls.py` into each of your apps, with this content:

```python

app_name = "<your app name here>"

urlpatterns = []
```

Then, add each app to your `config/urls.py`, like this:
```python
from django.contrib import admin
from django.urls import path, include

from demoapi import views

urlpatterns = [
    path("your_app_path/", include("your_app.urls")),
    path('admin/', admin.site.urls),
]
```

Do this, whenever you start an app, and do it for every app! After some time, this will become automatic for you. This
way, we make sure all URLs are defined in their respective apps, and each app can have URLs without further
configuration.

## <a id="structure"></a> Step 4: Success!

Our final structure looks like this:

```
project_root/
  apps/
    your_app/
    ...
  config/
    settings/
      base.py
      development.py
      production.py
      test.py
    asgi.py
    wsgi.py
    urls.py
  static/
    ...
  templates/
    ...
```

We have achieved our goals!

* everything has its place
* what belongs together, stays together
* code/URLs are easily found
* settings are flexible


Hooray!
