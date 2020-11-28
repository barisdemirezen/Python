<p><h1>GENERAL EXPLANATIONS</h1></p>
<p><b>--This project is written for school assignment.--</b></p> 
<i><h4>This readme file is converted from an pdf file. Feel free to contact if you don't understand any part of code. Have a nice day.</h4></i>
<p>In this project, we selected a topic which is really getting in our lives recently. We are simulating one of the A.I supported customer services. Our application searches for pre-defined keywords in sentences. So basically if our customer writes a sentence which has &lsquo;&ccedil;ek&rsquo; in it, application forwards to &ldquo;withdrawing&rdquo; function. Here is a table below which shows keywords for functions. We have also defined english keyboard versions for keywords like &ldquo;yatır&rdquo; and &ldquo;yatir&rdquo;.</p>
<table width="100%">
<tbody>
<tr>
<td width="24%">
<p>&nbsp;</p>
</td>
<td colspan="6" width="75%">
<p><strong>KEYWORDS</strong></p>
</td>
</tr>
<tr>
<td width="24%">
<p><strong>Para &Ccedil;ekme</strong></p>
</td>
<td width="14%">
<p><strong>&ccedil;ek</strong></p>
</td>
<td width="13%">
<p><strong>cek</strong></p>
</td>
<td width="10%">&nbsp;</td>
<td width="16%">&nbsp;</td>
<td width="11%">
<p><strong>&nbsp;</strong></p>
</td>
<td width="9%">
<p><strong>&nbsp;</strong></p>
</td>
</tr>
<tr>
<td width="24%">
<p><strong>Para Yatırma</strong></p>
</td>
<td width="14%">
<p><strong>yatır</strong></p>
</td>
<td width="13%">
<p><strong>yatir</strong></p>
</td>
<td width="10%">
<p><strong>&nbsp;</strong></p>
</td>
<td width="16%">
<p><strong>&nbsp;</strong></p>
</td>
<td width="11%">
<p><strong>&nbsp;</strong></p>
</td>
<td width="9%">
<p><strong>&nbsp;</strong></p>
</td>
</tr>
<tr>
<td width="24%">
<p><strong>Para G&ouml;nderme</strong></p>
</td>
<td width="14%">
<p><strong>g&ouml;nder</strong></p>
</td>
<td width="13%">
<p><strong>gonder</strong></p>
</td>
<td width="10%">
<p><strong>havale</strong></p>
</td>
<td width="16%">
<p><strong>eft</strong></p>
</td>
<td width="11%">
<p><strong>transfer&nbsp;</strong></p>
</td>
<td width="9%">
<p><strong>&nbsp;</strong></p>
</td>
</tr>
<tr>
<td width="24%">
<p><strong>Fatura &Ouml;deme</strong></p>
</td>
<td width="14%">
<p><strong>fatura</strong></p>
</td>
<td width="13%">
<p><strong>&ouml;de</strong></p>
</td>
<td width="10%">
<p><strong>ode</strong></p>
</td>
<td width="16%">
<p><strong>&nbsp;</strong></p>
</td>
<td width="11%">
<p><strong>&nbsp;</strong></p>
</td>
<td width="9%">
<p><strong>&nbsp;</strong></p>
</td>
</tr>
<tr>
<td width="24%">
<p><strong>Hesap Değiştirme</strong></p>
</td>
<td width="14%">
<p><strong>hesap</strong></p>
</td>
<td width="13%">
<p><strong>değiş</strong></p>
</td>
<td width="10%">
<p><strong>degis</strong></p>
</td>
<td width="16%">
<p><strong>başka</strong></p>
</td>
<td width="11%">
<p><strong>baska</strong></p>
</td>
<td width="9%">
<p><strong>&nbsp;</strong></p>
</td>
</tr>
<tr>
<td width="24%">
<p><strong>&Ccedil;ıkış</strong></p>
</td>
<td width="14%">
<p><strong>&ccedil;ık</strong></p>
</td>
<td width="13%">
<p><strong>cik</strong></p>
</td>
<td width="10%">
<p><strong>&ccedil;ıkış</strong></p>
</td>
<td width="16%">
<p><strong>cikis</strong></p>
</td>
<td width="11%">
<p><strong>kapat</strong></p>
</td>
<td width="9%">
<p><strong>iptal</strong></p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>We have searched for some kind of database systems to keep datas. We didn&rsquo;t want all variables in our code. So results were &ldquo;Sqlite&rdquo; and &ldquo;MySql&rdquo; but we don&rsquo;t need this kind of advanced systems. Also we found out it was a library called &ldquo; tinyDB&rdquo;. This library works like simple databases but runs on local machine which is better for simple usage.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; TinyDB creates a local json file. This file has no security protocols, editing json file with any editor is possible but as long as it is school project we can use it. Here is our json code.</p>
<ol>
<li>{"_default":&nbsp;{"1":&nbsp;{"tcno":&nbsp;"12345678910",&nbsp;"isim":&nbsp;"Barış&nbsp;Demirezen",&nbsp;"password":&nbsp;"0000",&nbsp;"balance":&nbsp;"20000"},&nbsp;&nbsp;</li>
<li>"2":&nbsp;{"tcno":&nbsp;"12345678911",&nbsp;"isim":&nbsp;"Ege&nbsp;&Ouml;zfırıncı",&nbsp;"password":&nbsp;"0000",&nbsp;"balance":&nbsp;"2000"},&nbsp;&nbsp;</li>
<li>"3":&nbsp;{"tcno":&nbsp;"12345678912",&nbsp;"isim":&nbsp;"Hakan&nbsp;Canbi&ccedil;en",&nbsp;"password":&nbsp;"0000",&nbsp;"balance":&nbsp;"100"}}}&nbsp;&nbsp;</li>
</ol>
<p>Our object have four attributes. Those are ; tcno, isim, password, balance. We prefered storing them as string. There is three object is avaliable at the moment but adding more user is possible with editing json file.</p>
<p>More documents about tinyDB can be find in here: <a href="https://tinydb.readthedocs.io/en/latest/index.html">https://tinydb.readthedocs.io/en/latest/index.html</a></p>
<p><strong>Installing &nbsp;&ldquo; pip &ldquo; and &ldquo; tinydb &ldquo; is mandatory to run code.</strong></p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; To install &rdquo; tindb &ldquo; run the following command:</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; pip install tinydb</p>
<p>It&rsquo;s possible to move around documents by using hyperlinks that defined for functions in explainings. We didn&rsquo;t wanted to cut codes so we have skipped to new pages if needed.</p>
<p><h1>CODE EXPLANATION</h1></p>
<p><h2>Connecting To Database</h2></p>
<ol>
<li>db&nbsp;=&nbsp;TinyDB('db.json',ensure_ascii=False,&nbsp;encoding='utf-8')&nbsp;&nbsp;&nbsp;</li>
<li>User&nbsp;=&nbsp;Query()&nbsp;&nbsp;</li>
<li>login()</li>
</ol>
<p>We are introducing our database file to code with parameters. Encoding&nbsp; utf-8 supports turkish characters in file so we must use it to keep turkish names. Also we are defining an object to use Query() function named &ldquo;User&rdquo;. After that we are calling our main function named &ldquo;login()&rdquo;</p>
<p><h2>Login Function</h2></p>
<ol>
<li><strong>def</strong>login():&nbsp;&nbsp;</li>
<li>taken_pass="null"&nbsp;&nbsp;</li>
<li>taken_tcno&nbsp;=&nbsp;input("L&uuml;tfen&nbsp;11&nbsp;haneli&nbsp;tc&nbsp;numaranızı&nbsp;giriniz\n")&nbsp;&nbsp;</li>
<li>testint(taken_tcno)&nbsp;&nbsp;</li>
<li><strong>if</strong>&nbsp;len(taken_tcno)!=11&nbsp;<strong>or</strong>&nbsp;int(taken_tcno)&nbsp;&lt;0:&nbsp;&nbsp;</li>
<li><strong>print</strong>("Tc&nbsp;numaranızı&nbsp;hatalı&nbsp;girdiniz.&nbsp;Tekrar&nbsp;deneyiniz.\n")&nbsp;&nbsp;</li>
<li>login()&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li>taken_pass=&nbsp;input("L&uuml;tfen&nbsp;şifrenizi&nbsp;giriniz\n")&nbsp;&nbsp;</li>
<li>testint(taken_pass)&nbsp;&nbsp;</li>
<li>control&nbsp;=&nbsp;db.search((User.tcno&nbsp;==&nbsp;taken_tcno)&nbsp;&amp;&nbsp;(User.password&nbsp;==&nbsp;taken_pass&nbsp;))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>
<li><strong>if</strong>control&nbsp;==[]:&nbsp;&nbsp;&nbsp;&nbsp;</li>
<li><strong>print</strong>("Hatalı&nbsp;Giriş\n")&nbsp;&nbsp;</li>
<li>login()&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li>control&nbsp;=&nbsp;db.get(User.tcno&nbsp;==&nbsp;taken_tcno)&nbsp;&nbsp;</li>
<li>isim&nbsp;=&nbsp;control.get('isim')&nbsp;&nbsp;</li>
<li>tcno&nbsp;=&nbsp;control.get('tcno')&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>
<li><strong>print</strong>("Giriş&nbsp;Başarılı!\n")&nbsp;&nbsp;</li>
<li><strong>print</strong>("Merhaba,&nbsp;"+&nbsp;isim&nbsp;+&nbsp;"&nbsp;hoşgeldiniz.\n")&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>
<li>islemsecici(tcno)&nbsp;&nbsp;</li>
</ol>
<p>In this part user is trying to login.&nbsp; We are controlling if &ldquo;tcno&rdquo; is 11 digit. Else, application asks for new tcno. After that application calls testint() function. It will be explained next. If &ldquo; tcno &ldquo; is valid we are moving to next step. Password is also goes through testint(). Application checks password for tcno. If it&rsquo;s matched we are calling islemsecici(tcno). We are using &ldquo; tcno &ldquo; as parameter for all functions because of it&rsquo;s unique for every user.</p>
<p><h2>Test Integer Function</h2></p>
<ol>
<li><strong>def</strong>testint(tested_input):&nbsp;&nbsp;</li>
<li><strong>try</strong>:&nbsp;&nbsp;</li>
<li><strong>return</strong>&nbsp;int(tested_input)&nbsp;&nbsp;</li>
<li><strong>except</strong>&nbsp;ValueError:&nbsp;&nbsp;</li>
<li><strong>print</strong>("L&uuml;tfen&nbsp;sadece&nbsp;sayı&nbsp;giriniz.\n")&nbsp;&nbsp;</li>
<li>login()&nbsp;&nbsp;</li>
</ol>
<p>It&rsquo;s the testint() function that we mentioned. This codeblock tests user input type. It returns input if input is number. Else gives error and starts login function again.</p>
<p><h2>Process Selector Function</h2></p>
<ol>
<li><strong>def</strong>islemsecici(tcno):&nbsp;&nbsp;</li>
<li>balance&nbsp;=&nbsp;balancecheck(tcno)&nbsp;&nbsp;</li>
<li><strong>print</strong>("Mevcut&nbsp;Bakiyeniz:&nbsp;"&nbsp;+&nbsp;balance&nbsp;+&nbsp;"\n")&nbsp;&nbsp;</li>
<li>islem&nbsp;=&nbsp;input("L&uuml;tfen&nbsp;yapmak&nbsp;istediğiniz&nbsp;işlemi&nbsp;yazınız\n")&nbsp;&nbsp;</li>
<li>islem&nbsp;=&nbsp;islem.lower()&nbsp;&nbsp;</li>
<li><strong>if</strong>&nbsp;'cek'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'&ccedil;ek'&nbsp;<strong>in</strong>&nbsp;islem:&nbsp;&nbsp;</li>
<li>paracekme(tcno)&nbsp;&nbsp;</li>
<li><strong>elif</strong>&nbsp;'yatir'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'yatır'&nbsp;<strong>in</strong>&nbsp;islem:&nbsp;&nbsp;</li>
<li>parayatirma(tcno)&nbsp;&nbsp;</li>
<li><strong>elif</strong>'gonder'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'g&ouml;nder'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'havale'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'eft'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'transfer'&nbsp;<strong>in</strong>&nbsp;islem:&nbsp;&nbsp;</li>
<li>paragonderme(tcno)&nbsp;&nbsp;</li>
<li><strong>elif</strong>'fatura'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'&ouml;de'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'ode'&nbsp;<strong>in</strong>&nbsp;islem:&nbsp;&nbsp;</li>
<li><strong>if</strong>int(balance)&gt;0:&nbsp;&nbsp;</li>
<li>fatura(tcno)&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>print</strong>("Bu&nbsp;işlem&nbsp;i&ccedil;in&nbsp;yeterli&nbsp;bakiyeniz&nbsp;bulunmamakta.\n")&nbsp;&nbsp;</li>
<li>islemsecici(tcno)&nbsp;&nbsp;</li>
<li><strong>elif</strong>'hesap'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'değiş'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'degis'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'başka'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'baska'&nbsp;<strong>in</strong>&nbsp;islem:&nbsp;&nbsp;</li>
<li><strong>print</strong>("Hesabınızdan&nbsp;&ccedil;ıkış&nbsp;yapılıyor.\nYeni&nbsp;hesap&nbsp;i&ccedil;in&nbsp;")&nbsp;&nbsp;</li>
<li>login()&nbsp;&nbsp;</li>
<li><strong>elif</strong>'&ccedil;ık'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'cik'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'&ccedil;ıkış'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'cikis'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'kapat'&nbsp;<strong>in</strong>&nbsp;islem&nbsp;<strong>or</strong>&nbsp;'iptal'&nbsp;<strong>in</strong>&nbsp;islem:&nbsp;&nbsp;</li>
<li>quit()&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>print</strong>("İstediğiniz&nbsp;islem&nbsp;anlasilamadi.&nbsp;Şunları&nbsp;deneyebilirsiniz:\npara&nbsp;&ccedil;ekme\npara&nbsp;yatırma&nbsp;\npara&nbsp;g&ouml;nderme\nfatura&nbsp;&ouml;de\nhesap&nbsp;değiştir\n&ccedil;ıkış&nbsp;\n")&nbsp;&nbsp;</li>
<li>islemsecici(tcno)&nbsp;&nbsp;</li>
</ol>
<p>Actually this part is brain of our code. Code checks users balance with balancecheck(tcno) function. Since &ldquo; tcno &ldquo; is unique, it&rsquo;s possible to check values with this parameter. We will explain balancheck() function later.</p>
<p>User inputs a sentence or a word. In python there is no use case like other high-level languages so using if and if elses are obligatory. In line 5, islem.lower() changes all strings to lower case. You can clearly read commands to call functions about sentences. Also it was a table that shows commands in &ldquo; General Explanations &ldquo;. Every word calls functions but&nbsp; fatura statement checks if user balance is greater than zero if it is, moves to &ldquo; fatura(tcno) &ldquo; function.</p>
<p><h2>Balance Check Function </h2></p>
<ol>
<li><strong>def</strong>balancecheck(tcno):&nbsp;&nbsp;</li>
<li>balancechecked&nbsp;=&nbsp;db.get(User.tcno&nbsp;==&nbsp;tcno)&nbsp;&nbsp;</li>
<li>balancechecked&nbsp;=&nbsp;balancechecked.get('balance')&nbsp;&nbsp;</li>
<li><strong>return</strong>&nbsp;balancechecked&nbsp;&nbsp;</li>
</ol>
<p>Since we need to show balance many times in application, we used a function to use it in case needed. This function is also called with &ldquo; tcno &ldquo; parameter. After controlling database, returns balance of user back.</p>
<p><h2>Withdraw Function</h2></p>
<ol>
<li><strong>def</strong>paracekme(tcno):&nbsp;&nbsp;</li>
<li>bakiye&nbsp;=&nbsp;balancecheck(tcno)&nbsp;&nbsp;</li>
<li><strong>print</strong>("Mevcut&nbsp;bakiyeniz&nbsp;=&nbsp;"&nbsp;+&nbsp;bakiye)&nbsp;&nbsp;</li>
<li>cekilecek&nbsp;=&nbsp;input("L&uuml;tfen&nbsp;&ccedil;ekmek&nbsp;istediğiniz&nbsp;miktarı&nbsp;giriniz.\n&Ccedil;ıkış&nbsp;i&ccedil;in&nbsp;'iptal'&nbsp;yazınız.\n")&nbsp;&nbsp;</li>
<li><strong>if</strong>lower()&nbsp;==&nbsp;"iptal":&nbsp;&nbsp;</li>
<li>islemsecici(tcno)&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>try</strong>:&nbsp;&nbsp;</li>
<li>int(cekilecek)&nbsp;&nbsp;</li>
<li><strong>if</strong>int(cekilecek)&nbsp;&lt;=&nbsp;int(bakiye)&nbsp;<strong>and</strong>&nbsp;int(cekilecek)&nbsp;&gt;&nbsp;0:&nbsp;&nbsp;</li>
<li>yeni_bakiye&nbsp;=&nbsp;int(bakiye)&nbsp;-&nbsp;int(cekilecek)&nbsp;&nbsp;</li>
<li>update({'balance':&nbsp;str(yeni_bakiye)},&nbsp;User.tcno&nbsp;==&nbsp;tcno)&nbsp;&nbsp;</li>
<li><strong>print</strong>("İşlem&nbsp;başarılı.\nHesabınızdan&nbsp;"+&nbsp;cekilecek&nbsp;+&nbsp;"tl&nbsp;&ccedil;ektiniz.&nbsp;Yeni&nbsp;bakiyeniz:&nbsp;"+&nbsp;str(yeni_bakiye))&nbsp;&nbsp;</li>
<li>islemsecici(tcno)&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>print</strong>("İşleminizi&nbsp;ger&ccedil;ekleştiremiyoruz.&nbsp;L&uuml;tfen&nbsp;tekrar&nbsp;deneyiniz!\n")&nbsp;&nbsp;</li>
<li>paracekme(tcno)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>
<li><strong>except</strong>ValueError:&nbsp;&nbsp;</li>
<li><strong>print</strong>("L&uuml;tfen&nbsp;sadece&nbsp; tam sayı&nbsp;giriniz.\n")&nbsp;&nbsp;</li>
<li>paracekme(tcno)&nbsp;&nbsp;</li>
</ol>
<p>Function calls for user balance with &ldquo; balancecheck(tcno) &ldquo;. User can abort process with writing &ldquo; iptal &ldquo;. This code checks if input is integer or &ldquo; iptal &ldquo; too. In case of entering integer, we are controlling if there is enough balance to withdraw from account. After valid inputs balance gets updated with new one and goes back to islemsecici(tcno).</p>
<p><h2>Deposit Function</h2></p>
<ol>
<li><strong>def</strong>parayatirma(tcno):&nbsp;&nbsp;</li>
<li>bakiye&nbsp;=&nbsp;balancecheck(tcno)&nbsp;&nbsp;</li>
<li><strong>print</strong>("Mevcut&nbsp;bakiyeniz&nbsp;=&nbsp;"&nbsp;+&nbsp;bakiye)&nbsp;&nbsp;</li>
<li>yatirilacak&nbsp;=&nbsp;input("L&uuml;tfen&nbsp;yatırmak&nbsp;istediğiniz&nbsp;miktarı&nbsp;giriniz.\n&Ccedil;ıkış&nbsp;i&ccedil;in&nbsp;'iptal'&nbsp;yazınız.\n")&nbsp;&nbsp;</li>
<li><strong>if</strong>lower()&nbsp;==&nbsp;"iptal":&nbsp;&nbsp;</li>
<li>islemsecici(tcno)&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>try</strong>:&nbsp;&nbsp;</li>
<li>int(yatirilacak)&nbsp;&nbsp;</li>
<li><strong>if</strong>int(yatirilacak)&nbsp;&gt;&nbsp;0:&nbsp;&nbsp;</li>
<li>yeni_bakiye&nbsp;=&nbsp;int(bakiye)&nbsp;+&nbsp;int(yatirilacak)&nbsp;&nbsp;</li>
<li>update({'balance':&nbsp;str(yeni_bakiye)},&nbsp;User.tcno&nbsp;==&nbsp;tcno)&nbsp;&nbsp;</li>
<li><strong>print</strong>("İşlem&nbsp;başarılı.\nHesabınıza&nbsp;"+&nbsp;yatirilacak&nbsp;+&nbsp;"tl&nbsp;yatırdınız.&nbsp;Yeni&nbsp;bakiyeniz:&nbsp;"+&nbsp;str(yeni_bakiye))&nbsp;&nbsp;</li>
<li>islemsecici(tcno)&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>print</strong>("İşleminizi&nbsp;ger&ccedil;ekleştiremiyoruz.&nbsp;L&uuml;tfen&nbsp;tekrar&nbsp;deneyiniz!\n")&nbsp;&nbsp;</li>
<li>parayatirma(tcno)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>
<li><strong>except</strong>ValueError:&nbsp;&nbsp;</li>
<li><strong>print</strong>("L&uuml;tfen&nbsp;sadece&nbsp;tam sayı&nbsp;giriniz.\n")&nbsp;&nbsp;</li>
<li>parayatirma(tcno)&nbsp;&nbsp;</li>
</ol>
<p>This is our deposit function. It works almost like withdraw. Deposits must be bigger than zero and must be integer. It&rsquo;s only condition on this part. We are updating balance on deposit after valid inputs. We will continue next part in other page.</p>
<p><h2>Money Transfer Function&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </h2></p>
<ol>
<li><strong>def</strong>paragonderme(tcno):&nbsp;&nbsp;</li>
<li>bakiye&nbsp;=&nbsp;balancecheck(tcno)&nbsp;&nbsp;</li>
<li><strong>print</strong>("Mevcut&nbsp;bakiyeniz&nbsp;=&nbsp;"&nbsp;+&nbsp;bakiye)&nbsp;&nbsp;</li>
<li>yatirilacak&nbsp;=&nbsp;input("L&uuml;tfen&nbsp;g&ouml;ndermek&nbsp;istediğiniz&nbsp;miktarı&nbsp;giriniz.\n&Ccedil;ıkış&nbsp;i&ccedil;in&nbsp;'iptal'&nbsp;yazınız.\n")&nbsp;&nbsp;</li>
<li><strong>if</strong>lower()&nbsp;==&nbsp;"iptal":&nbsp;&nbsp;</li>
<li>islemsecici(tcno)&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>try</strong>:&nbsp;&nbsp;</li>
<li>int(yatirilacak)&nbsp;&nbsp;</li>
<li><strong>if</strong>int(bakiye)&gt;&nbsp;int(yatirilacak)&nbsp;<strong>and</strong>&nbsp;int(yatirilacak)&gt;0:&nbsp;&nbsp;</li>
<li>alici_tc&nbsp;=&nbsp;input&nbsp;("L&uuml;tfen&nbsp;g&ouml;ndermek&nbsp;istediğiniz&nbsp;kişinin&nbsp;tc&nbsp;numarasını&nbsp;giriniz\n")&nbsp;&nbsp;</li>
<li><strong>if</strong>len(alici_tc)==11:&nbsp;&nbsp;</li>
<li><strong>try</strong>:&nbsp;&nbsp;</li>
<li>int(alici_tc)&nbsp;&nbsp;</li>
<li>alici_tc&nbsp;=&nbsp;str(alici_tc)&nbsp;&nbsp;</li>
<li>control&nbsp;=&nbsp;db.search(User.tcno&nbsp;==&nbsp;alici_tc)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>
<li><strong>if</strong>control&nbsp;==[]:&nbsp;&nbsp;&nbsp;&nbsp;</li>
<li><strong>print</strong>("Sistemde&nbsp;bu&nbsp;tc&nbsp;numarası&nbsp;bulunamadı.\n")&nbsp;&nbsp;</li>
<li>paragonderme(tcno)&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li>control&nbsp;=&nbsp;db.get(User.tcno&nbsp;==&nbsp;alici_tc)&nbsp;&nbsp;</li>
<li>alici_isim&nbsp;=&nbsp;control.get('isim')&nbsp;&nbsp;</li>
<li>alici_bakiye&nbsp;=&nbsp;control.get('balance')&nbsp;&nbsp;</li>
<li>onay&nbsp;=&nbsp;input(alici_isim&nbsp;+&nbsp;"&nbsp;adlı&nbsp;kullanıcıya&nbsp;"+&nbsp;yatirilacak&nbsp;+&nbsp;"&nbsp;tl&nbsp;g&ouml;nderiyi&nbsp;onaylıyor&nbsp;musunuz?&nbsp;evet/hayır\n")&nbsp;&nbsp;</li>
<li><strong>if</strong>lower()&nbsp;==&nbsp;"evet":&nbsp;&nbsp;</li>
<li>yeni_bakiye&nbsp;=&nbsp;int(bakiye)&nbsp;-&nbsp;int(yatirilacak)&nbsp;&nbsp;</li>
<li>update({'balance':&nbsp;str(yeni_bakiye)},&nbsp;User.tcno&nbsp;==&nbsp;tcno)&nbsp;&nbsp;</li>
<li>control&nbsp;=&nbsp;db.search(User.tcno&nbsp;==&nbsp;alici_tc)&nbsp;&nbsp;</li>
<li>control&nbsp;=&nbsp;db.get(User.tcno&nbsp;==&nbsp;alici_tc)&nbsp;&nbsp;</li>
<li>alici_bakiye&nbsp;=&nbsp;control.get('balance')&nbsp;&nbsp;</li>
<li>alici_bakiye&nbsp;=&nbsp;int(alici_bakiye)&nbsp;+&nbsp;int(yatirilacak)</li>
<li>update({'balance':&nbsp;str(alici_bakiye)},&nbsp;User.tcno&nbsp;==&nbsp;alici_tc)&nbsp;&nbsp;</li>
<li><strong>print</strong>("İşlem&nbsp;başarılı.\n")&nbsp;&nbsp;</li>
<li>islemsecici(tcno)&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>print</strong>("İşleminiz&nbsp;iptal&nbsp;edilmiştir.\n")&nbsp;&nbsp;</li>
<li>islemsecici(tcno)&nbsp;&nbsp;</li>
<li><strong>except</strong>ValueError:&nbsp;&nbsp;</li>
<li><strong>print</strong>("L&uuml;tfen 11&nbsp;karakterlik&nbsp;tc&nbsp;numarasını&nbsp;giriniz.\n")&nbsp;&nbsp;</li>
<li>paragonderme(tcno)&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>print</strong>("L&uuml;tfen&nbsp;11&nbsp;karakterlik&nbsp;tc&nbsp;numarasını&nbsp;giriniz.\n")&nbsp;&nbsp;</li>
<li>paragonderme(tcno)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>print</strong>("İşleminizi&nbsp;ger&ccedil;ekleştiremiyoruz.&nbsp;L&uuml;tfen&nbsp;tekrar&nbsp;deneyiniz!\n"</li>
<li>islemsecici(tcno)&nbsp;&nbsp;</li>
<li><strong>except</strong>ValueError:&nbsp;&nbsp;</li>
<li><strong>print</strong>("L&uuml;tfen&nbsp;sadece&nbsp;tam&nbsp;sayı&nbsp;giriniz.\n")&nbsp;&nbsp;</li>
<li>paragonderme(tcno)&nbsp;&nbsp;</li>
</ol>
<p>There are many of exception handlings in this part. Here is what code checks for errors.</p>
<ul>
<li>Money to be transfered must be integer and bigger than zero but less than balance</li>
<li>Receiver &ldquo; tc &ldquo; must be integer and eleven digit.</li>
<li>Receiver &ldquo;tc &ldquo; must be exist on database.</li>
</ul>
<p>In line 28 we are refreshing our queried values to handle error if users send money to itself.</p>
<p><h2>Bill Selector Function</h2></p>
<ol>
<li><strong>def</strong>fatura(tcno):&nbsp;&nbsp;</li>
<li>bakiye&nbsp;=&nbsp;balancecheck(tcno)&nbsp;&nbsp;</li>
<li><strong>print</strong>("Mevcut&nbsp;bakiyeniz&nbsp;=&nbsp;"&nbsp;+&nbsp;bakiye)&nbsp;&nbsp;</li>
<li>secim&nbsp;=&nbsp;input("L&uuml;tfen&nbsp;yatırmak&nbsp;istediğiniz&nbsp;faturanın&nbsp;numarasını&nbsp;se&ccedil;iniz.\n1&nbsp;-&nbsp;Elektrik\n2&nbsp;-&nbsp;Su\n3&nbsp;-&nbsp;Doğalgaz\n&Ccedil;ıkış&nbsp;i&ccedil;in&nbsp;'iptal'&nbsp;yazınız.\n")&nbsp;&nbsp;</li>
<li><strong>if</strong>&nbsp;secim&nbsp;==&nbsp;"iptal":&nbsp;&nbsp;</li>
<li>islemsecici(tcno)&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>if</strong>&nbsp;secim&nbsp;==&nbsp;"1":&nbsp;&nbsp;</li>
<li>fatura_tur&nbsp;=&nbsp;"Elektrik"&nbsp;&nbsp;</li>
<li><strong>elif</strong>secim&nbsp;==&nbsp;"2":&nbsp;&nbsp;</li>
<li>fatura_tur&nbsp;=&nbsp;"Su"</li>
<li><strong>elif</strong>secim&nbsp;==&nbsp;"3":&nbsp;&nbsp;</li>
<li>fatura_tur&nbsp;=&nbsp;"Doğalgaz"</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>print</strong>("Hatalı&nbsp;giriş&nbsp;yaptınız.&nbsp;L&uuml;tfen&nbsp;tekrar&nbsp;deneyiniz.\n")&nbsp;&nbsp;</li>
<li>fatura(tcno)&nbsp;&nbsp;</li>
<li>faturaode(tcno,fatura_tur)&nbsp;&nbsp;&nbsp;&nbsp;</li>
</ol>
<p>This is our &ldquo; pay the bills &ldquo; function. This part only asks users to select a bill to pay. There are three options. If input is valid calls faturaode(tcno,fatura_tur) function.</p>
<p><h2>Pay Selected Bill Function</h2></p>
<ol>
<li><strong>def</strong>faturaode(tcno,fatura_tur):&nbsp;&nbsp;</li>
<li>bakiye=balancecheck(tcno)&nbsp;&nbsp;</li>
<li><strong>if</strong>&nbsp;int(bakiye)&nbsp;&gt;&nbsp;202:&nbsp;&nbsp;</li>
<li>rastgele_tutar&nbsp;=&nbsp;random.randrange(10,201)&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li>rastgele_tutar&nbsp;=&nbsp;random.randrange(1,int(bakiye)+1)&nbsp;&nbsp;</li>
<li>onay&nbsp;=&nbsp;input(str(rastgele_tutar)&nbsp;+&nbsp;"&nbsp;tl&nbsp;tutarındaki&nbsp;"&nbsp;+&nbsp;fatura_tur&nbsp;+&nbsp;"&nbsp;faturanızı&nbsp;&ouml;demeyi&nbsp;onaylıyor&nbsp;musunuz?&nbsp;evet/hayır\n")&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>
<li><strong>if</strong>lower()&nbsp;==&nbsp;"evet":&nbsp;&nbsp;</li>
<li>yeni_bakiye&nbsp;=&nbsp;int(bakiye)&nbsp;-&nbsp;int(rastgele_tutar)&nbsp;&nbsp;</li>
<li>update({'balance':&nbsp;str(yeni_bakiye)},&nbsp;User.tcno&nbsp;==&nbsp;tcno)&nbsp;&nbsp;</li>
<li><strong>print</strong>("Faturanız&nbsp;başarıyla&nbsp;yatırıldı.\n")&nbsp;&nbsp;</li>
<li>islemsecici(tcno)&nbsp;&nbsp;</li>
<li><strong>else</strong>:&nbsp;&nbsp;</li>
<li><strong>print</strong>("İşleminiz&nbsp;iptal&nbsp;edilmiştir.\n")&nbsp;&nbsp;</li>
<li>islemsecici(tcno)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>
</ol>
<p>We have parameters from fatura(tcno) functions. This is where this parameters gonna be processed. We added approving question, to pay bills. There is a random function to create random bills. If user has more than 202 liras, our bill prices will be maximum 200 liras. In case of user have less than 200 liras, our maximum bill price will be same as users balance. For example, if user have 150 liras, expected bill must be maximum 150 liras. User can abort process with writing &ldquo; iptal &ldquo;.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
