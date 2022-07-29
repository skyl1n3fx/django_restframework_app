from tests.test_setup import TestSetup
from tests.factories.expense_manager.expense_factories import SupplierFactory
from rest_framework import status

class ExpenseTestCase(TestSetup):

    url = '/expense/expense/'

    def test_search_supplier(self):
        supplier = SupplierFactory().create_supplier()
        response = self.client.get(
            self.url + 'search-supplier/',
            {
                'ruc_or_business_name' : supplier.ruc
            }, 
            format = 'json'
        )

        # Corroboramos si la respuesta a la petición es 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Corroboramos si el supplier buscado coincide con el supplier creado.
        self.assertEqual(response.data['ruc'],supplier.ruc)

    def test_search_supplier_error(self):
        supplier = SupplierFactory().create_supplier()
        response = self.client.get(
            self.url + 'search-supplier/',
            {
                'ruc_or_business_name' : '35903485904830948390483904'
            }, 
            format = 'json'
        )

        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(supplier.ruc, '35903485904830948390483904')
        self.assertEqual(response.data['message'], 'No se ha entrado un proveedor.')

        '''
            Method                          Checks that
            assertEqual(a, b)               a == b
            assertNotEqual(a, b)            a != b
            assertTrue(x)                   bool(x) is True
            assertFalse(x)                  bool(x) is False
            assertis(a, b)                  a is b
            assertIsNot(a, b)               a is not b
            assertIsNone(x)                 x is None
            assertIsNotNone(x)              x is not None
            assertIn(a, b)                  a in b
            assertNotIn(a, b)               a not in b
            assertIsInstance(a, b)          isinstance(a, b)
            assertNotIsInstance(a, b)       not isinstance(a, b)
        '''
