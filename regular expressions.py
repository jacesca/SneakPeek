s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

# to match the word Bitcoin at the beginning of the string using the match() method.
result = re.match('Bitcoin', s)
print(result.group()) # Bitcoin

# to match the word Bitcoin at the beginning of the string using the match() method and ignoring the case. 
# This way, no matter if you have bitcoin or Bitcoin, the match is done either way.
result = re.match("Bitcoin", s, re.IGNORECASE)
print(result.group()) # Bitcoin

# To match the words Bitcoin was at the beginning of the string using the match() method. 
# Use the dot (.) belonging to regex syntax in your solution.
result = re.match('B.{6} .{3}', s)
print(result.group()) # Bitcoin was

# to match the year 2009 in the string using the search() method. Use the \d in your solution.
result = re.search(r'(\d{4})\s', s)
print(result.group(1)) # 2009

# to match the year 2017 in the string using the search() method. Use the \d in your solution.
result =re.search(r'(\d{4}),', s)
print(result.group(1)) # 2017

# to match the date Jan 3rd 2009 in the string using the search() method. Use the \d in your solution.
result = re.search(r'(\w{3}\s\d{1}\w{2}\s\d{4})', s)
print(result.group(1)) # Jan 3rd 2009

# to match BTC in the string using the search() method.
result = re.search(r'(BTC)', s)
result = re.search(r"([A-Z]{3})", s)
print(result.group(1)) # BTC

# to match 1 BTC in the string using the search() method.
result = re.search(r'(\d{1}\s\w{3})', s)
print(result.group(1)) # 1 BTC

# to match $20000 in the string using the search() method.
result = re.search(r'(\$\d{5})', s)
print(result.group(1)) # $20000

# to match $300B in the string using the search() method.
result = re.search(r'(\$\d{3}B)', s)
result = re.search(r"(\$\d{3}[A-Z])\.", s)
print(result.group(1)) # $300B

# to match market cap of in the string using the search() method.
result = re.search(r'\s([A-Za-z]{6}\s\w{3}\s.{2})\s', s)
print(result.group(1)) # market cap of

# to match all the years in the string using the findall() method.
result = re.findall(r'\s(\d{4})', s)
print(result) # ['2009', '2017']

# to match all the numbers (3, 2009, 2017 etc.) in the string using the findall() method.
result = re.findall(r'\d+', s)
result = re.findall(r"\d{1,}", s)
print(result) # ['3', '2009', '2017', '1', '20000', '300']

# to match all the three-letter words in the string using the findall() method.
result = re.findall(r'\s(\w{3})\s', s)
print(result) # ['was', 'Jan', 'the', 'the', 'the', 'BTC', 'cap']

# to match all the words starting with an uppercase letter in the string using the findall() method.
result = re.findall(r'\s*([A-Z][A-Za-z]*)\s', s)
result = re.findall(r"([A-Z]{1}.+?)\s", s)
print(result) # ['Bitcoin', 'Jan', 'In', 'BTC']

# to match all the two-letter words starting with the letter o in the string using the findall() method.
result = re.findall(r'\s(o\w*)\s', s)
result = re.findall(r"\s(o.{1})\s", s)
print(result) # ['on', 'of', 'of', 'of']

# to match all the words that have at least 8 characters in the string using the findall() method
result = re.findall(r'\s(\w{8,})\s', s)
result = re.findall(r"\w{8,}", s)
print(result) # ['alternative', 'financial']

# to match all the words starting with a or c and that have at least 3 letters in the string using the findall() method.
result = re.findall(r'\s([a|c]\w{2,})', s)
result = re.findall(r"\s([ac]\w{2,})\s", s)
print(result) # ['alternative', 'current', 'cap']

# to replace all the years in the string with XXXX using the sub() method.




#########################################################################
#########################################################################
#########################################################################
s = "Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"

# to match 184,073,529,068 in the string using the search() method.
result = re.search(r'(\d{3},\d{3},\d{3},\d{3})', s)
result = re.search(r'(\d{3}(,\d{3}){3})', s)
print(result.group(1)) # 184,073,529,068

