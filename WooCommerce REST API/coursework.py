from woocommerce import API

wcapi = API(
    url = "https://cool-bardeen.77-68-12-181.plesk.page",
    consumer_key="ck_6a5afa13b217c5797a5931c71f7ffebc483f863a",
    consumer_secret="cs_a6f65d69e89b1ce8b33cf84f71bebea1fc9a4ef6",
    version="wc/v3"
)


r = wcapi.get("orders")
print(wcapi.get("orders?_status=completed", params={'first_name': '', 'last_name': '', 'email':'', 'name':'', 'price':'', 'customer_note':''}).json())        

# data = {
#     "note":"",
#     "billing": {
#         "first_name": "",
#          "last_name": "",
#          "email": "",
#     },
#      "line_items": {
#          "name":"",
#          "quantity":"",
#          "total":"",
#    }
# }

# print(wcapi.put("orders", data).json())