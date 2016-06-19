---
layout: base
title:  'Features'
generated: 'true'
permalink: bg/feat/all.html
---

{% capture lcode %}{{ page.permalink | split:"/" | first }}{% endcapture %}

# Features

<span about="." property="rdf:type" resource="owl:Ontology">
	<span property="owl:imports" resource="
https://www.w3.org/2012/pyRdfa/extract?uri=http://universaldependencies.org/docs/u/feat/all.html&format=xml&rdfagraph=output&vocab_expansion=false&rdfa_lite=false&embedded_rdf=true&space_preserve=false&vocab_cache=true&vocab_cache_report=false&vocab_cache_refresh=false"/>
</span>

<span about="#feat_{{ lcode }}" property="rdfs:label" style="visibility: hidden">{{ page.title }}</span>
<span about="#feat_{{ lcode }}" property="rdfs:subClassOf" resource="_:{{ lcode }}">
	<span about="_:{{ lcode }}" property="rdf:type" resource="owl:Restriction">
		<span property="owl:onProperty" resource="http://purl.org/dc/terms/language"/>
		<span property="owl:hasValue" lang=""  style="visibility: hidden">{{ lcode }}</span>
	</span>
</span>

{% include bg-feat-table.html %}

----------

{% assign sorted = site.bg-feat | sort: 'title' %}
{% for p in sorted %}
<div about="#{{ p.title | url_encode }}_{{ lcode }}" property="rdfs:subClassOf" resource="#feat_{{ lcode }}">
	<a id="al-{{ lcode }}-feat/{{ p.title }}" class="al-dest"/>
	<h2><code property="rdfs:label" lang="">{{ p.title }}</code>: <span property="rdfs:label">{{ p.shortdef }}</span>
	<code>[</code> 
	{% assign pars = p.content | split: "### " %}
	{% for par in pars %}
		{% assign cand_feats = par | split: ":" %}
		{% for cand_feat in cand_feats %}
			{% if cand_feat contains "`" %}
				{% if cand_feat contains " " %}{% else %}
					{% assign feat = cand_feat | replace: "`","" %}
					<span about="#{{ p.title | url_encode }}{{ feat | url_encode }}_{{ lcode }}" property="rdf:type" resource="#{{ p.title | url_encode }}_{{ lcode }}">
						<span property="rdf:type" resource="../../u/feat/all.html#{{ p.title | split:':' | first }}{{ feat | split:':' | first }}"/>
						<code property="oliasystem:hasTagContaining" lang="">{{ p.title }}={{ feat }}</code>
					</span>
				{% endif %}
			{% endif %}
		{% endfor %}
	{% endfor %}
	<code>]</code>
	</h2>
	<div about="#{{ p.title | url_encode }}_{{ lcode }}" property="rdfs:comment">	
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
