---
author: Anshul Behl
date: 2022-02-16 00:00 UTC
description:  The new capabilities of Ansible Platform 2 enable easier
  to scale automation across the globe and allow you to run your
  automation as close to the source as possible without being bound to
  running automation in a single data center.
lang: en-us
title: Migrating from Python virtual environments to automation execution environments in Ansible Automation Platform 2
---

# Migrating from Python virtual environments to automation execution environments in Ansible Automation Platform 2

Red Hat Ansible Tower (included in Ansible Automation Platform 1.x)
used Python virtual environments to manage dependencies and implement
consistent automation execution across multiple Red Hat Ansible
Automation Platform instances. This method of managing dependencies came
with its own set of limitations:

-   Managing Python virtual environments across multiple Ansible Tower instances. 
-   Confirming custom dependencies across Ansible Tower instances grew in complexity as more end-users interacted with it.
-   Python virtual environments were tightly coupled to the control plane, resulting in Operations teams bearing the majority of the burden to maintain them.
-   There were no tools supported and maintained by Red Hat to manage custom dependencies across Ansible Automation Platform deployments.

Ansible Automation Platform 2 introduced automation execution environments.
These are container images in which all automation is packaged and run,
which includes components such as Ansible Core, Ansible Content
Collections, a version of Python, Red Hat Enterprise Linux UBI 8, and any additional
package dependencies.

# Why should you upgrade?

