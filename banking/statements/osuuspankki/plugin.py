# -*- encoding: utf-8 -*-
from ofxstatement.plugin import Plugin
from .parser import OPCsvStatementParser, OPCsvStatementParser2021v1, SIGNATURES, SIGNATURES_2021v1


class OPPlugin(Plugin):
    "Suomen Osuuspankki / Finnish Osuuspankki"

    def get_parser(self, fin):
        encoding = 'iso-8859-1'
        signature = self.get_signature(fin, encoding)

        if signature.startswith('ï»¿'):
            # Switch to UTF-8 with BOM
            encoding = 'utf-8-sig'
            signature = self.get_signature(fin, encoding)

        f = open(fin, "r", encoding=encoding)

        if signature in SIGNATURES:
            return self.with_settings(OPCsvStatementParser(f))

        if signature in SIGNATURES_2021v1:
            return self.with_settings(OPCsvStatementParser2021v1(f))

        f.close()

        # no plugin with matching signature was found
        raise Exception(
            "No suitable Osuuspankki parser found for this statement file.")

    def get_signature(self, fin, encoding):
        with open(fin, "r", encoding=encoding) as f:
            signature = f.readline().strip()
        return signature

    def with_settings(self, parser):
        parser.statement.account_id = self.settings.get(
            'account', "FIVVXXXXYYYYZZZZWW")
        parser.statement.currency = self.settings.get('currency', "EUR")
        parser.statement.bank_id = self.settings.get('bank', 'Osuuspankki')
        return parser
