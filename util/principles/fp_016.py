#!/usr/bin/env python3

## ## "Maintenance" Automated Check
##
## ### Requirements
## 1. The ontology *should* be regularly updated.
##
## ### Implementation
## A version IRI is retrieved from the ontology, either using OWL API or parsing RDF/XML for large ontologies. This version IRI is checked against a regex pattern to determine if it is in date format. If so, the date is retrieved. If the last version IRI date is older than three years, this is an error. If it is older than two years, this is a warning. If it is older than one year, this will be an info message.

import datetime
import re

import dash_utils
from dash_utils import format_msg

# version IRI pattern
vpat = r'http:\/\/purl\.obolibrary\.org/obo/.*/([0-9]{4}-[0-9]{2}-[0-9]{2})/.*'

# violation message
old_version_msg = 'last version ({0}) is over {1} year(s) old'


def is_maintained(ontology):
    """Check fp 16 - maintenance.

    This method uses OWL API to retrieve the version IRI.

    Args:
        ontology (OWLOntology): ontology object

    Return:
        PASS, INFO, WARN, or ERROR with optional help message
    """
    if ontology is None:
        return format_msg('INFO', ['unable to load ontology'])

    version_iri = ontology.getOntologyID().getVersionIRI().orNull()

    if version_iri:
        return check_version_iri(version_iri.toString())

    # no version IRI (is Null)
    return format_msg('INFO', ['missing version IRI to check date'])


def big_is_maintained(file):
    """Check fp 16 - maintenance - on large ontologies.

    This is suitible for large ontologies as it reads the file line by line,
    instead of loading an OWLOntology object. This method looks for the
    owl:versionIRI property in the header.

    Args:
        file (str): path to ontology file

    Return:
        PASS, INFO, WARN, or ERROR with optional help message
    """
    # may return empty string if version IRI is missing
    # or None if ontology cannot be parsed
    version_iri = dash_utils.get_version_iri(file)

    if version_iri and version_iri != '':
        return check_version_iri(version_iri)
    elif version_iri == '':
        # no version IRI to check
        return format_msg('INFO', ['missing version IRI to check date'])
    else:
        # ontology was in bad format
        return format_msg('INFO', ['unable to parse ontology'])


def check_version_iri(version_iri):
    """Check if the version IRI is in date format then check when the version
    IRI was last updated.

    Args:
        version_iri (str): version IRI from ontology header

    Return:
        PASS, INFO, WARN, or ERROR with optional help message
    """
    # serach for date in version IRI using regex pattern
    search = re.search(vpat, version_iri)
    if search:
        date = search.group(1)
        splits = date.split('-')
        version_date = datetime.datetime(
            int(splits[0]), int(splits[1]), int(splits[2]))

        # check 3 years (error)
        three_years_ago = datetime.datetime.now() \
            - datetime.timedelta(days=3*365)
        if version_date < three_years_ago:
            return format_msg(
                'ERROR', [old_version_msg.format(date, 'three')])

        # check 2 years (warn)
        two_years_ago = datetime.datetime.now() \
            - datetime.timedelta(days=2*365)
        if version_date < two_years_ago:
            return format_msg(
                'WARN', [old_version_msg.format(date, 'two')])

        # check 1 year (info)
        one_year_ago = datetime.datetime.now() - datetime.timedelta(days=365)
        if version_date < one_year_ago:
            return format_msg(
                'INFO', [old_version_msg.format(date, 'one')])

        # has valid version IRI and it has been updated within the past year
        return 'PASS'
    else:
        # version IRI is not in the expected date format
        return format_msg(
            'INFO', ['version IRI does not have date information'])