Ansible Automation Platform 2, [announced at AnsibleFest 2021](https://www.redhat.com/en/about/press-releases/red-hat-ansible-automation-platform-2-drives-cloud-native-automation-and-helps-developers-become-automators),
comes with a re-imagined architecture that fully decouples the
automation control plane and execution plane. The new capabilities
enable easier to scale automation across the globe and allow you to run
your automation as close to the source as possible without being bound
to running automation in a single data center. It's more dynamic,
scalable, resilient and secure compared to Ansible Automation Platform 1.2.

If you are an existing Red Hat customer using Ansible Automation
Platform 1.2 (Ansible Tower 3.8), an important migration recommendation
is to convert any custom Python virtual environments in your cluster to
automation execution environments. This one-time effort opens the door
to take advantage of the latest Ansible Automation Platform 2
capabilities and the ability to execute consistent automation across
multiple platforms with lower long-term maintenance.

We will now explain this specific migration consideration and provide
you with some best practices on how to migrate to automation execution
environments.

# The manual process of upgrading

As outlined in this
[document](https://docs.ansible.com/automation-controller/4.1.0/html/upgrade-migration-guide/upgrade_to_ees.html),
the manual process of upgrading to automation execution environments
would go something like this:

1.  Prerequisite is a running Ansible Automation Platform 1.2 cluster
    where customers have configured one or more custom Python virtual
    environments in addition to the default one.
2.  Use the
    `awx-manage`
    command line utility present on the Ansible Tower node to get the
    list of custom Python virtual environments using the
    `list_custom_venvs` subcommand.
3.  Run the `awx-manage export_custom_venv`
    command on each virtual environment to get the list of Python
    packages installed in that virtual environment.
4.  Check the association of a virtual environment using the
    `awx-manage custom_venv_associations`
    command. This list of associations/information will help customers
    make associations of new execution environments in the Ansible
    Automation Platform 2.x cluster.
5.  Filtering the above information manually and feeding the list of
    requirements from step 3 above to the execution environment builder
    (ansible-builder) to create necessary custom execution
    environment(s).

Looking at the above process there can be two enhancements to this flow,
which would help customers adopt automation execution environments
faster:

1.  Exported requirements from step 3 above can be compared with the
    list of Python packages already present in the automation execution
    environment that will serve as the base layer for the newly created
    ones. This will be helpful, because there are dependencies that will
    already be resolved by the base automation execution environment and
    it will help customers if they can focus on **what's needed** when
    they start creating automation execution environments for their
    clusters.
2.  Since we love Ansible, why not just automate the above process,
    right? :)

# The automated process of upgrading

The intent of this section is to explain how you can automate this
process using Ansible. We have a few example Ansible Content Collections
and roles that can be used to achieve this automation. The playbook
would look something like this at a high level:

1.  Pull the list of packages from all the custom Python virtual
    environments present on the Ansible Tower node in Ansible Automation
    Platform 1.2.
2.  Compare the package lists from step 1 with the package list in the
    automation execution environment you decide to use as basis
    (ansible-2.9 in our example), to find the packages that are not
    present in the base.
3.  List from step 2 can be fed to an Ansible Role that can automate the
    execution environment creation, keeping the base  as the one we did
    the comparison with in step 2.

Let's take an existing Ansible Automation Platform 1.2 setup that has
two custom virtual environments, called custom-venv1 and custom-venv2,
which both have their own list of Python packages:

```yaml
# awx-manage export_custom_venv /opt/my-envs/custom-venv1/ -q
certifi==2021.10.8
charset-normalizer==2.0.10
enum34==1.1.10
future==0.18.2
idna==3.3
requests==2.27.1
solidfire-sdk-python==12.3.0.203
urllib3==1.26.8

# awx-manage export_custom_venv /opt/my-envs/custom-venv2/ -q
zabbix-api==0.5.4
```

We will use a role packaged in the [redhat_cop.ee_utilities Collection](https://galaxy.ansible.com/redhat_cop/ee_utilities)
called `virtualenv_migrate`, that is designed for this specific purpose
and run that against the Ansible Tower node. Below is a sample playbook
and inventory file respectively:

```yaml
---
- name: Review custom virtualenvs and diff packages from base EE
  hosts: tower
  become: true
  vars:
    - venv_migrate_ee_python_list: []
  tasks:
    - name: Include venv_migrate role
      include_role:
        name: redhat_cop.ee_utilities.virtualenv_migrate
```

```ini
[tower]
ansibletower.demoredhat.com

[local]
localhost

[all:vars]
venv_migrate_default_ee_url="registry.redhat.io/ansible-automation-platform-21/ee-29-rhel8:latest"
registry_username=myRedHatID
registry_password=mypassword
```

The output of the playbook is shown below. It did the comparison as
expected and gave us the list of packages from custom Python virtual
environments that were not present in the base automation execution
environment.

NOTE: The version based comparison for PIP packages is not included at this moment.

```bash
TASK [redhat_cop.tower_utilities.virtualenv_migrate : diff | Show the packages that are extra from default EEs in custom venvs.] ******************************************************************************
ok: [3.228.23.40 -> localhost] => {
    "msg": [
        {
            "/opt/my-envs/custom-venv1/": [
                "certifi",
                "charset-normalizer",
                "enum34",
                "future",
                "solidfire-sdk-python"
            ]
        },
        {
            "/opt/my-envs/custom-venv2/": [
                "zabbix-api"
            ]
        }
    ]
}
```

The above output can be directly passed to another Ansible Role in the
same [redhat_cop.ee_utilities Collection](https://galaxy.ansible.com/redhat_cop/ee_utilities)
called
[ee_builder](https://github.com/redhat-cop/ee_utilities/tree/main/roles/ee_builder);
its use case is to automate the execution environment creation process.

Briefly summing things up:

-   We ran a playbook against the Ansible Tower node to gather Python
    packages (from custom Python virtual environments) that are not in
    the base automation execution environment.
-   Output from above can help the creation of custom automation
    execution environments using the ee_builder role that automates
    execution environment creation.

# Key takeaways

-   Using this new Ansible Role in combination with the ee_builder role
    can be used to automate the migration from custom virtual
    environments to automation execution environments.
-   These roles are currently part of a community project and not
    officially supported by Red Hat. However, they can provide details
    in the understanding of the migration process.
