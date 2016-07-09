{{collection.info.description}}

{% for item in collection.item %}
# {{item.name}}

{{ item.description }}

{% for item in item.item %}
{% include 'endpoints.html.md' %}
{% endfor %}

{% endfor %}

