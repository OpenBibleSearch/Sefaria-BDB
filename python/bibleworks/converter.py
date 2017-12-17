import re
from HTMLParser import HTMLParser

h = HTMLParser()

bwhebb_map = { #org glyph: unicode
    unichr(0x0021): u"\u05df",
    unichr(0x0022): u"\u05b8",
    unichr(0x0023): u"\u05e5",
    unichr(0x0024): u"\u05da",
    unichr(0x0025): u"\u05da\u05b0",
    unichr(0x0026): u"\u05da\u05bc",
    unichr(0x0027): u"\u05b8",
    unichr(0x0028): u"\u05bd",
    unichr(0x0029): u"\u05bd",
    unichr(0x002A): u"\u05bd",
    unichr(0x002B): u"\u0591",
    unichr(0x002C): u"\u05b6",
    unichr(0x002D): u"\u05be",
    unichr(0x002E): u"\u0fb0",
    unichr(0x002F): u"\u05b1",
    unichr(0x003A): u"\u05b7",
    unichr(0x003B): u"\u05b7",
    unichr(0x003C): u"\u05b6",
    unichr(0x003D): u"\u0591",
    unichr(0x003E): u"\u05b0", # Changed from MAQAF 05be to SHEVA
    unichr(0x003F): u"\u05b1",
    unichr(0x0040): u"\u05e3",
    unichr(0x0041): u"\u05d5\u05ba",
    unichr(0x0042): u"\u05d1\u05bc",
    unichr(0x0043): u"\u05e6\u05bc",
    unichr(0x0044): u"\u05d3\u05bc",
    unichr(0x0045): u"\u05b5",
    unichr(0x0046): u"\u05e9\u05c2\u05bc",
    unichr(0x0047): u"\u05d2\u05bc",
    unichr(0x0048): u"\u05d4\u05bc",
    unichr(0x0049): u"\u05b4",
    unichr(0x004A): u"\u05d8\u05bc",
    unichr(0x004B): u"\u05d8\u05bc",
    unichr(0x004C): u"\u05dc\u05bc",
    unichr(0x004D): u"\u05dc\u05dc\u05bc",
    unichr(0x004E): u"\u05e0\u05bc",
    unichr(0x004F): u"\u05b9",
    unichr(0x0050): u"\u05e4\u05bc",
    unichr(0x0051): u"\u05e7\u05bc",
    unichr(0x0052): u"\u05e8\u05bc",
    unichr(0x0053): u"\u05e1\u05bc",
    unichr(0x0054): u"\u05ea\u05bc",
    unichr(0x0055): u"\u05bb",
    unichr(0x0056): u"\u05e9\u05c1\u05bc",
    unichr(0x0057): u"\u05d5\u05bc",
    unichr(0x0058): u"\u05e9",
    unichr(0x0059): u"\u05d9\u05bc",
    unichr(0x005A): u"\u05d6\u05bc",
    unichr(0x005B): u"\u05e2",
    unichr(0x005C): u"\u05b3",
    unichr(0x005D): u"\u05b2",
    unichr(0x005E): u"\u05da\u05b8",
    unichr(0x005F): u"\u0591",
    unichr(0x0060): u"\u05c3",
    unichr(0x0061): u"\u05d0",
    unichr(0x0062): u"\u05d1",
    unichr(0x0063): u"\u05e6",
    unichr(0x0064): u"\u05d3",
    unichr(0x0065): u"\u05b5",
    unichr(0x0066): u"\u05e9\u05c2",
    unichr(0x0067): u"\u05d2",
    unichr(0x0068): u"\u05d4",
    unichr(0x0069): u"\u05b4",
    unichr(0x006A): u"\u05d8",
    unichr(0x006B): u"\u05d8",
    unichr(0x006C): u"\u05dc",
    unichr(0x006D): u"\u05dc",
    unichr(0x006E): u"\u05e0",
    unichr(0x006F): u"\u05b9",
    unichr(0x0070): u"\u05e4",
    unichr(0x0071): u"\u05e7",
    unichr(0x0072): u"\u05e8",
    unichr(0x0073): u"\u05e1",
    unichr(0x0074): u"\u05ea",
    unichr(0x0075): u"\u05bb",
    unichr(0x0076): u"\u05e9\u05c1",
    unichr(0x0077): u"\u05d5",
    unichr(0x0078): u"\u05d7",
    unichr(0x0079): u"\u05d9",
    unichr(0x007A): u"\u05d6",
    unichr(0x007B): u"\u05b9",
    unichr(0x007C): u"\u05b3",
    unichr(0x007D): u"\u05b2",
    unichr(0x007E): u"\u05dd",
    unichr(0x00A1): u"\u059f",
    unichr(0x00A2): u"\u05a6",
    unichr(0x00A5): u"\u05bd",
    unichr(0x00A6): u"\u0593",
    unichr(0x00A7): u"\u0595",
    unichr(0x00A8): u"\u0595",
    unichr(0x00A9): u"\u0597",
    unichr(0x00AA): u"\u0597",
    unichr(0x00AB): u"\u0599", #not sure on this
    unichr(0x00AC): u"\u0599", #not sure on this
    unichr(0x00AD): u"\u05e3\u05bc",
    unichr(0x00AE): "",
    unichr(0x00AF): "",
    unichr(0x00B0): u"\u059b",
    unichr(0x00B1): u"\u059b",
    unichr(0x00B2): u"\u059b",
    unichr(0x00B3): u"\ua5a1", #not sure on this
    unichr(0x00DB): u"\u05a4",
    unichr(0x00DC): u"\u05a4",
    unichr(0x00DD): u"\u05a4",
    unichr(0x00DE): u"\u0596",
    unichr(0x00DF): u"\u0596",
    unichr(0x00E0): u"\u0596",
    unichr(0x00E1): u"\u05a2", #not sure on this
    unichr(0x00E2): u"\u0596",
    unichr(0x00E3): u"\u05bf",
    unichr(0x00E4): u"\u05a3",
    unichr(0x00E5): u"\u05a3",
    unichr(0x00E6): u"\u05a3",
    unichr(0x00E7): u"\u05a2", #not sure on this
    unichr(0x00E8): u"\u0592",
    unichr(0x00E9): u"\u0599",
    unichr(0x00EA): u"\u0594",
    unichr(0x00EB): u"\u0594",
    unichr(0x00EC): u"\u05ac",
    unichr(0x00ED): u"\u05ac",
    unichr(0x00EE): u"\u05a5",
    unichr(0x00EF): u"\u05a5",
    unichr(0x00F0): u"\u05a5",
    unichr(0x00F1): u"\u05ab",
    unichr(0x00F2): u"\u05ab",
    unichr(0x00F3): "",
    unichr(0x00F4): "",
    unichr(0x00F5): "",
    unichr(0x00F6): u"\u05a2", #not sure on this
    unichr(0x00F7): u"\u059c",
    unichr(0x00F8): u"\u059c",
    unichr(0x00F9): u"\u059e",
    unichr(0x00FA): u"\u059e",
    unichr(0x00FB): u"\u05a0",
    unichr(0x00FC): u"\u05a0",
    unichr(0x00FD): u"\u05a6",
    unichr(0x00FE): u"\u05bc",
    unichr(0x0160): "",
    unichr(0x0161): u"\u05af",
    unichr(0x0178): u"\u05c0",
    unichr(0x017E): "",
    unichr(0x02C6): u"\u059b",
    unichr(0x02DC): "",
    unichr(0x2013): u"\u05a6",
    unichr(0x2014): u"\u05a2", #not sure on this
    unichr(0x2018): u"\u0599",
    unichr(0x2019): u"\u0599",
    unichr(0x201A): u"\u05d0\u05bc",
    unichr(0x201C): u"\u0599",
    unichr(0x201D): u"\u05a9",
    unichr(0x201E): u"\u05bc",
    unichr(0x2020): u"\u05bd",
    unichr(0x2021): u"\u05a1", #not sure on this
    unichr(0x2022): u"\u05a9",
    unichr(0x2026): u"\u059a",
    unichr(0x2030): u"\u05a2", #not sure on this
    unichr(0x2039): u"\u05af",
    unichr(0x203A): u"\u05af",
    unichr(0x20AC): u"\u0597",
    unichr(0x2122): ""
}


def convert_bwhebb_char(orig_char):
    if isinstance(orig_char, str):  # needs to be unicode
        orig_char = unicode(orig_char, 'utf-8')
    return bwhebb_map.get(orig_char, orig_char)


def convert_bwhebb_string(orig_str):
    return re.sub(ur".", lambda match: convert_bwhebb_char(match.group()), orig_str)


def convert_web_encoded_bwhebb_string(web_encoded_str):
    decoded_string = h.unescape(web_encoded_str)
    backwards_unicode = convert_bwhebb_string(decoded_string)

    # bhwebb is encoded LTR, so the last character in the string is first.
    # BUT the vowels are written *after* the character, so it's not fully backwards
    # So we convert from "LTR top to bottom" -> "RTL top to bottom"
    newstr = "".join(re.findall(ur"[\u05d0-\u05ea][^\u05d0-\u05ea]*", backwards_unicode)[::-1])
    assert len(newstr) == len(backwards_unicode), u"{} converted to {} then  {}".format(decoded_string, backwards_unicode, newstr)
    return newstr

