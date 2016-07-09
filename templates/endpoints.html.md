## {{item.name}}

```python
import requests

{% if item.request.method == 'GET' %}
requests.get("{{item.request.url | postman_url}}")
{% elif item.request.method == 'POST' %}
requests.post("{{item.request.url | postman_url}}")
{% elif item.request.method == 'PUT' %}
requests.put("{{item.request.url | postman_url}}")
{% elif item.request.method == 'DELETE' %}
requests.delete("{{item.request.url | postman_url}}")
{% endif %}
```

```shell
curl "{{item.request.url | postman_url}}"
  -H "Authorization: meowmeowmeow"
```

> The above command returns JSON structured like this:

{% for response in item.response %}
```json
{{ response.body }}
```
{% endfor %}

{%if item.get('description') %}
{{item.get('description')}}
{% endif %}

### HTTP Request

`{{item.request.method}} {{item.request.url | postman_url}}`

{% if False %}
### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
include_cats | false | If set to true, the result will also include cats.
available | true | If set to false, the result will include kittens that have already been adopted.
{% endif %}

{% if item.request.body.urlencoded %}
### Attributes

Parameter | Type
--------- | ---- {% for attribute in item.request.body.urlencoded %}
{{attribute.key}} | {{attribute.value}}
{% endfor %}

{% endif %}