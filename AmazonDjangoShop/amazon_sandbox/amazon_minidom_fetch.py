import amazonproduct
from xml.dom.minidom import parse
from settings import AWS_KEY, SECRET_KEY, ASSOCIATE_TAG

def minidom_response_parser(fp):
    root = parse(fp)
    # parse errors
    for error in root.getElementsByTagName('Error'):
        code = error.getElementsByTagName('Code')[0].firstChild.nodeValue
        msg = error.getElementsByTagName('Message')[0].firstChild.nodeValue
        raise amazonproduct.AWSError(code, msg)
    return root

api = amazonproduct.API(AWS_KEY, SECRET_KEY, 'us', ASSOCIATE_TAG, processor=minidom_response_parser)
root = api.item_lookup('0718155157')
print root.toprettyxml()
