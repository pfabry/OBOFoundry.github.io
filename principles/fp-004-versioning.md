---
layout: principle
id: fp-004-versioning
title: Versioning (principle 4)
---

NOTE
-------

The content of this page is scheduled to be reviewed. Improved wording will be posted as it becomes available.

Summary
-------

The ontology provider has documented procedures for versioning the ontology, and different versions of ontology are marked, stored, and officially released.

Purpose
-------------

OBO projects share their ontologies using files in OWL or OBO format (see OBO Principle 2). Ontologies are expected to change over time as they are developed and refined (see OBO Principle 16 on maintenance). This will lead to a series of different files. Consumers of ontologies must be able to specify exactly which ontology files they used to encode their data or build their applications, and be able to retrieve unaltered copies of those files in perpetuity. Note that this applies only to those versions which have been officially released.

Recommendation
-------

Each official release MUST have a unique version identifier. Version identifiers for the ontology artifacts themselves may be of the form “YYYY-MM-DD” (that is, a date), or use a numbering system (such as semantic versioning, i.e, of the form "NN.n"), but in any case each MUST associate with a <i>distinct</i> official release. The date versioning system is preferred, as it meshes with the requirement that version IRIs be specified using dated PURLs (see below).

All OBO projects MUST also have PURLs that resolve to specific official releases of their ontology, in perpetuity. If the files are moved, the PURL MUST be updated to resolve to the new location. Consumers can then use the version IRI to uniquely identify which official release of the ontology they used, and to retrieve unaltered copies of the file(s).

Note that the content of official release files MUST NOT be changed. For example, if a bug is found in some official released file for some ontology, the bug MUST NOT be fixed by changing the file(s) for that official release. Instead the bug fixes should be included in a new official release, with new files, and consumers can switch to the new release.

Implementation
-------

See examples (below) for guidelines on how to specify the version within the ontology itself. If terms are imported from an external ontology, the “IAO:imported from” annotation (see [Principle 1](http://obofoundry.org/principles/fp-001-open.html)) may specify a dated version of the ontology from which they are imported.

Regardless of the versioning system used for the ontology artifact, the version IRI SHOULD use an ISO-8601 dated PURL. In cases where there are multiple releases on the same day, the PURL points to the newest, and the previous release stays in the same folder or a subfolder, named in such a way as to distinguish the releases. Specifications for version IRIs are fully described in the OBO Foundry [ID policy](http://obofoundry.org/id-policy) document. In short: 

For a given version of an ontology, the ontology should be accessible at the following URL, where 'idspace' is replaced by the IDSPACE in lower case:

    OWL: http://purl.obolibrary.org/obo/idspace/YYYY-MM-DD/idspace.owl
    OBO: http://purl.obolibrary.org/obo/idspace/YYYY-MM-DD/idspace.obo

For example, for the version of OBI released 2009-11-06, the OWL document is accessible at http://purl.obolibrary.org/obo/obi/2009-11-06/obi.owl.

An accepted alternative to the above scheme is to include /releases/ in the PURL, as follows:

    OWL: http://purl.obolibrary.org/obo/idspace/releases/YYYY-MM-DD/idspace.owl
    OBO: http://purl.obolibrary.org/obo/idspace/releases/YYYY-MM-DD/idspace.obo

Examples
--------

For an OBO format ontology use the metadata tag:

    data-version: 2015-03-31
    data-version: 44.0

For an OWL format ontology, owl:versionInfo identifies the version and versionIRI identifies the resource:

    <owl:versionInfo rdf:datatype="http://www.w3.org/2001/XMLSchema#string">2014-12-03</owl:versionInfo>
    <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/obi/2014-12-03/obi.owl"/>


Counter-Examples
----------------

<Category:Principles> <Category:Accepted>
