# Principles

This repository adheres to the following principles:

- Open: Contribution is always welcome.
- Respectful: See the [Code of Conduct](CODE_OF_CONDUCT.md).
- Transparent and accessible: Work and collaboration should be done in public.
- Merit: Ideas and contributions are accepted according to their merit and
  alignment with the project objectives principles.

## How to contribute

We are very happy to receive contributions from the community in any form, but in particular we would love:

- New resources
- Typos / fixes
- Style improvements

Please use a GitHub pull request to submit your contributions.
If you have a question or are unsure if a contribution is wanted, please join us in [Ansible Docs](https://matrix.to/#/#docs:ansible.com) on Matrix to discuss your change.
If you prefer async discussion, feel free to start a new [discussion topic](https://forum.ansible.com/c/project/7) on the Ansible forum or open a GitHub issue with your question/suggestion.

## Journey-based design

This project has a specific design that helps various personas in the Ansible community achieve their goals.
Contributions that add or modify the pages, templates, or data related to a specific persona, such as `users`, `developers`, `maintainers`, or `community`, should consider this design.

### Personas and journeys

You can consider a persona as a type of human role.
A persona describes the focus and general goals for someone in the Ansible community as well as the needs, attitude, and knowledge that a human in that role would have.

Each persona has milestones towards achieving their goals.
Each milestone has specific major actions that the persona must complete to make progress.
These milestones and major actions outline the journeys for each persona, for example:

```yaml
Milestone: Aware
  Learn about Ansible
Milestone: Evaluate
  Install Ansible
  Run some basic ad-hoc commands
Milestone: Adopt
  Build an inventory
  Create playbooks
Milestone: Scale
  Build execution environments
  Schedule automation jobs in AWX
```

- Ansible community personas are defined in [`data/journeys/personas.md`](https://github.com/ansible-community/ansible-docsite/blob/main/data/journeys/personas.md).
- Journeys are defined in [`data/journeys/journeys.md`](https://github.com/ansible-community/ansible-docsite/blob/main/data/journeys/journeys.md).

### How it works

The `pages/*.md` files define each page with frontmatter that maps a URL to a template.
The `templates/*.tmpl` templates contain the structure for the various homepage bands and subpages.
The `data/*.yaml` files contain the labels and links that appear on the generated pages.

The site is built with [Nikola](https://getnikola.com/), which uses `load_data()` in `conf.py` to make the YAML data available to the templates.
You do not need to modify `conf.py` to add or update content in existing data files.

#### Homepage bands for personas

Homepage bands are the horizontal sections at the root of `docs.ansible.com`.
Each persona has a dedicated band that provides entry points to their journeys.

For example, [`templates/homepage-users-band.tmpl`](https://github.com/ansible-community/ansible-docsite/blob/7d3c98f192eb04a9485c3a5e7901baa2e65c6714/templates/homepage-users-band.tmpl#L14) takes the key-value pairs defined for the user persona in [`data/homepage.yaml`](https://github.com/ansible-community/ansible-docsite/blob/7d3c98f192eb04a9485c3a5e7901baa2e65c6714/data/homepage.yaml#L58).

The homepage bands are intended to provide "quick wins" for personas.
Those links should not be changed in most cases because they are the most essential actions in the primary milestone for each persona.

It would not make sense, for instance, to link an action on the homepage band if it relates to an action that a given persona would complete during a much later milestone.

#### Persona journey pages

Each persona has a journey page that is linked from the homepage.
The journey pages outline all the milestones and actions for each persona.

For example, [`templates/users.tmpl`](https://github.com/ansible-community/ansible-docsite/blob/7d3c98f192eb04a9485c3a5e7901baa2e65c6714/templates/users.tmpl#L25) takes the key-value pairs for milestones defined in [`data/users.yaml`](https://github.com/ansible-community/ansible-docsite/blob/7d3c98f192eb04a9485c3a5e7901baa2e65c6714/data/users.yaml#L2).

This avoids the need to modify the template to add new labels and links.
More importantly, this design allows you to focus on specific journeys to better understand the needs of the persona and more effectively put a documentation link where the user expects to find it.

"If you are at milestone _foo_, then you need to complete task _bar_ before you can continue to the next milestone."

### Placing content in a journey

When adding or modifying content in this project, you should follow this journey-based design at all times.
For example, if you plan to add a link to a documentation page in `data/users.yaml`, you should consider where that page fits in the journey for the user persona.
Do not add links arbitrarily or based on visual layout alone.

Considering the user journey from the outset, when planning content, is a powerful way to take the user's perspective.
By thinking about what the persona needs at each milestone, you can identify gaps and deliver more complete content.

Ask these questions when deciding where content fits in the journey:

- "Which persona does this content serve?"
- "What milestone is the persona at when they need this content?"
- "Is this an essential action for that milestone, or does it belong in a later one?"
- "Does this content provide a high-level entry point for the action?"
- "Can the persona complete the action with this content alone, or are there missing steps?"
- "Does adding this content reveal any gaps in the surrounding milestone?"

### Milestone structure

The `data/*.yaml` files for personas have the following structure:

```yaml
milestones: # Root key for journeys
  automate: # Key that defines a milestone in the journey
    title: # Title for the milestone using imperative
    actions: # Root key for major actions
      start: # Key that defines a major action in the milestone
        label: # Label for the major action
        url: # Link to the corresponding documentation page
```

There can be any number of milestones in the journey.

A milestone must contain at least one action.
However, it is ideal for milestones to contain between three and five actions.

The `title` and `label` keys must always use the imperative form, for example:

```yaml
title: Create automation
label: Start writing Ansible playbooks
```

## Updating the quicklinks

Each of the persona pages includes a _quicklinks_ section.

For example, [`templates/users.tmpl`](https://github.com/ansible-community/ansible-docsite/blob/7d3c98f192eb04a9485c3a5e7901baa2e65c6714/templates/users.tmpl#L10) uses the quicklinks for users defined in [`data/quicklinks.yaml`](https://github.com/ansible-community/ansible-docsite/blob/7d3c98f192eb04a9485c3a5e7901baa2e65c6714/data/quicklinks.yaml#L18).

These quicklinks are intended to provide easy access to the top pages for each persona.
The quicklinks are determined by looking at anonymous traffic results to see which pages are most frequently searched for or accessed.

Never add an entry to the quicklinks section to promote or highlight pages.
