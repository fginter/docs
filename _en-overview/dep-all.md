---
layout: base
title:  'English grammatical relations'
generated: 'true'
permalink: en/dep/all.html
---

# not working yet:
<div about="#Concept" property="http://purl.org/dc/terms/language" style="visibility: hidden">{{ permalink | replace: '/.*', '' }}</div>

These pages draw from Section 2 of *[Stanford typed dependencies
manual](http://nlp.stanford.edu/software/dependencies_manual.pdf)* (de
Marneffe and Manning 2008), but have been updated for UD.

{% include en-dep-table.html %}

----------

{% assign sorted = site.en-dep | sort: 'title' %}
{% for p in sorted %}
<div about="#{{ p.title }}" property="rdf:type" resource="#Concept">
	<div property="rdf:type" resource="../../u/pos/all.html#{{ p.title }}">
	   <div about="../../u/pos/all.html#{{ p.title }}" property="rdf:type" resource="../../u/pos/all.html#Concept"/>
	</div>
	<a id="al-en-dep/{{ p.title }}" class="al-dest"/>

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
