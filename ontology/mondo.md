---
layout: ontology_detail
id: mondo
label: MONDO
title: Mondo Disease Ontology
description: An ontology that harmonizes multiple disease resources.
homepage: https://github.com/monarch-initiative/mondo
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
contact:
  email: vasilevs@ohsu.edu
  label: Nicole Vasilevsky
  github: nicolevasilevsky
taxon:
  id: NCBITaxon:33208
  label: Metazoa
domain: disease
tracker: https://github.com/monarch-initiative/mondo-build/issues
mailing_list: https://groups.google.com/group/mondo-users
canonical: mondo.owl
browsers:
  - label: Monarch
    title: Monarch Initiative Disease Browser
    url: https://monarchinitiative.org/disease/MONDO:0019609
products:
 - id: mondo.owl
   title: Main OWL edition
   description: Complete ontology, plus inter-ontology equivalence axioms. Uses MONDO IDs.
   format: owl-rdf/xml
   is_canonical: true
 - id: mondo.obo
   title: obo-format edition
   description: As OWL, but omits equivalence axioms. xrefs can be used as proxy for equivalence. Uses Mondo IDs
   format: obo
   derived_from: mondo.owl
 - id: mondo.json
   title: json edition
   description: Equivalent to the OWL edition
   format: obo
   derived_from: mondo.owl
usages:
 - user: https://monarchinitiative.org/
   type: annotation
   description: Mondo is used by the Monarch Initiative for disease annotations.
   examples:
    - url: https://monarchinitiative.org/phenotype/HP:0001300#diseases
   reference: https://academic.oup.com/nar/article/45/D1/D712/2605791
activity_status: active
---

The Mondo Disease Ontology (Mondo) aims to harmonize disease definitions across the world. It is a semi-automatically constructed ontology that merges in multiple disease resources to yield a coherent merged ontology. Original versions of Mondo were constructed entirely automatically and used the IDs of source databases and ontologies. Later, additional manually curated cross-ontology axioms were added, and a native Mondo ID system was used to avoid confusion with source databases.

One feature of Mondo is that it goes beyond loose xrefs. It curated precise 1:1 equivalence axioms connecting to other resources, validated by OWL reasoning. This means it is safe to propagate across these from OMIM, Orphanet, EFO, DOID (soon NCIT).

These precise mappings are available in three ways depending on the format:

 - the .owl edition uses OWL equivalence axioms directly in the ontology. Note this makes it harder to browse in some portals, but this edition may be preferable for computational use. The owl edition also includes axiomatization using CL, Uberon, GO, HP, RO, NCBITaxon.
 - the .obo versions are simpler, lacks inter-ontology axiomatization, and lack equivalence axioms to other databases; instead xrefs are used as the linking mechanism. If the ID is one of Orphanet, OMIM, DOID or EFO then the xref precisely shadows the equivalence axiom.
- the json edition.
  
Trackers

 - https://github.com/monarch-initiative/monarch-disease-ontology/issues - original tracker, primarily for examining kboom output and for feeding back changes to sources
 - https://github.com/monarch-initiative/mondo/issues - new tracker primarily for curating the grouped classes
