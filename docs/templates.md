# Templates and Statics: Placement, folders, blocks and inheritance and namespaces

Once a Django site gets to a certain size, templates abound. Each and every app has them, your project has some of its
own, it will overwrite some of the standard templates, and you'll have snippets for all kinds of things.

One problem with these templates is that they all live in the same global namespace. When you refer to
`"main_page.html"`, it could be in any of the apps you have or in any of the template directories you configured. If
there is more than one such file, which one you'll get depends on the _order of the template directories_ in your
settings. Such a brittle system!

Static files are completely identical to template files. So when we talk about templates here, just apply the same
things to static files.

# The challenge

All templates live in one big namespace.  
Yet there are many places in the filesystem.

We have to: 

* Decide where a template file goes and what it is called!
* Identify what a template belongs to!
* Make sure namespace clashes are minimal!

# Solutions

## <a id="main"></a> Step 1: Your main template directory

Your project should have exactly one main template directory. It should be in your main project directory and it should
be called `templates`. This makes your project structure look like this:

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
    snippets/
    base.html
```

(Refer to [App Management](app-management.md#structure) for the rest of the project structure.)

This directory must be put into the configuration:

```python
EMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],   # <-----
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

In this directory we will put all templates that belong to _the project_ itself, instead of a single app. These will be
the main base templates, utilities and snippets, and overrides.

The main base template is called `base.html` and will be the _base_ for most other templates. You might have other base
templates, such as `base_wide.html` or `base_narrow.html`. All error templates go into this directory as well.  
Adjacent to these base templates will be some snippets. I like to call their directory `snippets/`, but you might have
an app with that name, so you might have to choose a different name. In there, you put small parts of the project that
you'll want to reuse in different places. Two prime candidates are the sidebar menu (which might be in different base's),
and the pagination snippet. We used to have form rendering snippets in there as well, but there are other solutions for
those today.

One more thing that needs to go into the main template directory is _overrides_. When you use apps that can be
customized with your own templates, create the necessary files in this main directory. Most sites will use Django's
built-in login views (see also [Registration](registration.md)), so you'll simply put `registration/login.html` and
`registration/logged_out.html` in here for custom login and logged-out views.



## <a id="in-app"></a> Step 2: in-app template directories

As you've seen above, we have configured in-app template directories, as should be the case. Django loads these after
the configured specific directories, so our main directory is safe.

The in-app folders contain everything for that specific app. Each item in there should be tied either directly to a view
or to some other template.  
We must make sure that inside of in-app template directores, everything goes into a sub-folder with the app name to make
sure we do not clash with other apps or our main directory. Each template should be named the same as the view that it
is loaded from, so we can connect the two more easily. And finally, the url-pattern for that view should have the same
name, too. That way you can always find one from the other.

You should never need to include things from another app. If that is the case, think about whether you should migrate
that specific thing to the main directory.


## <a id="structure"></a> Step 3: Success!

Our final structure looks like this:

```
project_root/
  apps/
    your_app/
      templates/
        your_app/
          item_list.html
          ...
      static/
        your_app/
          css/
          ...
    ...
  config/
    ...
  static/
    ...
  templates/
    snippets/
    base.html
```

With this structure, we achieve our goals: We know where each template file goes and what we should call it. At the same
time, we can easily find what a template file belongs to by looking at its name and placement. We are avoiding namespace
clashes by choosing app-name paths that should be unique in the project.

Hooray!


## <a id="snippets"></a> Step X: Snippets

You must build a collection of snippets! There are just things that come up in every Django project, and the more
snippets you have collected, the better you can react to those eventualities. My collection includes things such as
log-in pages, menu structures, pagination snippets, form-rendering snippets and other things.

(At some point, we might have some of these snippets in here.)
