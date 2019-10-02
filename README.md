# Name: ensg2hugo

A basic python script for TRGN 510 [Basic Foundations in Translational Biomedical Informatics](https://www.bioinform.io/site/) that converts gene id to gene name.

## Prerequisites

[Python 3](https://www.python.org/download/releases/3.0/) required. I personally recommend [PyCharm](https://www.jetbrains.com/pycharm/).



## Installing

First, clone the repo to local machine
``` 
git clone https://github.com/phoebelxd/ensg2hugo.git
``` 
Second, download the file, `Homo_sapiens.GRCh37.75.gtf.gz`, from http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens using `wget` or `curl` 
``` 
curl http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens Homo_sapiens.GRCh37.75.gtf.gz -O
```
Unzip this file with `gunzip`
```
gunzip Homo_sapiens.GRCh37.75.gtf.gz
```

The command `head ~/data/Homo_sapiens.GRCh37.75.gtf` should give the start of the file `(#!genome-build GRCh37.p13)`.


## Usage
```
usage: ensg2hugo.py [-h] [-f COLUMN] FILENAME
```
The unit test for you is here: https://github.com/davcraig75/unit

```
ensg2hugo.py -f2 expression_analysis.tsv >expression_analysis.hugo.tsv
```
will turn this file from

```
"","gene_id","gene_type","logFC","AveExpr"
"14541","ENSG00000248546.3","processed_pseudogene",0.449817926522256,0.0739725408539951
"14546","ENSG00000201050.1","snRNA",0.380944080200912,0.169836608364135
```
into:
```
"",""gene_name","gene_type","logFC","AveExpr"
"14541","ANP32C","processed_pseudogene",0.449817926522256,0.0739725408539951
"14546","RNU6-668P","snRNA",0.380944080200912,0.169836608364135,2.92569531023051
```



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* [David Wesley Craig, PhD](https://keck.usc.edu/faculty-search/david-wesley-craig/)


