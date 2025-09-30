# Custom 404 page

Here are instructions for creating a custom 404 page.
You should do this when the theme or navigation changes.

Read The Docs requires [custom 404 pages](https://docs.readthedocs.com/platform/stable/reference/404-not-found.html) to be located at the root directory.
The page must be named `404.html`.
However, nikola errors during generation if the slug contains an int.
In other words, nikola does not let you name the page `404.html`.

Here is what you need to do:

1. Copy `not-found.md` to the `pages` directory.
1. Copy `not-found.tmpl` to the `templates` directory.
   ```bash
   cp not-found/not-found.md pages/
   cp not-found/not-found.tmpl templates/
   ```
1. Build the site with nikola.
1. Overwrite `files/404.html` with the generated `output/not-found.html` page.
   ```bash
   mv output/not-found.html files/404.html
   ```
1. Clean up the copied files and then commit the updated `404.html` page.
   ```bash
   git clean -fd
   git add files/404.html
   ```
