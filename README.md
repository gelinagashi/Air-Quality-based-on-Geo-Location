# Air-Quality-based-on-Geo-Location

Ky grup të dhënash ofron informacion mbi masat e cilësisë së ajrit për ndotës të ndryshëm si ozoni (O3) dhe dioksidi i squfurit (SO2) në zona të ndryshme në botë.
Ky grup të dhënash mund të përdoret nga studiues dhe politikëbërës për të kuptuar tendencat në nivelet e ndotjes së ajrit dhe për të informuar ndërhyrjet për të përmirësuar cilësinë e ajrit dhe për të mbrojtur shëndetin publik. Cilësia e ajrit po përkeqësohet në shumë qytete anembanë botës. Rritja e niveleve të ndotjes,
emetimet industriale dhe faktorë të tjerë kontribuojnë në këtë efekt. Duke pasur parasysh kete grup të dhënash të mbikëqyrjes së cilësisë së ajrit, do të analizohet,  dhe krijohet një model për të analizuar cilësinë e ajrit në vendndodhje.

ID unike: Një identifikues unik i caktuar për çdo rresht në grupin e të dhënave.

ID e treguesit: Një kod i caktuar për çdo tregues ose masë të cilësisë së ajrit që gjurmohet.

Emri: Emri ose etiketa që i jepet treguesit ose masës që gjurmohet.

Masa: Njësia matëse e përdorur për të përcaktuar treguesin e cilësisë së ajrit, si p.sh. pjesë për miliard (ppb) për ozonin ose dioksidin e squfurit.

Informacioni i masës: Informacion shtesë në lidhje me matjen ose llogaritjen e treguesit të cilësisë së ajrit, nëse është e aplikueshme.

Emri i llojit gjeo: Lloji i zonës gjeografike që gjurmohet, si p.sh. distriktet e komunitetit (CD) ose bashkitë.

Geo Join ID: Një identifikues unik i caktuar për çdo zonë gjeografike që gjurmohet.

Emri i Vendit Gjeo: Emri i zonës specifike gjeografike që gjurmohet, si Coney Island ose Bronx.

Periudha kohore: Periudha kohore gjatë së cilës është bërë matja e cilësisë së ajrit, si p.sh. një sezon ose dimër i caktuar i një viti të caktuar.

Data_Start: Data në të cilën filloi periudha e matjes së cilësisë së ajrit.

Vlera e të dhënave: Vlera e treguesit të cilësisë së ajrit për zonën specifike gjeografike dhe periudhën kohore që gjurmohet.

Mesazhi: Informacion ose shënime shtesë në lidhje me matjen e cilësisë së ajrit ose vlerën e të dhënave, nëse është e aplikueshme.

########################################################################################################
Algoritmet qe do perdoren:
1. Decision tree
2. Random forect
3. Linear Regression
*
*
*
test_taining_with_linear_regerssion*-----------------------------------------------
Ky kod kryen një analizë të regresionit linear në një grup të dhënash të cilësisë së ajrit të parapërpunuar. Kodi përdor bibliotekën e pandas për të ngarkuar grupin e të dhënave dhe zgjedh kolonat e nevojshme, të cilat janë data e fillimit dhe vlera e të dhënave. Kolona e datës së fillimit konvertohet në një format numerik, i cili është i nevojshëm për analizën e regresionit.

Biblioteka sklearn përdoret për të ndarë të dhënat në grupe trajnimi dhe testimi. Të dhënat ndahen në një raport 80-20, ku 80% e të dhënave përdoren për trajnim dhe 20% për testim. Më pas krijohet modeli i regresionit linear dhe përshtatet me të dhënat e trajnimit.

Modeli përdoret më pas për të parashikuar vlerat për të dhënat e provës, dhe koeficientët dhe ndërprerja e modelit të regresionit linear printohen në tastierë. Së fundi, performanca e modelit vlerësohet duke përdorur gabimin mesatar në katror dhe rezultatin R2.

Në përgjithësi, ky kod tregon se si të kryhet një analizë bazë e regresionit linear në një grup të dhënash duke përdorur Python dhe bibliotekën sklearn. Kodi mund të përshtatet lehtësisht për të punuar me grupe të tjera të dhënash, duke e bërë atë një mjet të dobishëm për analizën e të dhënave dhe mësimin e makinerive.

