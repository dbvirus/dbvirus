from Bio import Entrez
import xml.etree.ElementTree as ET

Entrez.email = "osvaldor@unicamp.br"

def esearch(db, term):
    handle = Entrez.esearch(db=db, term=term, retmax=3)
    records = Entrez.read(handle)
    return records

def efetch(uid):
    handle = Entrez.efetch(db="sra", id=uid, rettype="fq", retmode="text")
    return handle

def extract_info_efetch(xml_string):
    root = ET.fromstring(xml_string)
    return root

records = esearch('sra', "\"Homo sapiens\"[Organism] AND 00000000050[ReadLength] AND (cluster_public[prop] AND \"biomol rna\"[Properties])")
sra = efetch(records['IdList'][0])
#root = extract_info_efetch(sra.read())
print(sra.read())
#print(root)