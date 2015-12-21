

--------------------------------------------------------------------------------

## Treebank Statistics

This relation is universal.

193 nodes (0%) are attached to their parents as `dep`.

157 instances of `dep` (81%) are left-to-right (parent precedes child).
Average distance between parent and child is 6.62694300518135.

The following 37 pairs of parts of speech are connected with `dep`: [pt-pos/VERB]()-[pt-pos/VERB]() (35; 18% instances), [pt-pos/NOUN]()-[pt-pos/VERB]() (24; 12% instances), [pt-pos/VERB]()-[pt-pos/PRON]() (18; 9% instances), [pt-pos/ADJ]()-[pt-pos/VERB]() (17; 9% instances), [pt-pos/VERB]()-[pt-pos/NOUN]() (16; 8% instances), [pt-pos/NOUN]()-[pt-pos/NOUN]() (13; 7% instances), [pt-pos/VERB]()-[pt-pos/PROPN]() (7; 4% instances), [pt-pos/ADV]()-[pt-pos/NOUN]() (6; 3% instances), [pt-pos/PROPN]()-[pt-pos/VERB]() (6; 3% instances), [pt-pos/ADP]()-[pt-pos/NOUN]() (4; 2% instances), [pt-pos/ADP]()-[pt-pos/VERB]() (4; 2% instances), [pt-pos/NOUN]()-[pt-pos/ADP]() (4; 2% instances), [pt-pos/ADV]()-[pt-pos/DET]() (3; 2% instances), [pt-pos/DET]()-[pt-pos/NOUN]() (3; 2% instances), [pt-pos/PRON]()-[pt-pos/VERB]() (3; 2% instances), [pt-pos/PROPN]()-[pt-pos/ADV]() (3; 2% instances), [pt-pos/PROPN]()-[pt-pos/NOUN]() (3; 2% instances), [pt-pos/ADJ]()-[pt-pos/NOUN]() (2; 1% instances), [pt-pos/NOUN]()-[pt-pos/ADJ]() (2; 1% instances), [pt-pos/NOUN]()-[pt-pos/INTJ]() (2; 1% instances), [pt-pos/PROPN]()-[pt-pos/PROPN]() (2; 1% instances), [pt-pos/ADV]()-[pt-pos/PRON]() (1; 1% instances), [pt-pos/ADV]()-[pt-pos/VERB]() (1; 1% instances), [pt-pos/DET]()-[pt-pos/ADV]() (1; 1% instances), [pt-pos/DET]()-[pt-pos/PROPN]() (1; 1% instances), [pt-pos/DET]()-[pt-pos/VERB]() (1; 1% instances), [pt-pos/INTJ]()-[pt-pos/NOUN]() (1; 1% instances), [pt-pos/INTJ]()-[pt-pos/PROPN]() (1; 1% instances), [pt-pos/NOUN]()-[pt-pos/PRON]() (1; 1% instances), [pt-pos/NUM]()-[pt-pos/NOUN]() (1; 1% instances), [pt-pos/NUM]()-[pt-pos/PRON]() (1; 1% instances), [pt-pos/NUM]()-[pt-pos/VERB]() (1; 1% instances), [pt-pos/PROPN]()-[pt-pos/ADJ]() (1; 1% instances), [pt-pos/PROPN]()-[pt-pos/ADP]() (1; 1% instances), [pt-pos/PROPN]()-[pt-pos/INTJ]() (1; 1% instances), [pt-pos/SCONJ]()-[pt-pos/VERB]() (1; 1% instances), [pt-pos/VERB]()-[pt-pos/DET]() (1; 1% instances).


~~~ conllu
# visual-style 9	bgColor:blue
# visual-style 9	fgColor:white
# visual-style 1	bgColor:blue
# visual-style 1	fgColor:white
# visual-style 1 9 dep	color:blue
1	Sabe	saber	VERB	v-fin|PR|3S|IND	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
2	que	que	SCONJ	conj-s	_	1	dobj	_	_
3	se	se	SCONJ	conj-s	_	5	mark	_	_
4	não	não	ADV	adv	_	5	neg	_	_
5	chegar	chegar	VERB	v-fin|FUT|3S|SUBJ	Mood=Sub|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin	2	advcl	_	_
6	a	a	ADP	prp	AdpType=Prep	7	case	_	_
7	acordo	acordo	NOUN	n|M|S	Gender=Masc|Number=Sing	5	nmod	_	_
8	,	,	PUNCT	punc	_	1	punct	_	_
9	é	ser	VERB	v-fin|PR|3S|IND	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	1	dep	_	_
10	chumbado	chumbar	VERB	v-pcp|M|S	Gender=Masc|Number=Sing|VerbForm=Part	9	ccomp	_	_
11	.	.	PUNCT	punc	_	1	punct	_	_

~~~


~~~ conllu
# visual-style 6	bgColor:blue
# visual-style 6	fgColor:white
# visual-style 8	bgColor:blue
# visual-style 8	fgColor:white
# visual-style 8 6 dep	color:blue
1	Um	um	NUM	num|<card>|M|S	Gender=Masc|Number=Sing|NumType=Card	8	cop	_	_
2	de	de	ADP	prp|<sam->	AdpType=Prep	5	case	_	_
3	estes	este	DET	pron-det|<-sam>|<dem>|M|P	Gender=Masc|Number=Plur|PronType=Dem	5	det	_	_
4	trágicos	trágico	ADJ	adj|M|P	Gender=Masc|Number=Plur	5	amod	_	_
5	erros	erro	NOUN	n|M|P	Gender=Masc|Number=Plur	8	nmod	_	_
6	foi	ser	VERB	v-fin|PS|3S|IND	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin	8	dep	_	_
7	o	o	DET	art|<artd>|M|S	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	8	det	_	_
8	maniqueísmo	maniqueísmo	NOUN	n|M|S	Gender=Masc|Number=Sing	0	root	_	_
9	.	.	PUNCT	punc	_	8	punct	_	_

~~~


~~~ conllu
# visual-style 2	bgColor:blue
# visual-style 2	fgColor:white
# visual-style 1	bgColor:blue
# visual-style 1	fgColor:white
# visual-style 1 2 dep	color:blue
1	Pense-	pensar	VERB	v-fin|PR|3S|SUBJ	Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
2	se	se	PRON	pron-pers|M/F|3S/P|ACC	Case=Acc|Person=3|PronType=Prs	1	dep	_	_
3	em	em	ADP	prp	AdpType=Prep	4	case	_	_
4	Kingsley	Kingsley	PROPN	prop|M/F|S	Number=Sing	1	dobj	_	_
5	Amis	Amis	PROPN	PROPN	Number=Sing	4	name	_	_
6	,	,	PUNCT	punc	_	4	punct	_	_
7	Malcolm	Malcolm	PROPN	prop|M|S	Gender=Masc|Number=Sing	4	conj	_	_
8	Bradbury	Bradbury	PROPN	PROPN	Gender=Masc|Number=Sing	7	name	_	_
9	e	e	CONJ	conj-c|<co-prparg>	_	4	cc	_	_
10	Albert	Albert	PROPN	prop|M|S	Gender=Masc|Number=Sing	4	conj	_	_
11	Finney	Finney	PROPN	PROPN	Gender=Masc|Number=Sing	10	name	_	_
12	.	.	PUNCT	punc	_	1	punct	_	_

~~~


