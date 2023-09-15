# ansible-role-admiral #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-admiral/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-admiral/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-admiral/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-admiral/actions/workflows/codeql-analysis.yml)

This is an Ansible role that installs the Docker composition for
[cisagov/admiral](https://github.com/cisagov/admiral), a Certificate
Transparency log harvester.

## Requirements ##

None.

## Role Variables ##

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| admiral_file_owner_group | The name of the group that should own files or directories created by this role. | [Omitted](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_filters.html#making-variables-optional) | No |
| admiral_file_owner_username | The name of the user that should own files or directories created by this role. | [Omitted](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_filters.html#making-variables-optional) | No |

## Dependencies ##

- [cisagov/ansible-role-docker](https://github.com/cisagov/ansible-role-docker)

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: docker
  become: yes
  become_method: sudo
  tasks:
    - name: Install the Admiral composition
      ansible.builtin.include_role:
        name: admiral
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Alexander King - <alexander.king@cisa.dhs.gov>
