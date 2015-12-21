

--------------------------------------------------------------------------------

## Treebank Statistics

This relation is universal.

989 nodes (0%) are attached to their parents as `iobj`.

735 instances of `iobj` (74%) are left-to-right (parent precedes child).
Average distance between parent and child is 2.685540950455.

The following 9 pairs of parts of speech are connected with `iobj`: [pt-pos/VERB]()-[pt-pos/NOUN]() (484; 49% instances), [pt-pos/VERB]()-[pt-pos/PRON]() (375; 38% instances), [pt-pos/VERB]()-[pt-pos/PROPN]() (106; 11% instances), [pt-pos/VERB]()-[pt-pos/DET]() (10; 1% instances), [pt-pos/VERB]()-[pt-pos/ADJ]() (5; 1% instances), [pt-pos/VERB]()-[pt-pos/NUM]() (4; 0% instances), [pt-pos/VERB]()-[pt-pos/ADV]() (2; 0% instances), [pt-pos/VERB]()-[pt-pos/SYM]() (2; 0% instances), [pt-pos/AUX]()-[pt-pos/NOUN]() (1; 0% instances).


~~~ conllu
# visual-style 6	bgColor:blue
# visual-style 6	fgColor:white
# visual-style 4	bgColor:blue
# visual-style 4	fgColor:white
# visual-style 4 6 iobj	color:blue
1	Eu	eu	PRON	pron-pers|M|1S|NOM	Case=Nom|Gender=Masc|Number=Sing|Person=1|PronType=Prs	4	nsubj	_	_
2	não	não	ADV	adv	_	4	neg	_	_
3	me	eu	PRON	pron-pers|<refl>|M|1S|ACC	Case=Acc|Gender=Masc|Number=Sing|Person=1|PronType=Prs|Reflex=Yes	4	dobj	_	_
4	associo	associar	VERB	v-fin|PR|1S|IND	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	_
5	com	com	ADP	prp	AdpType=Prep	6	case	_	_
6	moda	moda	NOUN	n|F|S	Gender=Fem|Number=Sing	4	iobj	_	_
7	.	.	PUNCT	punc	_	4	punct	_	_

~~~


~~~ conllu
# visual-style 2	bgColor:blue
# visual-style 2	fgColor:white
# visual-style 3	bgColor:blue
# visual-style 3	fgColor:white
# visual-style 3 2 iobj	color:blue
1	«	«	PUNCT	punc	_	3	punct	_	_
2	Me	eu	PRON	pron-pers|<refl>|M|1S|DAT	Case=Dat|Gender=Masc|Number=Sing|Person=1|PronType=Prs|Reflex=Yes	3	iobj	_	_
3	pergunto	perguntar	VERB	v-fin|PR|1S|IND	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	_
4	sempre	sempre	ADV	adv	_	3	advmod	_	_
5	quem	quem	PRON	pron-indp|<rel>|M|S	Gender=Masc|Number=Sing|PronType=Rel	6	nsubj	_	_
6	podia	poder	VERB	v-fin|IMPF|3S|IND	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	3	ccomp	_	_
7	ter	ter	AUX	v-inf	VerbForm=Inf	6	aux	_	_
8	sido	ser	VERB	v-pcp	VerbForm=Part	11	cop	_	_
9	aquele	aquele	DET	pron-det|<dem>|M|S	Gender=Masc|Number=Sing|PronType=Dem	11	det	_	_
10	jovem	jovem	ADJ	adj|M|S	Gender=Masc|Number=Sing	11	amod	_	_
11	alemão	alemão	NOUN	n|M|S	Gender=Masc|Number=Sing	7	ccomp	_	_
12	.	.	PUNCT	punc	_	3	punct	_	_
13	»	»	PUNCT	punc	_	3	punct	_	_

~~~


~~~ conllu
# visual-style 8	bgColor:blue
# visual-style 8	fgColor:white
# visual-style 4	bgColor:blue
# visual-style 4	fgColor:white
# visual-style 4 8 iobj	color:blue
1	O	o	DET	art|<artd>|M|S	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	2	det	_	_
2	PSD	PSD	PROPN	prop|M|S	Gender=Masc|Number=Sing	3	nsubj	_	_
3	decidiu	decidir	VERB	v-fin|PS|3S|IND	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin	0	root	_	_
4	deixar	deixar	VERB	v-inf	VerbForm=Inf	3	xcomp	_	_
5	hoje	hoje	ADV	adv	_	4	advmod	_	_
6	pronta	pronto	ADJ	adj|F|S	Gender=Fem|Number=Sing	4	xcomp	_	_
7	a	o	DET	art|<artd>|F|S	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	8	det	_	_
8	Lei_da_Greve	Lei_da_Greve	PROPN	prop|F|S	Gender=Fem|Number=Sing	4	iobj	_	_
9	.	.	PUNCT	punc	_	3	punct	_	_

~~~


