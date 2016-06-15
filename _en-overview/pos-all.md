---
layout: base
title:  'POS tags'
generated: 'true'
permalink: en/pos/all.html
---

{% capture lcode %}{{ page.permalink | split:"/" | first }}{% endcapture %}

# POS tags

# import UD POS ontology
<span about="." property="rdf:type" resource="owl:Ontology">
	<span property="owl:imports" resource="
https://www.w3.org/2012/pyRdfa/extract?uri=http://universaldependencies.org/docs/u/pos/all.html&format=xml&rdfagraph=output&vocab_expansion=false&rdfa_lite=false&embedded_rdf=true&space_preserve=false&vocab_cache=true&vocab_cache_report=false&vocab_cache_refresh=false"/>
</span>

<span about="#Concept" property="rdfs:subClassOf" resource="_:{{ lcode }}">
	<span about="_:{{ lcode }}" property="rdf:type" resource="owl:Restriction">
		<span property="owl:onProperty" resource="http://purl.org/dc/terms/language"/>
		<span property="owl:hasValue" lang=""  style="visibility: hidden">en</span>
	</span>
</span>

{% include en-pos-table.html %}

----------

{% assign sorted = site.en-pos | sort: 'title' %}
{% for p in sorted %}
<div about="#{{ p.title }}_{{ lcode }}" property="rdf:type" resource="#Concept">
	<div property="rdf:type" resource="../../u/pos/all.html#{{ p.title }}">
	   <div about="../../u/pos/all.html#{{ p.title }}" property="rdfs:subClassOf" resource="../../u/pos/all.html#Concept"/>
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
