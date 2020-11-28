<p><h1>GENERAL EXPLANATIONS</h1></p>
<p><b>--This project is written for school assignment.--</b></p> 
<i><h4>This readme file is converted from an pdf file. Feel free to contact if you don't understand any part of code. Have a nice day.</h4></i>
<p>In this project, we are crawling websites with python to get informations from web. For this process we are using one of the most common libraries called &lsquo; BeautifulSoup&rsquo; with requests library. This library helps us to parse html and find tags like id or class names.</p>
<p>There is also a limitation in our application. Because of request library, functions doesn&rsquo;t responds to turkish characters. So searching a strings that have any of &lsquo;&ccedil;,ğ,ı,&ouml;,ş,&uuml;,&rsquo; characters causes crash. Beside our efforts, this exception is not likely to handle since its working in library.</p>
<p>Before running code we need to install required libraries. After this process we can run our code. Here is code to install required libraries:</p>
<ol>
<li>pip&nbsp;install&nbsp;requests&nbsp;&nbsp;</li>
<li>pip&nbsp;install&nbsp;beautifulsoup4&nbsp;&nbsp;</li>
</ol>
<p><h1>CODE EXPLANATION</h1></p>
<p><strong><h2>Process list</h2></strong></p>
<ol>
<li><strong>def</strong>main():&nbsp;&nbsp;</li>
<li><strong>print</strong>("\n\nWelcome&nbsp;to&nbsp;webcrawler.&nbsp;Here&nbsp;is&nbsp;a&nbsp;menu&nbsp;for&nbsp;options:\nPlease&nbsp;dont&nbsp;use&nbsp;turkish&nbsp;characters&nbsp;in&nbsp;anyprocess[&ccedil;,ğ,ı,&ouml;,ş,&uuml;]\n"&nbsp;&nbsp;</li>
<li>"0-Exit\n1-wikipedia\n2-weather\n3-Search&nbsp;cheapest&nbsp;product\nPlease&nbsp;input&nbsp;index&nbsp;of&nbsp;process&nbsp;to&nbsp;begin")&nbsp;&nbsp;</li>
<li>process&nbsp;=&nbsp;input("")&nbsp;&nbsp;</li>
<li><strong>if</strong>&nbsp;process=='0':&nbsp;&nbsp;</li>
<li>exit()&nbsp;&nbsp;</li>
<li><strong>elif</strong>&nbsp;process=='1':&nbsp;&nbsp;</li>
<li>wikipedia()&nbsp;&nbsp;</li>
<li><strong>elif</strong>&nbsp;process&nbsp;==&nbsp;'2':&nbsp;&nbsp;</li>
<li>weather()&nbsp;&nbsp;</li>
<li><strong>elif</strong>process&nbsp;==&nbsp;'3':&nbsp;&nbsp;</li>
<li>searchProduct()&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>print</strong>('Unexpected input. Please try again.\n')&nbsp;&nbsp;</li>
<li>main()&nbsp;&nbsp;</li>
</ol>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Code prints a list like a menu. Input function waits for a input else gives error and starts same function again. Here is explanation of menu:</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0 - exit , stops code</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1 - wikipedia, searches on english wikipedia</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2 &ndash; weather, uses bing search build-in weather function to show weather</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3 &ndash; product search, uses Cimri.com to find searched product for cheapest price</p>
<p><strong><h2>Bracket Remover</h2></strong></p>
<ol>
<li><strong>def</strong>bracket_remover(text):&nbsp;&nbsp;</li>
<li>pattern&nbsp;=&nbsp;r'\[.*?\]'&nbsp;&nbsp;</li>
<li>paragraph&nbsp;=&nbsp;re.sub(pattern,&nbsp;'',&nbsp;text)&nbsp;&nbsp;</li>
<li><strong>print</strong>(paragraph)&nbsp;&nbsp;</li>
</ol>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This code helps wikipedia process to show outputs more clear to read. Function takes a text as an input. Removes brackets ( [ ] ) and information inside brackets. Returns cleared text to user. &nbsp; There is a example in case of you search&nbsp; &lsquo;Elon Musk &lsquo; :</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; CEO and product architect of Tesla, Inc.;[10][11] founder of The Boring Company;[12]&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; CEO and product architect of Tesla, Inc.; founder of The Boring Company;</p>
<p><strong><h2>Wikipedia Search</h2></strong></p>
<ol>
<li><strong>def</strong>wikipedia():&nbsp;&nbsp;</li>
<li>search&nbsp;=&nbsp;input("Please&nbsp;input&nbsp;your&nbsp;wikipedia&nbsp;search&nbsp;string\n")&nbsp;&nbsp;</li>
<li>url&nbsp;=&nbsp;"https://en.wikipedia.org/wiki/"&nbsp;+&nbsp;str(search)&nbsp;&nbsp;</li>
<li>url&nbsp;=&nbsp;url.replace('&nbsp;','%20')&nbsp;&nbsp;</li>
<li><strong>if</strong>&nbsp;(requests.get(url)).status_code&nbsp;==&nbsp;200:&nbsp;&nbsp;</li>
<li>source&nbsp;=&nbsp;urllib.request.urlopen(url).read()&nbsp;&nbsp;</li>
<li>soup&nbsp;=&nbsp;bs.BeautifulSoup(source,'html.parser')&nbsp;&nbsp;</li>
<li><strong>print</strong>((soup.find(id="firstHeading")).text)&nbsp;&nbsp;</li>
<li>tags&nbsp;=&nbsp;soup.find_all('p',attrs={'class':None})&nbsp;&nbsp;</li>
<li><strong>if</strong>len(tags)&gt;=2:&nbsp;&nbsp;</li>
<li><strong>for</strong>a&nbsp;<strong>in</strong>&nbsp;range(2):&nbsp;&nbsp;</li>
<li><strong>if</strong>tags[a]!=None:&nbsp;&nbsp;</li>
<li>paragraph&nbsp;=&nbsp;tags[a].text&nbsp;&nbsp;</li>
<li>bracket_remover(paragraph)&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>continue</strong></li>
<li><strong>elif</strong>len(tags)==1:&nbsp;&nbsp;</li>
<li>paragraph&nbsp;=&nbsp;tags[0].text&nbsp;&nbsp;</li>
<li>bracket_remover(paragraph)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>print</strong>("Cannot&nbsp;find&nbsp;results&nbsp;in&nbsp;wikipedia.")&nbsp;&nbsp;</li>
<li>main()</li>
</ol>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In this function we are searching on wikipedia. We are making a request on url so all spaces will be replaced with &lsquo;%20&rsquo; which is character set of space for HTML5. After that we are crawling website with called url like:</p>
<p>https://en.wikipedia.org/wiki/Elon%20Musk</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; We dont want all website to show up in our code. So we are just searching tags with &lt;p&gt; which refers to paragraphs in HTML5. If there is more than two &lt;p&gt; we just get first two paragraphs. If there is only one we are getting only one paragraph. If page response code is not equal to &lsquo;200&rsquo; which refers to unsuccesfull connection, we are printing &lsquo;Cannot find results in wikipedia&rsquo;.</p>
<p><strong><h2> Weather Search With Bing</h2></strong></p>
<ol>
<li><strong>def</strong>weather():&nbsp;&nbsp;</li>
<li>location&nbsp;=&nbsp;input("Please&nbsp;input&nbsp;your&nbsp;weather&nbsp;search&nbsp;location\nInput&nbsp;empty&nbsp;for&nbsp;automatic&nbsp;location[may&nbsp;be&nbsp;wrong!]\n")&nbsp;&nbsp;</li>
<li>url=&nbsp;"https://www.bing.com/search?q="+str(location)+"%20hava%20durumu"&nbsp;&nbsp;</li>
<li>url&nbsp;=&nbsp;url.replace('&nbsp;','%20')&nbsp;&nbsp;</li>
<li>source&nbsp;=&nbsp;urllib.request.urlopen(url).read()&nbsp;&nbsp;</li>
<li>soup&nbsp;=&nbsp;bs.BeautifulSoup(source,'html.parser')&nbsp;&nbsp;&nbsp;</li>
<li><strong>if</strong>find('div',attrs={'class':'wtr_locTitle&nbsp;wtr_nowrap&nbsp;wtr_ellipses'})&nbsp;!=&nbsp;None:&nbsp;&nbsp;</li>
<li><strong>print</strong>(soup.find('div',attrs={'class':'wtr_locTitle&nbsp;wtr_nowrap&nbsp;wtr_ellipses'}).text&nbsp;+"&nbsp;forecast for right now "+&nbsp;soup.find('div',attrs={'class':'wtr_caption'}).text&nbsp;+&nbsp;"&nbsp;"&nbsp;+&nbsp;soup.find('div',attrs={'class':'wtr_currTemp&nbsp;b_focusTextLarge'}).text&nbsp;+&nbsp;"&nbsp;degree")&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>print</strong>("Cant find location.")&nbsp;&nbsp;</li>
<li>main()&nbsp;&nbsp;</li>
</ol>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In this part we are crawling in bing search engine for weather forecast. We are waiting for user to input a location. User can either input a location or leave blank to get forecast on current location. To handle URL errors we are using same tecnique to replace spaces in text to &lsquo;%20&rsquo;.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; If bing engine finds any value that have class names like in line 7 ('wtr_locTitle wtr_nowrap wtr_ellipses'),&nbsp; we understands there is a succesfull call to bing. Then our crawler search for weather forecast and prints results.</p>
<p><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Cheapest Product Search With Cimri.com</strong></p>
<ol>
<li><strong>def</strong>searchProduct():&nbsp;&nbsp;</li>
<li>productName&nbsp;=&nbsp;input("Please&nbsp;enter&nbsp;your&nbsp;word&nbsp;to&nbsp;search.&nbsp;We&nbsp;will&nbsp;find&nbsp;cheapest&nbsp;in&nbsp;web&nbsp;(&nbsp;dont&nbsp;use&nbsp;turkish&nbsp;characters[&ccedil;,ğ,ı,&ouml;,ş,&uuml;]:\n")&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>
<li>url=&nbsp;"https://www.cimri.com/arama?q="+str(productName)&nbsp;&nbsp;</li>
<li>url&nbsp;=&nbsp;url.replace('&nbsp;','%20')&nbsp;&nbsp;</li>
<li>source&nbsp;=&nbsp;urllib.request.urlopen(url).read()&nbsp;&nbsp;</li>
<li>soup&nbsp;=&nbsp;bs.BeautifulSoup(source,'html.parser')&nbsp;&nbsp;&nbsp;</li>
<li>product&nbsp;=soup.find_all('h3',attrs={'class':'product-title'})&nbsp;&nbsp;</li>
<li><strong>if</strong>&nbsp;len(product)!=0:&nbsp;&nbsp;</li>
<li>productprice=soup.find_all('a',attrs={'s14oa9nh-0&nbsp;fFCyge'})&nbsp;&nbsp;</li>
<li><strong>print</strong>(product[0].text+"\n")&nbsp;&nbsp;</li>
<li><strong>print</strong>(productprice[0].text)&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>print</strong>("Cant&nbsp;find&nbsp;product")&nbsp;&nbsp;</li>
<li>main()&nbsp;&nbsp;</li>
</ol>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Cimri.com is one of a good example for webcrawler itself. Website searchs a product on different sites and compares them. Shows prices on different places for same item. We are using their website to make almost something similar. Of course we are replacing spaces with &lsquo;%20&rsquo;.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; After user inputs a text like &lsquo;kolonya&rsquo; cimri.com searches for cheapest products. Actually website shows many result for query &lsquo;kolonya&rsquo; but we are interested in for first one in list. We are crawling full product name and price that includes seller informations. If there is no product, code print &lsquo;Cant find product&rsquo;.</p>
