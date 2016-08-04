#Note: much of the at-glance table generation happens in templates/atglance.html -> go see there
# this code produces the dictionary which holds the data for rendering the template
# and then simply feeds that dictionary to jinja2 which does its magic with the template

import sys
import glob
import os.path
import json
import re
import codecs
import StringIO
import jinja2
jinja2_env=jinja2.Environment(loader=jinja2.FileSystemLoader("./templates", encoding='utf-8', followlinks=False))
languages_template=jinja2_env.get_template("atglance.html")



# categories={(u"Documentation status",u"stub"):"""<span class="widespan" style="color:gray"><span class="hint--top hint--info" data-hint="No documentation">-</span></span>""",
#             (u"Documentation status",u"partial"):"""<span class="widespan"><span class="hint--top hint--info" data-hint="Partial documentation"><i class="fa fa-file-o"></i></span></span>""",
#             (u"Documentation status",u"complete"):"""<span class="widespan"><span class="hint--top hint--info" data-hint="Complete documentation"><i class="fa fa-file-text-o"></i></span></span>""",
#             (u"Data source",u"unknown"):"""<span class="widespan"><span class="hint--top hint--info" data-hint="Data source not known">-</span></span>""",
#             (u"Data source",u"automatic"):"""<span class="widespan"><span class="hint--top hint--info" data-hint="Automatic conversion"><i class="fa fa-cogs"></i></span></span>""",
#             (u"Data source",u"semi-automatic"):"""<span class="widespan"><span class="hint--top hint--info" data-hint="Automatic conversion with manual corrections"><i class="fa fa-cogs"></i><!--<i class="fa fa-plus" style="font-size: 0.75em; line-height: 1.33em; vertical-align: +10%;">--><i class="fa fa-check"></i></span></span>""",
#             (u"Data source",u"manual"):"""<span class="widespan"><span class="hint--top hint--info" data-hint="Full manual check of the data"><i class="fa fa-user"></i></span></span>""",
#             (u"License",u"none"):"""<span class="widespan"><span class="hint--top hint--info" data-hint="License not known">-</span></span>""",
#             (u"Data available since",u"UD v1.0"):"""<span class="widespan"><span class="hint--top hint--info" data-hint="First released in UD version 1.0 (Jan 2015)"><i class="fa fa-check"></i></span></span>""",
#             (u"Data available since",u"UD v1.1"):"""<span class="widespan"><span class="hint--top hint--info" data-hint="First released in UD version 1.1 (May 2015)"><i class="fa fa-check"></i></span></span>""",
#             (u"Data available since",u"UD v1.2"):"""<span class="widespan"><span class="hint--top hint--info" data-hint="First released in UD version 1.2 (November 2015)"><i class="fa fa-check"></i></span></span>""",
#             (u"Data available since",u"UD v1.3"):"""<span class="widespan"><span class="hint--top hint--info" data-hint="First released in UD version 1.3 (May 2016)"><i class="fa fa-check"></i></span></span>""",
#             (u"Data available since",u"UD v2.0"):"""<span class="widespan"><span class="hint--top hint--info" data-hint="Scheduled for release in UD version 2.0 (November 2016)"><i class="fa fa-hourglass-end"></i></span></span>""",
#             (u"Data available since",u"none"):"""<span class="widespan"><span class="hint--top hint--info" data-hint="No firm schedule for data release">-</span></span>"""}

valueRe=re.compile(u"^([a-zA-Z ]+): (.+)$")
def analyze_readme(dir_name):
    readme_data={u"Documentation status":u"stub",u"Data source":u"unknown",u"License":u"unknown",u"Data available since":u"unknown", u"Genre":u"none",u"Contributors":u""}
    readmes=sorted(x for x in glob.glob(os.path.join(dir_name,"*")) if "readme" in x.lower())
    if not readmes: #No readme file!
        return readme_data
    with codecs.open(readmes[0],"r","utf-8") as f:
        for line in f:
            match=valueRe.match(line)
            if match: #Maybe one of our values?
                cat,val=match.group(1).strip(),match.group(2).strip()
                readme_data[cat]=val
                # if (cat,val) in categories:
                #     #Yes! this is a known category, we have a perfect match
                #     readme_data[cat]=val
                # elif cat in readme_data: #Known category but unknown value, I guess it's okay
                #     #Known cat, but weird val --- should we warn?
                #     readme_data[cat]=val
    return readme_data
                