# to match 10,259.02 in the string using the search() method.
result = re.search(r'(\d{2},\d{3}\.\d{2})', s)
result = re.search(r"\$(\d{1,3},\d{1,3}\.\d{1,3}),", s)
print(result.group(1)) # 10,259.02

# to match 17,942,600 BTC in the string using the search() method.
result = re.search(r'(\d{2}(,\d{3}){2}\s\w{3})', s)
result = re.search(r"\s([0-9]{2},[0-9]{3},[0-9]{3}\s.{3}),", s)
print(result.group(1)) # 17,942,600 BTC

# to match 24h: 0.10% in the string using the search() method.
result = re.search(r'(\d{2}h\:\s\d\.\d{2}\%)', s)
result = re.search(r"\s(.{4}\s\d\.\d\d%)", s)
print(result.group(1)) # 24h: 0.10%

# to match Volume 24h: $15,670,986,269 in the string using the search() method.
result = re.search(r'(.{6}\s.{4}\s\$\d{2}(,\d{3}){3})', s)
result = re.search(r"\.\d\d, (.{1,}:\s\$\d{2,},\d{2,},\d{2,},\d{2,}), ", s)
print(result.group(1)) # Volume 24h: $15,670,986,269

# to match Circulating Supply: 17,942,600 BTC in the string using the search() method.
result = re.search(r'(.{11}\s.{7}\s\d{2}(,\d{3}){2}\s\w{3})', s)
result = re.search(r"(\w+ \w+: \d{2}.+? [A-Z]{3}), ", s)
print(result.group(1)) # Circulating Supply: 17,942,600 BTC

# to match 259.02, V in the string using the search() method.
result = re.search(r'(\d{3}\.\d{2}, \w)', s)
result = re.search(r",([0-9]{3}\.[0-9]{2},\s.)", s)
print(result.group(1)) # 259.02, V





#########################################################################
#########################################################################
#########################################################################
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B. Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"

# to replace all the years in the string with XXXX using the sub() method.
result = re.sub(r'\s\d{4}', ' XXXX', s)
print(result) # Bitcoin was born on Jan 3rd XXXX as an alternative to the failure of the current financial system. In XXXX, the price of 1 BTC reached $20000, with a market cap of over $300B. Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%

# to replace each floating-point number in the string (10,259.02 and 0.10) with a dot (.) using the sub() method.
result = re.sub(r'(\d{1,3}(,\d{3})*\.\d{1,})', '.', s)
print(result) # Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B. Bitcoin, Market Cap: $184,073,529,068, Price: $., Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: .%

# to replace all occurrences of BTC in the string with Bitcoin using the sub() method.
result = re.sub('BTC', 'Bitcoin', s)
result = re.sub(r"[A-Z]{3}", "Bitcoin", s)
print(result) # Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 Bitcoin reached $20000, with a market cap of over $300B. Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 Bitcoin, Change 24h: 0.10%

# to replace all the digits less than or equal to 5 in the string with 8 using the sub() method.
result = re.sub(r'[0-5]', '8', s)
print(result) # Bitcoin was born on Jan 8rd 8889 as an alternative to the failure of the current financial system. In 8887, the price of 8 BTC reached $88888, with a market cap of over $888B. Bitcoin, Market Cap: $888,878,889,868, Price: $88,889.88, Volume 88h: $88,678,986,869, Circulating Supply: 87,988,688 BTC, Change 88h: 8.88%

# to replace all the words starting with an uppercase letter or digits greater than or equal to 6 in the string with W using the sub() method.
result = re.sub(r'([A-Z]\w{1,}|[6-9])', 'W', s)
result = re.sub(r"[A-Z]\w{1,}|[6-9]", "W", s)
print(result) # W was born on W 3rd 200W as an alternative to the failure of the current financial system. W 201W, the price of 1 W reached $20000, with a market cap of over $300B. W, W W: $1W4,0W3,52W,0WW, W: $10,25W.02, W 24h: $15,WW0,WWW,2WW, W W: 1W,W42,W00 W, W 24h: 0.10%

