---
layout: base
title:  'Universal POS tags'
generated: 'true'
permalink: u/pos/all.html
---

# Universal POS tags

<span about="#pos" property="rdfs:label" style="visibility: hidden">{{ page.title }}</span>
<span about="#pos" property="rdfs:subClassOf" resource="_:{{ tier }}">
	<span about="_:{{ tier }}" property="rdf:type" resource="owl:Restriction">
		<span property="owl:onProperty" resource="oliasystem:hasTier"/>
		<span property="owl:hasValue" lang=""  style="visibility: hidden">UPOS</span>
	</span>
</span>

{% include u-pos-table.html %}

----------

{% assign sorted = site.u-pos | sort: 'title' %}
{% for p in sorted %}
<div about="#{{ p.title }}" property="rdfs:subClassOf" resource="#pos">
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
