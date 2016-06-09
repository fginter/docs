---
layout: base
title:  'POS tags'
generated: 'true'
permalink: en/pos/all.html
---

# POS tags

<div about="#Concept" property="http://purl.org/dc/terms/language" style="visibility: hidden">{{ permalink | replace: '/.*', '' }}</div>
		

{% include en-pos-table.html %}

----------

{% assign sorted = site.en-pos | sort: 'title' %}
{% for p in sorted %}
<div about="#{{ p.title }}" property="rdf:type" resource="#Concept">
	<div property="rdf:type" resource="../../u/pos/all.html#{{ p.title }}">
	   <div about="../../u/pos/all.html#{{ p.title }}" property="rdf:type" resource="../../u/pos/all.html#Concept"/>
	</div>
<a id="al-en-pos/{{ p.title }}" class="al-dest"/>

<h2><code property="oliasystem:hasTag" lang="">{{ p.title }}</code>: <div property="rdfs:label">{{ p.shortdef }}</div></h2>
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
