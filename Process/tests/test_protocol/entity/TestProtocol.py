import unittest

from account.service.AccountServiceImpl import AccountServiceImpl
from custom_protocol.entity.CustomProtocol import CustomProtocol
from custom_protocol.service.CustomProtocolServiceImpl import CustomProtocolServiceImpl
from main import initCustomProtocol
from product.service.ProductServiceImpl import ProductServiceImpl


class TestProtocol(unittest.TestCase):



    def testInitCustomProtocol(self):
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        productService = ProductServiceImpl.getInstance()
        accountService = AccountServiceImpl.getInstance()

        print(f"enum value test: {CustomProtocol.ACCOUNT_REGISTER.value}")
        customProtocolService.registerCustomProtocol(
            CustomProtocol.ACCOUNT_REGISTER.value,
            accountService.registerAccount
        )

        print(f"enum value test: {CustomProtocol.PRODUCT_ADD.value}")
        customProtocolService.registerCustomProtocol(
            CustomProtocol.PRODUCT_ADD.value,
            productService.productAdd
        )

    def testCallProtocol(self):
        initCustomProtocol()


