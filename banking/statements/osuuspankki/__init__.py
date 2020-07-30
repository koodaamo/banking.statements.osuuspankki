# Transaction type mapping for Osuuspankki statement parsers

TRANSACTION_TYPES = {
   "TILISIIRTO": "XFER",
   "PALVELUMAKSU": "FEE",
   "PKORTTIMAKSU": "POS",
   "VIITESIIRTO": "XFER",
   "PIKASIIRTO": "XFER",
   "ETUUS": "XFER",
   "LAPSILISÄ": "XFER",
   "KORVAUS": "XFER",
   "AUTOMAATTINOSTO": "ATM",
   "MAKSUPALVELU": "REPEATPMT",
   "LUOTON MAKSU": "REPEATPMT",
   "TALLETUSKORKO": "INT",
   "KORKO": "INT",
   "LÄHDEVERO": "FEE",
   "SUORAVELOITUS": "DIRECTDEBIT",
   "PANO": "DEP",
   "PERUUTUS": "DIRECTDEP",
   "VUOKRA": "PAYMENT",
   "VERONPALAUTUS": "DIRECTDEP",
   "PALKKA": "DIRECTDEP",
   "ARVOPAPERI": "OTHER",
   "TALLETUSAUTOM.": "XFER",
   "LAINAAN": "FEE"
}

#   Other types available: 'CREDIT', 'DEBIT', 'INT', 'DIV', 'FEE', 'DEP',
#   'ATM', 'CHECK', 'CASH', 'DIRECTDEP', 'DIRECTDEBIT', 'REPEATPMT', 'OTHER'