REZULTATET:
*Coefficient: [-2.75440897e-08]
*Intercept: 57.18908890792791
*Mean Squared Error: 409.33047279103437
*R2 Score: 0.027400427668851424

ramdom_forest----------------------------------------------
Së pari, bibliotekat e kërkuara importohen, duke përfshirë Pandat për manipulimin e të dhënave, NumPy për llogaritjet numerike dhe scikit-learn për algoritmet e mësimit të makinerive.

Më pas, grupi i të dhënave i parapërpunuar ngarkohet duke përdorur funksionin read_csv të Pandas.

Të dhënat parapërpunohen duke konvertuar kolonën 'Data_Fillimi' në formatin e datës dhe më pas duke krijuar kolona të reja për vitin, muajin dhe ditën. Për më tepër, grupi i të dhënave është i koduar një herë duke përdorur funksionin get_dummies të Pandas.

Veçoritë dhe ndryshorja e synuar ndahen në variabla të veçanta dhe kolona 'Data_Fillimi' konvertohet në një format numerik.

Të dhënat më pas ndahen në grupe trajnimi dhe testimi duke përdorur funksionin train_test_split të scikit-learn.

Një model Random Forest Regressor krijohet duke përdorur klasën RandomForestRegressor të scikit-learn, me 100 pemë dhe një gjendje të rastësishme prej 42, dhe më pas përshtatet me të dhënat e trajnimit.

Modeli përdoret për të parashikuar variablin e synuar për grupin e testimit dhe Gabimi mesatar në katror llogaritet duke përdorur funksionin mean_squared_error të scikit-learn.

Më në fund, gabimi mesatar në katror shtypet në tastierë.

Në përgjithësi, kodi demonstron përdorimin e scikit-learn për të përpunuar paraprakisht të dhënat, për të ndërtuar një model të regresorit të rastësishëm të pyjeve dhe për të vlerësuar performancën e tij duke përdorur gabimin mesatar në katror. Ky lloj kodi mund të jetë i dobishëm për të analizuar dhe bërë parashikime nga lloje të ndryshme të grupeve të të dhënave.


decision_tree------------------------------------------------------

Kodi fillon duke importuar bibliotekat e nevojshme, duke përfshirë pandat, numpy, train_test_split nga sklearn.model_selection, DecisionTreeRegressor nga sklearn.tree dhe mean_squared_error dhe r2_score nga sklearn.metrics.
Më pas, kodi ngarkon një grup të dhënash të parapërpunuar nga një skedar CSV në një DataFrame panda duke përdorur metodën read_csv.
Të dhënat më pas përpunohen paraprakisht duke hequr vlerat që mungojnë duke përdorur metodën dropna.
Veçoritë dhe variablat e synuar më pas ndahen në DataFrames të veçanta X dhe y respektivisht.
Kolona 'Start_Date' në X konvertohet në një format numerik duke e kthyer atë në një objekt datatime dhe më pas në një format int64 të ndarë me 10^9.
Të dhënat më pas ndahen në grupe trajnimi dhe testimi duke përdorur train_test_split nga biblioteka sklearn.model_selection.
Një Regressor i Pemës së Vendimeve krijohet dhe trajnohet duke përdorur të dhënat e trajnimit duke përdorur klasën DecisionTreeRegressor nga biblioteka sklearn.tree.
Modeli më pas bën parashikime mbi të dhënat e testimit duke përdorur metodën e parashikimit.
Gabimi mesatar në katror dhe rezultati R2 llogariten më pas për të vlerësuar performancën e modelit duke përdorur mean_squared_error dhe r2_score nga biblioteka sklearn.metrics.
Më në fund, gabimi mesatar në katror dhe rezultati R2 shtypen në tastierë.
Në përgjithësi, ky kod tregon se si të ndërtohet një model i thjeshtë Regressor i Pemës së Vendimit për të parashikuar vlerat në një grup të dhënash dhe si të vlerësohet performanca e modelit duke përdorur gabimin mesatar në katror dhe rezultatin R2.
![image](https://github.com/gelinagashi/Air-Quality-based-on-Geo-Location/assets/25957526/08adf85e-2d68-45ef-977a-abf36d719b00)
