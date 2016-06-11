---
layout: base
title:  'Universal features'
generated: 'true'
permalink: u/feat/all.html
---

# Universal features

{% include u-feat-table.html %}

----------

{% assign sorted = site.u-feat | sort: 'title' %}
{% for p in sorted %}

<div about="#has{{ p.title }}" property="rdf:type" resource="owl:ObjectProperty">
	<div property="rdfs:range" resource="#{{ p.title }}"/>
</div>
<div about="#{{ p.title }}" property="rdfs:subClassOf" resource="#Concept">
	<a id="al-u-feat/{{ p.title }}" class="al-dest"/>
	<h2><code>{{ p.title }}</code>: {{ p.shortdef }}</h2>
	<div property="rdfs:comment">
	{% assign pars = p.content | split: "### " %}
	{% for par in pars %}
		{% assign cand_feats = par | split: ":" %}
		{% for cand_feat in cand_feats %}
			{% if cand_feat contains "`" %}
				{% if cand_feat contains " " %}
				{% else %}
					<div style="visibility: hidden">cf:{{ cand_feat }}</div>
				{% endif %}
			{% endif %}
		{% endfor %}
	{% endfor %}

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
