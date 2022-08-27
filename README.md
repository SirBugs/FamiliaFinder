# FamiliaFinder
FamiliaFinder is a subdomains mass searcher, looking about subdomains in source + subdomains from a mass list of subdomains containing 15K subdomains + Using https://crt.sh

# requirements:
- Python 2.7
- requests
- colorama

# Seeing after running:
```
	Current InUse Tool: SUB
	Subdomains List Current Size: 15074
	Method: GET
	Threads: 100
	Target: grab.com
	[02:04:35] STARTING BRUTE!

	[02:04:38] 403 (354) : food.grab.com
	[02:04:39] 404 (531) : partner-api2.grab.com
	[02:04:39] 404 (636) : daxexp.grab.com
	[02:04:39] 403 (731) : vendor-portal.grab.com
	[02:04:40] 403 (996) : gamma-ge-dashboard.grab.com
	[02:04:40] 403 (1176) : aries.grab.com
	[02:04:40] 403 (1231) : image.mkt.grab.com
	[02:04:41] 200 (1293) : commerce.grab.com
	[02:04:41] 403 (1482) : segments-ui.grab.com
	[02:04:41] 403 (1531) : hodor-assets.grab.com
	[02:04:42] 200 (1622) : developer.grab.com
	[02:04:42] 200 (1662) : supernova.ext.grab.com
	[02:04:42] 200 (1711) : admiral.grab.com
	[02:04:42] 200 (1718) : concierge.grab.com
	[02:04:42] 503 (1775) : public.grab.com
```

# Switches:
```
\t -s
\t    This switch would be followed by the .txt file name you wanna save in
\t -l
\t    This switch is selecting limit of the subs have to be checked
\t -h
\t    This switch is only submitted one
\t -t
\t    This switch is cotrolling the threads number (Suggested=50)
\t *
\t    All switches are written in SMALL letters normally
\t *
\t    This tool list is getting updated day by day, adding more stuff, options, subs, etc..
\t *
\t    For more info aboue HTTP STATUS CODES, Visit: https://github.com/SirBugs/FamiliaSubFinder/StatusCodes.txt
```

# Running:
```
python2 FamiliaFinder.py SUB yahoo.com
>> Normal Usage

python2 FamiliaFinder.py SUB yahoo.com -s yahoosubdomains.txt
>> Saving the results in a .txt file

python2 FamiliaFinder.py SUB yahoo.com -t 100
>> Selecting the threads to 100
```




