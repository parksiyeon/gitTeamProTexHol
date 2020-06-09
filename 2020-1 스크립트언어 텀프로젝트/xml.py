import urllib
import http.client

conn = http.client.HTTPConnection("apis.data.go.kr")
conn.request("GET", "/B553748/CertPrdListService/getCertPrdListService?ServiceKey=l7jUiHqsMAknou8LLaxhWULlaNvpEqIOEq8hVWpPCxVF5TFkzWM6xWibOTXujSOTcjcUnu10%2FnMTJT4EG5lzhw%3D%3D&prdlstReportNo=201806190059")
req = conn.getresponse()
print(req.status, req.reason)
print(req.read().decode('utf-8'))

