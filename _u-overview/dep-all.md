---
layout: base
title:  'Universal Dependencies'
generated: 'true'
permalink: u/dep/all.html
---

# Universal Dependencies

<span about="." property="rdf:type" resource="owl:Ontology">
	<span property="owl:versionInfo">
The inventory of dependency relations is adapted from [*Universal Stanford Dependencies:
A cross-linguistic typology*](http://nlp.stanford.edu/pubs/USD_LREC14_paper_camera_ready.pdf) (de Marneffe *et al.* 2014). There have been modifications in the relations: we now have 40 universal relations (instead of the 42 ones proposed in the paper).
	</span>
</span>

<span about="#dep" property="rdfs:label" style="visibility: hidden">{{ page.title }}</span>
<span about="#dep" property="rdfs:subClassOf" resource="_:{{ tier }}">
	<span about="_:{{ tier }}" property="rdf:type" resource="owl:Restriction">
		<span property="owl:onProperty" resource="oliasystem:hasTier"/>
		<span property="owl:hasValue" lang=""  style="visibility: hidden">DEPREL</span>
	</span>
</span>

{% include u-dep-table.html %}

----------

{% assign sorted = site.u-dep | sort: 'title' %}
{% for p in sorted %}
<div about="#{{ p.title }}" property="rdfs:subClassOf" resource="#dep">
	<a id="al-u-dep/{{ p.title }}" class="al-dest"/>
	<h2><code property="rdfs:label" lang="">{{ p.title }}</code>: <div property="rdfs:label">{{ p.shortdef }}</div></h2>
	<div property="rdfs:comment">
{% if p.content contains "<!--details-->" %}    
{{ p.content | split:"<!--details-->" | first | markdownify }}
		<a property="rdfs:seeAlso" href="{{ p.title }}" class="al-doc">See details</a>
{% else %}
{{ p.content | markdownify }}
{% endif %}
	</div>
	<a href="{{ site.git_edit }}/{% if p.collection %}{{ p.relative_path }}{% else %}{{ p.path }}{% endif %}" target="#">edit {{ p.title }}</a>
</div>
{% endfor %}
