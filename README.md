inline_python
=========

This role provides the `inline_python` and `inline_python_func` filters which allow you to "embed" python directly into your Ansible jinja templates.  `inline_python_func` allows you to "return" vars with `__return_var("<var name>")`, while `inline_python` has patched `print()` to return everything "printed."

Galaxy Install
------------

ansible-galaxy install git+https://github.com/ipchama/inline_python.git

Requirements
------------

Python3

Jinja2 >= 2.10 (for full functionality displayed in the examples, but should work with slightly older versions as welll)

Role Variables
--------------

None

Dependencies
------------

None

Example Playbook
----------------
```
  ---
  - hosts: localhost
    remote_user: root
    roles:
      - inline_python

  tasks:
  
    - debug:
        msg: |
          -----------------------------------------------

          TEST #1 (simple):
          {% set output = """
          print(val1)
          """ | inline_python(val1="Some output") %}
          {{ output }}

    - debug:
        msg: |
          -----------------------------------------------

          TEST #2 (simple here-doc style):
          {% set output | inline_python(val1="Some output") %}
          print(val1)
          {% endset %}
          {{ output }}

    - debug:
        msg: |
          -----------------------------------------------

          TEST #3 (full here-doc style with variable manipulation):

          {% set fruit_inventory = {"apples": 3, "oranges": 6} %}
          {% set fruit_list = ["apples", "oranges"] %}

          {% set output | inline_python(title="Fruit:", my_inventory=fruit_inventory, my_list=fruit_list) %}
          print(title)
          print(my_list)
          print(my_inventory)

          my_inventory['lemons'] = 1000
          my_inventory['apples'] = 0
          my_list.append("bananas")
          
          {% endset %}
          [---BEFORE---]{{ output }}

          [---AFTER---]
          {{ fruit_list }}

          {{ fruit_inventory }}

    - debug:
        msg: |
          -----------------------------------------------
          TEST #4 (inline python as a function with a return):
          {% set output = """          
          some_dict={'a': 1, 'b': val1}
          __return_var('some_dict')          
          """ | inline_python_func(val1="Some output") %}
          {{ output }}

```

License
-------

Apache 2.0

Author Information
------------------

https://github.com/ipchama
