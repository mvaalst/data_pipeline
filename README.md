# Building data pipelines uploading raw json files in BigQuery tables

This repo has the purpose to upload raw json files, before unnesting them, into BigQuery tables.

The Github Actions workflow consists of several steps and is triggered when the main branch is changed or every week to keep the data fresh.
First we checkout the latest version of the code in the repository, before logging into Google cloud and setting up Python and installing the dependencies.

For a clear overview, the Github actions workflow currently consists of four different steps to upload the four different json files into BigQuery tables.
- Upload 1 = venues
- Upload 2 = groups
- Upload 3 = events (needed to be unnested first)
- Upload 4 = users (needed to be unnested first)

To keep the upload as clean as possible, there are no transformations applied yet. This will be done in the second repository where we build a small dbt project to perform these steps.

