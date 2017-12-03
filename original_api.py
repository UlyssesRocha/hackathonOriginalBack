#  sandbox_url = 'https://sandbox.original.com.br/accounts/v1/transaction-history?dateFrom=20120101&dateTo=20160101'
#
import requests, json

#
#  r = requests.get(sandbox_url, headers=headers)
#
#  print(r.text)
"""
enny Doe 222.222.222-22 123456 222222
"""
access_token2 = "Bearer YjYwNzkzMzAtZDdiZC0xMWU3LWJjNTEtMDA1MDU2OWE3MzA1OmV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUowZVhCbElqb2lUMEYxZEdnaUxDSnBZWFFpT2pFMU1USXlOVGsyTURjc0ltVjRjQ0k2TVRVeE1qWTVNVFl3Tnl3aVlYVmtJam9pTldJMFpqZG1PR1lpTENKcGMzTWlPaUphZFhBdWJXVWdSMkYwWlhkaGVTSXNJbk4xWWlJNkltSTJNRGM1TXpNd0xXUTNZbVF0TVRGbE55MWlZelV4TFRBd05UQTFOamxoTnpNd05TSXNJbXAwYVNJNkltUmhZV1JsTmpNd0xXUTNZbVF0TVRGbE55MWhOMk13TFdNeE56WXlaRFl3TlRRME5pSjkuZlBZTVQ4ZEdYMWFxVzF2UWxrTUtLbl94a3VPSk9ERF9rR2lyUXBjd2gydw=="
"""
Rose Doe 444.444.444-44 123456 444444
"""
access_token4 = "Bearer NDMyNDkzYTAtZDdjMS0xMWU3LWJjNTEtMDA1MDU2OWE3MzA1OmV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUowZVhCbElqb2lUMEYxZEdnaUxDSnBZWFFpT2pFMU1USXlOakV4TlRJc0ltVjRjQ0k2TVRVeE1qWTVNekUxTWl3aVlYVmtJam9pTldJMFpqZG1PR1lpTENKcGMzTWlPaUphZFhBdWJXVWdSMkYwWlhkaGVTSXNJbk4xWWlJNklqUXpNalE1TTJFd0xXUTNZekV0TVRGbE55MWlZelV4TFRBd05UQTFOamxoTnpNd05TSXNJbXAwYVNJNklqY3pPV0poTmprd0xXUTNZekV0TVRGbE55MWhOMk13TFdNeE56WXlaRFl3TlRRME5pSjkua0tkQVVOcHltdGZ6eHdwb1RFRnZ1LWs0V2RDWF92aG5ia1F1aU1rRU81aw=="
access_token = access_token4
headers = {
    'Authorization': access_token,
    'developer-key': '28f955c90b3a2940134ff1a970050f569a87facf'
}
url_prefix = 'https://sandbox.original.com.br/accounts/v1'


def make_get_request(path, queries):
    r = requests.get(url_prefix + path + queries, headers=headers)
    data = ""
    #  if r.status_code == requests.codes.ok:
    data = r.text
    return data