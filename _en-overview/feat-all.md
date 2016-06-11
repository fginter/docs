---
layout: base
title:  'Features'
generated: 'true'
permalink: en/feat/all.html
---

# Features

{% include en-feat-table.html %}

----------

{% assign sorted = site.en-feat | sort: 'title' %}
{% for p in sorted %}
<div about="#{{ p.title }}" property="rdfs:subClassOf" resource="#Concept">
	<a id="al-en-feat/{{ p.title }}" class="al-dest"/>
	<h2><code property="rdfs:label" lang="">{{ p.title }}</code>: <div property="rdfs:label">{{ p.shortdef }}</div></h2>
	{% assign pars = p.content | split: "### " %}
	{% for par in pars %}
		{% assign cand_feats = par | split: ":" %}
		{% for cand_feat in cand_feats %}
			{% if cand_feat contains "`" %}
				{% if cand_feat contains " " %}{% else %}
					{% assign feat = cand_feat | replace: "`","" %}
					<div about="#{{ p.title }}{{ feat }}" property="rdf:type" resource="#{{ p.title }}" style="visibility: hidden">
						<div property="rdf:type" resource="../../u/feat/all.html#{{ p.title }}{{ feat }}"/>
						<div property="oliasystem:hasTagContaining">{{ p.title }}={{ feat }}</div>
					</div>
				{% endif %}
			{% endif %}
		{% endfor %}
	{% endfor %}
	
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
