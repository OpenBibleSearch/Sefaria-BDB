import codecs
import xml.etree.ElementTree as ET
from bibleworks.converter import convert_web_encoded_bwhebb_string as bw_to_uni


#Unusual things to handle:
# <STRONGS>133</STRONGS>
# <xbr t="Ex 26:19">Ex 26:19</xbr>, <xbr t="Ex 26:19">26:19</xbr>, <xbr t="Ex 26:19">26:19</xbr> + 52 t. in <xbr t="Ex 26">Ex 26</xbr>, <xbr t="Ex 27">27</xbr>, <xbr t="Ex 35">35</xbr>
#  <span class="Bwhebb">&#97;&#116;&#39;&#109;&#39;&#100;&#46;&#97;&#59;</span>
# <span class="greek">)Adwra</span>
def _html_walker(elem):
    tag = elem.tag
    if not isinstance(tag, basestring) and tag is not None:
        return

    out = u""

    if tag == "STRONGS":
        return u"<span class='strongs-number'>{}</span>".format(elem.text)
    elif tag == "xbr":
        return u"<span class='ref' data-ref={}>{}</span>".format(elem.get("t"), elem.text)
    elif tag == "span":
        cls = elem.get("class")
        if cls == "Bwhebb":
            return u"<span class='hebrew'>{}</span>".format(bw_to_uni(elem.text))
        if cls == "greek":
            return u"<span class='greek'>{}</span>".format(elem.text)  # todo: method to convert Greek


    # otherwise - normal stuff

    if tag:
        out += u"<{}>".format(tag)
    if elem.text:
        out += elem.text
    for sub in elem:
        out += _html_walker(sub)
    if tag:
        out += u"</{}>".format(tag)
    if elem.tail:
        out += elem.tail
    return out


tree = ET.parse('../data/raw.html')
root = tree.getroot()

output = u"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="utf-8"/>
            <link rel="stylesheet" href="jastrow.css">
            </head>
        """
output += _html_walker(root.find("body"))
output += u"</html>"

with codecs.open('../data/legal_unicode.html', "w", "utf-8") as o:
    o.write(output)
