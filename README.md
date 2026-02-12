[![Discuss at #website:ansible.com on Matrix](https://img.shields.io/matrix/website:ansible.com.svg?server_fqdn=ansible-accounts.ems.host&label=Discuss%20at%20%23website:ansible.com&logo=matrix)](https://matrix.to/#/#website:ansible.com)

This repository contains the assets required to build the Ansible Community website, [docs.ansible.com](https://docs.ansible.com). Welcome!


## Contributing to the website

Please see [CONTRIBUTING](CONTRIBUTING.md)

## Governance

Please see [Governance](CONTRIBUTING.md#Governance)

## Contacting the maintainers

The Website Working group can be found in [Ansible Website WG](https://matrix.to/#/#website:ansible.com) on Matrix
or `#ansible-website` on IRC. Alternatively, a GitHub issue is also acceptable for asking
questions.

## Building the website locally

The Ansible community website is static HTML generated from this repository.
You can build the website locally if you want to evaluate changes or experiment.

### Using nox

This project includes a `nox` configuration to automate and simplify the build.

Install `nox`.

    # Install nox with pip
    python3 -m pip install nox

    # Install nox on MacOS
    brew install nox

Run `nox -s build -- --conf=dev.conf.py` to build the website locally.
To see other available sessions, run `nox --list`.

> By default the `conf.py` file uses absolute urls for style sheets and other resources.
> If you do not specify the `dev.conf.py` file the resulting output uses resources hosted on `docs.ansible.com`, which means you cannot view local changes to `.sass` files and so on.

### Running nikola directly

The website is built with nikola.
If you prefer using `nikola` commands directly, instead of using `nox`, you can.

#### Setting things up

We recommend that you use a Python virtual environment.

    # Create a virtual environment named "venv" in your current directory.
    python3 -m venv venv

    # Activate the virtual environment.
    source venv/bin/activate

    # Install the required packages.
    python -m pip install --upgrade -r ./requirements.in -c ./requirements.txt

#### Building and viewing the site

The Ansible community website is built with [Nikola](https://getnikola.com/).

    # Build the site with Nikola.
    nikola build --conf=dev.conf.py

    # View the site in your browser.
    nikola serve -b

    # List available commands.
    nikola help

> Check the [Nikola handbook](https://getnikola.com/handbook.html) for more details.

> Nikola configuration for the website is in `conf.py`.

## Site accessibility

Being considerate of users with assistive technology is a central part of the Ansible community pledge to be inclusive.
When adding a blog post or making changes to the templates, we ask that you perform some accessibility checks.
This ensures that everyone can read your post and our site remains open and accessible to all.

### Web Content Accessibility Guidelines (WCAG) 2.1

Changes should always adhere to [WCAG 2.1 guidelines](https://www.w3.org/TR/WCAG21/).
In most cases the guidelines provide relatively straightforward things to be aware of, such as:

- **Ensure images are not the sole means to convey information.**
  Images should only supplement the text.
  For instance, if you want to include a visual depiction of data such as a graph, then your blog post should adequately explain those data points in the surrounding text.
- **Images must have suitable alternative text.**
  The `alt` attribute should always be present for any image and provide a short, meaningful description.
  Think of what the image conveys "at a glance" and put that as the value of the `alt` attribute.
  For adding `alt` attributes to markdown files, [check out the GitHub docs](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images).
- **Avoid redundant and suspicious links.**
  Don't include the same `href` in more than one instance on the page or in a post.
  Don't use vague words like "here" or "this page" as your anchor text; make sure it clearly describes where the link takes you.
- **Think about how colors contrast.**
  Contrast is super important, kind of fun, and all about being able to tell things apart.
  Your goal is to make it easy for users to distinguish text or other elements.

### Testing changes for accessibility

Use these resources to check for web accessibility issues:

- [WAVE report](https://wave.webaim.org/)
- [Contrast checker](https://webaim.org/resources/contrastchecker/)
- [Link contrast checker](https://webaim.org/resources/linkcontrastchecker/)

To perform an accessibility check for a blog post, do the following:

1. When your final commit is ready, submit a pull request.
2. Grab the link for your Read the Docs build preview.
   You can find this in the "checks" section of your PR.
3. In a browser, append the link for your build preview to `https://wave.webaim.org/report#/`.
4. Check the WAVE report for errors and alerts.

The full url for your WAVE report should be similar to this one:

```
https://wave.webaim.org/report#/https://ansible-community-website--278.org.readthedocs.build/en/278/blog/2023/09/26/new-ansible-galaxy/
```

> If you see errors or alerts related to the underlying style sheets or templates - in other words not a problem with your post but the site itself - please create an issue in the repo and add the `accessibility` label.

#### Additional accessibility tooling

If your changes affect templates, consider using `axe` tooling to detect accessibility issues:

- [axe browser extension](https://www.deque.com/axe/browser-extensions/)
- [vscode axe linter](https://marketplace.visualstudio.com/items?itemName=deque-systems.vscode-axe-linter)

## Checking your changes before commit

This project includes some tests and checks that run against pull requests.
You can also run these checks before you commit changes.

    # Install nox if required.
    python -m pip install --upgrade nox

    # View available nox sessions.
    nox --list

### Spelling check

    # Spell check the page templates with the default session.
    nox -s spelling

    # Check a specific blog post for spelling errors.
    nox -s spelling -- ./posts/2023/02/24/2023-02-24-ansible_community_strategy_2023.md

    # Automatically correct any spelling errors in a blog post.
    nox -s spelling -- ./posts/2023/02/24/2023-02-24-ansible_community_strategy_2023.md -w

### Linting and formatting templates

This project includes a linter and formatter to guard against unintended errors and to ensure high quality templates.
If you modify the templates you should lint and format prior to commit.

    # Check templates for issues.
    nox -s lint

    # Check templates and ignore rules.
    nox -s lint -- --ignore=H006,H013,T002,T003,T028

    # Check changes before formatting.
    nox -s format -- --check

    # Format templates.
    nox -s format

Default configuration for the linter and formatter is in the `[tool.djlint]` section of `pyproject.toml`.
For more information about configuration options, see:

- [Linter](https://www.djlint.com/docs/linter/)
- [Formatter](https://www.djlint.com/docs/formatter/)



## Code of Conduct

The Ansible community team values diverse opinions and is committed to an inclusive
Please review and abide by our [CODE OF CONDUCT](CODE_OF_CONDUCT.md).

## License

[![License: CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)

## Thank you

Ansible depends on community involvement - thank you for being a part of it!
