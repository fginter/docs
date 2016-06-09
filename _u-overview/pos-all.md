---
layout: base
title:  'Universal POS tags'
generated: 'true'
permalink: u/pos/all.html
---

# Universal POS tags

{% include u-pos-table.html %}

----------

{% assign sorted = site.u-pos | sort: 'title' %}
{% for p in sorted %}
<div about="#{{ p.title }}" property="rdfs:subClassOf" resource="#Concept">
<a id="al-u-pos/{{ p.title }}" class="al-dest"/>
<h2><code property="rdfs:label" lang="">{{ p.title }}</code>: <div property="rdfs:label">{{ p.shortdef }}</div></h2>
<div property="rdfs:comment">
{% if p.content contains "<!--details-->" %}    
{{ p.content | split:"<!--details-->" | first }}
<a property="rdfs:seeAlso" href="{{ p.title }}" class="al-doc">See details</a>
{% else %}
{{ p.content }}
{% endif %}
</div>
<a href="{{ site.git_edit }}/{% if p.collection %}{{ p.relative_path }}{% else %}{{ p.path }}{% endif %}" target="#">edit {{ p.title }}</a>
</div>
{% endfor %}
