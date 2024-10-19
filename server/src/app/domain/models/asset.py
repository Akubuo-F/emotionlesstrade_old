from typing import Final

class InstrumentType:
    """
    A Category for an asset.
    """
    CURRENCY: Final[str] = "CURRENCY"
    COMMODITY: Final[str] = "COMMODITY"
    INDEX: Final[str] = "INDEX"
    CRYPTO: Final[str] = "CRYPTO"

class Asset:
    """
    A tradable financial instrument.
    """
    def __init__(self, code: str, name: str, instrument_type: str):
        """
        :param code: The unique code of the asset, e.g., 'XAU' for Gold.
        :param name: The name of the asset, e.g., NASDAQ.
        :param instrument_type: The type of the instrument, e.g., Crypto.
        """
        self._code = code
        self._name = name
        self._instrument_type = instrument_type

    @property
    def code(self):
        """The unique code of the asset, e.g., 'XAU' for Gold."""
        return self._code

    @property
    def name(self):
        """The name of the asset, e.g., NASDAQ."""
        return self._name

    @property
    def instrument_type(self):
        """The type of the instrument, e.g., Crypto."""
        return self._instrument_type


class ReportedAssets:
    """
    Contains All assets that are considered by EmotionlessTrade.io
    """
    aud: Final[Asset] = Asset(code="AUD", name="AUSTRALIAN DOLLAR", instrument_type=InstrumentType.CURRENCY)
    btc: Final[Asset] = Asset(code="BTC", name="BITCOIN", instrument_type=InstrumentType.CRYPTO)
    cad: Final[Asset] = Asset(code="CAD", name="CANADIAN DOLLAR", instrument_type=InstrumentType.CURRENCY)
    chf: Final[Asset] = Asset(code="CHF", name="SWISS FRANC", instrument_type=InstrumentType.CURRENCY)
    dji: Final[Asset] = Asset(code="DJI", name="DOW JONES", instrument_type=InstrumentType.INDEX)
    eur: Final[Asset] = Asset(code="EUR", name="EURO", instrument_type=InstrumentType.CURRENCY)
    gbp: Final[Asset] = Asset(code="GBP", name="BRITISH POUND", instrument_type=InstrumentType.CURRENCY)
    jpy: Final[Asset] = Asset(code="JPY", name="JAPANESE YEN", instrument_type=InstrumentType.CURRENCY)
    nzd: Final[Asset] = Asset(code="NZD", name="NEW ZEALAND DOLLAR", instrument_type=InstrumentType.CURRENCY)
    ndx: Final[Asset] = Asset(code="NDX", name="NASDAQ", instrument_type=InstrumentType.INDEX)
    spx: Final[Asset] = Asset(code="SPX", name="S&P 500", instrument_type=InstrumentType.INDEX)
    usd: Final[Asset] = Asset(code="USD", name="US DOLLAR", instrument_type=InstrumentType.CURRENCY)
    uso: Final[Asset] = Asset(code="USO", name="CRUDE OIL", instrument_type=InstrumentType.COMMODITY)
    xag: Final[Asset] = Asset(code="XAG", name="SILVER", instrument_type=InstrumentType.COMMODITY)
    xau: Final[Asset] = Asset(code="XAU", name="GOLD", instrument_type=InstrumentType.COMMODITY)
    xcu: Final[Asset] = Asset(code="XCU", name="COPPER", instrument_type=InstrumentType.COMMODITY)
    xpt: Final[Asset] = Asset(code="XPT", name="PLATINUM", instrument_type=InstrumentType.COMMODITY)
    ALL: Final[list[Asset]] = [aud, btc, cad, chf, dji, eur, gbp, jpy, nzd, ndx, spx, usd, uso, xag, xau, xcu, xpt]