def gen_table(args):
    flags=json.loads(open("flags.json").read())
    genres_map=json.loads(open("genre_symbols.json","r").read())
    lcodes=json.loads(open("lcodes.json").read())

    for k,v in genres_map.iteritems():
        genres_map[k]=v.replace("_","-")

    template_data={}  #{language -> {  }}

    jekyll_data=[] #this will go to jekyll then as data
    
    a_data=StringIO.StringIO()
    print >> a_data, "<!-- content of _includes/at_glance.html -->"
    print >> a_data, "<!-- do NOT edit by hand, that file is autogenerated using gen_index/index_page.py -->"
    # Will create a line for every language which has a repository
    langs=sorted(os.path.basename(x).replace(".json","") for x in glob.glob("_corpus_data/*.json"))
    for l in langs:
        with open(os.path.join("_corpus_data",l+".json"),"r") as f:
            corpus_data=json.load(f)
        readme_data=analyze_readme(os.path.join(args.ud_data,"UD_"+l))
        
        language_name=l.split("-")[0]
        ldict=template_data.setdefault(language_name,{"language_name":language_name,"language_code":lcodes[l].split("_")[0],"treebanks":[]})
        cdict={"treebank_name":l,"treebank_language_code":lcodes[l],"flag":flags[l]}
        ldict["treebanks"].append(cdict)
        if corpus_data.get("token_count",0):
            cdict["token_count_k"]="{:,}K".format(corpus_data.get("token_count")//1000)
            cdict["count_hint"]="{token_count:,} tokens {word_count:,} words {tree_count:,} sentences".format(**corpus_data)
        else:
            cdict["token_count_k"]="-"
            cdict["count_hint"]="No corpus data"
        cdict["columns"]=[]
        if corpus_data.get("words_with_lemma_count",0)>int(corpus_data.get("word_count")*0.9):
            cdict["columns"].append("L")
        else:
            cdict["columns"].append("N/A")
        if corpus_data.get("catvals",0)>0:
            cdict["columns"].append("F")
        else:
            cdict["columns"].append("N/A")
        if corpus_data.get("words_with_deps_count",0)>0:
            cdict["columns"].append("D")
        else:
            cdict["columns"].append("N/A")
        
        cdict["docstatus"]=readme_data.get("Documentation status","stub")
        cdict["source"]=readme_data.get("Data source","unknown")
        cdict["avail"]=readme_data["Data available since"]
        
        lic=readme_data.get("License","Unknown license")
        if "CC BY-NC-SA" in lic:
            cdict["liclogo"]="by-nc-sa.svg"
        elif "CC BY-SA" in lic:
            cdict["liclogo"]="by-sa.svg"
        elif "CC BY" in lic:
            cdict["liclogo"]="by.svg"
        elif "GPL" in lic:
            cdict["liclogo"]="gpl.svg"
        else:
            cdict["liclogo"]="N/A"
        cdict["lictext"]=lic
        cdict["genres"]=[]
        for g in readme_data["Genre"].split():
            cdict["genres"].append(genres_map.get(g,genres_map["none"]))
        cdict["genre_text"]=readme_data["Genre"]
        
    print languages_template.render(languages=template_data)


# # #        corpus_data[u"lang_code"]=lcodes[l]
# # #        corpus_data[u"lang_name"]=l
# # #        corpus_data[u"langfam_code"]=lcodes[l].split("_")[0]
# # #        corpus_data[u"langfam_name"]=l.split("-")[0]
# # #        print >> a_data, '<div data-lc="%s">' % lcodes[l]
# # #        print >> a_data, get_flag_span(l)
# # #        print >> a_data, get_language_span(l)
# #         print >> a_data, get_token_count_span(corpus_data)
# #         print >> a_data, get_column_icons(corpus_data)
# #         readme_data=analyze_readme(os.path.join(args.ud_data,"UD_"+l))
# #         print >> sys.stderr, l
# #         for c in (u"Documentation status", u"Data source", u"Data available since"):
# #             print >> a_data, categories.get((c,readme_data[c]),empty_wide_span.format(hint=readme_data[c]))
# #         print >> a_data, get_license_span(readme_data[u"License"])
# #         print >> a_data, get_genre_span(readme_data["Genre"])
# #         print >> a_data, "</div>"
# #         print >> a_data, "<div>"
# #         print >> a_data, link_template.format(**corpus_data)
# #         print >> a_data, "</div>"
        
# #         ldict={}
# #         ldict[u"lang_name"]=corpus_data[u"lang_name"]
# #         ldict[u"lang_code"]=corpus_data[u"lang_code"]
# #         ldict[u"contributors"]=[]
# #         if readme_data["Contributors"].strip():
# #             for c in readme_data["Contributors"].strip().split(u";"):
# #                 c=c.strip()
# #                 lf=c.split(u",",1)
# #                 if len(lf)==2:
# #                     ldict[u"contributors"].append({u"last":lf[0].strip(),u"first":lf[1].strip(), u"full":lf[1].strip()+u" "+lf[0].strip()})
# #                 else:
# #                     ldict[u"contributors"].append({u"last":c,u"first":u"?",u"full":c})
# #         jekyll_data.append(ldict)
# #     return a_data,jekyll_data

# def gen_table_old(args):

#     jekyll_data=[] #this will go to jekyll then as data
    
#     a_data=StringIO.StringIO()
#     print >> a_data, "<!-- content of _includes/at_glance.html -->"
#     print >> a_data, "<!-- do NOT edit by hand, that file is autogenerated using gen_index/index_page.py -->"
#     # Will create a line for every language which has a repository
#     langs=sorted(os.path.basename(x).replace(".json","") for x in glob.glob("_corpus_data/*.json"))
#     for l in langs:
#         with open(os.path.join("_corpus_data",l+".json"),"r") as f:
#             corpus_data=json.load(f)
#         corpus_data[u"lang_code"]=lcodes[l]
#         corpus_data[u"lang_name"]=l
#         corpus_data[u"langfam_code"]=lcodes[l].split("_")[0]
#         corpus_data[u"langfam_name"]=l.split("-")[0]
#         print >> a_data, '<div data-lc="%s">' % lcodes[l]
#         print >> a_data, get_flag_span(l)
#         print >> a_data, get_language_span(l)
#         print >> a_data, get_token_count_span(corpus_data)
#         print >> a_data, get_column_icons(corpus_data)
#         readme_data=analyze_readme(os.path.join(args.ud_data,"UD_"+l))
#         print >> sys.stderr, l
#         for c in (u"Documentation status", u"Data source", u"Data available since"):
#             print >> a_data, categories.get((c,readme_data[c]),empty_wide_span.format(hint=readme_data[c]))
#         print >> a_data, get_license_span(readme_data[u"License"])
#         print >> a_data, get_genre_span(readme_data["Genre"])
#         print >> a_data, "</div>"
#         print >> a_data, "<div>"
#         print >> a_data, link_template.format(**corpus_data)
#         print >> a_data, "</div>"
        
#         ldict={}
#         ldict[u"lang_name"]=corpus_data[u"lang_name"]
#         ldict[u"lang_code"]=corpus_data[u"lang_code"]
#         ldict[u"contributors"]=[]
#         if readme_data["Contributors"].strip():
#             for c in readme_data["Contributors"].strip().split(u";"):
#                 c=c.strip()
#                 lf=c.split(u",",1)
#                 if len(lf)==2:
#                     ldict[u"contributors"].append({u"last":lf[0].strip(),u"first":lf[1].strip(), u"full":lf[1].strip()+u" "+lf[0].strip()})
#                 else:
#                     ldict[u"contributors"].append({u"last":c,u"first":u"?",u"full":c})
#         jekyll_data.append(ldict)
#     return a_data,jekyll_data

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='generates the index page')
    parser.add_argument('--ud-data', required=True, help='Where is the UD data, so I can grab the readmes? (DIRECTORY)')
    parser.add_argument('--ldict', default="../_data/ldata.json", help='Where to write the language dict file? (Default %(default)s)')
    args = parser.parse_args()
    gen_table(args)
    
    # a_data,ldict=gen_table(args)
    # print a_data.getvalue()
    # if args.ldict:
    #     with open(args.ldict,"w") as out:
    #         json.dump(ldict,out,indent=2)

    
