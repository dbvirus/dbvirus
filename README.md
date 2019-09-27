# DB Virus

[![Maintainability](https://api.codeclimate.com/v1/badges/35e1406de7bd3e0a656b/maintainability)](https://codeclimate.com/github/dbvirus/dbvirus/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/35e1406de7bd3e0a656b/test_coverage)](https://codeclimate.com/github/dbvirus/dbvirus/test_coverage)

Pipeline for transcriptomic data analysis with the goal of identifying novel virus sequences in publicly available data.

## Architecture

The pipeline is comprised of three main steps:

1. Searching [SRA](https://www.ncbi.nlm.nih.gov/sra) for a given query and downloading the results metadata
2. Downloading the RNA sequences found by step 1
3. Analyzing the sequences acquired by step 2

From a system design point of view, it makes sense to implement each step as different
module that shares a mutual understanding. The first step promises the second one that it
will store the data in a given way and step two promises step three that it will download
and store the RNA sequences in another given way. In Computer Science parlance, this
structure is usually called a 'micro services oriented architecture', or simply
'microsservices'. This is in direct oposition to writing a monolith, a single – and
probably quite big – code that handles all the tasks.

Each step will be implemented as separate Python code.
