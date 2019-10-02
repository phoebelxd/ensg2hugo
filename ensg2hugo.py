#!/usr/bin/python
import argparse
import fileinput # This module gives us the ability to read filescd
import re # This imports the regex capability
my_file= "Homo_sapiens.GRCh37.75.gtf" # Assign my_file to whatever was argument 1
gene={}
for each_line_of_text in fileinput.input(my_file):
    if re.match(r'.*\t.*\tgene\t', each_line_of_text):
        gene_id_matches = re.findall('gene_id \"(.*?)\";', each_line_of_text)
        gene_name_matches = re.findall('gene_name \"(.*?)\";',each_line_of_text)
        if gene_id_matches and gene_name_matches:
            gene[gene_id_matches[0]] = gene_name_matches[0]

parser = argparse.ArgumentParser(description='Process CSV formate biodata.')
parser.add_argument('bioname', metavar='FILENAME', type=str, nargs=1,
                    help='an integer for the accumulator')
parser.add_argument('-f', dest='column', type=int, default=1,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
for each_line_of_text in fileinput.input(args.bioname):
    columns = each_line_of_text.split (",")
    if len(columns)>1:
        match = re.search('(\w+)\.*(\w+)', columns[args.column-1])
        if match:
            if  match.group(1) in gene:
                columns[args.column - 1]='"' + gene[match.group(1)] + '"'
            print ",".join (columns),
